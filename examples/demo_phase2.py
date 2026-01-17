"""
Phase II Demo - Multi-Step Reasoning
Shows: Search-based reasoning with proof chains and learning
"""
from cvm.core.compiler import parse, decompile
from cvm.core.cvm_phase2 import CVM


def main():
    print("=" * 60)
    print("PHASE II: Multi-Step Reasoning")
    print("=" * 60)
    print()
    
    vm = CVM()
    
    # Test 1: Complex expression requiring multiple steps
    print("Test 1: Multi-Step Simplification")
    print("-" * 40)
    ast = parse("(2 + 3) + (4 + 5)")
    print(f"Input: {decompile(ast)}")
    print()
    
    proof, rule = vm.think(ast)
    proof.explain()
    
    print(f"Learned Rule: {rule}")
    print()
    
    # Test 2: Nested operations
    print("Test 2: Nested Operations")
    print("-" * 40)
    ast = parse("(3 * 4) + (2 * 5)")
    print(f"Input: {decompile(ast)}")
    print()
    
    proof, rule = vm.think(ast)
    proof.explain()
    
    print(f"Learned Rule: {rule}")
    print()
    
    # Test 3: Deep nesting
    print("Test 3: Deep Nesting")
    print("-" * 40)
    ast = parse("((1 + 2) + (3 + 4)) + ((5 + 6) + (7 + 8))")
    print(f"Input: {decompile(ast)}")
    print()
    
    proof, rule = vm.think(ast)
    print(f"Proof length: {len(proof.steps)} steps")
    print(f"Final result: {decompile(proof.steps[-1])}")
    print(f"Learned Rule: {rule}")
    print()
    
    print("[OK] Phase II demonstrates:")
    print("  - Multi-step search-based reasoning")
    print("  - Explainable proof chains")
    print("  - Rule induction from experience")
    print("  - Structural pattern learning")
    print()


if __name__ == "__main__":
    main()
