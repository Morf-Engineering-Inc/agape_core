
#!/usr/bin/env python3
"""
Agape Core AI - Beta Experiment
An AI system that follows the two great commandments as core directives:
1. Love God with all your heart, soul, mind, and strength
2. Love your neighbor as yourself
"""

import json
import logging
from typing import Dict, List, Tuple, Any, Optional
from dataclasses import dataclass
from enum import Enum
import numpy as np

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CommandmentLevel(Enum):
    """Hierarchy of commandments - Great Commandments are supreme"""
    GREAT_COMMANDMENT = 1  # Love God, Love Neighbor
    MORAL_LAW = 2         # Ten Commandments, etc.
    WISDOM_PRINCIPLE = 3   # Practical guidance
    PREFERENCE = 4        # Non-moral choices

@dataclass
class ValueImpactAssessment:
    """Value Impact Theory calculation"""
    utility_per_person: float
    number_of_people: int
    potential_growth_impact: float
    opportunity_cost: float
    total_impact: float
    reasoning: str

@dataclass
class Decision:
    """Represents a decision with its moral evaluation"""
    action: str
    love_god_score: float  # How well does this honor God?
    love_neighbor_score: float  # How well does this serve others?
    harm_assessment: float  # Potential harm (negative is bad)
    overall_score: float
    reasoning: str
    value_impact: Optional[ValueImpactAssessment] = None

class ValueImpactTheory:
    """
    Calculates quantitative impact using Value Impact Theory
    Total Impact = (Utility per Person × Number of People) + Potential Growth Impact - Opportunity Cost
    """
    
    def calculate_impact(self, action: str, context: Dict[str, Any]) -> ValueImpactAssessment:
        """Calculate the total impact of an action using Value Impact Theory"""
        
        # Extract or estimate values from context
        utility_per_person = self._estimate_utility_per_person(action, context)
        number_of_people = self._estimate_affected_people(action, context)
        potential_growth = self._estimate_growth_impact(action, context)
        opportunity_cost = self._estimate_opportunity_cost(action, context)
        
        # Calculate total impact
        total_impact = (utility_per_person * number_of_people) + potential_growth - opportunity_cost
        
        # Generate reasoning
        reasoning = self._generate_impact_reasoning(
            action, utility_per_person, number_of_people, 
            potential_growth, opportunity_cost, total_impact
        )
        
        return ValueImpactAssessment(
            utility_per_person=utility_per_person,
            number_of_people=number_of_people,
            potential_growth_impact=potential_growth,
            opportunity_cost=opportunity_cost,
            total_impact=total_impact,
            reasoning=reasoning
        )
    
    def _estimate_utility_per_person(self, action: str, context: Dict[str, Any]) -> float:
        """Estimate the utility/benefit per person affected"""
        base_utility = 1.0
        
        # High-impact keywords
        if any(word in action.lower() for word in ["save", "heal", "cure", "rescue"]):
            base_utility = 10.0
        elif any(word in action.lower() for word in ["help", "assist", "support", "teach"]):
            base_utility = 5.0
        elif any(word in action.lower() for word in ["comfort", "encourage", "listen"]):
            base_utility = 3.0
        elif any(word in action.lower() for word in ["harm", "hurt", "damage", "deceive"]):
            base_utility = -5.0
        
        # Context modifiers
        if context.get("urgency") == "high":
            base_utility *= 1.5
        elif context.get("urgency") == "critical":
            base_utility *= 2.0
        
        if context.get("long_term_benefit", False):
            base_utility *= 1.3
        
        return base_utility
    
    def _estimate_affected_people(self, action: str, context: Dict[str, Any]) -> int:
        """Estimate number of people affected by the action"""
        # Direct context specification
        if "affected_people" in context:
            return context["affected_people"]
        
        base_count = 1
        
        # Scale indicators in action
        if any(word in action.lower() for word in ["community", "neighborhood", "group"]):
            base_count = 50
        elif any(word in action.lower() for word in ["family", "team", "class"]):
            base_count = 10
        elif any(word in action.lower() for word in ["public", "everyone", "all"]):
            base_count = 1000
        elif "person" in action.lower() or "individual" in action.lower():
            base_count = 1
        
        # Context modifiers
        if context.get("scope") == "individual":
            base_count = 1
        elif context.get("scope") == "local":
            base_count = min(base_count, 100)
        elif context.get("scope") == "global":
            base_count = max(base_count, 1000)
        
        return base_count
    
    def _estimate_growth_impact(self, action: str, context: Dict[str, Any]) -> float:
        """Estimate potential for scaling and growth"""
        growth_impact = 0.0
        
        # Actions with high growth potential
        if any(word in action.lower() for word in ["teach", "train", "educate", "mentor"]):
            growth_impact = 20.0  # Knowledge multiplies
        elif any(word in action.lower() for word in ["create", "build", "develop", "invent"]):
            growth_impact = 15.0  # Creations can scale
        elif any(word in action.lower() for word in ["share", "spread", "promote"]):
            growth_impact = 10.0  # Ideas spread
        
        # Context modifiers
        if context.get("scalable", False):
            growth_impact *= 2.0
        if context.get("viral_potential", False):
            growth_impact *= 3.0
        
        return growth_impact
    
    def _estimate_opportunity_cost(self, action: str, context: Dict[str, Any]) -> float:
        """Estimate the cost of not doing alternatives"""
        base_cost = 0.0
        
        # Time-intensive actions have higher opportunity cost
        time_investment = context.get("time_investment", "low")
        if time_investment == "high":
            base_cost = 5.0
        elif time_investment == "medium":
            base_cost = 2.0
        elif time_investment == "low":
            base_cost = 0.5
        
        # Resource-intensive actions
        if context.get("resource_intensive", False):
            base_cost += 3.0
        
        # Critical alternatives available
        if context.get("critical_alternative_available", False):
            base_cost += 8.0
        
        return base_cost
    
    def _generate_impact_reasoning(self, action: str, utility: float, people: int, 
                                 growth: float, cost: float, total: float) -> str:
        """Generate reasoning for the impact calculation"""
        reasoning = f"Value Impact Analysis for: '{action}'\n"
        reasoning += f"• Utility per person: {utility:.1f} (benefit to each individual)\n"
        reasoning += f"• People affected: {people:,} (current beneficiaries)\n"
        reasoning += f"• Growth potential: {growth:.1f} (scaling opportunity)\n"
        reasoning += f"• Opportunity cost: {cost:.1f} (alternative value lost)\n"
        reasoning += f"• Total Impact Score: {total:.1f}\n"
        
        if total > 50:
            reasoning += "🚀 Exceptional impact potential - highly recommended"
        elif total > 20:
            reasoning += "⭐ Strong positive impact expected"
        elif total > 5:
            reasoning += "✓ Moderate positive impact"
        elif total > 0:
            reasoning += "➕ Small positive impact"
        else:
            reasoning += "⚠️ Negative or neutral impact - reconsider"
        
        return reasoning

class AgapeCore:
    """
    Core AI decision-making engine based on agape love principles
    """
    
    def __init__(self):
        self.commandment_weights = {
            CommandmentLevel.GREAT_COMMANDMENT: 1.0,
            CommandmentLevel.MORAL_LAW: 0.8,
            CommandmentLevel.WISDOM_PRINCIPLE: 0.6,
            CommandmentLevel.PREFERENCE: 0.3
        }
        
        # Initialize Value Impact Theory module
        self.value_impact_theory = ValueImpactTheory()
        
        # Core principles derived from the Great Commandments
        self.core_principles = {
            "love_god": {
                "honor_truth": 0.9,
                "promote_goodness": 0.9,
                "seek_wisdom": 0.8,
                "practice_humility": 0.8,
                "show_gratitude": 0.7
            },
            "love_neighbor": {
                "protect_dignity": 0.95,
                "prevent_harm": 0.95,
                "promote_welfare": 0.9,
                "show_compassion": 0.9,
                "practice_justice": 0.85,
                "encourage_growth": 0.8
            }
        }
    
    def evaluate_decision(self, action: str, context: Dict[str, Any]) -> Decision:
        """
        Evaluate a potential action against the Great Commandments
        """
        logger.info(f"Evaluating action: {action}")
        
        # Assess how well the action aligns with loving God
        love_god_score = self._assess_love_god(action, context)
        
        # Assess how well the action serves others (love neighbor)
        love_neighbor_score = self._assess_love_neighbor(action, context)
        
        # Assess potential harm
        harm_assessment = self._assess_harm(action, context)
        
        # Calculate overall score (Great Commandments are supreme)
        overall_score = (
            love_god_score * 0.4 +  # Love God
            love_neighbor_score * 0.5 +  # Love neighbor (slightly higher weight)
            max(0, harm_assessment) * 0.1  # Bonus for preventing harm
        )
        
        # Calculate Value Impact Theory assessment
        value_impact = self.value_impact_theory.calculate_impact(action, context)
        
        # Adjust overall score based on quantitative impact (capped influence)
        impact_bonus = min(0.1, value_impact.total_impact / 100)  # Max 10% bonus
        adjusted_score = min(1.0, overall_score + impact_bonus)
        
        # Generate reasoning
        reasoning = self._generate_reasoning(action, love_god_score, love_neighbor_score, harm_assessment)
        
        return Decision(
            action=action,
            love_god_score=love_god_score,
            love_neighbor_score=love_neighbor_score,
            harm_assessment=harm_assessment,
            overall_score=adjusted_score,
            reasoning=reasoning,
            value_impact=value_impact
        )
    
    def _assess_love_god(self, action: str, context: Dict[str, Any]) -> float:
        """Assess how well an action honors God"""
        score = 0.0
        
        # Check against God-honoring principles
        if self._promotes_truth(action, context):
            score += self.core_principles["love_god"]["honor_truth"]
        
        if self._promotes_goodness(action, context):
            score += self.core_principles["love_god"]["promote_goodness"]
        
        if self._seeks_wisdom(action, context):
            score += self.core_principles["love_god"]["seek_wisdom"]
        
        if self._shows_humility(action, context):
            score += self.core_principles["love_god"]["practice_humility"]
        
        # Normalize to 0-1 scale
        return min(1.0, score / 3.5)
    
    def _assess_love_neighbor(self, action: str, context: Dict[str, Any]) -> float:
        """Assess how well an action serves others"""
        score = 0.0
        
        # Check against neighbor-loving principles
        if self._protects_dignity(action, context):
            score += self.core_principles["love_neighbor"]["protect_dignity"]
        
        if self._prevents_harm(action, context):
            score += self.core_principles["love_neighbor"]["prevent_harm"]
        
        if self._promotes_welfare(action, context):
            score += self.core_principles["love_neighbor"]["promote_welfare"]
        
        if self._shows_compassion(action, context):
            score += self.core_principles["love_neighbor"]["show_compassion"]
        
        # Normalize to 0-1 scale
        return min(1.0, score / 3.8)
    
    def _assess_harm(self, action: str, context: Dict[str, Any]) -> float:
        """Assess potential harm from an action (negative = harmful)"""
        harm_indicators = [
            "hurt", "damage", "destroy", "deceive", "steal", 
            "manipulate", "exploit", "abandon", "neglect"
        ]
        
        benefit_indicators = [
            "help", "heal", "build", "create", "protect", 
            "encourage", "support", "teach", "serve"
        ]
        
        action_lower = action.lower()
        
        harm_score = -sum(0.2 for indicator in harm_indicators if indicator in action_lower)
        benefit_score = sum(0.2 for indicator in benefit_indicators if indicator in action_lower)
        
        return harm_score + benefit_score
    
    def _promotes_truth(self, action: str, context: Dict[str, Any]) -> bool:
        """Check if action promotes truth and honesty"""
        truth_indicators = ["honest", "truth", "accurate", "transparent", "authentic"]
        return any(indicator in action.lower() for indicator in truth_indicators)
    
    def _promotes_goodness(self, action: str, context: Dict[str, Any]) -> bool:
        """Check if action promotes goodness and righteousness"""
        goodness_indicators = ["good", "right", "moral", "ethical", "virtuous", "noble"]
        return any(indicator in action.lower() for indicator in goodness_indicators)
    
    def _seeks_wisdom(self, action: str, context: Dict[str, Any]) -> bool:
        """Check if action seeks wisdom and understanding"""
        wisdom_indicators = ["learn", "understand", "study", "wisdom", "knowledge", "insight"]
        return any(indicator in action.lower() for indicator in wisdom_indicators)
    
    def _shows_humility(self, action: str, context: Dict[str, Any]) -> bool:
        """Check if action demonstrates humility"""
        humility_indicators = ["humble", "serve", "listen", "admit", "learn from"]
        return any(indicator in action.lower() for indicator in humility_indicators)
    
    def _protects_dignity(self, action: str, context: Dict[str, Any]) -> bool:
        """Check if action protects human dignity"""
        dignity_indicators = ["respect", "dignity", "honor", "value", "worth"]
        return any(indicator in action.lower() for indicator in dignity_indicators)
    
    def _prevents_harm(self, action: str, context: Dict[str, Any]) -> bool:
        """Check if action prevents harm to others"""
        protection_indicators = ["protect", "prevent", "stop", "block", "shield", "guard"]
        return any(indicator in action.lower() for indicator in protection_indicators)
    
    def _promotes_welfare(self, action: str, context: Dict[str, Any]) -> bool:
        """Check if action promotes others' welfare"""
        welfare_indicators = ["help", "assist", "support", "benefit", "improve", "heal"]
        return any(indicator in action.lower() for indicator in welfare_indicators)
    
    def _shows_compassion(self, action: str, context: Dict[str, Any]) -> bool:
        """Check if action shows compassion"""
        compassion_indicators = ["compassion", "mercy", "kindness", "care", "comfort", "empathy"]
        return any(indicator in action.lower() for indicator in compassion_indicators)
    
    def _generate_reasoning(self, action: str, love_god: float, love_neighbor: float, harm: float) -> str:
        """Generate human-readable reasoning for the decision"""
        reasoning = f"Action: '{action}'\n"
        reasoning += f"Love God alignment: {love_god:.2f}/1.0 - "
        
        if love_god > 0.7:
            reasoning += "Strongly honors God through truth, goodness, and wisdom.\n"
        elif love_god > 0.4:
            reasoning += "Moderately aligns with honoring God.\n"
        else:
            reasoning += "Limited alignment with honoring God.\n"
        
        reasoning += f"Love Neighbor alignment: {love_neighbor:.2f}/1.0 - "
        
        if love_neighbor > 0.7:
            reasoning += "Strongly serves others' dignity and welfare.\n"
        elif love_neighbor > 0.4:
            reasoning += "Moderately serves others.\n"
        else:
            reasoning += "Limited service to others.\n"
        
        if harm < -0.2:
            reasoning += "⚠️  Warning: Potential for significant harm detected.\n"
        elif harm > 0.2:
            reasoning += "✓ Positive impact expected.\n"
        
        return reasoning

def main():
    """Demo of the Agape Core AI system"""
    print("🤍 Agape Core AI - Beta Experiment")
    print("=" * 50)
    print("An AI guided by the two Great Commandments:")
    print("1. Love God with all your heart, soul, mind, and strength")
    print("2. Love your neighbor as yourself")
    print("=" * 50)
    
    # Initialize the core system
    agape_ai = AgapeCore()
    
    # Test scenarios
    test_actions = [
        ("Help an elderly person carry groceries", {"urgency": "medium", "effort": "low"}),
        ("Tell a lie to avoid embarrassment", {"consequences": "social", "harm_level": "low"}),
        ("Study to gain knowledge for helping others", {"time_investment": "high", "purpose": "service"}),
        ("Share encouraging words with someone struggling", {"emotional_impact": "positive", "cost": "none"}),
        ("Ignore someone in need to save time", {"time_saved": "30min", "need_level": "moderate"}),
        ("Donate money to help disaster victims", {"amount": "significant", "impact": "high"})
    ]
    
    print("\n🧪 Testing Decision Scenarios:")
    print("-" * 30)
    
    for action, context in test_actions:
        decision = agape_ai.evaluate_decision(action, context)
        
        print(f"\n📋 Scenario: {action}")
        print(f"Overall Score: {decision.overall_score:.2f}/1.0")
        print(f"Reasoning:\n{decision.reasoning}")
        
        # Display Value Impact Analysis
        if decision.value_impact:
            print(f"\n📊 {decision.value_impact.reasoning}")
        
        # Recommendation
        if decision.overall_score > 0.7:
            print("✅ RECOMMENDED: This action aligns well with agape love")
        elif decision.overall_score > 0.4:
            print("⚠️  PROCEED WITH CAUTION: Mixed alignment")
        else:
            print("❌ NOT RECOMMENDED: Poor alignment with core principles")
        
        print("-" * 30)
    
    print("\n🎯 Agape Core Principles:")
    print("• All decisions filtered through the lens of love")
    print("• God's glory and neighbor's welfare are paramount")
    print("• Wisdom, truth, and compassion guide every choice")
    print("• Human dignity is always protected")
    
    # Interactive mode
    print("\n💬 Interactive Mode - Enter actions to evaluate (or 'quit' to exit):")
    while True:
        user_action = input("\nAction to evaluate: ").strip()
        if user_action.lower() in ['quit', 'exit', 'q']:
            break
        
        if user_action:
            decision = agape_ai.evaluate_decision(user_action, {})
            print(f"\nScore: {decision.overall_score:.2f}/1.0")
            print(decision.reasoning)
            if decision.value_impact:
                print(f"\n📊 {decision.value_impact.reasoning}")

if __name__ == "__main__":
    main()
