"""
Meta-rules - rules about rules
Self-modifying rule engine
"""


class MetaRules:
    """
    Stores and evolves the rule set itself
    This enables self-modification
    """
    
    def __init__(self):
        self.rules = []
        self.usage_counts = {}
    
    def add(self, rule):
        """Add a new rule if not already present"""
        if rule and rule not in self.rules:
            self.rules.append(rule)
            self.usage_counts[rule] = 0
    
    def use(self, rule):
        """Record usage of a rule"""
        if rule in self.usage_counts:
            self.usage_counts[rule] += 1
    
    def evolve(self):
        """
        Optimize the rule set
        Future: merge similar rules, prune unused ones, discover higher-order patterns
        """
        # Sort by usage
        sorted_rules = sorted(self.rules, key=lambda r: self.usage_counts.get(r, 0), reverse=True)
        return sorted_rules
    
    def prune(self, min_usage=1):
        """Remove rarely used rules"""
        self.rules = [r for r in self.rules if self.usage_counts.get(r, 0) >= min_usage]
