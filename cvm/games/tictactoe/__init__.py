"""
Tic-Tac-Toe Game Module
========================

Tic-Tac-Toe implementation with Q-learning agents.

Classes:
    TicTacToeEnvironment: Game environment
    TicTacToeBoard: Board representation
    TicTacToeAgent: Learning agent
    TicTacToeTrainer: Self-play trainer
    Player: Player markers enum
"""

from cvm.games.tictactoe.game import (
    TicTacToeEnvironment,
    TicTacToeBoard,
    Player,
    GameResult,
)
from cvm.games.tictactoe.agent import TicTacToeAgent, TicTacToeTrainer

__all__ = [
    "TicTacToeEnvironment",
    "TicTacToeBoard",
    "Player",
    "GameResult",
    "TicTacToeAgent",
    "TicTacToeTrainer",
]
