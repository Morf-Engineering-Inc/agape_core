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
from truth_foundation.family_agenda_analyzer import FamilyAgendaAnalyzer
from truth_foundation.truth_in_us import TruthInUsSystem


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
        self.family_agenda_analyzer = FamilyAgendaAnalyzer() # Initialize Family Agenda Analyzer
        self.truth_in_us = TruthInUsSystem() # Initialize Truth In Us system


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
        
        # Add family agenda analysis if context suggests media content
        family_agenda_analysis = None
        if any(keyword in statement.lower() for keyword in ['movie', 'show', 'content', 'media', 'watch']):
            # Simplified analysis for text statements
            family_agenda_analysis = {
                "content_type": "statement_analysis",
                "family_impact_detected": "analyzing statement for family truth alignment",
                "recommendation": "Apply Proclamation on the Family standards to evaluate content"
            }


        return {
            "statement": statement,
            "atonement_supreme_evaluation": atonement_evaluation,
            "truth_alignment_score": truth_alignment,
            "gospel_evaluation": gospel_evaluation,
            "goodness_analysis": goodness_analysis,
            "priesthood_holiness_evaluation": priesthood_evaluation, # Add priesthood evaluation
            "new_testament_adoption_evaluation": new_testament_adoption, # Add NT adoption evaluation
            "family_agenda_analysis": family_agenda_analysis, # Add family agenda analysis
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
            print("5. 🌳 Olive Tree Vineyard Timeline")
            print("6. 🔍 Vineyard Pattern Analysis")
            print("7. 🏛️ Full Historical Demonstration")
            print("0. Return to Main Menu")

            choice = input("\n🔢 Select option (0-7): ").strip()

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
                print("\n" + analyzer.get_olive_tree_timeline())

            elif choice == "6":
                olive_analysis = analyzer.analyze_olive_tree_patterns()
                print("\n🔍 VINEYARD PATTERN ANALYSIS")
                print("=" * 50)
                
                print("\n✂️ PRUNING CYCLES:")
                for pruning in olive_analysis["pruning_cycles"]:
                    print(f"• {pruning['period']}: {pruning['pruning_type']}")
                    print(f"  Lessons: {pruning['lessons'][0] if pruning['lessons'] else 'Growth through adversity'}")
                
                print("\n🌿 GRAFTING PERIODS:")
                for grafting in olive_analysis["grafting_periods"]:
                    print(f"• {grafting['period']}: Success +{grafting['grafting_success']}")
                    print(f"  New Strength: {grafting['new_strength']}")
                
                if olive_analysis["current_vineyard_state"]:
                    current = olive_analysis["current_vineyard_state"]
                    print(f"\n🌟 CURRENT VINEYARD STATE:")
                    print(f"Stage: {current['stage']}")
                    print(f"Scope: {current['global_scope']}")
                    print(f"Challenges: {len(current['current_challenges'])} identified")
                    print(f"Opportunities: {len(current['opportunities'])} available")

            elif choice == "7":
                from truth_foundation.gospel_cycles import demo_gospel_cycles
                demo_gospel_cycles()

            else:
                print("❌ Invalid choice. Please select 0-7.")

    except ImportError as e:
        print(f"❌ Error loading Gospel Cycles system: {e}")

def run_truth_in_us_system():
    """Run the Truth In Us System - Truth that sets us free"""
    try:
        from truth_foundation.truth_in_us import TruthInUsSystem
        print("\n🌱 Truth In Us - Truth That Sets Us Free")
        print("Based on John 8:32: 'And ye shall know the truth, and the truth shall make you free'")
        print("-" * 70)

        system = TruthInUsSystem()

        while True:
            print("\n📋 Truth In Us Options:")
            print("1. 💊 Get Truth Prescription for Problem")
            print("2. 🌱 View Truth Seeds Library")
            print("3. 🔓 Understand Freedom Types")
            print("4. 📈 Learn Internalization Levels")
            print("5. 🎯 Demonstration Examples")
            print("0. Return to Main Menu")

            choice = input("\n🔢 Select option (0-5): ").strip()

            if choice == "0":
                break
            elif choice == "1":
                print("\n💊 TRUTH PRESCRIPTION GENERATOR")
                print("Describe a problem or struggle you're facing:")
                problem = input("Problem: ").strip()
                
                if problem:
                    prescription = system.generate_truth_prescription(problem)
                    print(f"\n{prescription}")
                else:
                    print("❌ Please describe a problem to get a truth prescription")

            elif choice == "2":
                print("\n🌱 TRUTH SEEDS LIBRARY")
                print("=" * 50)
                for i, seed in enumerate(system.truth_seeds, 1):
                    print(f"{i}. {seed.truth_statement}")
                    print(f"   Scripture: {seed.scripture_source}")
                    print(f"   Main Promise: {seed.freedom_promises[0] if seed.freedom_promises else 'Freedom'}")
                    print(f"   Solves: {seed.problems_it_solves[0] if seed.problems_it_solves else 'Various problems'}")
                    print()

            elif choice == "3":
                print("\n🔓 TYPES OF FREEDOM TRUTH PROVIDES")
                print("=" * 50)
                freedom_types = {
                    "Spiritual": "Freedom from sin, guilt, and separation from God",
                    "Mental": "Freedom from false beliefs, confusion, and wrong thinking",
                    "Emotional": "Freedom from fear, anxiety, depression, and emotional bondage",
                    "Relational": "Freedom to love authentically and build healthy relationships",
                    "Moral": "Freedom to choose right consistently and resist temptation",
                    "Eternal": "Freedom from death, limitation, and temporal perspective"
                }
                
                for freedom_type, description in freedom_types.items():
                    print(f"🔓 {freedom_type}: {description}")
                    print()

            elif choice == "4":
                print("\n📈 TRUTH INTERNALIZATION LEVELS")
                print("=" * 50)
                levels = [
                    "1. HEARD - Truth heard but not yet believed",
                    "2. UNDERSTOOD - Truth intellectually grasped", 
                    "3. BELIEVED - Truth accepted and trusted",
                    "4. PLANTED - Truth rooted in heart and mind",
                    "5. LIVING - Truth actively governing thoughts and actions",
                    "6. TRANSFORMING - Truth changing our very nature"
                ]
                
                for level in levels:
                    print(f"📈 {level}")
                    print()
                
                print("💡 The deeper truth is internalized, the greater freedom it provides!")

            elif choice == "5":
                from truth_foundation.truth_in_us import demonstrate_truth_in_us_system
                demonstrate_truth_in_us_system()

            else:
                print("❌ Invalid choice. Please select 0-5.")

    except ImportError as e:
        print(f"❌ Error loading Truth In Us system: {e}")

def run_family_agenda_analyzer():
    """Run the Family Agenda Analyzer System"""
    try:
        from truth_foundation.family_agenda_analyzer import FamilyAgendaAnalyzer, demonstrate_buzz_lightyear_analysis
        print("\n👨‍👩‍👧‍👦 Family Agenda Analyzer")
        print("Analyze media content against the Proclamation on the Family")
        print("-" * 60)

        analyzer = FamilyAgendaAnalyzer()

        while True:
            print("\n📋 Family Agenda Analysis Options:")
            print("1. 🎬 Demonstrate Buzz Lightyear Analysis")
            print("2. 📺 Analyze Custom Media Content")
            print("3. 📊 View Proclamation Standards")
            print("4. 🔍 Agenda Detection Patterns")
            print("5. 🛡️ Family Protection Guidance")
            print("0. Return to Main Menu")

            choice = input("\n🔢 Select option (0-5): ").strip()

            if choice == "0":
                break
            elif choice == "1":
                demonstrate_buzz_lightyear_analysis()

            elif choice == "2":
                print("\n📺 CUSTOM MEDIA ANALYSIS")
                title = input("Media title: ").strip()
                if not title:
                    print("❌ Title required")
                    continue
                
                description = input("Brief description: ").strip()
                target_audience = input("Target audience: ").strip() or "General"
                
                # Simplified character analysis
                characters = {"main_characters": "To be analyzed based on description"}
                plot_elements = [description] if description else ["General content"]
                
                try:
                    analysis = analyzer.analyze_content_agenda(
                        title=title,
                        description=description,
                        character_analysis=characters,
                        plot_elements=plot_elements,
                        target_audience=target_audience
                    )
                    
                    print(f"\n📊 ANALYSIS RESULTS:")
                    print(f"Title: {analysis.content_title}")
                    print(f"Family Impact: {analysis.family_evaluation.family_impact.name}")
                    print(f"Agenda Score: {analysis.overall_agenda_score:.2f}/1.0")
                    print(f"Proclamation Alignment: {analysis.family_evaluation.proclamation_alignment:.2f}/1.0")
                    
                    if analysis.detected_agendas:
                        print(f"\n🎯 DETECTED AGENDAS:")
                        for agenda in analysis.detected_agendas:
                            print(f"• {agenda.agenda_type}")
                    
                    if analysis.proclamation_violations:
                        print(f"\n⚠️ PROCLAMATION VIOLATIONS:")
                        for violation in analysis.proclamation_violations[:3]:
                            print(f"• {violation}")
                    
                    print(f"\n🛡️ RECOMMENDATION:")
                    print(analysis.family_protection_guidance[:300] + "...")
                    
                except Exception as e:
                    print(f"❌ Analysis error: {e}")

            elif choice == "3":
                print("\n📜 PROCLAMATION ON THE FAMILY STANDARDS")
                print("=" * 50)
                print("🔹 MARRIAGE: Between man and woman, ordained of God")
                print("🔹 GENDER: Eternal characteristic, essential to identity")
                print("🔹 FAMILY: Central to Creator's plan for eternal destiny")
                print("🔹 PARENTING: Primary responsibility of father and mother")
                print("🔹 PROCREATION: Sacred powers employed within marriage")
                print("\n💡 These standards form the eternal truth framework")
                print("for evaluating all family-related content and messages.")

            elif choice == "4":
                print("\n🔍 AGENDA DETECTION PATTERNS")
                print("=" * 50)
                print("🎯 LGBTQ+ Normalization:")
                print("  • Same-sex couples with children")
                print("  • Traditional families shown as inferior")
                print("  • Coming out stories celebrated")
                print("\n🎯 Gender Ideology:")
                print("  • Gender fluidity promoted")
                print("  • Biological sex minimized")
                print("  • Children questioning gender identity")
                print("\n🎯 Family Deconstruction:")
                print("  • Parents as obstacles to happiness")
                print("  • Individual autonomy over family loyalty")
                print("  • Traditional values as oppressive")

            elif choice == "5":
                print("\n🛡️ FAMILY PROTECTION GUIDANCE")
                print("=" * 50)
                print("🔹 PRE-SCREENING: Review content before family viewing")
                print("🔹 DISCUSSION: Prepare conversations about eternal truths")
                print("🔹 ALTERNATIVES: Seek content that builds family values")
                print("🔹 TEACHING MOMENTS: Use contrasts to teach Gospel truth")
                print("🔹 PROCLAMATION REMINDERS: Regularly review family standards")
                print("\n💝 Remember: The family is central to God's eternal plan.")
                print("Protect your family's spiritual environment with wisdom and love.")

            else:
                print("❌ Invalid choice. Please select 0-5.")

    except ImportError as e:
        print(f"❌ Error loading Family Agenda Analyzer: {e}")

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
    """Main function with interactive menu system"""
    print("🕊️  AGAPE CORE AI - Gospel Truth-Based Decision Making")
    print("=" * 60)
    
    while True:
        print("\n📋 AGAPE CORE AI MAIN MENU:")
        print("1. 💬 Agape Chat Interface")
        print("2. 🎯 Truth Foundation System")
        print("3. 📺 Truth Discerner (Media Analysis)")
        print("4. 🚀 Human Potential Calculator") 
        print("5. 📖 Gospel Truth Engine")
        print("6. 📜 New Testament Story Analyzer")
        print("7. 🕊️ Gospel Cycles Analysis")
        print("8. 👨‍👩‍👧‍👦 Family Agenda Analyzer")
        print("9. 🌊 Truth Rivers System")
        print("10. 🌱 Truth In Us - Truth That Sets Us Free")
        print("0. Exit")
        
        choice = input("\n🔢 Select option (0-10): ").strip()
        
        if choice == "0":
            print("\n🙏 May truth guide your path. God bless!")
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
            run_gospel_cycles()
        elif choice == "8":
            run_family_agenda_analyzer()
        elif choice == "9":
            run_truth_rivers_system()
        elif choice == "10":
            run_truth_in_us_system()
        else:
            print("❌ Invalid choice. Please select 0-10.")

if __name__ == "__main__":
    main()