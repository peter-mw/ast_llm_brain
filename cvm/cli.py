"""
CVM Command Line Interface
===========================

Entry point for the CVM package.
"""

import sys


def main():
    """Main CLI entry point."""
    print("""
    ╔═══════════════════════════════════════════════════════════╗
    ║   Cognitive Virtual Machine (CVM)                         ║
    ║   A Post-Transformer Architecture                         ║
    ╚═══════════════════════════════════════════════════════════╝
    
    Usage: cvm <command>
    
    Commands:
      version    - Show version information
      demo       - Run interactive demos
      help       - Show this help message
    
    For Python API usage:
      >>> from cvm import CVM
      >>> from cvm.core.compiler import parse
      >>> vm = CVM()
      >>> result = vm.think(parse("2 + 3"))
    
    For more information, visit:
    https://github.com/yourusername/cvm
    """)
    
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        
        if command == "version":
            from cvm import __version__
            print(f"CVM version {__version__}")
        
        elif command == "demo":
            print("Demo mode - import examples manually:")
            print("  from examples import demo_phase1")
            print("  demo_phase1.main()")
        
        elif command == "help":
            pass  # Already printed above
        
        else:
            print(f"Unknown command: {command}")
            print("Run 'cvm help' for usage information")


if __name__ == "__main__":
    main()
