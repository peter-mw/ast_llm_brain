"""
Verifier - ensures rewrites preserve semantics
This is what makes the system hallucination-free
"""
from cvm.core.executor import Executor


class Verifier:
    """
    Verifies that AST transformations preserve semantic equivalence
    Every rewrite must pass verification or be rejected
    """
    
    def __init__(self):
        self.executor = Executor()
    
    def verify(self, before, after):
        """
        Check if two ASTs produce the same result
        Returns True only if semantically equivalent
        """
        try:
            result_before = self.executor.eval(before)
            result_after = self.executor.eval(after)
            return result_before == result_after
        except Exception:
            # If either fails to execute, they are not equivalent
            return False
