"""
Environment - the world the CVM interacts with
Provides state and accepts actions
"""


class Environment:
    """
    An executable environment
    The CVM is embedded in this, not reasoning in isolation
    """
    
    def __init__(self, initial_state=None):
        self.state = initial_state or {}
        self.history = [self.state.copy()]
    
    def step(self, action):
        """
        Execute an action and update state
        Returns new state
        """
        self.state = action.apply(self.state)
        self.history.append(self.state.copy())
        return self.state
    
    def reset(self, state=None):
        """Reset to initial or specified state"""
        self.state = state or {}
        self.history = [self.state.copy()]
    
    def get_state(self):
        """Get current state"""
        return self.state.copy()
