
#!/usr/bin/env python3
"""
Agape Core AI - Beta Experiment
An AI system that follows the two great commandments as core directives:
1. Love God with all your heart, soul, mind, and strength
2. Love your neighbor as yourself
"""

import json
import logging
from typing import Dict, List, Tuple, Any
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
class Decision:
    """Represents a decision with its moral evaluation"""
    action: str
    love_god_score: float  # How well does this honor God?
    love_neighbor_score: float  # How well does this serve others?
    harm_assessment: float  # Potential harm (negative is bad)
    overall_score: float
    reasoning: str

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
        
        # Generate reasoning
        reasoning = self._generate_reasoning(action, love_god_score, love_neighbor_score, harm_assessment)
        
        return Decision(
            action=action,
            love_god_score=love_god_score,
            love_neighbor_score=love_neighbor_score,
            harm_assessment=harm_assessment,
            overall_score=overall_score,
            reasoning=reasoning
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

if __name__ == "__main__":
    main()
