"""
Rule induction - learning from experience
Generalizes from specific transformations to abstract rules
"""


class Induction:
    """
    Learns rewrite rules from successful transformations
    This is the learning mechanism
    """
    
    def induce(self, proof):
        """
        Extract a generalized rule from a proof chain
        Returns a symbolic rule description
        """
        if len(proof.steps) < 2:
            return None
        
        start = proof.steps[0]
        end = proof.steps[-1]
        
        # Pattern: Operation on two numbers -> Simplified number
        if start.type == "Add" and end.type == "Number":
            a, b = start.inputs
            if a.type == "Number" and b.type == "Number":
                return "Add(Number(a), Number(b)) -> Number(a+b)"
        
        if start.type == "Mul" and end.type == "Number":
            a, b = start.inputs
            if a.type == "Number" and b.type == "Number":
                return "Mul(Number(a), Number(b)) -> Number(a*b)"
        
        if start.type == "Sub" and end.type == "Number":
            a, b = start.inputs
            if a.type == "Number" and b.type == "Number":
                return "Sub(Number(a), Number(b)) -> Number(a-b)"
        
        if start.type == "Div" and end.type == "Number":
            a, b = start.inputs
            if a.type == "Number" and b.type == "Number":
                return "Div(Number(a), Number(b)) -> Number(a/b)"
        
        # Pattern: Nested operations
        return f"{start.type}(...) -> {end.type}(...)"
