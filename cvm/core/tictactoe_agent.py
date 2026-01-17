"""
Tic-Tac-Toe Learning Agent
===========================

Agent that learns to play tic-tac-toe using the CVM Phase IV architecture.
Uses reinforcement learning (Q-learning) with self-play.
"""

from typing import Dict, List, Tuple, Optional
import random
from cvm.core.cvm_phase4 import CVM
from cvm.core.tictactoe_game import TicTacToeEnvironment, Player


class TicTacToeAgent:
    """
    Agent that learns to play tic-tac-toe.
    
    Uses:
    - Q-learning for strategy development
    - State abstraction for generalization
    - CVM Phase IV for memory and planning
    """
    
    def __init__(self, name: str = "Agent"):
        """
        Initialize agent.
        
        Args:
            name: Agent identifier
        """
        self.name = name
        self.cvm = CVM()
        
        # Q-table: state_key -> {action: value}
        self.q_table: Dict[str, Dict[Tuple[int, int], float]] = {}
        
        # Learning parameters
        self.learning_rate = 0.1
        self.discount_factor = 0.95
        self.epsilon = 0.2  # Exploration rate
        
        # Statistics
        self.games_played = 0
        self.wins = 0
        self.losses = 0
        self.draws = 0
        
        # Episode memory for learning
        self.episode_history: List[Tuple[str, Tuple[int, int], float]] = []
    
    def get_state_key(self, state: dict) -> str:
        """
        Convert game state to string key for Q-table.
        
        Creates board pattern representation.
        """
        board = state['board']
        symbols = {Player.X: 'X', Player.O: 'O', Player.EMPTY: '.'}
        
        # Convert board to string
        board_str = ""
        for row in range(3):
            for col in range(3):
                cell = board.get_cell(row, col)
                board_str += symbols[cell]
        
        # Include current player
        player_str = state['current_player'].name
        
        return f"{board_str}_{player_str}"
    
    def get_q_value(self, state_key: str, action: Tuple[int, int]) -> float:
        """Get Q-value for state-action pair."""
        if state_key not in self.q_table:
            self.q_table[state_key] = {}
        
        if action not in self.q_table[state_key]:
            self.q_table[state_key][action] = 0.0
        
        return self.q_table[state_key][action]
    
    def update_q_value(self, state_key: str, action: Tuple[int, int], 
                       reward: float, next_state_key: str, 
                       next_legal_actions: List[Tuple[int, int]]):
        """
        Update Q-value using Q-learning update rule.
        
        Q(s,a) ← Q(s,a) + α[r + γ max_a' Q(s',a') - Q(s,a)]
        """
        current_q = self.get_q_value(state_key, action)
        
        # Find max Q-value for next state
        if next_legal_actions:
            max_next_q = max(
                self.get_q_value(next_state_key, next_action)
                for next_action in next_legal_actions
            )
        else:
            max_next_q = 0.0  # Terminal state
        
        # Q-learning update
        new_q = current_q + self.learning_rate * (
            reward + self.discount_factor * max_next_q - current_q
        )
        
        self.q_table[state_key][action] = new_q
    
    def choose_action(self, state: dict, training: bool = True) -> Tuple[int, int]:
        """
        Choose action using epsilon-greedy policy.
        
        Args:
            state: Current game state
            training: If True, use exploration; if False, be greedy
            
        Returns:
            Action (row, col)
        """
        legal_actions = state['legal_moves']
        
        if not legal_actions:
            raise ValueError("No legal actions available")
        
        state_key = self.get_state_key(state)
        
        # Epsilon-greedy exploration
        if training and random.random() < self.epsilon:
            # Explore: random action
            action = random.choice(legal_actions)
        else:
            # Exploit: best known action
            q_values = {
                action: self.get_q_value(state_key, action)
                for action in legal_actions
            }
            
            # Choose action with highest Q-value
            max_q = max(q_values.values())
            best_actions = [a for a, q in q_values.items() if q == max_q]
            action = random.choice(best_actions)
        
        return action
    
    def record_transition(self, state_key: str, action: Tuple[int, int], 
                         reward: float):
        """Record state-action-reward for episode."""
        self.episode_history.append((state_key, action, reward))
    
    def learn_from_episode(self, final_reward: float):
        """
        Learn from complete episode using temporal difference.
        
        Args:
            final_reward: Reward at end of game (+1 win, 0 draw, -1 loss)
        """
        # Backward pass through episode
        for i in range(len(self.episode_history) - 1, -1, -1):
            state_key, action, immediate_reward = self.episode_history[i]
            
            # Use final reward for last move, 0 for others
            reward = final_reward if i == len(self.episode_history) - 1 else 0.0
            
            # Get next state (if exists)
            if i < len(self.episode_history) - 1:
                next_state_key = self.episode_history[i + 1][0]
                # Approximate next legal actions (not perfect but works)
                next_legal_actions = list(self.q_table.get(next_state_key, {}).keys())
            else:
                next_state_key = state_key
                next_legal_actions = []
            
            # Update Q-value
            self.update_q_value(state_key, action, reward, 
                              next_state_key, next_legal_actions)
        
        # Clear episode history
        self.episode_history = []
        
        # Store in CVM temporal memory
        self.cvm.temporal_memory.store(
            f"game_{self.games_played}",
            final_reward
        )
    
    def update_statistics(self, result: float):
        """Update win/loss/draw statistics."""
        self.games_played += 1
        if result > 0:
            self.wins += 1
        elif result < 0:
            self.losses += 1
        else:
            self.draws += 1
    
    def get_win_rate(self) -> float:
        """Calculate win rate."""
        if self.games_played == 0:
            return 0.0
        return self.wins / self.games_played
    
    def get_stats(self) -> dict:
        """Get agent statistics."""
        return {
            'games_played': self.games_played,
            'wins': self.wins,
            'losses': self.losses,
            'draws': self.draws,
            'win_rate': self.get_win_rate(),
            'states_learned': len(self.q_table)
        }


class TicTacToeTrainer:
    """Trainer for self-play learning."""
    
    def __init__(self):
        """Initialize trainer."""
        self.env = TicTacToeEnvironment()
    
    def play_game(self, agent1: TicTacToeAgent, agent2: TicTacToeAgent,
                  training: bool = True) -> dict:
        """
        Play one game between two agents.
        
        Args:
            agent1: First agent (plays X)
            agent2: Second agent (plays O)
            training: Whether agents should learn
            
        Returns:
            Game results dict
        """
        state = self.env.reset()
        agents = {Player.X: agent1, Player.O: agent2}
        
        # Play until game ends
        while not state['game_over']:
            current_agent = agents[state['current_player']]
            
            # Choose and execute action
            action = current_agent.choose_action(state, training)
            state_key = current_agent.get_state_key(state)
            
            new_state, reward, done = self.env.take_action(action)
            
            # Record transition
            if training:
                current_agent.record_transition(state_key, action, reward)
            
            state = new_state
        
        # Determine rewards from each agent's perspective
        winner = self.env.winner
        if winner == Player.X:
            agent1_reward = 1.0
            agent2_reward = -1.0
        elif winner == Player.O:
            agent1_reward = -1.0
            agent2_reward = 1.0
        else:  # Draw
            agent1_reward = 0.0
            agent2_reward = 0.0
        
        # Learn from episode
        if training:
            agent1.learn_from_episode(agent1_reward)
            agent2.learn_from_episode(agent2_reward)
        
        # Update statistics
        agent1.update_statistics(agent1_reward)
        agent2.update_statistics(agent2_reward)
        
        return {
            'winner': winner,
            'agent1_reward': agent1_reward,
            'agent2_reward': agent2_reward,
            'moves': len(self.env.board.move_history)
        }
    
    def train(self, agent1: TicTacToeAgent, agent2: TicTacToeAgent,
              num_games: int = 1000) -> dict:
        """
        Train agents through self-play.
        
        Args:
            agent1: First agent
            agent2: Second agent
            num_games: Number of games to play
            
        Returns:
            Training results
        """
        results = []
        
        for game in range(num_games):
            result = self.play_game(agent1, agent2, training=True)
            results.append(result)
        
        return {
            'num_games': num_games,
            'agent1_stats': agent1.get_stats(),
            'agent2_stats': agent2.get_stats(),
            'results': results
        }


if __name__ == "__main__":
    print("Tic-Tac-Toe Agent Test")
    print("=" * 50)
    print()
    
    # Create agents
    agent1 = TicTacToeAgent("Agent 1")
    agent2 = TicTacToeAgent("Agent 2")
    
    # Train through self-play
    print("Training agents through self-play...")
    trainer = TicTacToeTrainer()
    results = trainer.train(agent1, agent2, num_games=100)
    
    print("\nTraining Results:")
    print(f"Agent 1: {results['agent1_stats']}")
    print(f"Agent 2: {results['agent2_stats']}")
    print(f"\nAgent 1 learned {len(agent1.q_table)} states")
    print(f"Agent 2 learned {len(agent2.q_table)} states")
