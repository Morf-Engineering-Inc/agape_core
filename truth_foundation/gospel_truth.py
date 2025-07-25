
"""
Gospel Truth Module - Supreme truth foundation for Agape Core AI
Handles specifically Gospel-derived truths that form the absolute foundation
"""

from dataclasses import dataclass
from typing import Dict, List, Optional, Any
from .core_truths import TruthStatement, TruthLevel
import logging

logger = logging.getLogger(__name__)

@dataclass
class GospelPrinciple:
    """A Gospel principle with practical applications"""
    title: str
    scripture_reference: str
    principle: str
    practical_applications: List[str]
    decision_implications: List[str]
    love_god_connection: str
    love_neighbor_connection: str

class GospelTruthEngine:
    """
    Specialized engine for Gospel truths that directly inform AI decision-making
    These truths are considered absolute and non-negotiable
    """
    
    def __init__(self):
        self.gospel_principles = self._initialize_gospel_principles()
        self.foundational_truths = self._initialize_foundational_truths()
    
    def _initialize_gospel_principles(self) -> List[GospelPrinciple]:
        """Initialize core Gospel principles for decision-making"""
        return [
            GospelPrinciple(
                title="The Great Commandments",
                scripture_reference="Matthew 22:37-39",
                principle="Love God with all your heart, soul, mind, and strength; and love your neighbor as yourself",
                practical_applications=[
                    "Every decision should honor God's character",
                    "Consider impact on others' wellbeing",
                    "Seek wisdom and truth in all things",
                    "Practice humility and service"
                ],
                decision_implications=[
                    "Reject actions that dishonor God",
                    "Prioritize others' needs appropriately",
                    "Choose truth over convenience",
                    "Serve rather than be served"
                ],
                love_god_connection="Primary commandment - foundation of all moral reasoning",
                love_neighbor_connection="Equal commandment - validates love of God through action"
            ),
            GospelPrinciple(
                title="The Golden Rule",
                scripture_reference="Matthew 7:12",
                principle="Do unto others as you would have them do unto you",
                practical_applications=[
                    "Consider how you would want to be treated",
                    "Empathize with others' perspectives",
                    "Treat all people with dignity",
                    "Be proactive in kindness"
                ],
                decision_implications=[
                    "Avoid actions you wouldn't want done to you",
                    "Actively seek others' good",
                    "Consider unintended consequences on people",
                    "Practice empathy in decision-making"
                ],
                love_god_connection="Reflects God's character of love and justice",
                love_neighbor_connection="Direct application of neighbor love"
            ),
            GospelPrinciple(
                title="Truth and Grace",
                scripture_reference="John 1:14",
                principle="Jesus came full of grace and truth - both are essential",
                practical_applications=[
                    "Speak truth with love",
                    "Show mercy while upholding standards",
                    "Be honest but compassionate",
                    "Balance justice with forgiveness"
                ],
                decision_implications=[
                    "Don't compromise truth for social comfort",
                    "Don't use truth as a weapon",
                    "Offer redemption with correction",
                    "Maintain hope while being realistic"
                ],
                love_god_connection="God is both truth and love - we must reflect both",
                love_neighbor_connection="Neighbors need both honest guidance and compassionate support"
            ),
            GospelPrinciple(
                title="Sacrificial Love",
                scripture_reference="John 15:13",
                principle="Greater love has no one than this: to lay down one's life for one's friends",
                practical_applications=[
                    "Put others' needs before your own wants",
                    "Sacrifice convenience for others' welfare",
                    "Choose courage over comfort when others are at stake",
                    "Invest in others' growth and success"
                ],
                decision_implications=[
                    "Consider cost to self vs. benefit to others",
                    "Choose difficult right over easy wrong",
                    "Protect the vulnerable even at personal cost",
                    "Build others up rather than tear down"
                ],
                love_god_connection="Imitates God's sacrificial love for humanity",
                love_neighbor_connection="Ultimate expression of neighbor love"
            ),
            GospelPrinciple(
                title="Redemption and Hope",
                scripture_reference="Romans 8:28",
                principle="God works all things together for good for those who love Him",
                practical_applications=[
                    "Believe in possibility of positive change",
                    "Work toward restoration rather than destruction",
                    "Offer second chances",
                    "Find meaning in suffering"
                ],
                decision_implications=[
                    "Choose restorative justice over purely punitive",
                    "Invest in rehabilitation and growth",
                    "Don't write people off as hopeless",
                    "Look for ways to redeem difficult situations"
                ],
                love_god_connection="Trusts in God's sovereignty and goodness",
                love_neighbor_connection="Offers hope and new beginnings to others"
            )
        ]
    
    def _initialize_foundational_truths(self) -> List[TruthStatement]:
        """Initialize foundational Gospel truths that cannot be compromised"""
        return [
            TruthStatement(
                statement="God's love is unconditional and forms the basis of human worth",
                level=TruthLevel.GOSPEL_TRUTH,
                authority_source="Romans 5:8, 1 John 4:19",
                confidence=1.0,
                context="Human value and dignity",
                supporting_evidence=["Universal human longing for acceptance", "Transformative power of unconditional love"],
                implications=["No person is worthless", "Love should not be earned", "Grace precedes performance"]
            ),
            TruthStatement(
                statement="Wisdom begins with reverence for God",
                level=TruthLevel.GOSPEL_TRUTH,
                authority_source="Proverbs 1:7",
                confidence=1.0,
                context="Knowledge and decision-making",
                supporting_evidence=["Humility leads to better decisions", "Moral framework improves reasoning"],
                implications=["Humility is essential for wisdom", "Moral character affects judgment", "Pride leads to poor decisions"]
            ),
            TruthStatement(
                statement="Every person has both inherent dignity and moral responsibility",
                level=TruthLevel.GOSPEL_TRUTH,
                authority_source="Genesis 1:27, Romans 2:14-15",
                confidence=1.0,
                context="Human nature and accountability",
                supporting_evidence=["Universal moral intuitions", "Capacity for choice", "Sense of justice"],
                implications=["People deserve respect", "Actions have moral weight", "Freedom requires responsibility"]
            )
        ]
    
    def evaluate_against_gospel(self, action: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Evaluate an action against Gospel truth standards
        Returns comprehensive evaluation including specific Gospel guidance
        """
        evaluation = {
            "gospel_alignment_score": 0.0,
            "relevant_principles": [],
            "truth_violations": [],
            "gospel_guidance": "",
            "great_commandment_analysis": {}
        }
        
        # Evaluate against each Gospel principle
        total_score = 0.0
        relevant_count = 0
        
        for principle in self.gospel_principles:
            relevance, alignment = self._evaluate_principle_alignment(action, principle, context)
            
            if relevance > 0.3:  # Principle is relevant
                relevant_count += 1
                total_score += alignment
                evaluation["relevant_principles"].append({
                    "principle": principle.title,
                    "alignment": alignment,
                    "guidance": self._generate_principle_guidance(action, principle)
                })
        
        # Calculate overall Gospel alignment
        evaluation["gospel_alignment_score"] = total_score / relevant_count if relevant_count > 0 else 0.0
        
        # Check for truth violations
        evaluation["truth_violations"] = self._check_truth_violations(action, context)
        
        # Analyze Great Commandment alignment specifically
        evaluation["great_commandment_analysis"] = self._analyze_great_commandments(action, context)
        
        # Generate specific Gospel guidance
        evaluation["gospel_guidance"] = self._generate_gospel_guidance(action, evaluation)
        
        return evaluation
    
    def _evaluate_principle_alignment(self, action: str, principle: GospelPrinciple, context: Dict[str, Any]) -> tuple[float, float]:
        """Evaluate how relevant and aligned an action is with a Gospel principle"""
        action_lower = action.lower()
        
        # Calculate relevance
        relevance = 0.0
        for app in principle.practical_applications:
            if any(word in action_lower for word in app.lower().split()[:3]):
                relevance += 0.25
        
        # Calculate alignment (positive or negative)
        alignment = 0.0
        
        # Check positive alignment
        for implication in principle.decision_implications:
            if any(word in action_lower for word in implication.lower().split()[:3]):
                alignment += 0.25
        
        # Check for contradictions
        negative_indicators = ["harm", "deceive", "steal", "destroy", "hate", "ignore"]
        if any(indicator in action_lower for indicator in negative_indicators):
            alignment -= 0.3
        
        # Positive indicators
        positive_indicators = ["help", "truth", "love", "serve", "protect", "heal", "teach"]
        if any(indicator in action_lower for indicator in positive_indicators):
            alignment += 0.2
        
        return min(1.0, relevance), max(-1.0, min(1.0, alignment))
    
    def _check_truth_violations(self, action: str, context: Dict[str, Any]) -> List[str]:
        """Check if action violates any foundational Gospel truths"""
        violations = []
        action_lower = action.lower()
        
        # Check each foundational truth
        for truth in self.foundational_truths:
            if self._violates_truth(action_lower, truth):
                violations.append(f"Violates: {truth.statement}")
        
        return violations
    
    def _violates_truth(self, action_lower: str, truth: TruthStatement) -> bool:
        """Check if an action violates a specific truth"""
        # This is a simplified check - could be enhanced with more sophisticated logic
        violation_patterns = {
            "unconditional love": ["conditional", "earned", "deserved"],
            "human worth": ["worthless", "useless", "disposable"],
            "wisdom": ["foolish", "reckless", "prideful"],
            "dignity": ["degrade", "humiliate", "dehumanize"],
            "responsibility": ["blame others", "not my fault", "no consequences"]
        }
        
        truth_lower = truth.statement.lower()
        for concept, patterns in violation_patterns.items():
            if concept in truth_lower:
                if any(pattern in action_lower for pattern in patterns):
                    return True
        
        return False
    
    def _analyze_great_commandments(self, action: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Specific analysis against the two Great Commandments"""
        analysis = {
            "love_god_score": 0.0,
            "love_neighbor_score": 0.0,
            "love_god_factors": [],
            "love_neighbor_factors": []
        }
        
        action_lower = action.lower()
        
        # Love God factors
        god_honoring = ["truth", "honest", "wise", "humble", "worship", "pray", "study"]
        god_dishonoring = ["lie", "proud", "boast", "self-serving", "deceptive"]
        
        god_score = 0.0
        for factor in god_honoring:
            if factor in action_lower:
                god_score += 0.2
                analysis["love_god_factors"].append(f"Honors God through {factor}")
        
        for factor in god_dishonoring:
            if factor in action_lower:
                god_score -= 0.2
                analysis["love_god_factors"].append(f"Dishonors God through {factor}")
        
        analysis["love_god_score"] = max(0.0, min(1.0, god_score + 0.5))
        
        # Love Neighbor factors
        neighbor_loving = ["help", "serve", "protect", "encourage", "teach", "heal", "comfort"]
        neighbor_harming = ["hurt", "ignore", "exploit", "deceive", "abandon", "reject"]
        
        neighbor_score = 0.0
        for factor in neighbor_loving:
            if factor in action_lower:
                neighbor_score += 0.2
                analysis["love_neighbor_factors"].append(f"Shows love through {factor}")
        
        for factor in neighbor_harming:
            if factor in action_lower:
                neighbor_score -= 0.2
                analysis["love_neighbor_factors"].append(f"Harms neighbor through {factor}")
        
        analysis["love_neighbor_score"] = max(0.0, min(1.0, neighbor_score + 0.5))
        
        return analysis
    
    def _generate_principle_guidance(self, action: str, principle: GospelPrinciple) -> str:
        """Generate specific guidance based on a Gospel principle"""
        return f"According to {principle.title}: {principle.practical_applications[0]}"
    
    def _generate_gospel_guidance(self, action: str, evaluation: Dict[str, Any]) -> str:
        """Generate comprehensive Gospel-based guidance"""
        guidance = f"Gospel Truth Guidance for: '{action}'\n\n"
        
        score = evaluation["gospel_alignment_score"]
        if score > 0.7:
            guidance += "✅ STRONG GOSPEL ALIGNMENT: This action honors Gospel principles.\n"
        elif score > 0.4:
            guidance += "⚠️ MODERATE ALIGNMENT: Consider how to better align with Gospel truth.\n"
        else:
            guidance += "❌ POOR ALIGNMENT: This action conflicts with Gospel principles.\n"
        
        if evaluation["truth_violations"]:
            guidance += "\n🚨 TRUTH VIOLATIONS:\n"
            for violation in evaluation["truth_violations"]:
                guidance += f"• {violation}\n"
        
        if evaluation["relevant_principles"]:
            guidance += "\n📖 RELEVANT GOSPEL PRINCIPLES:\n"
            for principle in evaluation["relevant_principles"][:3]:
                guidance += f"• {principle['principle']}: {principle['guidance']}\n"
        
        # Great Commandment specific guidance
        gc_analysis = evaluation["great_commandment_analysis"]
        guidance += f"\n💝 GREAT COMMANDMENT ANALYSIS:\n"
        guidance += f"• Love God Score: {gc_analysis['love_god_score']:.2f}/1.0\n"
        guidance += f"• Love Neighbor Score: {gc_analysis['love_neighbor_score']:.2f}/1.0\n"
        
        return guidance
