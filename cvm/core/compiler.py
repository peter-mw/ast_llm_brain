"""
Natural Language Compiler - converts expressions to AST
This is the input interface, replacing tokenization
"""
from cvm.core.ast import Node
import re


def parse(expr):
    """
    Parse a mathematical expression into an AST
    This is a simple recursive descent parser
    
    Future: expand to handle full natural language
    """
    expr = expr.replace(" ", "")
    
    # Handle outer parentheses
    if expr.startswith("(") and expr.endswith(")"):
        # Check if these are matching outer parens
        depth = 0
        for i, ch in enumerate(expr):
            if ch == '(':
                depth += 1
            elif ch == ')':
                depth -= 1
            if depth == 0 and i < len(expr) - 1:
                break
        if i == len(expr) - 1:
            expr = expr[1:-1]
    
    # Addition (lowest precedence)
    depth = 0
    for i in range(len(expr) - 1, -1, -1):
        if expr[i] == ')':
            depth += 1
        elif expr[i] == '(':
            depth -= 1
        elif depth == 0 and expr[i] == '+':
            left = expr[:i]
            right = expr[i+1:]
            return Node("Add", inputs=[parse(left), parse(right)])
    
    # Subtraction
    depth = 0
    for i in range(len(expr) - 1, -1, -1):
        if expr[i] == ')':
            depth += 1
        elif expr[i] == '(':
            depth -= 1
        elif depth == 0 and expr[i] == '-' and i > 0:  # Not unary minus
            left = expr[:i]
            right = expr[i+1:]
            return Node("Sub", inputs=[parse(left), parse(right)])
    
    # Multiplication
    depth = 0
    for i in range(len(expr) - 1, -1, -1):
        if expr[i] == ')':
            depth += 1
        elif expr[i] == '(':
            depth -= 1
        elif depth == 0 and expr[i] == '*':
            left = expr[:i]
            right = expr[i+1:]
            return Node("Mul", inputs=[parse(left), parse(right)])
    
    # Division
    depth = 0
    for i in range(len(expr) - 1, -1, -1):
        if expr[i] == ')':
            depth += 1
        elif expr[i] == '(':
            depth -= 1
        elif depth == 0 and expr[i] == '/':
            left = expr[:i]
            right = expr[i+1:]
            return Node("Div", inputs=[parse(left), parse(right)])
    
    # Number (base case)
    try:
        return Node("Number", int(expr))
    except ValueError:
        try:
            return Node("Number", float(expr))
        except ValueError:
            raise ValueError(f"Cannot parse: {expr}")


def decompile(node):
    """Convert AST back to human-readable expression"""
    if node.type == "Number":
        return str(node.value)
    elif node.type == "Add":
        return f"({decompile(node.inputs[0])} + {decompile(node.inputs[1])})"
    elif node.type == "Sub":
        return f"({decompile(node.inputs[0])} - {decompile(node.inputs[1])})"
    elif node.type == "Mul":
        return f"({decompile(node.inputs[0])} * {decompile(node.inputs[1])})"
    elif node.type == "Div":
        return f"({decompile(node.inputs[0])} / {decompile(node.inputs[1])})"
    return str(node)
