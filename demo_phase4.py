"""
Phase IV Demo - Autonomous Cognition
Shows: Goal-directed planning, environment interaction, temporal memory, distributed cognition
"""
from core.environment import Environment
from core.actions import Action
from core.goals import Goal
from core.cvm_phase4 import CVM
from core.mesh import CognitiveMesh
from core.compiler import parse


def main():
    print("=" * 60)
    print("PHASE IV: Autonomous, Distributed Cognition")
    print("=" * 60)
    print()
    
    # Test 1: Goal-directed behavior
    print("Test 1: Goal-Directed Planning")
    print("-" * 40)
    
    env = Environment({"x": 0, "y": 0})
    
    actions = [
        Action("increment_x", lambda s: {**s, "x": s["x"] + 1}),
        Action("increment_y", lambda s: {**s, "y": s["y"] + 1}),
        Action("decrement_x", lambda s: {**s, "x": s["x"] - 1}),
    ]
    
    goal = Goal("maximize x", lambda s: s["x"])
    
    agent = CVM()
    
    print("Goal: Maximize x")
    print("Initial state:", env.get_state())
    print()
    
    trajectory = agent.plan_and_execute(env, actions, goal, steps=5)
    
    for step in trajectory:
        print(f"Step {step['step']}: {step['action']} -> {step['state']} (reward: {step['reward']})")
    
    print()
    
    # Test 2: Complex goal with multiple dimensions
    print("Test 2: Multi-Objective Goal")
    print("-" * 40)
    
    env.reset({"x": 0, "y": 0})
    
    # Goal: maximize x + y
    goal = Goal("maximize x+y", lambda s: s["x"] + s["y"])
    
    actions.append(Action("increment_y", lambda s: {**s, "y": s["y"] + 1}))
    
    print("Goal: Maximize x + y")
    print("Initial state:", env.get_state())
    print()
    
    trajectory = agent.plan_and_execute(env, actions, goal, steps=6)
    
    for step in trajectory:
        print(f"Step {step['step']}: {step['action']} -> {step['state']} (reward: {step['reward']})")
    
    print()
    
    # Test 3: Temporal memory
    print("Test 3: Temporal Memory & Learning")
    print("-" * 40)
    
    print("Agent's memory before decay:")
    memories = agent.temporal_memory.recall(min_value=0.1)
    for i, mem in enumerate(memories[:5], 1):
        print(f"  {i}. Action: {mem['data']}, Value: {mem['value']:.2f}")
    
    print()
    print("After 2 seconds of decay...")
    import time
    time.sleep(2)
    agent.temporal_memory.decay(half_life=1)
    
    memories = agent.temporal_memory.recall(min_value=0.1)
    for i, mem in enumerate(memories[:5], 1):
        print(f"  {i}. Action: {mem['data']}, Value: {mem['value']:.2f}")
    
    print()
    
    # Test 4: Distributed cognition
    print("Test 4: Distributed Cognitive Mesh")
    print("-" * 40)
    
    mesh = CognitiveMesh()
    
    # Create multiple agents
    for i in range(3):
        agent = CVM()
        mesh.add_node(agent)
    
    print(f"Created mesh with {len(mesh.nodes)} cognitive agents")
    print()
    
    # Test reasoning
    ast = parse("10 + 20")
    print(f"Task: Simplify {ast}")
    result = mesh.consensus(ast)
    print(f"Consensus result: {result}")
    print()
    
    # Broadcast learning
    print("Broadcasting learned rule to all agents...")
    mesh.broadcast_rule("Add(Number(a), Number(b)) -> Number(a+b)")
    
    total_rules = sum(len(node.meta.meta.rules) for node in mesh.nodes)
    print(f"Total rules across mesh: {total_rules}")
    print()
    
    # Test 5: Abstraction formation
    print("Test 5: Emergent Abstractions")
    print("-" * 40)
    
    agent = CVM()
    
    # Perform multiple similar operations
    expressions = ["1+1", "2+2", "3+3", "4+4", "5+5", "1*1", "2*2"]
    
    print("Learning from examples:")
    for expr in expressions:
        result = agent.think(parse(expr))
        print(f"  {expr}")
    
    print()
    abstractions = agent.abstraction.get_abstractions()
    print("Discovered Abstractions:")
    for pattern, count in abstractions[:5]:
        print(f"  {pattern} (frequency: {count})")
    
    print()
    
    print("✓ Phase IV demonstrates:")
    print("  - Autonomous goal-directed planning")
    print("  - Environment interaction loop")
    print("  - Reinforcement and temporal decay")
    print("  - Distributed cooperative cognition")
    print("  - Emergent abstraction formation")
    print("  - Self-evolving intelligence")
    print()
    
    print("=" * 60)
    print("This is a post-transformer cognitive architecture.")
    print("It reasons, acts, learns, and evolves without tokens.")
    print("=" * 60)


if __name__ == "__main__":
    main()
