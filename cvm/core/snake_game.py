"""
Snake Game Environment for CVM Learning
========================================

Classic Snake game implementation for agent learning.
"""

from enum import Enum
from typing import List, Tuple, Optional
import random


class Direction(Enum):
    """Movement directions."""
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)


class SnakeEnvironment:
    """
    Snake game environment.
    
    Rules:
    - Snake moves continuously in current direction
    - Eating food makes snake grow
    - Hitting wall or self ends game
    - Goal: Eat as much food as possible
    """
    
    def __init__(self, width: int = 10, height: int = 10):
        """
        Initialize environment.
        
        Args:
            width: Board width
            height: Board height
        """
        self.width = width
        self.height = height
        
        # Game state
        self.snake: List[Tuple[int, int]] = []
        self.direction: Direction = Direction.RIGHT
        self.food: Optional[Tuple[int, int]] = None
        self.score = 0
        self.steps = 0
        self.game_over = False
        
        # For starvation prevention
        self.max_steps_without_food = width * height * 2
        self.steps_since_food = 0
        
        self.reset()
    
    def reset(self) -> dict:
        """
        Reset game to initial state.
        
        Returns:
            Initial state dictionary
        """
        # Start snake in middle
        start_x = self.width // 2
        start_y = self.height // 2
        
        self.snake = [(start_x, start_y)]
        self.direction = Direction.RIGHT
        self.score = 0
        self.steps = 0
        self.steps_since_food = 0
        self.game_over = False
        
        self._place_food()
        
        return self.get_state()
    
    def _place_food(self):
        """Place food at random empty location."""
        empty_cells = []
        for x in range(self.width):
            for y in range(self.height):
                if (x, y) not in self.snake:
                    empty_cells.append((x, y))
        
        if empty_cells:
            self.food = random.choice(empty_cells)
        else:
            self.food = None  # Board full (snake won!)
    
    def get_state(self) -> dict:
        """
        Get current game state.
        
        Returns:
            State dictionary with snake, food, score, etc.
        """
        head = self.snake[0]
        
        # Calculate relative food position
        if self.food:
            food_dx = self.food[0] - head[0]
            food_dy = self.food[1] - head[1]
        else:
            food_dx, food_dy = 0, 0
        
        # Check for obstacles in each direction
        obstacles = {
            Direction.UP: self._is_obstacle(head[0], head[1] - 1),
            Direction.DOWN: self._is_obstacle(head[0], head[1] + 1),
            Direction.LEFT: self._is_obstacle(head[0] - 1, head[1]),
            Direction.RIGHT: self._is_obstacle(head[0] + 1, head[1])
        }
        
        return {
            'snake': self.snake[:],
            'direction': self.direction,
            'food': self.food,
            'score': self.score,
            'steps': self.steps,
            'game_over': self.game_over,
            'head': head,
            'food_direction': (food_dx, food_dy),
            'obstacles': obstacles,
            'board_size': (self.width, self.height)
        }
    
    def _is_obstacle(self, x: int, y: int) -> bool:
        """Check if position is obstacle (wall or snake body)."""
        # Wall
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return True
        
        # Snake body
        if (x, y) in self.snake:
            return True
        
        return False
    
    def get_legal_actions(self) -> List[Direction]:
        """
        Get legal actions (can't reverse direction).
        
        Returns:
            List of valid directions
        """
        if self.game_over:
            return []
        
        # Can't go opposite direction
        opposite = {
            Direction.UP: Direction.DOWN,
            Direction.DOWN: Direction.UP,
            Direction.LEFT: Direction.RIGHT,
            Direction.RIGHT: Direction.LEFT
        }
        
        legal = [d for d in Direction if d != opposite[self.direction]]
        return legal
    
    def step(self, action: Direction) -> Tuple[dict, float, bool]:
        """
        Execute one game step.
        
        Args:
            action: Direction to move
            
        Returns:
            (new_state, reward, done) tuple
        """
        if self.game_over:
            return self.get_state(), 0.0, True
        
        # Update direction (if legal)
        legal_actions = self.get_legal_actions()
        if action in legal_actions:
            self.direction = action
        
        # Move snake
        head_x, head_y = self.snake[0]
        dx, dy = self.direction.value
        new_head = (head_x + dx, head_y + dy)
        
        # Check collision
        if self._is_obstacle(new_head[0], new_head[1]):
            self.game_over = True
            return self.get_state(), -10.0, True  # Large penalty for dying
        
        # Move snake
        self.snake.insert(0, new_head)
        
        # Check if food eaten
        reward = 0.0
        if new_head == self.food:
            self.score += 1
            self.steps_since_food = 0
            reward = 10.0  # Large reward for food
            self._place_food()
        else:
            # Remove tail (snake moves)
            self.snake.pop()
            reward = 0.0  # Small reward for surviving
        
        self.steps += 1
        self.steps_since_food += 1
        
        # Check starvation (prevents infinite loops)
        if self.steps_since_food >= self.max_steps_without_food:
            self.game_over = True
            reward = -10.0  # Penalty for starvation
        
        return self.get_state(), reward, self.game_over
    
    def render(self, compact: bool = False):
        """
        Display current game state.
        
        Args:
            compact: If True, use compact one-line display
        """
        if compact:
            print(f"Score: {self.score} | Steps: {self.steps} | Length: {len(self.snake)}")
            return
        
        # Create board
        board = [['.' for _ in range(self.width)] for _ in range(self.height)]
        
        # Place snake body
        for i, (x, y) in enumerate(self.snake):
            if i == 0:
                board[y][x] = 'H'  # Head
            else:
                board[y][x] = 'O'  # Body
        
        # Place food
        if self.food:
            fx, fy = self.food
            board[fy][fx] = 'F'
        
        # Print board
        print('+' + '-' * self.width + '+')
        for row in board:
            print('|' + ''.join(row) + '|')
        print('+' + '-' * self.width + '+')
        print(f"Score: {self.score} | Steps: {self.steps} | Direction: {self.direction.name}")
        print()


def play_random_game(width: int = 10, height: int = 10, max_steps: int = 200):
    """Play a game with random moves."""
    env = SnakeEnvironment(width, height)
    state = env.reset()
    
    print("Playing random snake game:")
    print(f"Board: {width}x{height}\n")
    
    step_count = 0
    while not state['game_over'] and step_count < max_steps:
        # Random action
        legal_actions = env.get_legal_actions()
        if not legal_actions:
            break
        
        action = random.choice(legal_actions)
        state, reward, done = env.step(action)
        step_count += 1
    
    env.render()
    
    print(f"Game Over! Final score: {state['score']}")
    print(f"Snake length: {len(state['snake'])}")
    print(f"Steps taken: {step_count}")
    
    return state['score']


if __name__ == "__main__":
    print("Snake Game Environment Test")
    print("=" * 50)
    print()
    
    # Play a few random games
    scores = []
    for i in range(5):
        print(f"\nGame {i+1}")
        print("-" * 50)
        score = play_random_game(width=8, height=8, max_steps=100)
        scores.append(score)
    
    print(f"\n{'='*50}")
    print("Results Summary:")
    print(f"Average score: {sum(scores) / len(scores):.1f}")
    print(f"Best score: {max(scores)}")
    print(f"Worst score: {min(scores)}")
