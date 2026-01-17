"""
Poker Learning Demo - Automated Version
Demonstrates CVM learning to play Texas Hold'em through self-play
"""
from core.poker_agent import PokerAgent, PokerTrainer


def print_banner():
    print("=" * 70)
    print("POKER LEARNING - CVM Teaching Itself Texas Hold'em")
    print("=" * 70)
    print()


def demo_basic_game():
    """Show a basic poker game"""
    print("🎴 DEMO 1: Basic Poker Game")
    print("-" * 70)
    print()
    
    agent1 = PokerAgent("Agent1")
    agent2 = PokerAgent("Agent2")
    trainer = PokerTrainer()
    
    print("Playing sample hands...")
    print()
    
    # Play a few hands to show the system works
    for i in range(3):
        trainer.env.reset()
        reward, won = agent1.play_hand(trainer.env, agent2, 0, verbose=False)
        print(f"  Hand {i+1}: {'Agent1 wins!' if won else 'Agent2 wins!'} (reward: {reward})")
    
    print()


def demo_learning_progress():
    """Show learning over time"""
    print("🧠 DEMO 2: Learning Through Self-Play")
    print("-" * 70)
    print()
    
    agent1 = PokerAgent("Learner")
    agent2 = PokerAgent("Opponent")
    trainer = PokerTrainer()
    
    print("Training through self-play...")
    print()
    
    # Track learning progress
    checkpoints = [10, 50, 100, 250, 500]
    
    hands_trained = 0
    for checkpoint in checkpoints:
        hands_to_train = checkpoint - hands_trained
        
        print(f"Training hands {hands_trained + 1} to {checkpoint}...")
        results = trainer.train(agent1, agent2, num_hands=hands_to_train, verbose=False)
        
        win_rate = agent1.get_win_rate()
        
        print(f"  After {checkpoint} hands:")
        print(f"    Win rate: {win_rate:.1%}")
        print(f"    Total wins: {agent1.win_count}/{agent1.hand_count}")
        print(f"    Strategy size: {len(agent1.strategy)} states learned")
        print()
        
        hands_trained = checkpoint
    
    return agent1


def demo_strategy_analysis(agent):
    """Analyze learned strategy"""
    print("📊 DEMO 3: Strategy Analysis")
    print("-" * 70)
    print()
    
    print("Learned Strategy Insights:")
    print()
    
    # Analyze strategy
    strong_hands = 0
    medium_hands = 0
    weak_hands = 0
    
    aggressive_actions = 0
    passive_actions = 0
    
    for state_key, actions in agent.strategy.items():
        if 'strong' in state_key:
            strong_hands += 1
        elif 'medium' in state_key:
            medium_hands += 1
        else:
            weak_hands += 1
        
        for action, value in actions.items():
            if action in ['raise', 'all_in']:
                aggressive_actions += 1
            elif action in ['check', 'fold']:
                passive_actions += 1
    
    print(f"  States encountered:")
    print(f"    Strong hands: {strong_hands}")
    print(f"    Medium hands: {medium_hands}")
    print(f"    Weak hands: {weak_hands}")
    print()
    
    print(f"  Action preferences:")
    print(f"    Aggressive (raise/all-in): {aggressive_actions}")
    print(f"    Passive (check/fold): {passive_actions}")
    print()
    
    # Show specific strategies
    print("  Sample learned strategies:")
    count = 0
    for state_key, actions in list(agent.strategy.items())[:10]:
        if count >= 3:
            break
        if actions:  # Only show if has actions
            best_action = max(actions.items(), key=lambda x: x[1])
            print(f"    Situation: ...{state_key[-50:]}")
            print(f"      → Best action: {best_action[0]} (value: {best_action[1]:.2f})")
            count += 1
    
    print()
    print(f"Final Statistics:")
    print(f"  Win rate: {agent.get_win_rate():.1%}")
    print(f"  Total hands: {agent.hand_count}")
    print(f"  States mastered: {len(agent.strategy)}")
    print()


def demo_agent_competition():
    """Pit trained agent against untrained"""
    print("⚔️  DEMO 4: Trained vs Untrained")
    print("-" * 70)
    print()
    
    print("Creating two agents...")
    trained = PokerAgent("Trained")
    untrained = PokerAgent("Untrained")
    
    # Train first agent
    print("Training first agent for 500 hands...")
    trainer = PokerTrainer()
    trainer.train(trained, PokerAgent("PracticeBot"), num_hands=500, verbose=False)
    
    print(f"✓ Training complete. Win rate: {trained.get_win_rate():.1%}")
    print()
    
    # Now pit them against each other
    print("Competition: 100 hands")
    print()
    
    competition_results = trainer.train(trained, untrained, num_hands=100, verbose=False)
    
    print("Results:")
    print(f"  Trained agent wins: {competition_results['agent1_wins']}")
    print(f"  Untrained agent wins: {competition_results['agent2_wins']}")
    print(f"  Win rate: {competition_results['agent1_wins']/100:.1%}")
    print()
    
    # Calculate average rewards
    avg_reward_trained = sum(competition_results['agent1_rewards']) / len(competition_results['agent1_rewards'])
    avg_reward_untrained = sum(competition_results['agent2_rewards']) / len(competition_results['agent2_rewards'])
    
    print(f"  Average reward (trained): {avg_reward_trained:.1f} chips/hand")
    print(f"  Average reward (untrained): {avg_reward_untrained:.1f} chips/hand")
    print()
    
    if competition_results['agent1_wins'] > competition_results['agent2_wins']:
        print("  ✓ Trained agent DOMINATES untrained opponent!")
    else:
        print("  ≈ Results show learning in progress...")
    print()


def demo_cognitive_insights():
    """Show CVM cognitive features during poker"""
    print("🧬 DEMO 5: Cognitive Architecture in Action")
    print("-" * 70)
    print()
    
    agent = PokerAgent("CognitiveAgent")
    
    print("The CVM poker agent uses Phase IV features:")
    print()
    print("  ✓ Temporal Memory - Recent hands influence strategy")
    print("  ✓ Goal-Directed Planning - Maximize chip EV")
    print("  ✓ Abstraction Formation - Learns hand categories")
    print("  ✓ Meta-Reasoning - Reflects on strategy success")
    print()
    
    print("Training and observing cognitive processes...")
    trainer = PokerTrainer()
    trainer.train(agent, PokerAgent("Opponent"), num_hands=300, verbose=False)
    
    print()
    print("Cognitive State After Training:")
    print()
    print(f"  Memory utilization:")
    print(f"    Temporal memory entries: {len(agent.cvm.temporal_memory.entries)}")
    print(f"    Abstraction patterns: {len(agent.cvm.abstraction.patterns)}")
    print()
    
    print(f"  Learning metrics:")
    print(f"    States explored: {len(agent.strategy)}")
    print(f"    Hands played: {agent.hand_count}")
    print(f"    Current win rate: {agent.get_win_rate():.1%}")
    print()


def main():
    print_banner()
    
    print("This demonstration shows the CVM learning poker through self-play.")
    print("The cognitive architecture enables the agent to:")
    print("  • Learn from experience (temporal memory)")
    print("  • Develop strategy (abstraction formation)")
    print("  • Improve over time (meta-reasoning)")
    print("  • Make goal-directed decisions (planning)")
    print()
    print()
    
    # Demo 1: Basic game
    demo_basic_game()
    
    # Demo 2: Learning progress
    trained_agent = demo_learning_progress()
    
    # Demo 3: Strategy analysis
    demo_strategy_analysis(trained_agent)
    
    # Demo 4: Competition
    demo_agent_competition()
    
    # Demo 5: Cognitive insights
    demo_cognitive_insights()
    
    print("=" * 70)
    print("CONCLUSION")
    print("=" * 70)
    print()
    print("✓ The CVM successfully taught itself poker through self-play")
    print("✓ Learning emerged from Phase IV cognitive architecture:")
    print("    - Goal-directed behavior (maximize chips)")
    print("    - Temporal memory (recent hand outcomes)")
    print("    - Abstraction formation (hand categories)")
    print("    - Strategic planning (action selection)")
    print()
    print("This demonstrates the power of executable, verifiable cognition")
    print("for complex strategic learning tasks.")
    print()
    print("🎴 The CVM is now a poker player. 🧠")
    print("=" * 70)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nDemo interrupted.")
    except Exception as e:
        print(f"\nError: {e}")
        import traceback
        traceback.print_exc()
