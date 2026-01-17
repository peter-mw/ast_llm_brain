"""
Persistent thought memory - stores reasoning traces
Uses JSON for human-readable, safe, cross-platform storage
"""
import json
import os
from typing import List, Dict, Any


class Memory:
    """
    Persistent storage for cognitive operations.
    Stores both raw ASTs and proof chains as JSON for:
    - Human readability (debuggable)
    - Security (no code execution risk vs pickle)
    - Portability (cross-language compatible)
    """
    
    def __init__(self, file: str = "memory.json"):
        self.file = file
        self.data: List[Dict[str, Any]] = self.load()
    
    def load(self) -> List[Dict[str, Any]]:
        """Load memory from JSON file"""
        if os.path.exists(self.file):
            try:
                with open(self.file, "r", encoding="utf-8") as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError) as e:
                print(f"Warning: Could not load memory from {self.file}: {e}")
                return []
        return []
    
    def save(self) -> None:
        """Persist memory to JSON file with pretty formatting"""
        try:
            with open(self.file, "w", encoding="utf-8") as f:
                json.dump(self.data, f, indent=2, ensure_ascii=False)
        except IOError as e:
            print(f"Warning: Could not save memory to {self.file}: {e}")
    
    def store(self, before, after) -> None:
        """Store a transformation pair (before -> after)"""
        self.data.append({
            "type": "transformation",
            "before": before.to_dict(),
            "after": after.to_dict(),
            "timestamp": None  # Can add time.time() if needed
        })
        self.save()
    
    def store_proof(self, proof) -> None:
        """Store a complete proof chain"""
        self.data.append({
            "type": "proof",
            "steps": [n.to_dict() for n in proof.steps],
            "timestamp": None
        })
        self.save()
    
    def clear(self) -> None:
        """Clear all memory and persist empty state"""
        self.data = []
        self.save()
    
    def migrate_from_pickle(self, pickle_file: str = "memory.pkl") -> bool:
        """Migrate old pickle-based memory to JSON format"""
        if not os.path.exists(pickle_file):
            return False
        
        try:
            import pickle
            with open(pickle_file, "rb") as f:
                old_data = pickle.load(f)
            
            # Convert tuples to dicts (this is simplified - adjust as needed)
            print(f"Migrating {len(old_data)} entries from {pickle_file} to {self.file}...")
            self.data = old_data  # Basic migration
            self.save()
            print(f"Migration complete. Backup your {pickle_file} and remove it.")
            return True
        except Exception as e:
            print(f"Migration failed: {e}")
            return False
