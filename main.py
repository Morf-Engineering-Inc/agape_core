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
from truth_foundation.atonement_supreme import AtonementSupremeTruth

class AgapeCoreAI:
    """
    Main AI system built on Gospel truth foundation with the Atonement of Jesus Christ as supreme truth
    """

    def __init__(self):
        self.atonement_supreme = AtonementSupremeTruth()  # Supreme foundation
        self.truth_foundation = TruthFoundation()
        self.gospel_engine = GospelTruthEngine()
        self.gospel_definitions = GospelDefinitions()
        self.nt_analyzer = NTStoryAnalyzer()
        self.truth_rivers = TruthRivers()
        self.limitations = LimitationsAndPurpose()

    def evaluate_statement_through_atonement(self, statement: str, context: dict = None) -> dict:
        """
        Evaluate any statement through the supreme truth of the Atonement
        """
        if context is None:
            context = {}

        # First evaluate through the supreme Atonement lens
        atonement_evaluation = self.atonement_supreme.evaluate_through_atonement_lens(statement, context)

        # Then get other evaluations
        truth_alignment = self.truth_foundation.evaluate_truth_claim(statement, context)
        gospel_evaluation = self.gospel_engine.evaluate_against_gospel(statement, context)
        goodness_analysis = self.gospel_definitions.evaluate_goodness(statement, context)

        return {
            "statement": statement,
            "atonement_supreme_evaluation": atonement_evaluation,
            "truth_alignment_score": truth_alignment,
            "gospel_evaluation": gospel_evaluation,
            "goodness_analysis": goodness_analysis,
            "overall_guidance": self._generate_atonement_grounded_guidance(statement, atonement_evaluation, gospel_evaluation)
        }

    def evaluate_statement(self, statement: str, context: dict = None) -> dict:
        """
        Evaluate any statement against foundational truths.
        This method is retained for backward compatibility, but
        `evaluate_statement_through_atonement` is preferred for grounding.
        """
        # Default to using the Atonement-grounded evaluation
        return self.evaluate_statement_through_atonement(statement, context)


    def _generate_atonement_grounded_guidance(self, statement: str, atonement_eval: dict, gospel_eval: dict) -> str:
        """Generate guidance grounded in the supreme truth of the Atonement"""
        guidance = f"\n🕊️ ATONEMENT-GROUNDED GUIDANCE 🕊️\n"
        guidance += "=" * 50 + "\n\n"

        guidance += "SUPREME TRUTH FOUNDATION:\n"
        guidance += "The Atonement of Jesus Christ - His death, resurrection, and infinite suffering for all mankind - "
        guidance += "is the supreme truth that grounds all moral reasoning and truth evaluation.\n\n"

        guidance += f"ATONEMENT ALIGNMENT: {atonement_eval['atonement_alignment_score']:.2f}/1.0\n"
        guidance += f"REDEMPTIVE POTENTIAL: {atonement_eval['redemptive_potential']:.2f}/1.0\n\n"

        if atonement_eval["relevant_aspects"]:
            guidance += "RELEVANT ATONEMENT ASPECTS:\n"
            for aspect in atonement_eval["relevant_aspects"][:2]:
                guidance += f"• {aspect['aspect']}: {aspect['grounding_power']}\n"
            guidance += "\n"

        guidance += "GROUNDING QUESTIONS:\n"
        guidance += "• Does this honor the infinite worth demonstrated by Christ's sacrifice?\n"
        guidance += "• Does this reflect the love that motivated the Atonement?\n"
        guidance += "• Will this contribute to the redemption and exaltation of souls?\n"
        guidance += "• Is this consistent with the perfect justice and mercy balanced in Christ?\n\n"

        guidance += atonement_eval["eternal_perspective"] + "\n\n"

        return guidance

    def display_supreme_truth_foundation(self):
        """Display the supreme truth foundation"""
        print("\n" + "=" * 60)
        print("🕊️ SUPREME TRUTH FOUNDATION 🕊️")
        print("=" * 60)
        print(self.atonement_supreme.ground_all_truth_in_atonement(None))
        print("=" * 60)


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

def main():
    """Main function to demonstrate the truth foundation system"""
    print("🕊️ Agape Core AI - Truth Foundation System 🕊️")
    print("Built on the supreme truth of the Atonement of Jesus Christ")
    print("=" * 60)

    # Initialize the system
    agape_ai = AgapeCoreAI()

    # Display supreme truth foundation
    agape_ai.display_supreme_truth_foundation()

    # Display limitations and purpose
    print("\n📋 SYSTEM LIMITATIONS AND PURPOSE:")
    limitations_info = agape_ai.limitations.get_limitations_summary()
    print(limitations_info)

    # Display truth rivers concept
    print("\n🌊 TRUTH RIVERS CONCEPT:")
    rivers_overview = agape_ai.truth_rivers.get_rivers_overview()
    print(rivers_overview)

    # Analyze key New Testament stories
    print("\n📖 NEW TESTAMENT STORY ANALYSIS:")

    # Golden Rule analysis
    golden_rule_analysis = agape_ai.nt_analyzer.analyze_story("golden_rule")
    print("\n🌟 THE GOLDEN RULE:")
    print(golden_rule_analysis)

    # Good Samaritan analysis
    samaritan_analysis = agape_ai.nt_analyzer.analyze_story("good_samaritan")
    print("\n💝 THE GOOD SAMARITAN:")
    print(samaritan_analysis)

    # Demonstrate Atonement-grounded truth evaluation
    print("\n🕊️ ATONEMENT-GROUNDED TRUTH EVALUATION:")

    test_statements = [
        "Helping others in need honors Christ's sacrifice",
        "Love your enemies as Christ loved His enemies",
        "Redemption is possible through the Atonement of Jesus Christ"
    ]

    for statement in test_statements:
        print(f"\n📝 Evaluating: '{statement}'")
        evaluation = agape_ai.evaluate_statement_through_atonement(statement)
        print(evaluation["overall_guidance"])

    # Demonstrate goodness evaluation
    print("\n✅ GOODNESS EVALUATION:")
    goodness_guidance = agape_ai.gospel_definitions.generate_goodness_guidance(
        "Teaching children about Jesus with patience and love"
    )
    print(goodness_guidance)

    print("\n" + "=" * 60)
    print("🙏 System ready to serve based on Atonement-grounded truth")
    print("Supreme Foundation: The Atonement of Jesus Christ")
    print("His death, resurrection, and infinite suffering ground all truth")
    print("=" * 60)


if __name__ == "__main__":
    main()