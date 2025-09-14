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
from truth_foundation.seekgood import SeekGoodEvaluator
# Import NTStoryAnalyzer and TruthRivers, assuming they exist in truth_foundation
from truth_foundation.nt_story_analyzer import NTStoryAnalyzer
from truth_foundation.truth_rivers import TruthRivers
# Import LimitationsAndPurpose, assuming it exists in limitations_and_purpose
from limitations_and_purpose import LimitationsAndPurpose
# Import AdviceCredibilityAnalyzer and related functions
from truth_foundation.advice_credibility import AdviceCredibilityAnalyzer, analyze_sam_altman_example
from truth_foundation.gospel_cycles import GospelCyclesAnalyzer
from truth_foundation.priesthood_holiness import PriesthoodHolinessFramework


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
        self.seekgood_evaluator = SeekGoodEvaluator()
        self.advice_analyzer = AdviceCredibilityAnalyzer() # Initialize AdviceCredibilityAnalyzer
        self.gospel_cycles = GospelCyclesAnalyzer() # Initialize Gospel Cycles Analyzer
        self.priesthood_holiness = PriesthoodHolinessFramework() # Initialize Priesthood Holiness Framework


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

        # Integrate Priesthood Holiness framework
        priesthood_evaluation = self.priesthood_holiness.evaluate_priesthood_pattern(statement, context)
        new_testament_adoption = self.priesthood_holiness.evaluate_new_testament_adoption(statement, context)


        return {
            "statement": statement,
            "atonement_supreme_evaluation": atonement_evaluation,
            "truth_alignment_score": truth_alignment,
            "gospel_evaluation": gospel_evaluation,
            "goodness_analysis": goodness_analysis,
            "priesthood_holiness_evaluation": priesthood_evaluation, # Add priesthood evaluation
            "new_testament_adoption_evaluation": new_testament_adoption, # Add NT adoption evaluation
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

def run_gospel_cycles():
    """Run the Gospel Cycles Analysis System"""
    try:
        from truth_foundation.gospel_cycles import GospelCyclesAnalyzer
        print("\n🕊️ Gospel Cycles Analysis")
        print("Understanding God's relationship with His people through D&C 121:40-45")
        print("-" * 70)

        analyzer = GospelCyclesAnalyzer()

        while True:
            print("\n📋 Gospel Cycles Options:")
            print("1. 📊 View Historical Cycle Summary")
            print("2. 🔮 Predict Cycle Behavior")
            print("3. 🌟 Analyze Current Restoration")
            print("4. 📖 D&C 121 Pattern Analysis")
            print("5. 🏛️ Full Historical Demonstration")
            print("0. Return to Main Menu")

            choice = input("\n🔢 Select option (0-5): ").strip()

            if choice == "0":
                break
            elif choice == "1":
                print("\n" + analyzer.get_cycle_summary())

            elif choice == "2":
                print("\n🔮 BEHAVIORAL PREDICTION")
                print("Enter current conditions to predict cycle behavior:")

                triggers_input = input("Current triggers (comma-separated): ").strip()
                weaknesses_input = input("Observed weaknesses (comma-separated): ").strip()
                strengths_input = input("Present strengths (comma-separated): ").strip()
                emotions_input = input("Dominant emotions (comma-separated): ").strip()

                conditions = {}
                if triggers_input:
                    conditions["triggers"] = [t.strip() for t in triggers_input.split(",")]
                if weaknesses_input:
                    conditions["weaknesses"] = [w.strip() for w in weaknesses_input.split(",")]
                if strengths_input:
                    conditions["strengths"] = [s.strip() for s in strengths_input.split(",")]
                if emotions_input:
                    conditions["emotions"] = [e.strip() for e in emotions_input.split(",")]

                if conditions:
                    prediction = analyzer.predict_cycle_behavior(conditions)

                    print(f"\n📈 PREDICTION RESULTS:")
                    print(f"Likely Pattern: {prediction['likely_pattern'] or 'Unknown'}")
                    print(f"Confidence: {prediction['confidence_score']:.2f}/1.0")
                    print(f"Cycle Direction: {prediction['cycle_direction'] or 'Unclear'}")
                    print(f"Duration Estimate: {prediction['duration_estimate'] or 'Unknown'}")

                    if prediction["key_warnings"]:
                        print(f"\n⚠️ D&C 121 WARNINGS:")
                        for warning in prediction["key_warnings"]:
                            print(f"• {warning}")

                    if prediction["dc_121_guidance"]:
                        print(f"\n💡 D&C 121 GUIDANCE:")
                        for guidance in prediction["dc_121_guidance"]:
                            print(f"• {guidance}")

            elif choice == "3":
                current_analysis = analyzer.analyze_current_restoration_cycle()
                print(f"\n🌟 CURRENT RESTORATION ANALYSIS:")
                print(f"Phase: {current_analysis['current_phase']}")
                print(f"Duration: {current_analysis['duration_so_far']} years")
                print(f"Faithfulness: {current_analysis['faithfulness_trajectory']}")
                print(f"Stage: {current_analysis['olive_tree_stage']}")

                if current_analysis["potential_threats"]:
                    print(f"\n⚠️ POTENTIAL THREATS:")
                    for threat in current_analysis["potential_threats"][:3]:
                        print(f"• {threat}")

                if current_analysis["strengthening_opportunities"]:
                    print(f"\n💪 STRENGTHENING OPPORTUNITIES:")
                    for opp in current_analysis["strengthening_opportunities"][:3]:
                        print(f"• {opp}")

            elif choice == "4":
                print("\n📖 D&C 121:40-45 PATTERN ANALYSIS")
                print("=" * 50)
                print("Key Principle: 'No power or influence can or ought to be maintained")
                print("by virtue of the priesthood, only by persuasion, by long-suffering,")
                print("by gentleness and meekness, and by love unfeigned'")
                print("\nHistorical patterns show:")
                print("• Pride/compulsion → Heaven's withdrawal → Apostasy")
                print("• Humility/persuasion → Divine favor → Restoration")
                print("• Righteousness → Gathering and prosperity")
                print("• Wickedness → Scattering and bondage")

            elif choice == "5":
                from truth_foundation.gospel_cycles import demo_gospel_cycles
                demo_gospel_cycles()

            else:
                print("❌ Invalid choice. Please select 0-5.")

    except ImportError as e:
        print(f"❌ Error loading Gospel Cycles system: {e}")

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
    print("🕊️  AGAPE CORE AI - Gospel Truth-Based Decision Making")
    print("=" * 60)

    print("\n🔍 ADVICE CREDIBILITY ANALYSIS DEMO")
    print("-" * 40)
    print("Demonstrating how our framework handles apparent contradictions...")

    # Import and run the synthesis analysis
    from truth_foundation.advice_credibility import analyze_jobs_yc_scaling_synthesis
    analyze_jobs_yc_scaling_synthesis()

    print("\n" + "-" * 40)
    analyze_sam_altman_example()

    print("\n" + "=" * 60)
    print("💬 INTERACTIVE CHAT INTERFACE")
    print("-" * 40)

    # Initialize chat interface
    try:
        from chat_interface.agape_chat import AgapeChat
        chat = AgapeChat()
        chat.start_chat()
    except ImportError as e:
        print(f"❌ Error loading chat interface: {e}")

if __name__ == "__main__":
    main()