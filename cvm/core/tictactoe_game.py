"""
Tic-Tac-Toe Game Environment for CVM Learning
==============================================

Complete tic-tac-toe implementation for agent learning.
"""

from enum import Enum
from typing import List, Tuple, Optional
import random


class Player(Enum):
    """Player markers."""
    X = 1
    O = -1
    EMPTY = 0


class GameResult(Enum):
    """Game outcome."""
    X_WINS = 1
    O_WINS = -1
    DRAW = 0
    IN_PROGRESS = None


class TicTacToeBoard:
    """3x3 Tic-Tac-Toe board."""
    
    def __init__(self):
        """Initialize empty board."""
        self.board = [[Player.EMPTY for _ in range(3)] for _ in range(3)]
        self.move_history = []
    
    def reset(self):
        """Reset board to empty state."""
        self.board = [[Player.EMPTY for _ in range(3)] for _ in range(3)]
        self.move_history = []
    
    def copy(self) -> 'TicTacToeBoard':
        """Create a copy of the board."""
        new_board = TicTacToeBoard()
        new_board.board = [row[:] for row in self.board]
        new_board.move_history = self.move_history[:]
        return new_board
    
    def get_cell(self, row: int, col: int) -> Player:
        """Get value at position."""
        return self.board[row][col]
    
    def set_cell(self, row: int, col: int, player: Player):
        """Set value at position."""
        self.board[row][col] = player
        self.move_history.append((row, col, player))
    
    def is_valid_move(self, row: int, col: int) -> bool:
        """Check if move is valid."""
        return (0 <= row < 3 and 
                0 <= col < 3 and 
                self.board[row][col] == Player.EMPTY)
    
    def get_empty_cells(self) -> List[Tuple[int, int]]:
        """Get list of empty cell positions."""
        empty = []
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == Player.EMPTY:
                    empty.append((row, col))
        return empty
    
    def is_full(self) -> bool:
        """Check if board is full."""
        return len(self.get_empty_cells()) == 0
    
    def check_winner(self) -> Optional[Player]:
        """
        Check if there's a winner.
        Returns Player.X, Player.O, or None.
        """
        # Check rows
        for row in range(3):
            if (self.board[row][0] == self.board[row][1] == self.board[row][2] 
                and self.board[row][0] != Player.EMPTY):
                return self.board[row][0]
        
        # Check columns
        for col in range(3):
            if (self.board[0][col] == self.board[1][col] == self.board[2][col] 
                and self.board[0][col] != Player.EMPTY):
                return self.board[0][col]
        
        # Check diagonals
        if (self.board[0][0] == self.board[1][1] == self.board[2][2] 
            and self.board[0][0] != Player.EMPTY):
            return self.board[0][0]
        
        if (self.board[0][2] == self.board[1][1] == self.board[2][0] 
            and self.board[0][2] != Player.EMPTY):
            return self.board[0][2]
        
        return None
    
    def get_result(self) -> GameResult:
        """Get current game result."""
        winner = self.check_winner()
        if winner == Player.X:
            return GameResult.X_WINS
        elif winner == Player.O:
            return GameResult.O_WINS
        elif self.is_full():
            return GameResult.DRAW
        else:
            return GameResult.IN_PROGRESS
    
    def __str__(self) -> str:
        """String representation of board."""
        symbols = {Player.X: 'X', Player.O: 'O', Player.EMPTY: '.'}
        lines = []
        lines.append("  0 1 2")
        for i, row in enumerate(self.board):
            row_str = f"{i} " + " ".join(symbols[cell] for cell in row)
            lines.append(row_str)
        return "\n".join(lines)
    
    def to_compact_string(self) -> str:
        """Compact string for display."""
        symbols = {Player.X: 'X', Player.O: 'O', Player.EMPTY: '.'}
        rows = []
        for row in self.board:
            rows.append("".join(symbols[cell] for cell in row))
        return " | ".join(rows)


class TicTacToeEnvironment:
    """
    Tic-Tac-Toe game environment for agent interaction.
    
    Provides:
    - Game state management
    - Legal move validation
    - Win/draw detection
    - Reward calculation
    """
    
    def __init__(self):
        """Initialize environment."""
        self.board = TicTacToeBoard()
        self.current_player = Player.X
        self.game_over = False
        self.winner = None
    
    def reset(self) -> dict:
        """
        Reset game to initial state.
        
        Returns:
            Initial state dictionary
        """
        self.board.reset()
        self.current_player = Player.X
        self.game_over = False
        self.winner = None
        return self.get_state()
    
    def get_state(self) -> dict:
        """
        Get current game state.
        
        Returns:
            State dict with board, player, legal moves
        """
        return {
            'board': self.board.copy(),
            'current_player': self.current_player,
            'legal_moves': self.get_legal_moves(),
            'game_over': self.game_over,
            'winner': self.winner
        }
    
    def get_legal_moves(self) -> List[Tuple[int, int]]:
        """Get list of legal moves (empty cells)."""
        if self.game_over:
            return []
        return self.board.get_empty_cells()
    
    def take_action(self, action: Tuple[int, int]) -> Tuple[dict, float, bool]:
        """
        Execute a move.
        
        Args:
            action: (row, col) tuple
            
        Returns:
            (new_state, reward, done) tuple
        """
        row, col = action
        
        # Validate move
        if self.game_over:
            raise ValueError("Game is over")
        
        if not self.board.is_valid_move(row, col):
            raise ValueError(f"Invalid move: ({row}, {col})")
        
        # Make move
        self.board.set_cell(row, col, self.current_player)
        
        # Check for game end
        result = self.board.get_result()
        
        if result != GameResult.IN_PROGRESS:
            self.game_over = True
            self.winner = self.board.check_winner()
            
            # Calculate reward from current player's perspective
            if result == GameResult.DRAW:
                reward = 0.0
            elif result == GameResult.X_WINS:
                reward = 1.0 if self.current_player == Player.X else -1.0
            else:  # O wins
                reward = 1.0 if self.current_player == Player.O else -1.0
        else:
            reward = 0.0  # No reward for ongoing game
        
        # Switch player
        self.current_player = (Player.O if self.current_player == Player.X 
                              else Player.X)
        
        return self.get_state(), reward, self.game_over
    
    def render(self):
        """Display current board."""
        print(self.board)
        print()


def play_random_game():
    """Play a game with random moves (for testing)."""
    env = TicTacToeEnvironment()
    state = env.reset()
    
    print("Playing random game:\n")
    env.render()
    
    while not state['game_over']:
        legal_moves = state['legal_moves']
        action = random.choice(legal_moves)
        
        print(f"Player {state['current_player'].name} plays: {action}")
        state, reward, done = env.take_action(action)
        env.render()
    
    result = env.board.get_result()
    if result == GameResult.DRAW:
        print("Game ended in a DRAW")
    else:
        print(f"Winner: {env.winner.name}")
    
    return result


if __name__ == "__main__":
    print("Tic-Tac-Toe Environment Test")
    print("=" * 50)
    print()
    
    # Play a few random games
    results = {GameResult.X_WINS: 0, GameResult.O_WINS: 0, GameResult.DRAW: 0}
    
    for i in range(5):
        print(f"\n{'='*50}")
        print(f"Game {i+1}")
        print('='*50)
        result = play_random_game()
        results[result] += 1
    
    print(f"\n{'='*50}")
    print("Results Summary:")
    print(f"X wins: {results[GameResult.X_WINS]}")
    print(f"O wins: {results[GameResult.O_WINS]}")
    print(f"Draws: {results[GameResult.DRAW]}")
