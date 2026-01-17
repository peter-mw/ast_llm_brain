"""
AST embeddings - structural vector representations
Graph-aware, not sequential like transformers
"""
import hashlib
import numpy as np


def embed(node):
    """
    Create a structural embedding for an AST node
    This is graph-aware, not sequential
    Uses recursive hashing to capture tree structure
    """
    def rec(n):
        # Hash the node type
        h = hashlib.sha256(n.type.encode()).digest()
        v = np.frombuffer(h, dtype=np.uint8).astype(float)
        
        # Add value if present
        if n.value is not None:
            val_hash = hashlib.sha256(str(n.value).encode()).digest()
            v += np.frombuffer(val_hash, dtype=np.uint8).astype(float)
        
        # Recursively add child embeddings
        for i in n.inputs:
            v += rec(i)
        
        return v
    
    v = rec(node)
    
    # Normalize to unit vector
    norm = np.linalg.norm(v)
    if norm > 0:
        return v / norm
    return v


def similarity(node1, node2):
    """Calculate cosine similarity between two AST nodes"""
    v1 = embed(node1)
    v2 = embed(node2)
    return np.dot(v1, v2)
