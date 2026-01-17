"""
Tests for CVM Core Components
==============================

Unit tests for AST, Executor, Verifier, Compiler, and CVM phases.
"""

import pytest
from cvm import CVM, Node, parse, decompile, Executor, Verifier


class TestAST:
    """Test AST Node representation."""
    
    def test_node_creation(self):
        """Test creating a Node."""
        node = Node("Number", 42)
        assert node.type == "Number"
        assert node.value == 42
        assert node.inputs == []
    
    def test_node_with_inputs(self):
        """Test creating a Node with inputs."""
        left = Node("Number", 2)
        right = Node("Number", 3)
        add = Node("Add", inputs=[left, right])
        
        assert add.type == "Add"
        assert add.value is None
        assert len(add.inputs) == 2
    
    def test_node_equality(self):
        """Test Node equality."""
        node1 = Node("Number", 5)
        node2 = Node("Number", 5)
        node3 = Node("Number", 6)
        
        assert node1 == node2
        assert node1 != node3


class TestExecutor:
    """Test Executor evaluation."""
    
    def test_execute_number(self):
        """Test executing a number."""
        executor = Executor()
        result = executor.eval(Node("Number", 42))
        assert result == 42
    
    def test_execute_add(self):
        """Test executing addition."""
        executor = Executor()
        ast = Node("Add", inputs=[Node("Number", 2), Node("Number", 3)])
        result = executor.eval(ast)
        assert result == 5
    
    def test_execute_multiply(self):
        """Test executing multiplication."""
        executor = Executor()
        ast = Node("Mul", inputs=[Node("Number", 4), Node("Number", 5)])
        result = executor.eval(ast)
        assert result == 20


class TestVerifier:
    """Test Verifier."""
    
    def test_verify_valid_transformation(self):
        """Test verifying a valid transformation."""
        verifier = Verifier()
        before = Node("Add", inputs=[Node("Number", 1), Node("Number", 2)])
        after = Node("Number", 3)
        
        assert verifier.verify(before, after)
    
    def test_verify_invalid_transformation(self):
        """Test rejecting invalid transformation."""
        verifier = Verifier()
        before = Node("Add", inputs=[Node("Number", 1), Node("Number", 2)])
        after = Node("Number", 4)  # Wrong result
        
        assert not verifier.verify(before, after)


class TestCompiler:
    """Test Compiler (parse and decompile)."""
    
    def test_parse_number(self):
        """Test parsing a number."""
        ast = parse("42")
        assert ast.type == "Number"
        assert ast.value == 42
    
    def test_parse_addition(self):
        """Test parsing addition."""
        ast = parse("2 + 3")
        assert ast.type == "Add"
        assert len(ast.inputs) == 2
    
    def test_decompile_number(self):
        """Test decompiling a number."""
        node = Node("Number", 42)
        text = decompile(node)
        assert "42" in text
    
    def test_round_trip(self):
        """Test parse then decompile."""
        original = "5"
        ast = parse(original)
        text = decompile(ast)
        assert "5" in text


class TestCVM:
    """Test complete CVM."""
    
    def test_cvm_basic_thinking(self):
        """Test CVM basic thinking."""
        vm = CVM()
        ast = parse("2 + 3")
        result = vm.think(ast)
        
        # Should return some result structure
        assert result is not None
    
    def test_cvm_imports(self):
        """Test CVM can be imported from top level."""
        from cvm import CVM
        vm = CVM()
        assert vm is not None


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
