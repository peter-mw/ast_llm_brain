"""
Actions - executable behaviors
Actions are programs, not text outputs
"""


class Action:
    """
    An executable action that transforms environment state
    This grounds behavior in deterministic operations
    """
    
    def __init__(self, name, fn):
        self.name = name
        self.fn = fn
    
    def apply(self, state):
        """
        Apply this action to a state
        Returns new state
        """
        return self.fn(state)
    
    def __str__(self):
        return f"Action: {self.name}"
