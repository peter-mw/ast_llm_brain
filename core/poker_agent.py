"""
Poker Learning Agent
Uses CVM Phase IV to learn poker strategy through self-play
"""
from core.cvm_phase4 import CVM
from core.poker_game import PokerEnvironment
from core.actions import Action
from core.goals import Goal
import random


class PokerAgent:
    """
    Poker agent that learns through self-play
    Uses the CVM cognitive architecture
    """
    
    def __init__(self, name="PokerAgent"):
        self.name = name
        self.cvm = CVM()
        self.hand_history = []
        self.strategy = {}  # Maps game states to action preferences
        self.win_count = 0
        self.hand_count = 0
    
    def get_state_key(self, state, player_idx):
        """
        Create a simplified state representation for learning
        Focus on key features
        """
        player = state["players"][player_idx]
        opponent = state["players"][1 - player_idx]
        
        # Simplify to key features
        key = {
            "round": state["round"],
            "pot_size": "small" if state["pot"] < 50 else "medium" if state["pot"] < 150 else "large",
            "position": "sb" if player_idx == 0 else "bb",
            "chips": "short" if player["chips"] < 500 else "medium" if player["chips"] < 1500 else "deep",
            "opponent_chips": "short" if opponent["chips"] < 500 else "medium" if opponent["chips"] < 1500 else "deep",
            "current_bet": state["current_bet"],
            "hand_strength": self._evaluate_hand_strength(player["hand"], state["community_cards"])
        }
        
        return str(key)
    
    def _evaluate_hand_strength(self, hole_cards, community_cards):
        """
        Simple hand strength evaluation
        Returns: "weak", "medium", "strong"
        """
        if not hole_cards:
            return "unknown"
        
        # Pre-flop hand strength
        if not community_cards:
            ranks = sorted([c.rank.value for c in hole_cards], reverse=True)
            # Pocket pairs
            if ranks[0] == ranks[1]:
                if ranks[0] >= 10:
                    return "strong"
                elif ranks[0] >= 7:
                    return "medium"
                else:
                    return "weak"
            # High cards
            elif ranks[0] >= 12:  # Q or better
                return "strong" if ranks[1] >= 10 else "medium"
            elif ranks[0] >= 10:
                return "medium"
            else:
                return "weak"
        
        # Post-flop: simplified evaluation
        # In real implementation, would use PokerEvaluator
        return "medium"  # Placeholder
    
    def choose_action(self, state, legal_actions, player_idx, explore_rate=0.2):
        """
        Choose an action based on current strategy
        Uses epsilon-greedy exploration
        """
        # Exploration: random action
        if random.random() < explore_rate:
            return random.choice(legal_actions)
        
        # Exploitation: use learned strategy
        state_key = self.get_state_key(state, player_idx)
        
        if state_key in self.strategy:
            # Get action preferences
            prefs = self.strategy[state_key]
            
            # Choose best legal action
            best_action = None
            best_value = float('-inf')
            
            for action in legal_actions:
                value = prefs.get(action, 0)
                if value > best_value:
                    best_value = value
                    best_action = action
            
            if best_action:
                return best_action
        
        # Default strategy if no learned strategy
        return self._default_strategy(state, legal_actions, player_idx)
    
    def _default_strategy(self, state, legal_actions, player_idx):
        """
        Default poker strategy for unknown situations
        """
        hand_strength = self._evaluate_hand_strength(
            state["players"][player_idx]["hand"],
            state["community_cards"]
        )
        
        if hand_strength == "strong":
            # Strong hand: raise or call
            if "raise" in legal_actions:
                return "raise"
            elif "call" in legal_actions:
                return "call"
            elif "check" in legal_actions:
                return "check"
        
        elif hand_strength == "medium":
            # Medium hand: call or check
            if "check" in legal_actions:
                return "check"
            elif "call" in legal_actions and state["current_bet"] <= 40:
                return "call"
            else:
                return "fold"
        
        else:
            # Weak hand: check or fold
            if "check" in legal_actions:
                return "check"
            else:
                return "fold"
        
        # Fallback
        return legal_actions[0] if legal_actions else "fold"
    
    def update_strategy(self, state_key, action, reward):
        """
        Update strategy based on outcome
        Uses temporal difference learning
        """
        if state_key not in self.strategy:
            self.strategy[state_key] = {}
        
        # Update action value
        current_value = self.strategy[state_key].get(action, 0)
        learning_rate = 0.1
        new_value = current_value + learning_rate * (reward - current_value)
        self.strategy[state_key][action] = new_value
    
    def play_hand(self, env, opponent, player_idx, verbose=False):
        """
        Play a single hand of poker
        Returns (reward, winner)
        """
        state = env.get_state()
        hand_memory = []
        
        done = False
        total_reward = 0
        
        while not done:
            current = state["current_player"]
            
            # Determine which agent acts
            if current == player_idx:
                agent = self
            else:
                agent = opponent
            
            # Get legal actions
            legal_actions = env.get_legal_actions(current)
            
            if not legal_actions:
                break
            
            # Choose action
            action = agent.choose_action(state, legal_actions, current)
            
            if verbose and current == player_idx:
                print(f"  {self.name} {action}")
            
            # Record state-action for learning
            if current == player_idx:
                state_key = self.get_state_key(state, current)
                hand_memory.append((state_key, action))
            
            # Take action
            state, reward, done = env.take_action(current, action)
            
            if done and current == player_idx:
                total_reward = reward
        
        # Learn from hand
        for state_key, action in hand_memory:
            self.update_strategy(state_key, action, total_reward)
        
        # Update statistics
        self.hand_count += 1
        if total_reward > 0:
            self.win_count += 1
        
        return total_reward, total_reward > 0
    
    def get_win_rate(self):
        """Calculate win rate"""
        if self.hand_count == 0:
            return 0.0
        return self.win_count / self.hand_count


class PokerTrainer:
    """
    Trains poker agents through self-play
    """
    
    def __init__(self):
        self.env = PokerEnvironment()
    
    def train(self, agent1, agent2, num_hands=100, verbose=False):
        """
        Train two agents against each other
        """
        results = {
            "agent1_wins": 0,
            "agent2_wins": 0,
            "agent1_rewards": [],
            "agent2_rewards": []
        }
        
        for hand_num in range(num_hands):
            # Reset for new hand
            self.env.reset()
            
            if verbose and hand_num % 10 == 0:
                print(f"\n--- Hand {hand_num + 1} ---")
            
            # Play hand (agent1 is player 0)
            reward1, won1 = agent1.play_hand(self.env, agent2, 0, verbose and hand_num % 10 == 0)
            
            # Track results
            results["agent1_rewards"].append(reward1)
            results["agent2_rewards"].append(-reward1)  # Zero-sum
            
            if won1:
                results["agent1_wins"] += 1
            else:
                results["agent2_wins"] += 1
            
            # Swap positions for next hand
            agent1, agent2 = agent2, agent1
        
        return results
