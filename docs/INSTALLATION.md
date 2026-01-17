# Installation Guide

## Quick Install

### From PyPI (when published)

```bash
pip install cvm
```

### From Source

1. Clone the repository:
```bash
git clone https://github.com/yourusername/cvm.git
cd cvm
```

2. Install in development mode:
```bash
pip install -e .
```

3. Install with optional dependencies:
```bash
# For visual memory support
pip install -e ".[visual]"

# For games
pip install -e ".[games]"

# For development
pip install -e ".[dev]"

# Install everything
pip install -e ".[all]"
```

## Requirements

- Python 3.8 or higher
- No required dependencies (pure Python core)

### Optional Dependencies

- **numpy** (>=1.20.0): For embeddings and visual memory
- **pillow** (>=8.0.0): For visual memory image generation
- **matplotlib**: For visualizations (used in demos)

## Verify Installation

```python
import cvm
print(cvm.__version__)

from cvm import CVM
vm = CVM()
print("CVM installed successfully!")
```

## Development Setup

For contributors:

```bash
# Clone repository
git clone https://github.com/yourusername/cvm.git
cd cvm

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements-dev.txt

# Install package in editable mode
pip install -e ".[dev]"

# Run tests
pytest

# Run linter
flake8 cvm/

# Format code
black cvm/
```

## Troubleshooting

### Import Errors

If you see `ModuleNotFoundError: No module named 'cvm'`:

1. Ensure you installed the package: `pip install -e .`
2. Check your Python path: `python -c "import sys; print(sys.path)"`
3. Verify the package is installed: `pip list | grep cvm`

### Test Failures

If tests fail:

1. Ensure all dependencies are installed: `pip install -e ".[dev]"`
2. Run tests with verbose output: `pytest -v`
3. Check for conflicting packages: `pip list`

## Uninstallation

```bash
pip uninstall cvm
```
