# CVM Quick Start

## Installation

```bash
# Install from source (editable mode for development)
pip install -e .

# Or install specific features
pip install -e ".[visual]"  # Visual memory support
pip install -e ".[games]"   # Games with numpy
pip install -e ".[dev]"     # Development tools
pip install -e ".[all]"     # Everything
```

## Basic Usage

```python
from cvm import CVM
from cvm.core.compiler import parse

# Create cognitive virtual machine
vm = CVM()

# Think about math
result = vm.think(parse("2 + 3"))
print(result)
```

## Play Games

```python
# Poker
from cvm.games.poker import PokerAgent, PokerTrainer
agent = PokerAgent("AI")
trainer = PokerTrainer()
trainer.train(agent, PokerAgent("Opponent"), num_hands=500)
print(f"Win rate: {agent.get_win_rate():.1%}")

# Snake
from cvm.games.snake import SnakeAgent, SnakeTrainer
agent = SnakeAgent("Bot")
trainer = SnakeTrainer(10, 10)
trainer.train(agent, num_games=500)
print(f"Avg score: {agent.get_average_score():.2f}")

# Tic-Tac-Toe
from cvm.games.tictactoe import TicTacToeAgent, TicTacToeTrainer
agent = TicTacToeAgent("AI")
trainer = TicTacToeTrainer()
trainer.train(agent, TicTacToeAgent("Opp"), num_games=500)
print(f"Win rate: {agent.get_win_rate():.1%}")
```

## Run Examples

```bash
python examples/main.py poker
python examples/main.py snake
python examples/main.py tictactoe
```

## CLI

```bash
cvm version  # Show version
cvm help     # Show help
```

## Run Tests

```bash
pytest              # Run all tests
pytest -v           # Verbose
pytest --cov=cvm    # With coverage
```

## Development

```bash
# Format code
black cvm/

# Check style
flake8 cvm/

# Build package
python -m build

# Install locally
pip install -e .
```

## Next Steps

- Read [docs/USAGE.md](docs/USAGE.md) for detailed examples
- Check [docs/INSTALLATION.md](docs/INSTALLATION.md) for troubleshooting
- Explore [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) to understand the design
- Try [examples/](examples/) for demonstrations

**The CVM is ready to use!** 🚀
