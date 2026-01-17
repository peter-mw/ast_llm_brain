"""
Temporal memory - time-aware memory with decay and reinforcement
Memory has importance and can forget
"""
import time


class TemporalMemory:
    """
    Memory with temporal dynamics
    Implements decay and reinforcement
    """
    
    def __init__(self):
        self.entries = []
    
    def store(self, data, value):
        """
        Store data with an initial value/importance
        """
        self.entries.append({
            "time": time.time(),
            "data": data,
            "value": value,
            "access_count": 0
        })
    
    def decay(self, half_life=60):
        """
        Apply temporal decay to all memories
        half_life: time in seconds for value to halve
        """
        now = time.time()
        for entry in self.entries:
            age = now - entry["time"]
            entry["value"] *= 0.5 ** (age / half_life)
    
    def reinforce(self, data, boost=0.1):
        """
        Reinforce memories matching data
        """
        for entry in self.entries:
            if entry["data"] == data:
                entry["value"] += boost
                entry["access_count"] += 1
    
    def recall(self, min_value=0.1):
        """
        Recall memories above threshold
        Returns sorted by value
        """
        self.decay()
        active = [e for e in self.entries if e["value"] >= min_value]
        return sorted(active, key=lambda e: e["value"], reverse=True)
    
    def forget(self, threshold=0.01):
        """
        Remove memories below threshold
        """
        self.decay()
        self.entries = [e for e in self.entries if e["value"] >= threshold]
