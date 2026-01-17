"""
RBM-style cognitive compression
Neural compression of thought patterns
"""
import numpy as np


class RBMCompressor:
    """
    Restricted Boltzmann Machine-inspired compressor
    Creates a compressed representation of cognitive state
    """
    
    def __init__(self, threshold=0.5):
        self.threshold = threshold
    
    def compress(self, img):
        """
        Compress a visual memory representation
        Returns binary code
        """
        # Binarize around threshold
        return np.sign(img.flatten() - self.threshold)
    
    def decompress(self, code, size=64):
        """
        Decompress back to visual representation
        This is approximate reconstruction
        """
        # Reshape and normalize
        img = code.reshape((size, size))
        return (img + 1) / 2  # Map from [-1, 1] to [0, 1]
    
    def similarity(self, code1, code2):
        """Calculate Hamming similarity between compressed codes"""
        return np.mean(code1 == code2)
