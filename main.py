#!/usr/bin/env python3
"""
Agape Core AI - Main Application
A Christ-centered AI system built on the foundation of the two greatest commandments
"""

import sys
import os
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from truth_foundation.gospel_truth import GospelTruthEngine
from truth_foundation.core_truths import TruthFoundation
from truth_foundation.limitations_and_purpose import AILimitationsFramework
from truth_foundation.gospel_definitions import GospelDefinitions

def main():
    """Main application entry point"""
    print("🤖 Agape Core AI - Christ-Centered Intelligence System")
    print("═" * 60)
    print("Built on the foundation of the Two Greatest Commandments:")
    print("1. Love God with all your heart, soul, mind, and strength")
    print("2. Love your neighbor as yourself")
    print("═" * 60)

    while True:
        print("\n📋 Available Modules:")
        print("1. 💬 Agape Chat Interface")
        print("2. 🎯 Truth Foundation System")
        print("3. 📺 Truth Discerner (Media Analysis)")
        print("4. 🚀 Human Potential Calculator")
        print("5. 📖 Gospel Truth Engine")
        print("6. 📜 New Testament Story Analyzer")
        print("7. 🌊 Truth Rivers System")
        print("0. Exit")

        choice = input("\n🔢 Select a module (0-7): ").strip()

        if choice == "0":
            print("\n✝️  'Grace and peace be with you!' - Agape Core AI")
            break
        elif choice == "1":
            run_agape_chat()
        elif choice == "2":
            run_truth_foundation()
        elif choice == "3":
            run_truth_discerner()
        elif choice == "4":
            run_human_potential()
        elif choice == "5":
            run_gospel_engine()
        elif choice == "6":
            run_nt_story_analyzer()
        elif choice == "7":
            run_truth_rivers_system()
        else:
            print("❌ Invalid choice. Please select 0-7.")

def run_agape_chat():
    """Run the Agape Chat Interface"""
    try:
        from chat_interface.agape_chat import AgapeChat
        print("\n💬 Agape Chat Interface")
        print("Type 'exit' to return to main menu")
        print("-" * 40)

        chat = AgapeChat()

        while True:
            user_input = input("\n🙏 You: ").strip()
            if user_input.lower() == 'exit':
                break

            response = chat.respond(user_input)
            print(f"\n🤖 Agape AI: {response}")

    except ImportError as e:
        print(f"❌ Error loading chat interface: {e}")

def run_truth_foundation():
    """Run the Truth Foundation System"""
    try:
        from truth_foundation.core_truths import TruthFoundation
        print("\n🎯 Truth Foundation System")
        print("-" * 40)

        foundation = TruthFoundation()

        situation = input("💭 Describe a situation for truth-based guidance: ")
        if situation.strip():
            guidance = foundation.generate_truth_guidance(situation)
            print(f"\n📖 Truth Guidance:\n{guidance}")

    except ImportError as e:
        print(f"❌ Error loading truth foundation: {e}")

def run_truth_discerner():
    """Run the Truth Discerner (Media Analysis)"""
    print("\n📺 Truth Discerner - Media Analysis")
    print("-" * 40)
    print("🚧 Media analysis module ready for content evaluation")
    print("📖 Evaluate media content against biblical truth standards")
    input("Press Enter to continue...")

def run_human_potential():
    """Run the Human Potential Calculator"""
    try:
        import asyncio
        from human_potential.developmentship import HumanPotentialCalculator

        print("\n🚀 Human Potential Calculator")
        print("-" * 40)

        calc = HumanPotentialCalculator()

        try:
            mass = float(input("👥 Enter mass (number of people/resources): "))
            creativity = float(input("💡 Enter creativity score (0.0-1.0): "))

            # Run async calculation
            async def calculate():
                return await calc.calculate_hp(mass, creativity)

            hp = asyncio.run(calculate())
            print(f"\n📊 Human Potential Score: {hp:.2f}")

        except ValueError:
            print("❌ Please enter valid numbers")

    except ImportError as e:
        print(f"❌ Error loading human potential calculator: {e}")

def run_gospel_engine():
    """Run the Gospel Truth Engine"""
    try:
        from truth_foundation.gospel_truth import GospelTruthEngine
        print("\n📖 Gospel Truth Engine")
        print("-" * 40)

        engine = GospelTruthEngine()

        action = input("⚖️  Describe an action to evaluate against Gospel truth: ")
        if action.strip():
            evaluation = engine.evaluate_against_gospel(action, {})
            print(f"\n{evaluation['gospel_guidance']}")

    except ImportError as e:
        print(f"❌ Error loading gospel engine: {e}")

def run_nt_story_analyzer():
    """Run the New Testament Story Analyzer"""
    try:
        from truth_foundation.nt_story_analyzer import NTStoryAnalyzer
        print("\n📜 New Testament Story Analyzer")
        print("Focus: Golden Rule & Good Samaritan")
        print("-" * 40)

        analyzer = NTStoryAnalyzer()

        while True:
            print("\n📋 Analysis Options:")
            print("1. 🏆 Analyze Golden Rule")
            print("2. ❤️  Analyze Good Samaritan")
            print("3. 🔄 Compare Both Stories")
            print("4. 📚 Generate Teaching Outline")
            print("5. 📊 Get Summary Report")
            print("0. Return to Main Menu")

            choice = input("\n🔢 Select option (0-5): ").strip()

            if choice == "0":
                break
            elif choice == "1":
                analysis = analyzer.analyze_story("golden_rule")
                print(f"\n📖 {analysis.story.title} Analysis")
                print(f"Central Message: {analysis.story.central_message}")
                print(f"Relevance Score: {analysis.relevance_score:.2f}/1.0")
                print(f"\n💡 Modern Parallel Example:")
                print(f"• {analysis.modern_parallels[0] if analysis.modern_parallels else 'None available'}")

            elif choice == "2":
                analysis = analyzer.analyze_story("good_samaritan")
                print(f"\n📖 {analysis.story.title} Analysis")
                print(f"Central Message: {analysis.story.central_message}")
                print(f"Relevance Score: {analysis.relevance_score:.2f}/1.0")
                print(f"\n💡 Modern Parallel Example:")
                print(f"• {analysis.modern_parallels[0] if analysis.modern_parallels else 'None available'}")

            elif choice == "3":
                comparison = analyzer.compare_stories()
                print(f"\n🔄 Story Comparison")
                print(f"Common Themes:")
                for theme in comparison["common_themes"][:3]:
                    print(f"• {theme}")
                print(f"\n🤝 How They Work Together:")
                for point in comparison["complementary_nature"][:2]:
                    print(f"• {point}")

            elif choice == "4":
                story_choice = input("Generate outline for (golden_rule/good_samaritan): ").strip()
                if story_choice in ["golden_rule", "good_samaritan"]:
                    outline = analyzer.generate_teaching_outline(story_choice)
                    print(f"\n📚 Teaching Outline:\n{outline}")
                else:
                    print("❌ Invalid story choice")

            elif choice == "5":
                summary = analyzer.get_story_summary()
                print(f"\n📊 Summary Report:\n{summary}")

            else:
                print("❌ Invalid choice. Please select 0-5.")

    except ImportError as e:
        print(f"❌ Error loading NT story analyzer: {e}")

def run_truth_rivers_system():
    """Run the Truth Rivers System"""
    try:
        from truth_foundation.truth_rivers import TruthRiversSystem
        print("\n🌊 Truth Rivers System")
        print("All rivers of truth flow into the ocean of applied wisdom")
        print("-" * 60)

        system = TruthRiversSystem()

        while True:
            print("\n📋 Truth Rivers Options:")
            print("1. 🍎 Demonstrate Gravity Example")
            print("2. 💡 Seek Applied Wisdom")
            print("3. 📊 View Convergence Report")
            print("4. 🌊 Full System Demonstration")
            print("0. Return to Main Menu")

            choice = input("\n🔢 Select option (0-4): ").strip()

            if choice == "0":
                break
            elif choice == "1":
                print("\n" + system.demonstrate_gravity_example())

            elif choice == "2":
                question = input("\n❓ What wisdom do you seek? ")
                if question.strip():
                    wisdom = system.seek_wisdom(question)
                    print(f"\n{wisdom}")

            elif choice == "3":
                print("\n" + system.get_convergence_report())

            elif choice == "4":
                print("\n🌊 FULL TRUTH RIVERS DEMONSTRATION")
                print("=" * 50)

                # Show system overview
                print(system.get_convergence_report())

                # Demonstrate gravity
                print("\n" + system.demonstrate_gravity_example())

                # Test wisdom seeking
                print("\n💡 WISDOM SEEKING EXAMPLES:")
                examples = [
                    "How do I integrate science and faith?",
                    "What should guide my research decisions?",
                    "How do I handle conflicting truth claims?"
                ]

                for example in examples:
                    print(f"\n❓ {example}")
                    wisdom = system.seek_wisdom(example)
                    print(wisdom)
                    print("-" * 40)

            else:
                print("❌ Invalid choice. Please select 0-4.")

    except ImportError as e:
        print(f"❌ Error loading Truth Rivers System: {e}")

if __name__ == "__main__":
    main()