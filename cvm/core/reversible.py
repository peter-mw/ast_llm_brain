"""
Reversible AST encoding - lossless thought compression
Enables perfect reconstruction of reasoning traces
"""
import json
import base64


def encode_ast(node):
    """
    Encode an AST into a reversible string representation
    This is lossless - the exact AST can be reconstructed
    """
    raw = json.dumps(node.to_tuple()).encode()
    return base64.b64encode(raw).decode()


def decode_ast(encoded):
    """
    Decode a reversible string back into an AST
    Perfect reconstruction guaranteed
    """
    from cvm.core.ast import Node
    
    def rebuild(t):
        typ, val, inputs = t
        return Node(typ, val, [rebuild(i) for i in inputs])
    
    raw = base64.b64decode(encoded)
    return rebuild(json.loads(raw))
