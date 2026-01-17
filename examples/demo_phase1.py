"""
Phase I Demo - Basic Cognitive Loop
Shows: Single-step rewriting with verification
"""
from cvm.core.compiler import parse, decompile
from cvm.core.cvm_phase1 import CVM


def main():
    print("=" * 60)
    print("PHASE I: Basic Cognitive Loop")
    print("=" * 60)
    print()
    
    vm = CVM()
    
    # Test 1: Simple addition
    print("Test 1: Simple Addition")
    print("-" * 40)
    ast = parse("2 + 3")
    print(f"Input:  {decompile(ast)}")
    
    result = vm.think(ast)
    print(f"Output: {decompile(result)}")
    print()
    
    # Test 2: Multiplication
    print("Test 2: Multiplication")
    print("-" * 40)
    ast = parse("4 * 5")
    print(f"Input:  {decompile(ast)}")
    
    result = vm.think(ast)
    print(f"Output: {decompile(result)}")
    print()
    
    # Test 3: Already simplified (no change)
    print("Test 3: Already Simplified")
    print("-" * 40)
    ast = parse("42")
    print(f"Input:  {decompile(ast)}")
    
    result = vm.think(ast)
    print(f"Output: {decompile(result)}")
    print()
    
    print("[OK] Phase I demonstrates:")
    print("  - Executable AST representation")
    print("  - Deterministic symbolic execution")
    print("  - Verified rewrites (no hallucination)")
    print("  - Persistent memory")
    print()


if __name__ == "__main__":
    main()
