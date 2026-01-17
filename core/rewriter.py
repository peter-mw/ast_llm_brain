"""
Rewriter - the neural rewrite engine
Proposes transformations that preserve semantics
"""
from core.ast import Node


class Rewriter:
    """
    Rule-based rewrite engine
    In full implementation, this would be learned from experience
    """
    
    def propose(self, node):
        """
        Propose a single rewrite for Phase I
        Returns None if no rewrite available
        """
        # Simplify Add(Number(a), Number(b)) -> Number(a+b)
        if node.type == "Add":
            a, b = node.inputs
            if a.type == "Number" and b.type == "Number":
                return Node("Number", a.value + b.value)
        
        # Simplify Mul(Number(a), Number(b)) -> Number(a*b)
        if node.type == "Mul":
            a, b = node.inputs
            if a.type == "Number" and b.type == "Number":
                return Node("Number", a.value * b.value)
        
        # Simplify Sub(Number(a), Number(b)) -> Number(a-b)
        if node.type == "Sub":
            a, b = node.inputs
            if a.type == "Number" and b.type == "Number":
                return Node("Number", a.value - b.value)
        
        # Simplify Div(Number(a), Number(b)) -> Number(a/b)
        if node.type == "Div":
            a, b = node.inputs
            if a.type == "Number" and b.type == "Number":
                if b.value != 0:
                    return Node("Number", a.value / b.value)
        
        return None
    
    def expand(self, node):
        """
        Generate all possible rewrites for Phase II
        Returns list of candidate transformations
        """
        candidates = []
        
        # Try simplification rules
        simplified = self.propose(node)
        if simplified:
            candidates.append(simplified)
        
        # Recursively rewrite children
        for i, child in enumerate(node.inputs):
            rewritten_child = self.propose(child)
            if rewritten_child:
                new_inputs = node.inputs[:i] + [rewritten_child] + node.inputs[i+1:]
                candidates.append(Node(node.type, node.value, new_inputs))
        
        return candidates
