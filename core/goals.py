"""
Goals - explicit intent representation
Goals are executable constraints, not text wishes
"""


class Goal:
    """
    An executable goal with a reward function
    This grounds intent in verifiable outcomes
    """
    
    def __init__(self, description, reward_fn):
        self.description = description
        self.reward_fn = reward_fn
    
    def evaluate(self, state):
        """
        Evaluate how well the current state satisfies this goal
        Returns a numeric score
        """
        return self.reward_fn(state)
    
    def __str__(self):
        return f"Goal: {self.description}"
