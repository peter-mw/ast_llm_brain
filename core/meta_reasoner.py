"""
Meta-reasoner - thinking about thinking
Reflects on and improves the reasoning process itself
"""
from core.meta_rules import MetaRules


class MetaReasoner:
    """
    Reasons about the reasoning process
    This is the self-awareness layer
    """
    
    def __init__(self):
        self.meta = MetaRules()
    
    def reflect(self, learned_rule):
        """
        Reflect on a newly learned rule
        Integrates it into the rule set
        """
        if learned_rule:
            self.meta.add(learned_rule)
        return self.meta.evolve()
    
    def analyze_proof(self, proof):
        """
        Analyze a proof for meta-patterns
        Returns insights about the reasoning process
        """
        if len(proof.steps) == 1:
            return "trivial"
        elif len(proof.steps) == 2:
            return "single_step"
        else:
            return "multi_step"
    
    def suggest_improvements(self):
        """
        Suggest improvements to the reasoning process
        Future: identify missing rules, redundant rules, etc.
        """
        return {
            "total_rules": len(self.meta.rules),
            "most_used": self.meta.evolve()[:3] if self.meta.rules else [],
            "suggestions": []
        }
