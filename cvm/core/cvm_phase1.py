"""
Cognitive Virtual Machine - Phase I
The basic thinking loop
"""
from cvm.core.rewriter import Rewriter
from cvm.core.verifier import Verifier
from cvm.core.memory import Memory


class CVM:
    """
    Phase I: Basic cognitive loop
    Proposes rewrites and verifies them before accepting
    """
    
    def __init__(self):
        self.rewriter = Rewriter()
        self.verifier = Verifier()
        self.memory = Memory()
    
    def think(self, ast):
        """
        Perform one thinking step
        Returns rewritten AST if valid, original otherwise
        """
        candidate = self.rewriter.propose(ast)
        
        if candidate and self.verifier.verify(ast, candidate):
            self.memory.store(ast, candidate)
            return candidate
        
        return ast
