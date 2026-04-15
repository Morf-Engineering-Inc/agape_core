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
from truth_foundation.truth_rivers import TruthRiversSystem as TruthRivers
# Import AdviceCredibilityAnalyzer and related functions
from truth_foundation.advice_credibility import AdviceCredibilityAnalyzer, analyze_sam_altman_example
from truth_foundation.gospel_cycles import GospelCyclesAnalyzer
from truth_foundation.priesthood_holiness import PriesthoodHolinessFramework
from truth_foundation.family_agenda_analyzer import FamilyAgendaAnalyzer
from truth_foundation.book_of_mormon_precepts import BookOfMormonPreceptsFramework
from truth_foundation.glory_to_god import GloryToGodEvaluator
from truth_foundation.truth_system_evaluator import TruthSystemEvaluator # Import the new evaluator
from truth_foundation.truth_in_us import TruthInUsSystem as TruthInUsFramework
from truth_foundation.temple_laws import TempleLawsFramework
from truth_foundation.natural_man_flesh import NaturalManAnalyzer
from arcos.arcos_core import ArcOsCore # Import NaturalManAnalyzer

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
        self.limitations = AILimitationsFramework()
        self.seekgood_evaluator = SeekGoodEvaluator()
        self.advice_analyzer = AdviceCredibilityAnalyzer() # Initialize AdviceCredibilityAnalyzer
        self.gospel_cycles = GospelCyclesAnalyzer() # Initialize Gospel Cycles Analyzer
        self.priesthood_holiness = PriesthoodHolinessFramework() # Initialize Priesthood Holiness Framework
        self.family_agenda_analyzer = FamilyAgendaAnalyzer() # Initialize Family Agenda Analyzer
        self.bom_precepts = BookOfMormonPreceptsFramework() # Initialize Book of Mormon Precepts
        self.glory_evaluator = GloryToGodEvaluator() # Initialize Glory to God Evaluator
        self.truth_evaluator = TruthSystemEvaluator() # Initialize TruthSystemEvaluator
        self.truth_in_us = TruthInUsFramework()
        self.temple_laws = TempleLawsFramework()
        self.natural_man_analyzer = NaturalManAnalyzer() # Initialize NaturalManAnalyzer
        self.arcos = ArcOsCore() # Initialize ArcOs - Advanced Revelation and Covenant Operating System


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

        # Add sanctification assessment for spiritual growth statements
        sanctification_assessment = None
        if any(keyword in statement.lower() for keyword in ['god', 'holy', 'sanctif', 'love', 'neighbor', 'christ', 'gospel']):
            # Create sample person data based on statement context
            person_data = {
                "spiritual_stirrings": "spiritual" in statement.lower(),
                "faith_strong": "faith" in statement.lower(),
                "prayer_regular": "pray" in statement.lower(),
                "service_regular": "serv" in statement.lower() or "help" in statement.lower(),
                "love_expressed": "love" in statement.lower(),
                "seeking_truth": "truth" in statement.lower() or "god" in statement.lower()
            }
            sanctification_assessment = self.bom_precepts.assess_sanctification_progress(person_data)

        # Add Glory to God evaluation
        glory_evaluation = self.glory_evaluator.evaluate_glory_to_god(statement, context)


        return {
            "statement": statement,
            "atonement_supreme_evaluation": atonement_evaluation,
            "truth_alignment_score": truth_alignment,
            "gospel_evaluation": gospel_evaluation,
            "goodness_analysis": goodness_analysis,
            "priesthood_holiness_evaluation": priesthood_evaluation, # Add priesthood evaluation
            "new_testament_adoption_evaluation": new_testament_adoption, # Add NT adoption evaluation
            "family_agenda_analysis": family_agenda_analysis, # Add family agenda analysis
            "sanctification_assessment": sanctification_assessment, # Add sanctification assessment
            "glory_to_god_evaluation": {
                "glory_level": glory_evaluation.glory_level.name,
                "glory_score": glory_evaluation.glory_score,
                "attributes_glorified": glory_evaluation.attributes_glorified,
                "attributes_dishonored": glory_evaluation.attributes_dishonored,
                "eternal_perspective": glory_evaluation.eternal_perspective
            }, # Add Glory to God evaluation
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

def run_truth_system_evaluator():
    """Run the Truth System Evaluator"""
    print("\n💡 Truth System Evaluator")
    print("Analyze the laws and truth principles governing a system.")
    print("-" * 40)

    try:
        # Assuming TruthSystemEvaluator has a method to run its interface or demonstration
        # If it has a specific method like 'run_evaluator' or similar, call it here.
        # For now, we'll call a placeholder method or assume it has a demo.
        # Replace 'demonstrate_truth_system' with the actual method if it exists.
        # If no specific demo method, you might need to implement an interface here.
        from truth_foundation.truth_system_evaluator import TruthSystemEvaluator
        evaluator = TruthSystemEvaluator()
        # Example: If TruthSystemEvaluator has a method called 'run_interactive_analysis'
        # evaluator.run_interactive_analysis()
        # Or a demonstration method:
        evaluator.demonstrate_truth_system()

    except ImportError as e:
        print(f"❌ Error loading Truth System Evaluator: {e}")
    except AttributeError:
        print("❌ Truth System Evaluator module found, but required method for demonstration is missing.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

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

def run_book_of_mormon_precepts():
    """Run the Book of Mormon Precepts System for Sanctification"""
    try:
        from truth_foundation.book_of_mormon_precepts import BookOfMormonPreceptsFramework, demonstrate_sanctification_system
        print("\n📚 Book of Mormon Precepts - Drawing Nearer to God")
        print("Living precepts to become holy through loving God and neighbor")
        print("-" * 70)

        framework = BookOfMormonPreceptsFramework()

        while True:
            print("\n📋 Book of Mormon Precepts Options:")
            print("1. 🕊️ View All Precepts Summary")
            print("2. 📊 Assess Personal Sanctification Progress")
            print("3. 🎯 Get Specific Precept Details")
            print("4. 💝 Focus on Love of God and Neighbor")
            print("5. 🌍 World Peace Through Gospel Living")
            print("6. 🌟 Full Sanctification Demonstration")
            print("0. Return to Main Menu")

            choice = input("\n🔢 Select option (0-6): ").strip()

            if choice == "0":
                break
            elif choice == "1":
                print("\n" + framework.get_all_precepts_summary())

            elif choice == "2":
                print("\n📊 PERSONAL SANCTIFICATION ASSESSMENT")
                print("Answer yes/no to assess your spiritual progress:")

                person_data = {}
                questions = [
                    ("prayer_regular", "Do you pray regularly with sincere intent?"),
                    ("scripture_study", "Do you study scriptures daily?"),
                    ("faith_strong", "Do you have strong faith in Jesus Christ?"),
                    ("service_regular", "Do you regularly serve others?"),
                    ("charity_giving", "Do you give generously to those in need?"),
                    ("obedience_willing", "Do you willingly obey God's commandments?"),
                    ("born_again", "Have you experienced conversion/mighty change?"),
                    ("charity_developed", "Have you developed charity (pure love)?"),
                    ("forgiveness_practiced", "Do you readily forgive others?"),
                    ("endurance_shown", "Do you endure trials with faith?")
                ]

                for key, question in questions:
                    while True:
                        answer = input(f"{question} (y/n): ").strip().lower()
                        if answer in ['y', 'yes', 'n', 'no']:
                            person_data[key] = answer in ['y', 'yes']
                            break
                        print("Please answer y/yes or n/no")

                assessment = framework.assess_sanctification_progress(person_data)
                guidance = framework.generate_sanctification_guidance(assessment)
                print(f"\n{guidance}")

            elif choice == "3":
                print("\n🎯 PRECEPT DETAILS")
                print("Available precepts:")
                precepts = ["faith_in_christ", "charity_pure_love", "prayer_communion",
                           "scripture_feasting", "service_poor", "repentance_change",
                           "obedience_commandments", "endurance_steadfastness"]

                for i, precept in enumerate(precepts, 1):
                    print(f"{i}. {precept.replace('_', ' ').title()}")

                try:
                    choice_num = int(input("\nSelect precept number: "))
                    if 1 <= choice_num <= len(precepts):
                        precept_key = precepts[choice_num - 1]
                        precept = framework.get_precept_details(precept_key)
                        if precept:
                            print(f"\n📖 {precept.precept.upper()}")
                            print(f"How it draws closer: {precept.how_it_draws_closer}")
                            print(f"Love of God: {precept.love_god_connection}")
                            print(f"Love of Neighbor: {precept.love_neighbor_connection}")
                            print(f"Sanctification Power: {precept.sanctification_power}")
                            print(f"World Peace: {precept.world_peace_contribution}")
                            print(f"\nPractical Applications:")
                            for app in precept.practical_applications:
                                print(f"• {app}")
                    else:
                        print("Invalid selection")
                except ValueError:
                    print("Please enter a valid number")

            elif choice == "4":
                print("\n💝 LOVE OF GOD AND NEIGHBOR - THE GREAT COMMANDMENTS")
                print("=" * 60)
                print("Jesus said: 'Thou shalt love the Lord thy God with all thy")
                print("heart, and with all thy soul, and with all thy mind.")
                print("This is the first and great commandment.")
                print("And the second is like unto it, Thou shalt love thy")
                print("neighbour as thyself.' - Matthew 22:37-39")
                print("\n🔹 LOVE OF GOD demonstrated through:")
                print("• Regular prayer and communion")
                print("• Study of His word (scriptures)")
                print("• Willing obedience to His commandments")
                print("• Gratitude and worship")
                print("• Faith and trust in His plan")
                print("\n🔹 LOVE OF NEIGHBOR demonstrated through:")
                print("• Service and charity")
                print("• Forgiveness and patience")
                print("• Kindness and compassion")
                print("• Seeing others as God sees them")
                print("• Sacrificing for others' welfare")
                print("\n🌟 RESULT: Sanctification and becoming holy like God!")

            elif choice == "5":
                print("\n🌍 WORLD PEACE THROUGH GOSPEL LIVING")
                print("=" * 50)
                print("The Book of Mormon precepts create peace by:")
                print("\n🕊️ INDIVIDUAL LEVEL:")
                print("• Inner peace through faith in Christ")
                print("• Heart change through repentance")
                print("• Love replacing hatred and selfishness")
                print("\n🏠 FAMILY LEVEL:")
                print("• Love and service in families")
                print("• Forgiveness and patience")
                print("• Teaching children Gospel principles")
                print("\n🌎 SOCIETY LEVEL:")
                print("• Justice and equality through Gospel law")
                print("• Care for poor and needy")
                print("• Unity across racial and cultural lines")
                print("\n💡 'If all men would live by these precepts,")
                print("there would be peace on earth and goodwill toward men.'")

            elif choice == "6":
                demonstrate_sanctification_system()

            else:
                print("❌ Invalid choice. Please select 0-6.")

    except ImportError as e:
        print(f"❌ Error loading Book of Mormon Precepts system: {e}")

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
    """Main function to demonstrate the truth foundation system"""
    print("🕊️  AGAPE CORE AI - Gospel Truth-Based Decision Making")
    print("=" * 60)

    while True:
        print("\n📋 AGAPE CORE AI - MAIN MENU")
        print("Choose a system to explore:")
        print("1. 🔍 Truth System Evaluator (NEW)")
        print("2. 📊 Gospel Cycles Analysis")
        print("3. 👨‍👩‍👧‍👦 Family Agenda Analyzer")
        print("4. 📚 Book of Mormon Precepts")
        print("5. 📺 SeekGood Media Evaluation")
        print("6. 🌊 Truth Rivers System")
        print("7. 💬 Interactive Chat Interface")
        print("8. 🔍 Advice Credibility Analysis Demo")
        print("9. 😈 Natural Man / Works of Flesh Analyzer (NEW)")
        print("10. 🏛️  Epic of Gilgamesh — Gospel Truth RAG Evaluation (NEW)")
        print("0. Exit")

        choice = input("\n🔢 Select option (0-10): ").strip()

        if choice == "0":
            print("👋 Thank you for using Agape Core AI!")
            break
        elif choice == "1":
            run_truth_system_evaluator()
        elif choice == "2":
            run_gospel_cycles()
        elif choice == "3":
            run_family_agenda_analyzer()
        elif choice == "4":
            run_book_of_mormon_precepts()
        elif choice == "5":
            from truth_foundation.seekgood import demonstrate_seekgood_system
            demonstrate_seekgood_system()
        elif choice == "6":
            run_truth_rivers_system()
        elif choice == "7":
            try:
                from chat_interface.agape_chat import AgapeChat
                chat = AgapeChat()
                chat.start_chat()
            except ImportError as e:
                print(f"❌ Error loading chat interface: {e}")
        elif choice == "8":
            print("\n🔍 ADVICE CREDIBILITY ANALYSIS DEMO")
            print("-" * 40)
            print("Demonstrating how our framework handles apparent contradictions...")

            # Import and run the synthesis analysis
            from truth_foundation.advice_credibility import analyze_jobs_yc_scaling_synthesis
            analyze_jobs_yc_scaling_synthesis()

            print("\n" + "-" * 40)
            analyze_sam_altman_example()
        elif choice == "9":
            # Natural Man / Works of Flesh Analyzer Demo
            print("\n" + "="*60)
            print("NATURAL MAN / WORKS OF FLESH ANALYZER DEMO")
            print("="*60)

            flesh_analyzer = NaturalManAnalyzer()

            # Example analyses
            test_behaviors = [
                "I can't control my temper when things don't go my way",
                "I spend hours looking at things I want to buy on social media",
                "I refuse to forgive someone who hurt me years ago"
            ]

            for behavior in test_behaviors:
                print(f"\n🔍 ANALYZING: {behavior}")
                print("-" * 40)
                report = flesh_analyzer.generate_flesh_report(behavior)
                print(report)
                print("\n" + "="*60)
        elif choice == "10":
            print("\n🏛️  EPIC OF GILGAMESH — GOSPEL TRUTH RAG EVALUATION")
            print("=" * 60)
            print("Evaluates the world's oldest written epic against Gospel truth")
            print("Framework: SeekGood (Phil. 4:8) + Biblical Media Analysis")
            print("-" * 60)

            custom_file = input(
                "\n📂 Enter path to a Gilgamesh text file (or press Enter to use\n"
                "   the built-in 12-tablet knowledge base): "
            ).strip()

            verbose = input("🔍 Show per-tablet breakdown? (y/n): ").strip().lower() == "y"

            try:
                from gilgamesh_evaluator.gilgamesh_rag_evaluator import (
                    GilgameshRAGEvaluator, print_verdict
                )
                evaluator = GilgameshRAGEvaluator()
                file_path = custom_file if custom_file else None
                verdict = evaluator.evaluate(file_path=file_path)
                print_verdict(verdict, verbose=verbose)
            except Exception as e:
                print(f"❌ Error running Gilgamesh evaluator: {e}")
        else:
            print("❌ Invalid choice. Please select 0-10.")


if __name__ == "__main__":
    main()