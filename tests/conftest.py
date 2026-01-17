"""
Test Configuration
==================

Pytest configuration and shared fixtures.
"""

import pytest
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))


@pytest.fixture
def sample_ast():
    """Sample AST for testing."""
    from cvm import Node
    return Node("Add", inputs=[Node("Number", 2), Node("Number", 3)])


@pytest.fixture
def sample_cvm():
    """Sample CVM instance for testing."""
    from cvm import CVM
    return CVM()
