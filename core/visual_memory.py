"""
Visual memory substrate - numeric representation for fractal/shader encoding
Enables visual reasoning and GPU acceleration
"""
import numpy as np
from core.embedder import embed


def visual_encode(node, size=64):
    """
    Convert an AST into a 2D visual representation
    This can be rendered, compressed fractally, or processed by shaders
    """
    v = embed(node)
    img = np.zeros((size, size))
    
    # Map embedding vector to 2D space
    for i, val in enumerate(v[:size*size]):
        x = i // size
        y = i % size
        img[x, y] = val
    
    return img


def visual_decode(img):
    """
    Approximate reconstruction from visual representation
    Note: This is lossy, unlike reversible.py
    Used for similarity matching, not exact reconstruction
    """
    return img.flatten()


def save_visual(img, filename):
    """Save visual representation as image"""
    try:
        from PIL import Image
        # Normalize to 0-255
        normalized = ((img - img.min()) / (img.max() - img.min() + 1e-10) * 255).astype(np.uint8)
        Image.fromarray(normalized).save(filename)
        return True
    except ImportError:
        # PIL not available, save as numpy
        np.save(filename, img)
        return True
