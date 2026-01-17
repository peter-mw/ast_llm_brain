# Project Structure

```
ast_llm_brain/
│
├── README.md                    # Main documentation
├── TUTORIAL.md                  # Comprehensive tutorial
├── requirements.txt             # Dependencies
├── .gitignore                  # Git ignore rules
├── main.py                     # Main entry point
│
├── core/                       # Core cognitive engine
│   ├── __init__.py            # Package init
│   │
│   ├── ast.py                 # AST node representation
│   ├── executor.py            # Symbolic execution engine
│   ├── verifier.py            # Semantic verification
│   ├── compiler.py            # Natural language ↔ AST
│   │
│   ├── memory.py              # Persistent storage
│   ├── embedder.py            # Structural embeddings
│   ├── rewriter.py            # Transformation rules
│   │
│   ├── search.py              # Multi-step reasoning
│   ├── proof.py               # Proof chains
│   ├── induction.py           # Rule learning
│   │
│   ├── reversible.py          # Lossless encoding
│   ├── visual_memory.py       # Visual substrate
│   ├── compressor.py          # Neural compression
│   │
│   ├── meta_rules.py          # Self-modifying rules
│   ├── meta_reasoner.py       # Meta-reasoning
│   │
│   ├── goals.py               # Goal representation
│   ├── planner.py             # Planning engine
│   ├── environment.py         # World interface
│   ├── actions.py             # Executable behaviors
│   │
│   ├── temporal_memory.py     # Time-aware memory
│   ├── mesh.py                # Distributed cognition
│   ├── abstraction.py         # Concept formation
│   │
│   ├── cvm_phase1.py          # Phase I: Basic loop
│   ├── cvm_phase2.py          # Phase II: Multi-step
│   ├── cvm_phase3.py          # Phase III: Non-token
│   └── cvm_phase4.py          # Phase IV: Autonomous
│
├── demo_phase1.py              # Phase I demonstration
├── demo_phase2.py              # Phase II demonstration
├── demo_phase3.py              # Phase III demonstration
└── demo_phase4.py              # Phase IV demonstration
```

## Component Overview

### Foundation (Phase I)
- **ast.py**: Core data structure for thoughts
- **executor.py**: Deterministic evaluation
- **verifier.py**: Hallucination prevention
- **compiler.py**: Human ↔ machine interface
- **memory.py**: Persistent storage
- **embedder.py**: Vector representations
- **rewriter.py**: Transformation engine

### Reasoning (Phase II)
- **search.py**: Multi-step exploration
- **proof.py**: Explainable traces
- **induction.py**: Pattern learning

### Intelligence (Phase III)
- **reversible.py**: Lossless thought encoding
- **visual_memory.py**: Visual cognition substrate
- **compressor.py**: Neural compression
- **meta_rules.py**: Self-modification
- **meta_reasoner.py**: Thinking about thinking

### Autonomy (Phase IV)
- **goals.py**: Explicit intent
- **planner.py**: Strategic action selection
- **environment.py**: World interaction
- **actions.py**: Executable behaviors
- **temporal_memory.py**: Time-aware learning
- **mesh.py**: Distributed intelligence
- **abstraction.py**: Emergent concepts

## Lines of Code

- **Core modules**: ~1,500 lines
- **Demo files**: ~400 lines
- **Documentation**: ~1,000 lines
- **Total**: ~2,900 lines

## Key Innovations

1. **AST-First Architecture**: Thoughts are executable graphs, not token sequences
2. **Verification Loop**: Every transformation is mathematically verified
3. **Proof Chains**: Complete reasoning traces for explainability
4. **Reversible Memory**: Lossless compression of cognitive state
5. **Visual Substrate**: 2D numeric representations for GPU/shader processing
6. **Meta-Reasoning**: System reflects on and improves its own processes
7. **Temporal Dynamics**: Memory decays and reinforces like biological systems
8. **Distributed Cognition**: Multiple agents share and evolve knowledge
9. **Zero Hallucination**: Impossible to generate invalid transformations

## Usage Patterns

### Quick Test
```powershell
python main.py phase1
```

### Full Demo
```powershell
python main.py all
```

### Custom Usage
```python
from core.compiler import parse
from core.cvm_phase4 import CVM

agent = CVM()
result = agent.think(parse("10 + 20"))
```

## Dependencies

**Required**: None (pure Python)

**Optional**:
- numpy (for embeddings and visual memory)
- pillow (for image export)

## Performance

- **Memory**: ~10MB base, scales with proof history
- **Speed**: Milliseconds for simple expressions
- **Scalability**: Horizontal via cognitive mesh

## Future Extensions

- Natural language AST parsing
- Neural rewrite learning
- Multi-domain reasoning (code, logic, math)
- Visual shader compilation
- Distributed mesh protocols
- Self-generated goals
- Ethical constraint systems

## Philosophy

This is not an incremental improvement.
This is a **paradigm shift** from statistical compression to executable cognition.

The architecture after transformers is here.
