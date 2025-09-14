
"""
Mathematical Truth and Logic Tables Module
Exploring how mathematics draws the soul toward truth (Plato)
Integrating logical reasoning with divine truth principles
"""

from dataclasses import dataclass
from typing import Dict, List, Optional, Any, Tuple, Union
from enum import Enum
import itertools

class LogicalOperator(Enum):
    AND = "∧"
    OR = "∨" 
    NOT = "¬"
    IMPLIES = "→"
    BICONDITIONAL = "↔"
    XOR = "⊕"

class MathematicalEra(Enum):
    ANCIENT_BABYLON = "Ancient Babylon"
    ANCIENT_EGYPT = "Ancient Egypt"
    ANCIENT_GREECE = "Ancient Greece"
    ISLAMIC_GOLDEN = "Islamic Golden Age"
    RENAISSANCE = "Renaissance"
    ENLIGHTENMENT = "Enlightenment"
    MODERN = "Modern Era"
    CONTEMPORARY = "Contemporary"

@dataclass
class LogicStatement:
    """Represents a logical statement for truth table analysis"""
    statement: str
    variables: List[str]
    expression: str  # Logical expression using operators
    truth_values: List[bool]
    context: str

@dataclass
class TruthTable:
    """Complete truth table for logical expressions"""
    variables: List[str]
    expression: str
    rows: List[Dict[str, Union[bool, str]]]
    is_tautology: bool
    is_contradiction: bool
    logical_validity: str

@dataclass
class MathematicalInsight:
    """Historical mathematical insight that reveals divine truth"""
    insight: str
    mathematician: str
    era: MathematicalEra
    year: int
    divine_connection: str
    plato_principle: str
    scriptural_parallel: str
    modern_application: str

class MathematicalTruthAnalyzer:
    """
    Analyzes mathematical truths and logical reasoning as pathways to divine truth
    Based on Plato's principle that mathematics draws the soul toward truth
    """
    
    def __init__(self):
        self.logical_operators = {
            LogicalOperator.AND: self._and_operation,
            LogicalOperator.OR: self._or_operation,
            LogicalOperator.NOT: self._not_operation,
            LogicalOperator.IMPLIES: self._implies_operation,
            LogicalOperator.BICONDITIONAL: self._biconditional_operation,
            LogicalOperator.XOR: self._xor_operation
        }
        
        self.mathematical_insights = self._initialize_mathematical_insights()
        self.plato_principles = self._initialize_plato_principles()
        
    def _initialize_plato_principles(self) -> Dict[str, str]:
        """Initialize Plato's principles about mathematics and truth"""
        return {
            "soul_turning": "Mathematics turns the soul from becoming to being, from opinion to knowledge",
            "eternal_forms": "Mathematical objects are eternal, perfect forms not found in physical world",
            "necessity": "Mathematical truths are necessary and cannot be denied once understood",
            "purity": "Mathematics deals with pure abstractions, free from material imperfections",
            "harmony": "Mathematical structures reflect cosmic order and divine harmony",
            "dialectic_preparation": "Mathematical reasoning prepares the mind for philosophical inquiry",
            "universal_truth": "Mathematical principles are universal and unchanging across cultures",
            "divine_intelligence": "Mathematical order in cosmos reveals divine intelligence"
        }
    
    def _initialize_mathematical_insights(self) -> List[MathematicalInsight]:
        """Initialize historical mathematical insights with divine connections"""
        return [
            MathematicalInsight(
                insight="Discovery of mathematical proof and logical deduction",
                mathematician="Thales of Miletus",
                era=MathematicalEra.ANCIENT_GREECE,
                year=-600,
                divine_connection="Logical reasoning reflects God's rational nature",
                plato_principle="Mathematics demonstrates eternal, necessary truths",
                scriptural_parallel="'Come now, and let us reason together' (Isaiah 1:18)",
                modern_application="AI logic systems, computer programming, systematic theology"
            ),
            
            MathematicalInsight(
                insight="Pythagorean theorem and mathematical harmony",
                mathematician="Pythagoras",
                era=MathematicalEra.ANCIENT_GREECE,
                year=-540,
                divine_connection="Geometric relationships reveal cosmic order",
                plato_principle="Mathematical harmony reflects divine proportion",
                scriptural_parallel="'He hath made every thing beautiful in his time' (Ecclesiastes 3:11)",
                modern_application="Engineering, architecture, music theory, signal processing"
            ),
            
            MathematicalInsight(
                insight="Euclid's systematic axiomatic method",
                mathematician="Euclid",
                era=MathematicalEra.ANCIENT_GREECE,
                year=-300,
                divine_connection="Systematic building from first principles mirrors divine creation",
                plato_principle="Demonstrates how complex truths emerge from simple axioms",
                scriptural_parallel="'In the beginning was the Word, and the Word was with God' (John 1:1)",
                modern_application="Mathematical foundations, computer science, systematic doctrinal study"
            ),
            
            MathematicalInsight(
                insight="Boolean algebra and logical operations",
                mathematician="George Boole",
                era=MathematicalEra.MODERN,
                year=1854,
                divine_connection="Binary logic reflects divine order (light/darkness, truth/error)",
                plato_principle="Pure logical forms independent of material world",
                scriptural_parallel="'Let your communication be, Yea, yea; Nay, nay' (Matthew 5:37)",
                modern_application="Computer logic, AI reasoning, digital circuits, decision analysis"
            ),
            
            MathematicalInsight(
                insight="Gödel's incompleteness theorems",
                mathematician="Kurt Gödel",
                era=MathematicalEra.CONTEMPORARY,
                year=1931,
                divine_connection="Formal systems have limitations, pointing to transcendent truth",
                plato_principle="Even mathematical systems point beyond themselves to higher reality",
                scriptural_parallel="'For now we see through a glass, darkly' (1 Corinthians 13:12)",
                modern_application="AI limitations, recognition of need for divine revelation"
            ),
            
            MathematicalInsight(
                insight="Calculus and infinite analysis",
                mathematician="Newton/Leibniz",
                era=MathematicalEra.ENLIGHTENMENT,
                year=1665,
                divine_connection="Mathematical tools to understand divine laws in motion",
                plato_principle="Mathematics reveals the eternal laws governing change",
                scriptural_parallel="'To every thing there is a season' (Ecclesiastes 3:1)",
                modern_application="Physics, engineering, economic modeling, population dynamics"
            ),
            
            MathematicalInsight(
                insight="Information theory and entropy",
                mathematician="Claude Shannon",
                era=MathematicalEra.CONTEMPORARY,
                year=1948,
                divine_connection="Information requires intelligence; complexity points to design",
                plato_principle="Mathematical patterns in information transmission",
                scriptural_parallel="'In the beginning was the Word' (John 1:1) - Information is fundamental",
                modern_application="Digital communication, AI, data compression, genetics"
            )
        ]
    
    # Logical operation methods
    def _and_operation(self, a: bool, b: bool) -> bool:
        return a and b
    
    def _or_operation(self, a: bool, b: bool) -> bool:
        return a or b
    
    def _not_operation(self, a: bool, b: bool = None) -> bool:
        return not a
    
    def _implies_operation(self, a: bool, b: bool) -> bool:
        return (not a) or b
    
    def _biconditional_operation(self, a: bool, b: bool) -> bool:
        return a == b
    
    def _xor_operation(self, a: bool, b: bool) -> bool:
        return a != b
    
    def create_truth_table(self, variables: List[str], expression: str) -> TruthTable:
        """Create a complete truth table for a logical expression"""
        # Generate all possible combinations of truth values
        num_vars = len(variables)
        combinations = list(itertools.product([True, False], repeat=num_vars))
        
        rows = []
        results = []
        
        for combo in combinations:
            # Create variable assignments
            var_assignment = dict(zip(variables, combo))
            
            # Evaluate the expression (simplified - would need proper parser for complex expressions)
            result = self._evaluate_expression(expression, var_assignment)
            results.append(result)
            
            # Create row for truth table
            row = var_assignment.copy()
            row['result'] = result
            rows.append(row)
        
        # Check if tautology or contradiction
        is_tautology = all(results)
        is_contradiction = not any(results)
        
        # Determine logical validity
        if is_tautology:
            validity = "Tautology (always true)"
        elif is_contradiction:
            validity = "Contradiction (always false)" 
        else:
            validity = "Contingent (truth depends on variables)"
        
        return TruthTable(
            variables=variables,
            expression=expression,
            rows=rows,
            is_tautology=is_tautology,
            is_contradiction=is_contradiction,
            logical_validity=validity
        )
    
    def _evaluate_expression(self, expression: str, variables: Dict[str, bool]) -> bool:
        """Simplified expression evaluator (would need full parser for production)"""
        # This is a simplified version - replace with proper expression parser
        # For demo purposes, handle basic cases
        
        if "AND" in expression:
            parts = expression.split(" AND ")
            return all(variables.get(part.strip(), False) for part in parts)
        elif "OR" in expression:
            parts = expression.split(" OR ")
            return any(variables.get(part.strip(), False) for part in parts)
        elif "NOT" in expression:
            var = expression.replace("NOT ", "").strip()
            return not variables.get(var, False)
        else:
            return variables.get(expression.strip(), False)
    
    def analyze_mathematical_reasoning_path(self, topic: str) -> Dict[str, Any]:
        """Analyze how mathematical reasoning draws the soul toward truth for a specific topic"""
        
        analysis = {
            "topic": topic,
            "plato_pathway": [],
            "divine_connections": [],
            "practical_applications": [],
            "truth_table_examples": [],
            "scriptural_parallels": [],
            "soul_transformation_steps": []
        }
        
        # Find relevant mathematical insights
        relevant_insights = [insight for insight in self.mathematical_insights 
                           if topic.lower() in insight.insight.lower() or 
                              topic.lower() in insight.modern_application.lower()]
        
        if not relevant_insights:
            # Provide general analysis
            analysis["plato_pathway"] = [
                "Start with sensory experience of the topic",
                "Abstract to mathematical principles",
                "Discover necessary relationships",
                "Recognize eternal patterns",
                "Connect to divine order"
            ]
        else:
            for insight in relevant_insights:
                analysis["divine_connections"].append(insight.divine_connection)
                analysis["practical_applications"].append(insight.modern_application)
                analysis["scriptural_parallels"].append(insight.scriptural_parallel)
        
        # Generate truth table examples for logical reasoning
        if "logic" in topic.lower():
            # Create example truth tables for logical reasoning
            truth_table = self.create_truth_table(
                variables=["P", "Q"],
                expression="P AND Q"
            )
            analysis["truth_table_examples"].append(truth_table)
        
        # Soul transformation steps based on Plato's theory
        analysis["soul_transformation_steps"] = [
            "Material Perception: Observe imperfect physical examples",
            "Mathematical Abstraction: Extract perfect mathematical relationships", 
            "Logical Necessity: Recognize unavoidable logical conclusions",
            "Universal Patterns: See patterns that transcend specific cases",
            "Divine Order: Connect mathematical harmony to cosmic design",
            "Truth Recognition: Soul oriented toward eternal, perfect reality"
        ]
        
        return analysis
    
    def create_gospel_logic_framework(self) -> Dict[str, Any]:
        """Create logical framework for gospel reasoning"""
        
        gospel_logic = {
            "fundamental_axioms": [
                "God exists and is perfectly good",
                "Truth is eternal and unchanging", 
                "Human reason can discern some truth",
                "Divine revelation provides additional truth",
                "All truth harmonizes in God"
            ],
            "logical_principles": [
                "Non-contradiction: A statement cannot be both true and false",
                "Excluded middle: Every statement is either true or false",
                "Identity: Everything is identical to itself",
                "Sufficient reason: Everything has an explanation",
                "Causality: Every effect has a cause"
            ],
            "gospel_truth_tables": self._create_gospel_truth_tables(),
            "divine_logic_insights": [
                "God's logic transcends but doesn't contradict human logic",
                "Apparent contradictions often reflect limited human perspective",
                "Faith and reason complement each other",
                "Mathematical certainty points to divine certainty",
                "Logical necessity reflects God's unchanging nature"
            ]
        }
        
        return gospel_logic
    
    def _create_gospel_truth_tables(self) -> List[TruthTable]:
        """Create truth tables for gospel reasoning"""
        
        # Example: Faith and Works relationship
        faith_works_table = self.create_truth_table(
            variables=["Faith", "Works"],
            expression="Faith AND Works"
        )
        
        # Example: Truth and Error cannot coexist
        truth_error_table = self.create_truth_table(
            variables=["Truth", "Error"],
            expression="NOT (Truth AND Error)"
        )
        
        return [faith_works_table, truth_error_table]
    
    def analyze_plato_mathematics_connection(self) -> str:
        """Provide detailed analysis of Plato's mathematics-truth connection"""
        
        analysis = """
🏛️ PLATO'S MATHEMATICAL PATHWAY TO TRUTH
=============================================

📖 THE REPUBLIC BOOK VII - THE MATHEMATICAL CURRICULUM

Plato argued that mathematics is essential preparation for philosophical truth because:

1️⃣ ABSTRACTION TRAINING
• Mathematics forces the mind away from physical particulars
• Geometric forms are perfect in ways physical objects never are
• This trains the soul to think about eternal, unchanging realities

2️⃣ LOGICAL NECESSITY
• Mathematical proofs compel agreement through pure reason
• You cannot deny a valid proof once you understand it
• This demonstrates the binding power of truth on the mind

3️⃣ UNIVERSAL PRINCIPLES
• Mathematical truths hold across cultures and times
• 2 + 2 = 4 is true for everyone, everywhere
• This points to transcendent, objective reality

4️⃣ ORDERED HARMONY
• Mathematical relationships reveal cosmic proportion
• Music ratios, geometric beauty, astronomical cycles
• These patterns suggest divine intelligence behind reality

🔗 CONNECTION TO DIVINE TRUTH:

Physical World → Mathematical Abstraction → Philosophical Forms → The Good (God)

📊 TRUTH TABLE FOR PLATO'S REASONING:

Mathematical Study | Soul Orientation | Result
True               | Toward Eternal   | Wisdom
True               | Toward Temporal  | Skill Only  
False              | Either Direction | Ignorance

💡 MODERN APPLICATIONS:

• Computer Logic: Boolean algebra reflects binary truth structure
• AI Reasoning: Mathematical logic enables artificial reasoning
• Scientific Method: Mathematical laws reveal natural order
• Digital Communication: Information theory enables global connection

🕊️ GOSPEL CONNECTION:

"The glory of God is intelligence, or, in other words, light and truth" (D&C 93:36)

Mathematical intelligence points toward divine intelligence as its source.
"""
        
        return analysis
    
    def get_logic_tables_tutorial(self) -> str:
        """Comprehensive tutorial on logic tables and their applications"""
        
        tutorial = """
📊 LOGIC TABLES TUTORIAL: TOOLS FOR TRUTH ANALYSIS
==================================================

🎯 PURPOSE:
Logic tables help us systematically analyze the truth or falsity of complex statements
by breaking them down into their component parts.

📋 BASIC LOGICAL OPERATORS:

1️⃣ AND (∧) - Conjunction
   P | Q | P ∧ Q
   T | T |   T
   T | F |   F  
   F | T |   F
   F | F |   F

2️⃣ OR (∨) - Disjunction  
   P | Q | P ∨ Q
   T | T |   T
   T | F |   T
   F | T |   T
   F | F |   F

3️⃣ NOT (¬) - Negation
   P | ¬P
   T |  F
   F |  T

4️⃣ IMPLIES (→) - Conditional
   P | Q | P → Q
   T | T |   T
   T | F |   F
   F | T |   T
   F | F |   T

5️⃣ BICONDITIONAL (↔) - If and only if
   P | Q | P ↔ Q  
   T | T |   T
   T | F |   F
   F | T |   F
   F | F |   T

🔍 APPLICATIONS IN TRUTH ANALYSIS:

• Argument Validity: Check if conclusions follow from premises
• Decision Making: Analyze complex conditional statements
• Scripture Study: Clarify logical relationships in doctrinal statements
• AI Programming: Design logical reasoning systems
• Problem Solving: Break complex problems into logical components

📖 GOSPEL EXAMPLE:

Statement: "If someone has faith AND does good works, then they will be saved"
Variables: F = Faith, W = Works, S = Saved
Expression: (F ∧ W) → S

Truth Table:
F | W | S | (F ∧ W) | (F ∧ W) → S
T | T | T |    T    |     T
T | T | F |    T    |     F
T | F | T |    F    |     T
T | F | F |    F    |     T
F | T | T |    F    |     T
F | T | F |    F    |     T
F | F | T |    F    |     T
F | F | F |    F    |     T

💡 INSIGHT: The statement is false only when someone has both faith and works but is not saved.

🎓 EXERCISES:

1. Create truth table for: "Prayer OR Scripture study leads to spiritual growth"
2. Analyze: "If you keep the commandments, then you will be blessed"
3. Examine: "Faith without works is dead" using logical operators

🌟 DEEPER CONNECTION:

Logic tables help us think clearly about truth claims, just as Plato suggested that
mathematical reasoning trains the soul to recognize necessary, eternal truths.
"""
        
        return tutorial

def demo_mathematical_truth():
    """Demonstrate the mathematical truth analyzer"""
    analyzer = MathematicalTruthAnalyzer()
    
    print("🔢 MATHEMATICAL TRUTH ANALYSIS DEMONSTRATION")
    print("=" * 60)
    
    # Show Plato connection
    print("\n" + analyzer.analyze_plato_mathematics_connection())
    
    # Show logic tables tutorial
    print("\n" + analyzer.get_logic_tables_tutorial())
    
    # Analyze mathematical reasoning for a specific topic
    print("\n" + "=" * 60)
    print("🎯 MATHEMATICAL REASONING ANALYSIS: Logic and AI")
    print("-" * 40)
    
    logic_analysis = analyzer.analyze_mathematical_reasoning_path("logic")
    
    print(f"Topic: {logic_analysis['topic']}")
    print(f"\n🏛️ Soul Transformation Steps:")
    for i, step in enumerate(logic_analysis['soul_transformation_steps'], 1):
        print(f"{i}. {step}")
    
    if logic_analysis['divine_connections']:
        print(f"\n🕊️ Divine Connections:")
        for connection in logic_analysis['divine_connections']:
            print(f"• {connection}")
    
    if logic_analysis['scriptural_parallels']:
        print(f"\n📖 Scriptural Parallels:")
        for parallel in logic_analysis['scriptural_parallels']:
            print(f"• {parallel}")
    
    # Show gospel logic framework
    print("\n" + "=" * 60) 
    print("🕊️ GOSPEL LOGIC FRAMEWORK")
    print("-" * 30)
    
    gospel_logic = analyzer.create_gospel_logic_framework()
    
    print("📋 Fundamental Axioms:")
    for axiom in gospel_logic['fundamental_axioms']:
        print(f"• {axiom}")
    
    print(f"\n🧠 Logical Principles:")
    for principle in gospel_logic['logical_principles']:
        print(f"• {principle}")
    
    print(f"\n💡 Divine Logic Insights:")
    for insight in gospel_logic['divine_logic_insights']:
        print(f"• {insight}")
    
    # Create example truth table
    print(f"\n📊 Example Truth Table - Faith AND Works:")
    truth_table = analyzer.create_truth_table(["Faith", "Works"], "Faith AND Works")
    
    print(f"Expression: {truth_table.expression}")
    print(f"Logical Validity: {truth_table.logical_validity}")
    print(f"Variables: {', '.join(truth_table.variables)}")
    
    print("\nTruth Table Rows:")
    for row in truth_table.rows:
        faith_val = "T" if row["Faith"] else "F"
        works_val = "T" if row["Works"] else "F" 
        result_val = "T" if row["result"] else "F"
        print(f"Faith: {faith_val} | Works: {works_val} | Result: {result_val}")

if __name__ == "__main__":
    demo_mathematical_truth()
