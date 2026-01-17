"""
Persistent thought memory - stores reasoning traces
"""
import pickle
import os


class Memory:
    """
    Persistent storage for cognitive operations
    Stores both raw ASTs and proof chains
    """
    
    def __init__(self, file="memory.pkl"):
        self.file = file
        self.data = self.load()
    
    def load(self):
        """Load memory from disk"""
        if os.path.exists(self.file):
            try:
                with open(self.file, "rb") as f:
                    return pickle.load(f)
            except Exception:
                return []
        return []
    
    def save(self):
        """Persist memory to disk"""
        with open(self.file, "wb") as f:
            pickle.dump(self.data, f)
    
    def store(self, before, after):
        """Store a transformation pair"""
        self.data.append({
            "before": before.to_tuple(),
            "after": after.to_tuple()
        })
        self.save()
    
    def store_proof(self, proof):
        """Store a complete proof chain"""
        self.data.append({
            "type": "proof",
            "steps": [n.to_tuple() for n in proof.steps]
        })
        self.save()
    
    def clear(self):
        """Clear all memory"""
        self.data = []
        self.save()
