"""
Snake Learning Agent
====================

Agent that learns to play Snake using CVM Phase IV architecture.
Uses Q-learning with state abstraction for spatial reasoning.
"""

from typing import Dict, List, Tuple
import random
from cvm.core.cvm_phase4 import CVM
from cvm.core.snake_game import SnakeEnvironment, Direction


class SnakeAgent:
    """
    Agent that learns to play Snake.
    
    Uses:
    - Q-learning for action values
    - State abstraction (relative positions, obstacles)
    - CVM Phase IV for memory and planning
    """
    
    def __init__(self, name: str = "SnakeAgent", board_size: Tuple[int, int] = (10, 10)):
        """
        Initialize agent.
        
        Args:
            name: Agent identifier
            board_size: (width, height) of game board
        """
        self.name = name
        self.board_size = board_size
        self.cvm = CVM()
        
        # Q-table: state_key -> {action: value}
        self.q_table: Dict[str, Dict[Direction, float]] = {}
        
        # Learning parameters
        self.learning_rate = 0.1
        self.discount_factor = 0.95
        self.epsilon = 0.2  # Exploration rate
        
        # Statistics
        self.games_played = 0
        self.total_score = 0
        self.best_score = 0
        self.total_steps = 0
        
        # Episode memory
        self.episode_history: List[Tuple[str, Direction, float]] = []
    
    def get_state_key(self, state: dict) -> str:
        """
        Abstract game state to compact representation.
        
        Focuses on:
        - Food direction (8 directions)
        - Immediate obstacles (4 directions)
        - Current direction
        
        This abstraction makes learning tractable.
        """
        head = state['head']
        food = state['food']
        obstacles = state['obstacles']
        current_dir = state['direction']
        
        # Food direction (relative)
        if food:
            dx = food[0] - head[0]
            dy = food[1] - head[1]
            
            # Discretize to 8 directions
            if dx == 0 and dy < 0:
                food_dir = 'N'
            elif dx == 0 and dy > 0:
                food_dir = 'S'
            elif dx < 0 and dy == 0:
                food_dir = 'W'
            elif dx > 0 and dy == 0:
                food_dir = 'E'
            elif dx < 0 and dy < 0:
                food_dir = 'NW'
            elif dx > 0 and dy < 0:
                food_dir = 'NE'
            elif dx < 0 and dy > 0:
                food_dir = 'SW'
            elif dx > 0 and dy > 0:
                food_dir = 'SE'
            else:
                food_dir = 'C'  # On food (shouldn't happen)
        else:
            food_dir = 'NONE'
        
        # Obstacles (binary encoding)
        obs_up = '1' if obstacles[Direction.UP] else '0'
        obs_down = '1' if obstacles[Direction.DOWN] else '0'
        obs_left = '1' if obstacles[Direction.LEFT] else '0'
        obs_right = '1' if obstacles[Direction.RIGHT] else '0'
        
        # Current direction
        dir_str = current_dir.name[0]  # U/D/L/R
        
        # Combine into state key
        state_key = f"{food_dir}_{obs_up}{obs_down}{obs_left}{obs_right}_{dir_str}"
        
        return state_key
    
    def get_q_value(self, state_key: str, action: Direction) -> float:
        """Get Q-value for state-action pair."""
        if state_key not in self.q_table:
            self.q_table[state_key] = {}
        
        if action not in self.q_table[state_key]:
            self.q_table[state_key][action] = 0.0
        
        return self.q_table[state_key][action]
    
    def update_q_value(self, state_key: str, action: Direction,
                       reward: float, next_state_key: str,
                       next_legal_actions: List[Direction]):
        """
        Update Q-value using Q-learning.
        
        Q(s,a) ← Q(s,a) + α[r + γ max_a' Q(s',a') - Q(s,a)]
        """
        current_q = self.get_q_value(state_key, action)
        
        # Find max Q-value for next state
        if next_legal_actions and not reward < 0:  # If not terminal
            max_next_q = max(
                self.get_q_value(next_state_key, next_action)
                for next_action in next_legal_actions
            )
        else:
            max_next_q = 0.0
        
        # Q-learning update
        new_q = current_q + self.learning_rate * (
            reward + self.discount_factor * max_next_q - current_q
        )
        
        self.q_table[state_key][action] = new_q
    
    def choose_action(self, state: dict, training: bool = True) -> Direction:
        """
        Choose action using epsilon-greedy policy.
        
        Args:
            state: Current game state
            training: If True, explore; if False, exploit
            
        Returns:
            Direction to move
        """
        legal_actions = [d for d in Direction]  # All directions
        state_key = self.get_state_key(state)
        
        # Epsilon-greedy
        if training and random.random() < self.epsilon:
            # Explore
            action = random.choice(legal_actions)
        else:
            # Exploit
            q_values = {
                action: self.get_q_value(state_key, action)
                for action in legal_actions
            }
            
            max_q = max(q_values.values())
            best_actions = [a for a, q in q_values.items() if q == max_q]
            action = random.choice(best_actions)
        
        return action
    
    def record_transition(self, state_key: str, action: Direction, reward: float):
        """Record transition for episode learning."""
        self.episode_history.append((state_key, action, reward))
    
    def learn_from_episode(self):
        """Learn from complete episode using temporal difference."""
        # Backward pass through episode
        for i in range(len(self.episode_history) - 1, -1, -1):
            state_key, action, reward = self.episode_history[i]
            
            # Get next state
            if i < len(self.episode_history) - 1:
                next_state_key = self.episode_history[i + 1][0]
                next_legal_actions = list(Direction)
            else:
                next_state_key = state_key
                next_legal_actions = []
            
            # Update Q-value
            self.update_q_value(state_key, action, reward,
                              next_state_key, next_legal_actions)
        
        # Clear history
        self.episode_history = []
    
    def update_statistics(self, score: int, steps: int):
        """Update agent statistics."""
        self.games_played += 1
        self.total_score += score
        self.total_steps += steps
        
        if score > self.best_score:
            self.best_score = score
        
        # Store in CVM temporal memory
        self.cvm.temporal_memory.store(f"game_{self.games_played}", score)
    
    def get_average_score(self) -> float:
        """Calculate average score."""
        if self.games_played == 0:
            return 0.0
        return self.total_score / self.games_played
    
    def get_stats(self) -> dict:
        """Get agent statistics."""
        return {
            'games_played': self.games_played,
            'total_score': self.total_score,
            'average_score': self.get_average_score(),
            'best_score': self.best_score,
            'total_steps': self.total_steps,
            'states_learned': len(self.q_table)
        }


class SnakeTrainer:
    """Trainer for Snake agent."""
    
    def __init__(self, width: int = 10, height: int = 10):
        """
        Initialize trainer.
        
        Args:
            width: Board width
            height: Board height
        """
        self.env = SnakeEnvironment(width, height)
    
    def play_game(self, agent: SnakeAgent, training: bool = True,
                  max_steps: int = 1000) -> dict:
        """
        Play one game.
        
        Args:
            agent: Agent to play
            training: Whether to learn
            max_steps: Maximum steps per game
            
        Returns:
            Game results
        """
        state = self.env.reset()
        step_count = 0
        
        while not state['game_over'] and step_count < max_steps:
            # Choose action
            action = agent.choose_action(state, training)
            state_key = agent.get_state_key(state)
            
            # Take action
            new_state, reward, done = self.env.step(action)
            
            # Record transition
            if training:
                agent.record_transition(state_key, action, reward)
            
            state = new_state
            step_count += 1
        
        # Learn from episode
        if training:
            agent.learn_from_episode()
        
        # Update statistics
        agent.update_statistics(state['score'], step_count)
        
        return {
            'score': state['score'],
            'steps': step_count,
            'snake_length': len(state['snake'])
        }
    
    def train(self, agent: SnakeAgent, num_games: int = 100) -> dict:
        """
        Train agent.
        
        Args:
            agent: Agent to train
            num_games: Number of games to play
            
        Returns:
            Training results
        """
        results = []
        
        for game in range(num_games):
            result = self.play_game(agent, training=True)
            results.append(result)
        
        return {
            'num_games': num_games,
            'agent_stats': agent.get_stats(),
            'results': results
        }


if __name__ == "__main__":
    print("Snake Agent Test")
    print("=" * 50)
    print()
    
    # Create and train agent
    agent = SnakeAgent("TestAgent", board_size=(8, 8))
    trainer = SnakeTrainer(width=8, height=8)
    
    print("Training agent (100 games)...")
    results = trainer.train(agent, num_games=100)
    
    print("\nTraining Results:")
    stats = results['agent_stats']
    print(f"Games played: {stats['games_played']}")
    print(f"Average score: {stats['average_score']:.2f}")
    print(f"Best score: {stats['best_score']}")
    print(f"States learned: {stats['states_learned']}")
