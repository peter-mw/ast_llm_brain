"""
Symbolic executor - deterministic evaluation of AST graphs
No hallucination possible - only valid operations execute
"""


class Executor:
    """
    Executes AST nodes to produce deterministic results
    This is the 'truth layer' that prevents hallucination
    """
    
    def eval(self, node):
        """Evaluate an AST node recursively"""
        t = node.type

        if t == "Number":
            return node.value

        if t == "Add":
            return self.eval(node.inputs[0]) + self.eval(node.inputs[1])

        if t == "Mul":
            return self.eval(node.inputs[0]) * self.eval(node.inputs[1])
        
        if t == "Sub":
            return self.eval(node.inputs[0]) - self.eval(node.inputs[1])
        
        if t == "Div":
            return self.eval(node.inputs[0]) / self.eval(node.inputs[1])

        if t == "If":
            cond = self.eval(node.inputs[0])
            return self.eval(node.inputs[1] if cond else node.inputs[2])

        raise Exception(f"Unknown node type: {t}")
