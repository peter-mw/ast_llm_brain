# Usage Guide

## Basic Usage

### Import and Create CVM

```python
from cvm import CVM
from cvm.core.compiler import parse

# Create a cognitive virtual machine
vm = CVM()

# Parse and think about an expression
ast = parse("2 + 3")
result = vm.think(ast)

print(result)
```

### Working with ASTs

```python
from cvm import Node, Executor

# Create AST manually
ast = Node("Add", inputs=[
    Node("Number", 10),
    Node("Number", 20)
])

# Execute AST
executor = Executor()
result = executor.eval(ast)
print(f"Result: {result}")  # Output: Result: 30
```

### Verification

```python
from cvm import Verifier, Node

verifier = Verifier()

# Verify transformation is valid
before = Node("Add", inputs=[Node("Number", 1), Node("Number", 2)])
after = Node("Number", 3)

is_valid = verifier.verify(before, after)
print(f"Valid transformation: {is_valid}")  # True
```

## Games

### Playing Poker

```python
from cvm.games.poker import PokerAgent, PokerTrainer

# Create and train agent
agent = PokerAgent("MyAgent")
trainer = PokerTrainer()

# Train through self-play
opponent = PokerAgent("Opponent")
results = trainer.train(agent, opponent, num_hands=500)

# Check performance
stats = agent.get_stats()
print(f"Win rate: {stats['win_rate']:.1%}")
print(f"Strategy size: {len(agent.strategy)} states")
```

### Playing Snake

```python
from cvm.games.snake import SnakeAgent, SnakeTrainer

# Create agent
agent = SnakeAgent("SnakeBot", board_size=(10, 10))
trainer = SnakeTrainer(width=10, height=10)

# Train
trainer.train(agent, num_games=500)

# View results
stats = agent.get_stats()
print(f"Average score: {stats['average_score']:.2f}")
print(f"Best score: {stats['best_score']}")
```

### Playing Tic-Tac-Toe

```python
from cvm.games.tictactoe import TicTacToeAgent, TicTacToeTrainer

# Create agent
agent = TicTacToeAgent("TicTacBot")
trainer = TicTacToeTrainer()

# Train through self-play
opponent = TicTacToeAgent("Opponent")
trainer.train(agent, opponent, num_games=500)

# Check win rate
print(f"Win rate: {agent.get_win_rate():.1%}")
```

## Advanced Usage

### Goal-Directed Planning

```python
from cvm import CVM
from cvm.core.environment import Environment
from cvm.core.actions import Action
from cvm.core.goals import Goal

# Create environment
env = Environment({"position": 0, "target": 10})

# Define actions
actions = [
    Action("move_forward", lambda s: {**s, "position": s["position"] + 1}),
    Action("move_backward", lambda s: {**s, "position": s["position"] - 1}),
]

# Define goal
goal = Goal("reach target", lambda s: -abs(s["position"] - s["target"]))

# Create agent and plan
agent = CVM()
trajectory = agent.plan_and_execute(env, actions, goal, steps=10)
```

### Distributed Cognition

```python
from cvm.core.mesh import CognitiveMesh
from cvm import CVM
from cvm.core.compiler import parse

# Create mesh
mesh = CognitiveMesh()

# Add agents
for i in range(3):
    mesh.add_node(CVM())

# Get consensus
result = mesh.consensus(parse("5 + 5"))
print(f"Consensus: {result}")

# Broadcast learning
mesh.broadcast_rule("Add(a,b) -> Number(a+b)")
```

## Running Examples

The `examples/` directory contains demonstration scripts:

```bash
# Run Phase I demo
python examples/demo_phase1.py

# Run Phase II demo
python examples/demo_phase2.py

# Run Phase III demo
python examples/demo_phase3.py

# Run Phase IV demo
python examples/demo_phase4.py

# Run poker demo
python examples/demo_poker_auto.py

# Run snake demo
python examples/demo_snake_auto.py

# Run tic-tac-toe demo
python examples/demo_tictactoe_auto.py

# Run main menu
python examples/main.py poker
python examples/main.py snake
python examples/main.py tictactoe
```

## CLI Usage

After installation, you can use the `cvm` command:

```bash
# Show version
cvm version

# Show help
cvm help

# Run demos
cvm demo
```

## API Reference

For complete API documentation, see:

- [Core API](API.md)
- [Games API](GAMES_API.md)
- [Examples](../examples/)

## Best Practices

1. **Always verify transformations**: Use `Verifier` to ensure correctness
2. **Start with small ASTs**: Build complexity gradually
3. **Use type hints**: Add type annotations for better IDE support
4. **Test thoroughly**: Write tests for custom components
5. **Profile performance**: Use `cProfile` for optimization

## Troubleshooting

### Common Issues

**Import errors:**
- Ensure package is installed: `pip install -e .`
- Check Python version: `python --version` (requires 3.8+)

**Game training slow:**
- Reduce number of training games
- Use smaller board sizes for Snake
- Consider using numpy for faster computation

**Memory issues:**
- Clear temporal memory periodically
- Limit state space for game agents
- Use state abstraction effectively

## Next Steps

- Read the [Architecture Documentation](ARCHITECTURE.md)
- Explore [Tutorial](TUTORIAL.md)
- Check out [Poker Learning](POKER_LEARNING.md)
- Contribute to the project!
