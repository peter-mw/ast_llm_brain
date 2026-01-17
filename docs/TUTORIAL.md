# AST-Based Cognitive Virtual Machine - Tutorial

## Introduction

Welcome to the AST-based Cognitive Virtual Machine (CVM) - a revolutionary post-transformer architecture for AI that thinks in **executable graphs** instead of statistical tokens.

This tutorial will guide you through understanding and using all four phases of the system.

---

## Installation

```powershell
# Clone or download the project
cd ast_llm_brain

# Install optional dependencies (recommended)
pip install numpy pillow

# No other dependencies required!
```

---

## Quick Start

### Run All Demos

```powershell
python main.py all
```

### Run Individual Phases

```powershell
python main.py phase1  # Basic cognitive loop
python main.py phase2  # Multi-step reasoning
python main.py phase3  # Non-token intelligence
python main.py phase4  # Autonomous cognition
```

---

## Understanding Each Phase

### Phase I: Basic Cognitive Loop

**Concept:** Replace tokens with executable AST nodes that can be verified

```python
from core.compiler import parse
from core.cvm_phase1 import CVM

# Create a cognitive VM
vm = CVM()

# Parse expression to AST
ast = parse("5 + 10")

# Think (rewrite with verification)
result = vm.think(ast)
print(result.value)  # 15
```

**Key Innovation:** Every transformation is verified against execution semantics, making hallucination impossible.

---

### Phase II: Multi-Step Reasoning

**Concept:** Search through the space of valid transformations to build proof chains

```python
from core.compiler import parse, decompile
from core.cvm_phase2 import CVM

vm = CVM()

# Complex expression
ast = parse("(2 + 3) + (4 + 5)")

# Multi-step reasoning
proof, rule = vm.think(ast)

# View the proof
proof.explain()
# Step 0: ((2 + 3) + (4 + 5))
#     ↓
# Step 1: (5 + (4 + 5))
#     ↓
# Step 2: (5 + 9)
#     ↓
# Step 3: 14

print(f"Learned: {rule}")
# Add(Number(a), Number(b)) -> Number(a+b)
```

**Key Innovation:** The system builds verifiable proof chains and learns general rules from specific examples.

---

### Phase III: Non-Token Intelligence

**Concept:** Represent thoughts as visual/numeric patterns that can be compressed and stored

```python
from core.compiler import parse
from core.cvm_phase3 import CVM

vm = CVM()
ast = parse("10 * 20")

result = vm.think(ast)

# Access multiple representations
print(result["result"])           # Final AST
print(result["encoded"])          # Reversible string
print(result["visual"].shape)     # 2D visual memory
print(result["compressed"])       # Binary neural code
print(result["learned_rule"])     # Induced pattern
print(result["evolved_rules"])    # All known rules
```

**Key Innovation:** Thoughts can be represented visually, compressed neurally, and still be perfectly reconstructed.

---

### Phase IV: Autonomous Cognition

**Concept:** Enable goal-directed behavior in environments with planning and learning

```python
from core.environment import Environment
from core.actions import Action
from core.goals import Goal
from core.cvm_phase4 import CVM

# Create environment
env = Environment({"x": 0, "energy": 100})

# Define possible actions
actions = [
    Action("move_right", lambda s: {**s, "x": s["x"] + 1, "energy": s["energy"] - 1}),
    Action("move_left", lambda s: {**s, "x": s["x"] - 1, "energy": s["energy"] - 1}),
    Action("rest", lambda s: {**s, "energy": s["energy"] + 5}),
]

# Define goal
goal = Goal("reach position 10", lambda s: s["x"] if s["x"] <= 10 else 10 - abs(s["x"] - 10))

# Create agent
agent = CVM()

# Execute plan
trajectory = agent.plan_and_execute(env, actions, goal, steps=10)

# View results
for step in trajectory:
    print(f"{step['action']} -> {step['state']} (reward: {step['reward']})")
```

**Key Innovation:** The CVM becomes an autonomous agent that can plan, act, learn from experience, and adapt over time.

---

## Advanced Features

### Distributed Cognition

Create a network of CVMs that share knowledge:

```python
from core.mesh import CognitiveMesh
from core.cvm_phase4 import CVM
from core.compiler import parse

# Create mesh
mesh = CognitiveMesh()

# Add agents
for i in range(5):
    mesh.add_node(CVM())

# Distribute work
tasks = [parse("1+1"), parse("2*2"), parse("3+3"), parse("4*4")]
results = mesh.distribute_work(tasks)

# Broadcast learning
mesh.broadcast_rule("Add(a,b) -> Number(a+b)")
```

### Temporal Memory

Memory that decays over time and reinforces with use:

```python
from core.temporal_memory import TemporalMemory
import time

memory = TemporalMemory()

# Store experiences
memory.store("action1", value=1.0)
memory.store("action2", value=0.5)

# Wait and decay
time.sleep(5)
memory.decay(half_life=2)

# Recall important memories
important = memory.recall(min_value=0.1)
```

### Visual Memory Export

Save thought patterns as images:

```python
from core.compiler import parse
from core.cvm_phase3 import CVM
from core.visual_memory import save_visual

vm = CVM()
result = vm.think(parse("(10 + 20) * 2"))

# Save as image
save_visual(result["visual"], "thought_pattern.png")
```

### Custom Actions and Goals

Create domain-specific behaviors:

```python
from core.actions import Action
from core.goals import Goal

# Custom action
def complex_action(state):
    return {
        "position": state["position"] + state.get("velocity", 1),
        "velocity": state.get("velocity", 1) * 0.9,  # Friction
        "energy": state["energy"] - abs(state.get("velocity", 1))
    }

action = Action("move_with_physics", complex_action)

# Custom goal with multiple criteria
def goal_function(state):
    position_score = -abs(state["position"] - 100)  # Want to reach 100
    energy_score = state["energy"]  # Want to conserve energy
    return position_score + energy_score * 0.1

goal = Goal("reach target efficiently", goal_function)
```

---

## Building Your Own

### Create Custom AST Nodes

```python
from core.ast import Node

# Custom node type
logic_node = Node("And", inputs=[
    Node("Boolean", True),
    Node("Boolean", False)
])
```

### Extend the Executor

```python
from core.executor import Executor

class CustomExecutor(Executor):
    def eval(self, node):
        if node.type == "And":
            return all(self.eval(i) for i in node.inputs)
        elif node.type == "Or":
            return any(self.eval(i) for i in node.inputs)
        else:
            return super().eval(node)
```

### Add New Rewrite Rules

```python
from core.rewriter import Rewriter
from core.ast import Node

class CustomRewriter(Rewriter):
    def propose(self, node):
        # Your custom rule
        if node.type == "And":
            # De Morgan's law: not(A and B) = not(A) or not(B)
            pass
        
        return super().propose(node)
```

---

## Performance Tips

1. **Batch Processing**: Use the cognitive mesh for parallel reasoning
2. **Memory Management**: Call `temporal_memory.forget()` periodically
3. **Search Depth**: Adjust `max_depth` in Search for complex problems
4. **Rule Pruning**: Use `meta.prune()` to remove unused rules

---

## Debugging

### View AST Structure

```python
from core.compiler import parse

ast = parse("(1 + 2) * 3")
print(ast.to_dict())  # Human-readable
print(ast.to_tuple())  # Hashable
```

### Trace Execution

```python
from core.executor import Executor

executor = Executor()
ast = parse("5 + 10")

# Add debugging
import sys
result = executor.eval(ast)
print(f"Evaluated to: {result}")
```

### Verify Transformations

```python
from core.verifier import Verifier

verifier = Verifier()
before = parse("2 + 3")
after = parse("5")

is_valid = verifier.verify(before, after)
print(f"Valid transformation: {is_valid}")
```

---

## Common Patterns

### Pattern 1: Interactive REPL

```python
from core.compiler import parse, decompile
from core.cvm_phase2 import CVM

vm = CVM()

while True:
    expr = input("Enter expression: ")
    if expr.lower() in ['quit', 'exit']:
        break
    
    try:
        ast = parse(expr)
        proof, rule = vm.think(ast)
        print(f"Result: {decompile(proof[-1])}")
        if rule:
            print(f"Learned: {rule}")
    except Exception as e:
        print(f"Error: {e}")
```

### Pattern 2: Batch Learning

```python
from core.compiler import parse
from core.cvm_phase3 import CVM

vm = CVM()

# Learn from examples
examples = [
    "1 + 1", "2 + 2", "3 + 3",
    "1 * 2", "2 * 3", "3 * 4",
]

for expr in examples:
    vm.think(parse(expr))

# View learned patterns
insights = vm.meta.suggest_improvements()
print(f"Learned {insights['total_rules']} rules")
```

### Pattern 3: Autonomous Loop

```python
from core.environment import Environment
from core.cvm_phase4 import CVM

env = Environment()
agent = CVM()

for episode in range(10):
    env.reset()
    # ... run episode
    # Agent improves over time automatically
```

---

## Architecture Comparison

### Traditional LLM (Transformer)
```
Input Text → Tokenization → Embeddings → Attention Layers → Softmax → Output Tokens
```
- ❌ Statistical, not logical
- ❌ No verification
- ❌ Hallucination-prone
- ❌ Black box reasoning

### AST-based CVM
```
Expression → AST → Search → Verify → Proof Chain → Learn Rules
```
- ✅ Logical and executable
- ✅ Every step verified
- ✅ Hallucination-free
- ✅ Fully explainable

---

## FAQ

**Q: Can this replace transformers for all tasks?**
A: Currently optimized for structured reasoning. Natural language understanding would require extending the AST representation.

**Q: Is this actually trainable?**
A: Yes! The rewriter can be implemented as a neural network that learns which transformations to propose. Rules are learned from experience.

**Q: How does this scale?**
A: The cognitive mesh enables horizontal scaling. Each node can specialize in different domains.

**Q: What about natural language?**
A: The architecture is domain-agnostic. Expand the compiler to parse natural language into semantic ASTs.

**Q: Is this really hallucination-free?**
A: Yes. Every transformation is mathematically verified. Invalid operations are rejected.

---

## Next Steps

1. **Experiment** with the demos
2. **Extend** to new domains (logic, code, natural language)
3. **Train** neural rewrite models
4. **Build** distributed cognitive meshes
5. **Integrate** with existing systems

---

## Resources

- [README.md](README.md) - Full documentation
- [core/](core/) - Source code
- [demo_*.py](demo_phase1.py) - Working examples

---

## Philosophy

> "Transformers compress sequences.  
> The CVM executes thoughts."

This architecture represents a fundamental shift from statistical pattern matching to symbolic reasoning grounded in execution semantics.

The future of AI is not more tokens — it's **executable intelligence**.

---

*Happy reasoning!* 🚀
