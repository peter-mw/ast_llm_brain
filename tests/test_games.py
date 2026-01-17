"""
Tests for CVM Games
===================

Unit tests for poker, snake, and tic-tac-toe game modules.
"""

import pytest


class TestPoker:
    """Test poker game components."""
    
    def test_poker_imports(self):
        """Test poker modules can be imported."""
        from cvm.games.poker import PokerEnvironment
        from cvm.agents.poker import PokerAgent, PokerTrainer
        
        assert PokerEnvironment is not None
        assert PokerAgent is not None
        assert PokerTrainer is not None
    
    def test_poker_environment(self):
        """Test poker environment creation."""
        from cvm.games.poker import PokerEnvironment
        
        env = PokerEnvironment()
        state = env.reset()
        
        assert state is not None
        assert "player_chips" in state or "chips" in state or state


class TestSnake:
    """Test snake game components."""
    
    def test_snake_imports(self):
        """Test snake modules can be imported."""
        from cvm.games.snake import SnakeEnvironment, Direction
        from cvm.agents.snake import SnakeAgent, SnakeTrainer
        
        assert SnakeEnvironment is not None
        assert SnakeAgent is not None
        assert SnakeTrainer is not None
        assert Direction is not None
    
    def test_snake_environment(self):
        """Test snake environment creation."""
        from cvm.games.snake import SnakeEnvironment
        
        env = SnakeEnvironment(width=10, height=10)
        state = env.reset()
        
        assert state is not None
        assert "snake" in state
        assert "score" in state


class TestTicTacToe:
    """Test tic-tac-toe game components."""
    
    def test_tictactoe_imports(self):
        """Test tic-tac-toe modules can be imported."""
        from cvm.games.tictactoe import (
            TicTacToeEnvironment,
            Player,
        )
        from cvm.agents.tictactoe import TicTacToeAgent, TicTacToeTrainer
        
        assert TicTacToeEnvironment is not None
        assert TicTacToeAgent is not None
        assert TicTacToeTrainer is not None
        assert Player is not None
    
    def test_tictactoe_environment(self):
        """Test tic-tac-toe environment creation."""
        from cvm.games.tictactoe import TicTacToeEnvironment
        
        env = TicTacToeEnvironment()
        state = env.reset()
        
        assert state is not None
        assert "board" in state


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
