"""
Tests for JSON-based memory storage system
"""
import os
import json
import tempfile
import pytest
from cvm.core.memory import Memory
from cvm.core.ast import Node
from cvm.core.proof import Proof


class TestJSONMemory:
    """Test JSON-based memory persistence"""
    
    def setup_method(self):
        """Setup for each test - use temp file"""
        self.temp_file = tempfile.NamedTemporaryFile(
            mode='w', 
            suffix='.json', 
            delete=False
        )
        self.temp_file.close()
        self.memory = Memory(file=self.temp_file.name)
    
    def teardown_method(self):
        """Cleanup after each test"""
        if os.path.exists(self.temp_file.name):
            os.remove(self.temp_file.name)
    
    def test_memory_initialization(self):
        """Test memory initializes correctly"""
        assert self.memory.data == []
        assert self.memory.file == self.temp_file.name
    
    def test_store_transformation(self):
        """Test storing AST transformations"""
        before = Node("Add", None, [Node("Number", 2), Node("Number", 3)])
        after = Node("Number", 5)
        
        self.memory.store(before, after)
        
        # Verify data structure
        assert len(self.memory.data) == 1
        entry = self.memory.data[0]
        assert entry["type"] == "transformation"
        assert "before" in entry
        assert "after" in entry
    
    def test_json_serialization(self):
        """Test that memory is saved as valid JSON"""
        before = Node("Number", 10)
        after = Node("Number", 20)
        
        self.memory.store(before, after)
        
        # Read raw JSON file
        with open(self.temp_file.name, 'r') as f:
            data = json.load(f)
        
        assert isinstance(data, list)
        assert len(data) == 1
        assert data[0]["type"] == "transformation"
    
    def test_json_human_readable(self):
        """Test that JSON output is human-readable (formatted)"""
        n1 = Node("Number", 42)
        n2 = Node("Number", 84)
        
        self.memory.store(n1, n2)
        
        # Check file has indentation (not minified)
        with open(self.temp_file.name, 'r') as f:
            content = f.read()
        
        assert '\n' in content  # Has newlines
        assert '  ' in content  # Has indentation
    
    def test_memory_persistence(self):
        """Test memory persists across instances"""
        n1 = Node("Add", None, [Node("Number", 1), Node("Number", 2)])
        n2 = Node("Number", 3)
        
        # Store in first instance
        self.memory.store(n1, n2)
        
        # Create new instance with same file
        memory2 = Memory(file=self.temp_file.name)
        
        # Should load existing data
        assert len(memory2.data) == 1
        assert memory2.data[0]["type"] == "transformation"
    
    def test_store_proof_chain(self):
        """Test storing proof chains"""
        steps = [
            Node("Add", None, [Node("Number", 2), Node("Number", 3)]),
            Node("Number", 5)
        ]
        proof = Proof(steps)
        
        self.memory.store_proof(proof)
        
        assert len(self.memory.data) == 1
        entry = self.memory.data[0]
        assert entry["type"] == "proof"
        assert "steps" in entry
        assert len(entry["steps"]) == 2
    
    def test_clear_memory(self):
        """Test clearing all memory"""
        self.memory.store(Node("Number", 1), Node("Number", 2))
        self.memory.store(Node("Number", 3), Node("Number", 4))
        
        assert len(self.memory.data) == 2
        
        self.memory.clear()
        
        assert len(self.memory.data) == 0
        
        # Verify it persisted
        with open(self.temp_file.name, 'r') as f:
            data = json.load(f)
        assert data == []
    
    def test_corrupted_json_handling(self):
        """Test graceful handling of corrupted JSON"""
        # Write invalid JSON
        with open(self.temp_file.name, 'w') as f:
            f.write("{ invalid json }")
        
        # Should not crash, just return empty
        memory = Memory(file=self.temp_file.name)
        assert memory.data == []
    
    def test_missing_file_handling(self):
        """Test handling of non-existent file"""
        non_existent = "non_existent_memory_file.json"
        memory = Memory(file=non_existent)
        
        assert memory.data == []
        assert memory.file == non_existent
    
    def test_node_serialization_roundtrip(self):
        """Test Node.to_dict() and Node.from_dict() roundtrip"""
        original = Node(
            "Add", 
            None, 
            [
                Node("Number", 10),
                Node("Mul", None, [Node("Number", 2), Node("Number", 5)])
            ]
        )
        
        # Serialize
        data = original.to_dict()
        
        # Deserialize
        restored = Node.from_dict(data)
        
        # Compare structure (using string representation)
        assert str(original) == str(restored)
        assert restored.type == "Add"
        assert len(restored.inputs) == 2
        assert restored.inputs[0].type == "Number"
        assert restored.inputs[1].type == "Mul"


class TestMemoryMigration:
    """Test migration from pickle to JSON"""
    
    def test_migration_command(self):
        """Test that migration utility exists"""
        from cvm.core.memory import Memory
        
        memory = Memory()
        assert hasattr(memory, 'migrate_from_pickle')
        assert callable(memory.migrate_from_pickle)
