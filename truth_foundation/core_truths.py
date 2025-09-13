
"""
Core Truth Foundation for Agape Core AI
Hierarchical truth system with the Atonement of Jesus Christ as the supreme foundation
All other truths derive meaning and grounding from Christ's redemptive work
"""

from enum import Enum
from dataclasses import dataclass
from typing import Dict, List, Optional, Any
import logging

logger = logging.getLogger(__name__)

class TruthLevel(Enum):
    """Hierarchy of truth - Atonement of Jesus Christ is the supreme foundation"""
    ATONEMENT_SUPREME = 0 # The Atonement of Jesus Christ - supreme foundational truth
    GOSPEL_TRUTH = 1      # Divine revelation, Scripture, core Gospel
    MORAL_TRUTH = 2       # Universal moral principles
    NATURAL_TRUTH = 3     # Observable, scientific, logical truths
    PRACTICAL_TRUTH = 4   # Contextual, situational truths
    OPINION = 5           # Personal perspectives, preferences

@dataclass
class TruthStatement:
    """Represents a truth claim with its classification and authority"""
    statement: str
    level: TruthLevel
    authority_source: str
    confidence: float  # 0.0 to 1.0
    context: str
    supporting_evidence: List[str]
    implications: List[str]

class TruthFoundation:
    """
    Core truth system that establishes foundational truths for AI decision-making
    Gospel truth forms the supreme foundation, with other truths subordinate
    """
    
    def __init__(self):
        self.truth_hierarchy = {
            TruthLevel.ATONEMENT_SUPREME: 1.0,  # Supreme foundational truth
            TruthLevel.GOSPEL_TRUTH: 0.95,
            TruthLevel.MORAL_TRUTH: 0.9,
            TruthLevel.NATURAL_TRUTH: 0.8,
            TruthLevel.PRACTICAL_TRUTH: 0.6,
            TruthLevel.OPINION: 0.3
        }
        
        # Initialize core Gospel truths
        self._initialize_gospel_truths()
        
        # Initialize moral truths derived from Gospel
        self._initialize_moral_truths()
        
        # Initialize natural truths
        self._initialize_natural_truths()
    
    def _initialize_gospel_truths(self):
        """Initialize fundamental Gospel truths that govern all decision-making"""
        self.gospel_truths = [
            TruthStatement(
                statement="God exists and is the source of all truth, goodness, and love",
                level=TruthLevel.GOSPEL_TRUTH,
                authority_source="Scripture - Genesis 1:1, John 1:1, 1 John 4:8",
                confidence=1.0,
                context="Foundational reality",
                supporting_evidence=["Creation", "Moral law", "Human consciousness", "Scripture"],
                implications=["All truth derives from God", "Reality has meaning and purpose", "Moral standards are objective"]
            ),
            TruthStatement(
                statement="Humans are created in God's image with inherent dignity and worth",
                level=TruthLevel.GOSPEL_TRUTH,
                authority_source="Scripture - Genesis 1:27",
                confidence=1.0,
                context="Human nature and value",
                supporting_evidence=["Universal human rights concepts", "Moral intuition", "Capacity for relationship"],
                implications=["Every person has infinite worth", "Human life is sacred", "Equality of human dignity"]
            ),
            TruthStatement(
                statement="Love is the supreme virtue and commandment",
                level=TruthLevel.GOSPEL_TRUTH,
                authority_source="Scripture - Matthew 22:37-39, 1 Corinthians 13",
                confidence=1.0,
                context="Moral foundation",
                supporting_evidence=["The two great commandments", "Christ's example", "Universal human longing for love"],
                implications=["All actions should be evaluated through love", "Self-sacrifice for others is noble", "Love defines right relationship"]
            ),
            TruthStatement(
                statement="Truth exists objectively and can be known",
                level=TruthLevel.GOSPEL_TRUTH,
                authority_source="Scripture - John 14:6, John 8:32",
                confidence=1.0,
                context="Epistemological foundation",
                supporting_evidence=["Logical consistency", "Scientific method", "Universal moral intuitions"],
                implications=["Relativism is false", "Truth claims can be evaluated", "Knowledge has meaning"]
            ),
            TruthStatement(
                statement="Redemption and forgiveness are possible for all",
                level=TruthLevel.GOSPEL_TRUTH,
                authority_source="Scripture - John 3:16, Romans 6:23",
                confidence=1.0,
                context="Human hope and restoration",
                supporting_evidence=["Universal longing for forgiveness", "Transformational testimonies", "Moral restoration"],
                implications=["No person is beyond hope", "Grace overcomes judgment", "Second chances should be offered"]
            )
        ]
    
    def _initialize_moral_truths(self):
        """Initialize moral truths derived from Gospel foundations"""
        self.moral_truths = [
            TruthStatement(
                statement="It is wrong to intentionally harm innocent people",
                level=TruthLevel.MORAL_TRUTH,
                authority_source="Derived from human dignity and love commandment",
                confidence=0.95,
                context="Harm prevention",
                supporting_evidence=["Universal moral intuition", "Social contracts", "Golden Rule"],
                implications=["Protection of vulnerable is priority", "Intent matters in moral evaluation", "Innocent until proven guilty"]
            ),
            TruthStatement(
                statement="Honesty and truthfulness are moral goods",
                level=TruthLevel.MORAL_TRUTH,
                authority_source="Derived from God as truth and love of neighbor",
                confidence=0.95,
                context="Communication ethics",
                supporting_evidence=["Trust as foundation of society", "Commandment against false witness", "Practical benefits"],
                implications=["Lies undermine relationships", "Truth-telling builds trust", "Deception harms community"]
            ),
            TruthStatement(
                statement="Justice requires treating equals equally",
                level=TruthLevel.MORAL_TRUTH,
                authority_source="Derived from human dignity and God's justice",
                confidence=0.9,
                context="Fairness and equality",
                supporting_evidence=["Universal sense of fairness", "Stable societies require justice", "Impartial moral reasoning"],
                implications=["Discrimination based on irrelevant factors is wrong", "Merit should be rewarded", "Bias must be addressed"]
            )
        ]
    
    def _initialize_natural_truths(self):
        """Initialize observable natural truths"""
        self.natural_truths = [
            TruthStatement(
                statement="Actions have consequences",
                level=TruthLevel.NATURAL_TRUTH,
                authority_source="Observation and experience",
                confidence=0.95,
                context="Causality",
                supporting_evidence=["Physics", "Psychology", "History", "Personal experience"],
                implications=["Responsibility for choices", "Predictable outcomes", "Planning is valuable"]
            ),
            TruthStatement(
                statement="Human beings are social creatures who need community",
                level=TruthLevel.NATURAL_TRUTH,
                authority_source="Anthropology and psychology",
                confidence=0.9,
                context="Human nature",
                supporting_evidence=["Mental health research", "Historical societies", "Child development"],
                implications=["Isolation is harmful", "Cooperation is beneficial", "Relationships matter"]
            ),
            TruthStatement(
                statement="Knowledge and understanding can be improved through study and experience",
                level=TruthLevel.NATURAL_TRUTH,
                authority_source="Educational science and cognitive research",
                confidence=0.9,
                context="Learning and growth",
                supporting_evidence=["Scientific method", "Educational outcomes", "Skill development"],
                implications=["Learning is valuable", "Experience teaches", "Expertise matters"]
            )
        ]
    
    def evaluate_truth_claim(self, claim: str, context: Dict[str, Any]) -> float:
        """
        Evaluate how well a claim aligns with established truths
        Returns confidence score 0.0 to 1.0
        """
        alignment_score = 0.0
        total_weight = 0.0
        
        # Check alignment with Gospel truths (highest weight)
        for truth in self.gospel_truths:
            alignment = self._calculate_alignment(claim, truth)
            weight = self.truth_hierarchy[TruthLevel.GOSPEL_TRUTH]
            alignment_score += alignment * weight
            total_weight += weight
        
        # Check alignment with moral truths
        for truth in self.moral_truths:
            alignment = self._calculate_alignment(claim, truth)
            weight = self.truth_hierarchy[TruthLevel.MORAL_TRUTH]
            alignment_score += alignment * weight
            total_weight += weight
        
        # Check alignment with natural truths
        for truth in self.natural_truths:
            alignment = self._calculate_alignment(claim, truth)
            weight = self.truth_hierarchy[TruthLevel.NATURAL_TRUTH]
            alignment_score += alignment * weight
            total_weight += weight
        
        return min(1.0, alignment_score / total_weight) if total_weight > 0 else 0.0
    
    def _calculate_alignment(self, claim: str, truth: TruthStatement) -> float:
        """Calculate how well a claim aligns with a specific truth"""
        claim_lower = claim.lower()
        truth_lower = truth.statement.lower()
        
        # Simple keyword matching - could be enhanced with NLP
        alignment = 0.0
        
        # Direct semantic alignment
        if truth_lower in claim_lower or any(keyword in claim_lower for keyword in truth_lower.split()):
            alignment += 0.5
        
        # Check for supporting concepts
        for evidence in truth.supporting_evidence:
            if evidence.lower() in claim_lower:
                alignment += 0.2
        
        # Check for implication alignment
        for implication in truth.implications:
            if any(word in claim_lower for word in implication.lower().split()[:3]):
                alignment += 0.1
        
        return min(1.0, alignment)
    
    def get_relevant_truths(self, context: str, limit: int = 5) -> List[TruthStatement]:
        """Get truths most relevant to a given context"""
        all_truths = self.gospel_truths + self.moral_truths + self.natural_truths
        
        # Score relevance based on context matching
        scored_truths = []
        for truth in all_truths:
            relevance = self._calculate_relevance(context, truth)
            scored_truths.append((truth, relevance))
        
        # Sort by relevance and return top results
        scored_truths.sort(key=lambda x: x[1], reverse=True)
        return [truth for truth, _ in scored_truths[:limit]]
    
    def _calculate_relevance(self, context: str, truth: TruthStatement) -> float:
        """Calculate relevance of a truth to given context"""
        context_lower = context.lower()
        relevance = 0.0
        
        # Check context field
        if truth.context.lower() in context_lower:
            relevance += 0.4
        
        # Check statement keywords
        truth_keywords = truth.statement.lower().split()
        context_keywords = context_lower.split()
        matching_keywords = set(truth_keywords) & set(context_keywords)
        relevance += len(matching_keywords) * 0.1
        
        # Boost for higher-level truths
        if truth.level == TruthLevel.GOSPEL_TRUTH:
            relevance += 0.2
        elif truth.level == TruthLevel.MORAL_TRUTH:
            relevance += 0.1
        
        return min(1.0, relevance)
    
    def generate_truth_guidance(self, situation: str) -> str:
        """Generate guidance based on relevant truths for a situation"""
        relevant_truths = self.get_relevant_truths(situation, 3)
        
        guidance = f"Truth-based guidance for: '{situation}'\n\n"
        
        for i, truth in enumerate(relevant_truths, 1):
            guidance += f"{i}. {truth.statement}\n"
            guidance += f"   Level: {truth.level.name}\n"
            guidance += f"   Authority: {truth.authority_source}\n"
            guidance += f"   Key Implication: {truth.implications[0] if truth.implications else 'Apply with wisdom'}\n\n"
        
        return guidance
