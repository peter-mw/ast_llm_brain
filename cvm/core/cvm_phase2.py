"""
Cognitive Virtual Machine - Phase II
Adds multi-step reasoning and learning
"""
from cvm.core.search import Search
from cvm.core.proof import Proof
from cvm.core.induction import Induction
from cvm.core.memory import Memory
from cvm.core.rewriter import Rewriter
from cvm.core.verifier import Verifier


class CVM:
    """
    Phase II: Multi-step reasoning
    Can now search for optimal transformation sequences
    """
    
    def __init__(self, rewriter=None, verifier=None):
        self.rewriter = rewriter or Rewriter()
        self.verifier = verifier or Verifier()
        self.search = Search(self.rewriter, self.verifier)
        self.induction = Induction()
        self.memory = Memory()
    
    def think(self, ast):
        """
        Perform multi-step reasoning
        Returns proof and learned rule
        """
        steps = self.search.run(ast)
        proof = Proof(steps)
        
        self.memory.store_proof(proof)
        
        rule = self.induction.induce(proof)
        
        return proof, rule
