"""
Planner - goal-directed action selection
Symbolic planning grounded in execution
"""


class Planner:
    """
    Plans actions to achieve goals
    Uses lookahead search with goal evaluation
    """
    
    def plan(self, state, actions, goal, depth=3):
        """
        Select best action to achieve goal
        Uses greedy search with depth limit
        """
        best_action = None
        best_score = float("-inf")
        
        for action in actions:
            # Simulate action
            next_state = action.apply(state)
            
            # Evaluate against goal
            score = goal.evaluate(next_state)
            
            if score > best_score:
                best_action = action
                best_score = score
        
        return best_action
    
    def plan_sequence(self, state, actions, goal, depth=3):
        """
        Plan a sequence of actions
        Returns list of actions
        """
        sequence = []
        current_state = state
        
        for _ in range(depth):
            action = self.plan(current_state, actions, goal, depth=1)
            if action is None:
                break
            
            sequence.append(action)
            current_state = action.apply(current_state)
            
            # Stop if goal achieved
            if goal.evaluate(current_state) >= 1.0:
                break
        
        return sequence
