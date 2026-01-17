"""
Phase III Demo - Non-Token Intelligence
Shows: Reversible memory, visual encoding, neural compression, meta-reasoning
"""
from cvm.core.compiler import parse, decompile
from cvm.core.cvm_phase3 import CVM
import numpy as np


def main():
    print("=" * 60)
    print("PHASE III: Non-Token Intelligence")
    print("=" * 60)
    print()
    
    vm = CVM()
    
    # Test 1: Full cognitive cycle
    print("Test 1: Complete Cognitive Cycle")
    print("-" * 40)
    ast = parse("(7 + 8) * 3")
    print(f"Input: {decompile(ast)}")
    print()
    
    result = vm.think(ast)
    
    result["proof"].explain()
    
    print(f"Reversible Encoding: {result['encoded'][:60]}...")
    print(f"Visual Memory Shape: {result['visual'].shape}")
    print(f"Compressed Code Shape: {result['compressed'].shape}")
    print(f"Learned Rule: {result['learned_rule']}")
    print(f"Proof Type: {result['proof_type']}")
    print(f"Total Evolved Rules: {len(result['evolved_rules'])}")
    print()
    
    # Test 2: Visual representation analysis
    print("Test 2: Visual Memory Analysis")
    print("-" * 40)
    ast1 = parse("10 + 20")
    ast2 = parse("15 + 15")
    
    r1 = vm.think(ast1)
    r2 = vm.think(ast2)
    
    # Compare visual representations
    from cvm.core.embedder import similarity
    sim = similarity(r1['result'], r2['result'])
    
    print(f"Expression 1: {decompile(ast1)} -> {decompile(r1['result'])}")
    print(f"Expression 2: {decompile(ast2)} -> {decompile(r2['result'])}")
    print(f"Semantic Similarity: {sim:.4f}")
    print()
    
    # Test 3: Compression ratio
    print("Test 3: Cognitive Compression")
    print("-" * 40)
    ast = parse("((1+2)+(3+4))+((5+6)+(7+8))")
    result = vm.think(ast)
    
    original_size = len(str(ast.to_tuple()))
    compressed_size = len(result['compressed'])
    ratio = original_size / compressed_size
    
    print(f"Original Representation: {original_size} bytes")
    print(f"Compressed Code: {compressed_size} bytes")
    print(f"Compression Ratio: {ratio:.2f}x")
    print()
    
    # Test 4: Meta-reasoning insights
    print("Test 4: Meta-Reasoning")
    print("-" * 40)
    
    # Do several operations to accumulate rules
    for expr in ["1+1", "2+2", "3+3", "4*4", "5*5"]:
        vm.think(parse(expr))
    
    insights = vm.meta.suggest_improvements()
    print(f"Total Rules Discovered: {insights['total_rules']}")
    print("Most Used Rules:")
    for i, rule in enumerate(insights['most_used'][:3], 1):
        print(f"  {i}. {rule}")
    print()
    
    print("✓ Phase III demonstrates:")
    print("  - Lossless reversible thought encoding")
    print("  - Visual/numeric memory substrate")
    print("  - Neural compression of cognitive state")
    print("  - Self-modifying rule engine")
    print("  - Meta-reasoning about thinking process")
    print()


if __name__ == "__main__":
    main()
