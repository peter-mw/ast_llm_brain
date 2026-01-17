"""
Proof chains - explainable reasoning traces
"""


class Proof:
    """
    A complete reasoning trace showing all transformation steps
    This makes the system fully explainable
    """
    
    def __init__(self, steps):
        self.steps = steps
    
    def explain(self):
        """Print human-readable proof"""
        print("\n=== Proof Chain ===")
        for i, step in enumerate(self.steps):
            from core.compiler import decompile
            print(f"Step {i}: {decompile(step)}")
            if i < len(self.steps) - 1:
                print("    ↓")
        print("===================\n")
    
    def __len__(self):
        return len(self.steps)
    
    def __getitem__(self, idx):
        return self.steps[idx]
