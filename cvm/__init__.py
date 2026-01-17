"""
Cognitive Virtual Machine (CVM)
================================

A Post-Transformer Architecture for Deterministic, Verifiable AI.

This package provides a complete cognitive architecture that operates on
executable semantic graphs (ASTs) rather than statistical token sequences.

Core Components:
    - AST: Abstract Syntax Tree representation
    - Executor: Deterministic evaluation engine
    - Verifier: Semantic verification layer
    - CVM: Complete cognitive virtual machine (Phase I-IV)

Games:
    - poker: Texas Hold'em learning agent
    - snake: Classic Snake learning agent
    - tictactoe: Tic-Tac-Toe learning agent

Example:
    >>> from cvm import CVM
    >>> from cvm.core.compiler import parse
    >>> 
    >>> vm = CVM()
    >>> result = vm.think(parse("2 + 3"))
    >>> print(result)
"""

__version__ = "0.1.0"
__author__ = "CVM Project"
__license__ = "MIT"

# Core imports for convenience
from cvm.core.cvm_phase4 import CVM
from cvm.core.ast import Node
from cvm.core.compiler import parse, decompile
from cvm.core.executor import Executor
from cvm.core.verifier import Verifier

__all__ = [
    "CVM",
    "Node",
    "parse",
    "decompile",
    "Executor",
    "Verifier",
    "__version__",
]
