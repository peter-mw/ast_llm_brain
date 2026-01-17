"""
Main entry point for the AST-based Cognitive Virtual Machine
"""
import sys


def print_banner():
    print("""
    ╔═══════════════════════════════════════════════════════════╗
    ║   AST-Based Cognitive Virtual Machine                     ║
    ║   A Post-Transformer Architecture                         ║
    ╚═══════════════════════════════════════════════════════════╝
    """)


def main():
    print_banner()
    
    if len(sys.argv) < 2:
        print("Usage: python main.py <phase>")
        print("\nAvailable phases:")
        print("  phase1  - Basic cognitive loop")
        print("  phase2  - Multi-step reasoning")
        print("  phase3  - Non-token intelligence")
        print("  phase4  - Autonomous cognition")
        print("  poker   - Learn to play poker (self-play)")
        print("  tictactoe - Learn to play tic-tac-toe (self-play)")
        print("  all     - Run all phases sequentially")
        print("\nExample: python main.py phase1")
        print("Example: python main.py poker")
        return
    
    phase = sys.argv[1].lower()
    
    if phase == "phase1" or phase == "1":
        from demo_phase1 import main as demo
        demo()
    
    elif phase == "phase2" or phase == "2":
        from demo_phase2 import main as demo
        demo()
    
    elif phase == "phase3" or phase == "3":
        from demo_phase3 import main as demo
        demo()
    
    elif phase == "phase4" or phase == "4":
        from demo_phase4 import main as demo
        demo()
    
    elif phase == "poker":
        from demo_poker_auto import main as demo
        demo()
    
    elif phase == "tictactoe":
        from demo_tictactoe_auto import main as demo
        demo()
    
    elif phase == "all":
        print("\n" + "="*60)
        print("Running ALL phases sequentially...")
        print("="*60 + "\n")
        
        from demo_phase1 import main as demo1
        from demo_phase2 import main as demo2
        from demo_phase3 import main as demo3
        from demo_phase4 import main as demo4
        
        demo1()
        print("\n" + "="*60 + "\n")
        demo2()
        print("\n" + "="*60 + "\n")
        demo3()
        print("\n" + "="*60 + "\n")
        demo4()
    
    else:
        print(f"Unknown phase: {phase}")
        print("Use: phase1, phase2, phase3, phase4, or all")


if __name__ == "__main__":
    main()
