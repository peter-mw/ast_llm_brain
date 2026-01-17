"""
Snake Game Module
=================

Classic Snake game implementation with learning agents.

Classes:
    SnakeEnvironment: Game environment
    SnakeAgent: Learning agent with spatial reasoning
    SnakeTrainer: Self-play trainer
    Direction: Movement directions enum
"""

from cvm.games.snake.game import SnakeEnvironment, Direction
from cvm.games.snake.agent import SnakeAgent, SnakeTrainer

__all__ = ["SnakeEnvironment", "Direction", "SnakeAgent", "SnakeTrainer"]
