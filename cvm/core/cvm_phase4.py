"""
Cognitive Virtual Machine - Phase IV (Final Form)
Autonomous, distributed cognition with planning and adaptation
"""
from cvm.core.planner import Planner
from cvm.core.temporal_memory import TemporalMemory
from cvm.core.abstraction import Abstraction
from cvm.core.search import Search
from cvm.core.proof import Proof
from cvm.core.induction import Induction
from cvm.core.memory import Memory
from cvm.core.reversible import encode_ast
from cvm.core.visual_memory import visual_encode
from cvm.core.compressor import RBMCompressor
from cvm.core.meta_reasoner import MetaReasoner
from cvm.core.rewriter import Rewriter
from cvm.core.verifier import Verifier


class CVM:
    """
    Phase IV: Autonomous, distributed cognition
    A complete cognitive agent with:
    - Goal-directed planning
    - Time-aware memory
    - Environment interaction
    - Self-modification
    - Abstraction formation
    """
    
    def __init__(self, core_vm=None):
        # Core reasoning
        if core_vm:
            self.core = core_vm
        else:
            self.rewriter = Rewriter()
            self.verifier = Verifier()
            self.search = Search(self.rewriter, self.verifier)
            self.induction = Induction()
        
        # Phase IV additions
        self.planner = Planner()
        self.temporal_memory = TemporalMemory()
        self.abstraction = Abstraction()
        
        # Phase III features
        self.memory = Memory()
        self.compressor = RBMCompressor()
        self.meta = MetaReasoner()
    
    def think(self, ast):
        """
        Pure reasoning without environment
        Returns cognitive state
        """
        steps = self.search.run(ast)
        proof = Proof(steps)
        
        encoded = encode_ast(steps[-1])
        visual = visual_encode(steps[-1])
        compressed = self.compressor.compress(visual)
        
        self.memory.store_proof(proof)
        
        rule = self.induction.induce(proof)
        evolved_rules = self.meta.reflect(rule)
        
        if rule:
            self.abstraction.observe(rule)
        
        return {
            "proof": proof,
            "result": steps[-1],
            "encoded": encoded,
            "visual": visual,
            "compressed": compressed,
            "learned_rule": rule,
            "evolved_rules": evolved_rules
        }
    
    def act(self, env, actions, goal):
        """
        Goal-directed action in environment
        Returns action taken and reward received
        """
        action = self.planner.plan(env.state, actions, goal)
        
        if action is None:
            return None, 0
        
        new_state = env.step(action)
        reward = goal.evaluate(new_state)
        
        # Store in temporal memory
        self.temporal_memory.store(action.name, reward)
        
        # Reinforce if successful
        if reward > 0:
            self.temporal_memory.reinforce(action.name, boost=reward)
        
        return action.name, reward
    
    def plan_and_execute(self, env, actions, goal, steps=5):
        """
        Plan and execute a sequence of actions
        Returns trajectory
        """
        trajectory = []
        
        for i in range(steps):
            action_name, reward = self.act(env, actions, goal)
            
            if action_name is None:
                break
            
            trajectory.append({
                "step": i,
                "action": action_name,
                "state": env.get_state(),
                "reward": reward
            })
            
            # Stop if goal achieved
            if goal.evaluate(env.state) >= 1.0:
                break
        
        return trajectory
