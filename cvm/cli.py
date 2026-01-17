"""
CVM Command Line Interface
===========================

Entry point for the CVM package.
"""

import sys
import argparse
from typing import Optional


def print_banner():
    """Print CVM banner"""
    print("""
    ╔═══════════════════════════════════════════════════════════╗
    ║   Cognitive Virtual Machine (CVM)                         ║
    ║   A Post-Transformer Architecture                         ║
    ╚═══════════════════════════════════════════════════════════╝
    """)


def cmd_version():
    """Show version information"""
    from cvm import __version__, __author__, __license__
    print(f"CVM version {__version__}")
    print(f"Author: {__author__}")
    print(f"License: {__license__}")


def cmd_info():
    """Show package information"""
    from cvm import __version__
    print(f"CVM v{__version__} - Post-Transformer Cognitive Architecture")
    print("\nCore Components:")
    print("  • AST: Executable semantic graphs")
    print("  • Executor: Deterministic evaluation")
    print("  • Verifier: No-hallucination guarantees")
    print("  • CVM: 4-phase cognitive architecture")
    print("\nGames:")
    print("  • Poker: Texas Hold'em agent")
    print("  • Snake: Classic game AI")
    print("  • Tic-Tac-Toe: Strategy learning")
    print("\nStorage: JSON (human-readable, secure)")


def cmd_migrate():
    """Migrate old pickle memory to JSON"""
    from cvm.core.memory import Memory
    
    mem = Memory()
    if mem.migrate_from_pickle():
        print("✓ Migration successful!")
    else:
        print("No memory.pkl file found or migration failed.")


def cmd_clear_memory():
    """Clear memory storage"""
    from cvm.core.memory import Memory
    
    mem = Memory()
    mem.clear()
    print("✓ Memory cleared.")


def main():
    """Main CLI entry point with enhanced argument parsing"""
    parser = argparse.ArgumentParser(
        prog="cvm",
        description="Cognitive Virtual Machine - Post-Transformer AI Architecture",
        epilog="For more info: https://github.com/yourusername/cvm"
    )
    
    parser.add_argument(
        "command",
        nargs="?",
        choices=["version", "info", "migrate", "clear", "help"],
        default="help",
        help="Command to execute"
    )
    
    args = parser.parse_args()
    
    if args.command == "version":
        cmd_version()
    elif args.command == "info":
        print_banner()
        cmd_info()
    elif args.command == "migrate":
        cmd_migrate()
    elif args.command == "clear":
        cmd_clear_memory()
    else:
        print_banner()
        parser.print_help()
        print("\nPython API Example:")
        print("  >>> from cvm import CVM, parse")
        print("  >>> vm = CVM()")
        print("  >>> result = vm.think(parse('2 + 3'))")


if __name__ == "__main__":
    main()
