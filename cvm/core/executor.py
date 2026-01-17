"""
Symbolic executor - deterministic evaluation of AST graphs
No hallucination possible - only valid operations execute
"""
from typing import Union
from cvm.core.ast import Node


class ExecutionError(Exception):
    """Raised when AST execution fails"""
    pass


class Executor:
    """
    Executes AST nodes to produce deterministic results.
    This is the 'truth layer' that prevents hallucination.
    
    Only semantically valid operations execute - no ambiguity.
    """
    
    def eval(self, node: Node) -> Union[int, float, bool]:
        """Evaluate an AST node recursively
        
        Args:
            node: AST node to evaluate
            
        Returns:
            Computed value (number or boolean)
            
        Raises:
            ExecutionError: If node type is unknown or evaluation fails
        """
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

        raise ExecutionError(f"Unknown node type: {t}")
