"""
Abstraction formation - emergent concepts
Concepts emerge from repetition, not labels
"""


class Abstraction:
    """
    Discovers and compresses recurring patterns
    Enables hierarchical concept formation
    """
    
    def __init__(self):
        self.patterns = {}
    
    def observe(self, rule):
        """
        Observe a rule or pattern
        Track frequency
        """
        self.patterns.setdefault(rule, 0)
        self.patterns[rule] += 1
    
    def compress(self, min_frequency=3):
        """
        Extract patterns that occur frequently
        These become abstractions
        """
        return {k: v for k, v in self.patterns.items() if v >= min_frequency}
    
    def get_abstractions(self):
        """
        Get all discovered abstractions
        Sorted by frequency
        """
        return sorted(self.patterns.items(), key=lambda x: x[1], reverse=True)
    
    def generalize(self, pattern1, pattern2):
        """
        Find common structure between two patterns
        Future: create higher-order abstractions
        """
        # Simple string matching for now
        # Future: structural AST matching
        if pattern1 == pattern2:
            return pattern1
        return None
