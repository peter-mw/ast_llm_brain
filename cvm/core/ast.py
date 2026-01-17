"""
Core AST representation for cognitive graphs
"""
from dataclasses import dataclass, field
from typing import Any, List, Dict


@dataclass
class Node:
    """
    Executable semantic node - the fundamental unit of thought
    Replaces tokens with structured, verifiable computational elements
    """
    type: str
    value: Any = None
    inputs: List["Node"] = field(default_factory=list)
    meta: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization"""
        return {
            "type": self.type,
            "value": self.value,
            "inputs": [i.to_dict() for i in self.inputs],
            "meta": self.meta
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Node":
        """Reconstruct Node from dictionary (JSON deserialization)"""
        if data is None:
            return None
        inputs = [cls.from_dict(inp) for inp in data.get("inputs", [])]
        return cls(
            type=data["type"],
            value=data.get("value"),
            inputs=inputs,
            meta=data.get("meta", {})
        )

    def to_tuple(self):
        """Convert to immutable tuple for hashing and comparison"""
        return (self.type, self.value, tuple(i.to_tuple() for i in self.inputs))
    
    def __str__(self):
        """Human-readable representation"""
        if self.type == "Number":
            return str(self.value)
        elif self.type in ["Add", "Mul"]:
            return f"{self.type}({', '.join(str(i) for i in self.inputs)})"
        return f"{self.type}({self.value})"
