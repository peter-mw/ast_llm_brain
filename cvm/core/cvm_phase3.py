"""
Cognitive Virtual Machine - Phase III
Adds reversible memory, neural compression, and meta-reasoning
"""
from cvm.core.search import Search
from cvm.core.proof import Proof
from cvm.core.induction import Induction
from cvm.core.memory import Memory
from cvm.core.reversible import encode_ast
from cvm.core.visual_memory import visual_encode
from cvm.core.compressor import RBMCompressor
from cvm.core.meta_reasoner import MetaReasoner
from cvm.core.rewriter import Rewriter
from cvm.core.verifier import Verifier


class CVM:
    """
    Phase III: Non-token intelligence
    Adds reversible encoding, visual memory, and self-modification
    """
    
    def __init__(self, rewriter=None, verifier=None):
        self.rewriter = rewriter or Rewriter()
        self.verifier = verifier or Verifier()
        self.search = Search(self.rewriter, self.verifier)
        self.induction = Induction()
        self.memory = Memory()
        self.compressor = RBMCompressor()
        self.meta = MetaReasoner()
    
    def think(self, ast):
        """
        Full cognitive cycle with all Phase III features
        Returns comprehensive cognitive state
        """
        # Multi-step reasoning
        steps = self.search.run(ast)
        proof = Proof(steps)
        
        # Encode final result reversibly
        encoded = encode_ast(steps[-1])
        
        # Create visual representation
        visual = visual_encode(steps[-1])
        
        # Compress neurally
        compressed = self.compressor.compress(visual)
        
        # Store in memory
        self.memory.store_proof(proof)
        
        # Learn rule
        rule = self.induction.induce(proof)
        
        # Meta-reasoning
        evolved_rules = self.meta.reflect(rule)
        proof_type = self.meta.analyze_proof(proof)
        
        return {
            "proof": proof,
            "result": steps[-1],
            "encoded": encoded,
            "visual": visual,
            "compressed": compressed,
            "learned_rule": rule,
            "evolved_rules": evolved_rules,
            "proof_type": proof_type
        }
