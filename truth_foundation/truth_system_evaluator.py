
"""
Truth System Evaluator - Analyzing Laws and Principles in Truth Systems
Based on patterns like Russell Nelson's heart analogy and D&C 121:39-45
Evaluates what truth laws are in place and how they're being applied
"""

from dataclasses import dataclass
from typing import Dict, List, Optional, Any, Union
from enum import Enum
import logging

logger = logging.getLogger(__name__)

class TruthLaw(Enum):
    """Categories of truth laws that govern systems"""
    DIVINE_LAW = "divine_law"           # Eternal, unchanging principles from God
    NATURAL_LAW = "natural_law"         # Physical and observable laws
    MORAL_LAW = "moral_law"             # Universal moral principles
    SOCIAL_LAW = "social_law"           # Human-created laws and customs
    SPIRITUAL_LAW = "spiritual_law"     # Laws governing spiritual growth
    LOGICAL_LAW = "logical_law"         # Laws of reason and consistency

class TruthSystemType(Enum):
    """Types of systems that can be evaluated"""
    RELIGIOUS = "religious"
    SCIENTIFIC = "scientific"
    PHILOSOPHICAL = "philosophical"
    POLITICAL = "political"
    EDUCATIONAL = "educational"
    PERSONAL = "personal"
    ORGANIZATIONAL = "organizational"

@dataclass
class TruthPrinciple:
    """A specific principle or law within a truth system"""
    name: str
    law_type: TruthLaw
    statement: str
    source_authority: str
    evidence_supporting: List[str]
    contradictions_noted: List[str]
    practical_applications: List[str]
    verification_method: str
    universality_score: float  # 0.0 to 1.0
    consistency_score: float   # 0.0 to 1.0

@dataclass
class SystemEvaluation:
    """Comprehensive evaluation of a truth system"""
    system_name: str
    system_type: TruthSystemType
    active_principles: List[TruthPrinciple]
    truth_foundation: str
    consistency_analysis: Dict[str, Any]
    gaps_identified: List[str]
    contradictions_found: List[str]
    truth_utilization_score: float
    recommendation: str

class TruthSystemEvaluator:
    """
    Evaluates truth systems to identify what laws are in place
    and how truth is being utilized, similar to analyzing the heart
    """
    
    def __init__(self):
        self.known_truth_laws = self._initialize_truth_laws()
        self.evaluation_patterns = self._initialize_evaluation_patterns()
    
    def _initialize_truth_laws(self) -> Dict[TruthLaw, List[str]]:
        """Initialize known truth laws and their indicators"""
        return {
            TruthLaw.DIVINE_LAW: [
                "Love God with all your heart, soul, mind, strength",
                "Love your neighbor as yourself", 
                "Truth is eternal and unchanging",
                "God is the source of all truth",
                "The Atonement of Christ is supreme truth",
                "Moral agency is divine gift",
                "All people have inherent worth and dignity"
            ],
            
            TruthLaw.NATURAL_LAW: [
                "Actions have consequences",
                "Energy cannot be created or destroyed",
                "Living things require sustenance",
                "Gravity affects all matter",
                "Cause and effect relationships exist",
                "Growth requires proper conditions",
                "Systems tend toward entropy without input"
            ],
            
            TruthLaw.MORAL_LAW: [
                "Do unto others as you would have them do unto you",
                "Honesty builds trust, deception destroys it",
                "Justice requires treating equals equally",
                "Mercy can override strict justice",
                "Protecting innocent is moral imperative",
                "Promises should be kept",
                "Taking responsibility for actions is required"
            ],
            
            TruthLaw.SPIRITUAL_LAW: [
                "Faith precedes miracles",
                "Repentance enables spiritual growth",
                "Service to others brings spiritual fulfillment",
                "Prayer connects finite to infinite",
                "Scripture study increases understanding",
                "Gratitude increases spiritual sensitivity",
                "Humility enables learning"
            ],
            
            TruthLaw.SOCIAL_LAW: [
                "Trust is foundation of relationships",
                "Communication prevents misunderstanding",
                "Cooperation achieves more than competition",
                "Leadership requires service",
                "Communities need shared values",
                "Conflict resolution requires empathy",
                "Diversity strengthens groups when unified by common purpose"
            ],
            
            TruthLaw.LOGICAL_LAW: [
                "A thing cannot both be and not be",
                "If premises are true, conclusion follows",
                "Evidence should support conclusions",
                "Correlation does not imply causation",
                "Extraordinary claims require extraordinary evidence",
                "Internal consistency is required for truth",
                "Simpler explanations are often better"
            ]
        }
    
    def _initialize_evaluation_patterns(self) -> Dict[str, List[str]]:
        """Initialize patterns for evaluating truth system health"""
        return {
            "healthy_indicators": [
                "consistent application of principles",
                "openness to truth from multiple sources",
                "humility when confronted with error",
                "practical positive outcomes",
                "growth and improvement over time",
                "service orientation",
                "integration rather than contradiction"
            ],
            
            "warning_signs": [
                "pride and unteachability",
                "selective application of principles",
                "defensiveness about contradictions",
                "harm to innocent people",
                "stagnation or decline",
                "self-serving orientation",
                "internal contradictions ignored"
            ],
            
            "russell_nelson_heart_pattern": [
                "Regular spiritual nourishment (scripture study/prayer like food)",
                "Exercise of faith (spiritual exercise like physical exercise)",
                "Avoiding spiritual toxins (sin like avoiding poisons)",
                "Rest and renewal (Sabbath observance like sleep)",
                "Community connection (fellowship like social health)",
                "Growth and development (spiritual progression like physical growth)"
            ]
        }
    
    def evaluate_system(self, system_name: str, system_type: TruthSystemType, 
                       system_description: str, observed_practices: List[str],
                       claimed_principles: List[str] = None) -> SystemEvaluation:
        """
        Main evaluation function - analyze what truth laws are in place
        and how effectively truth is being used
        """
        if claimed_principles is None:
            claimed_principles = []
            
        logger.info(f"Evaluating truth system: {system_name}")
        
        # Identify active principles
        active_principles = self._identify_active_principles(
            system_description, observed_practices, claimed_principles
        )
        
        # Determine truth foundation
        truth_foundation = self._determine_truth_foundation(active_principles)
        
        # Analyze consistency
        consistency_analysis = self._analyze_consistency(active_principles, observed_practices)
        
        # Identify gaps and contradictions
        gaps_identified = self._identify_gaps(system_type, active_principles)
        contradictions_found = self._identify_contradictions(active_principles, observed_practices)
        
        # Calculate truth utilization score
        truth_utilization_score = self._calculate_truth_utilization(
            active_principles, consistency_analysis, gaps_identified, contradictions_found
        )
        
        # Generate recommendation
        recommendation = self._generate_recommendation(
            system_name, truth_utilization_score, gaps_identified, contradictions_found
        )
        
        return SystemEvaluation(
            system_name=system_name,
            system_type=system_type,
            active_principles=active_principles,
            truth_foundation=truth_foundation,
            consistency_analysis=consistency_analysis,
            gaps_identified=gaps_identified,
            contradictions_found=contradictions_found,
            truth_utilization_score=truth_utilization_score,
            recommendation=recommendation
        )
    
    def _identify_active_principles(self, description: str, practices: List[str], 
                                  claims: List[str]) -> List[TruthPrinciple]:
        """Identify what truth principles are actually active in the system"""
        active_principles = []
        full_text = f"{description} {' '.join(practices)} {' '.join(claims)}".lower()
        
        for law_type, principles in self.known_truth_laws.items():
            for principle in principles:
                if self._principle_is_active(principle, full_text, practices):
                    # Calculate scores
                    universality_score = self._calculate_universality(principle)
                    consistency_score = self._calculate_consistency_with_practices(principle, practices)
                    
                    active_principles.append(TruthPrinciple(
                        name=principle,
                        law_type=law_type,
                        statement=principle,
                        source_authority=self._determine_source_authority(principle, law_type),
                        evidence_supporting=self._find_supporting_evidence(principle, practices),
                        contradictions_noted=self._find_contradictions(principle, practices),
                        practical_applications=self._identify_applications(principle, practices),
                        verification_method=self._determine_verification_method(law_type),
                        universality_score=universality_score,
                        consistency_score=consistency_score
                    ))
        
        return active_principles
    
    def _principle_is_active(self, principle: str, full_text: str, practices: List[str]) -> bool:
        """Determine if a principle is actively present in the system"""
        principle_keywords = principle.lower().split()[:4]  # Key words from principle
        
        # Check for keyword matches
        keyword_matches = sum(1 for word in principle_keywords if word in full_text)
        if keyword_matches >= 2:
            return True
        
        # Check for behavioral evidence in practices
        practice_text = ' '.join(practices).lower()
        if any(word in practice_text for word in principle_keywords):
            return True
        
        return False
    
    def _determine_truth_foundation(self, principles: List[TruthPrinciple]) -> str:
        """Determine what serves as the foundational truth for this system"""
        if not principles:
            return "No clear truth foundation identified"
        
        # Count by law types
        law_counts = {}
        for principle in principles:
            law_counts[principle.law_type] = law_counts.get(principle.law_type, 0) + 1
        
        primary_law_type = max(law_counts, key=law_counts.get)
        
        foundation_descriptions = {
            TruthLaw.DIVINE_LAW: "Divine revelation and eternal principles",
            TruthLaw.NATURAL_LAW: "Observable natural phenomena and scientific method",
            TruthLaw.MORAL_LAW: "Universal moral intuitions and ethical reasoning",
            TruthLaw.SPIRITUAL_LAW: "Spiritual experience and growth principles",
            TruthLaw.SOCIAL_LAW: "Social contract and human agreement",
            TruthLaw.LOGICAL_LAW: "Rational thought and logical consistency"
        }
        
        return foundation_descriptions.get(primary_law_type, "Mixed foundation")
    
    def _analyze_consistency(self, principles: List[TruthPrinciple], 
                           practices: List[str]) -> Dict[str, Any]:
        """Analyze how consistently principles are applied"""
        if not principles:
            return {"overall_consistency": 0.0, "analysis": "No principles to analyze"}
        
        consistency_scores = [p.consistency_score for p in principles]
        overall_consistency = sum(consistency_scores) / len(consistency_scores)
        
        high_consistency = [p for p in principles if p.consistency_score > 0.8]
        low_consistency = [p for p in principles if p.consistency_score < 0.5]
        
        return {
            "overall_consistency": overall_consistency,
            "high_consistency_principles": [p.name for p in high_consistency],
            "low_consistency_principles": [p.name for p in low_consistency],
            "analysis": f"System shows {overall_consistency:.2f} consistency in applying stated principles"
        }
    
    def _identify_gaps(self, system_type: TruthSystemType, 
                      principles: List[TruthPrinciple]) -> List[str]:
        """Identify missing principles that should be present"""
        active_law_types = {p.law_type for p in principles}
        
        # Essential principles for different system types
        essential_for_type = {
            TruthSystemType.RELIGIOUS: [TruthLaw.DIVINE_LAW, TruthLaw.MORAL_LAW, TruthLaw.SPIRITUAL_LAW],
            TruthSystemType.SCIENTIFIC: [TruthLaw.NATURAL_LAW, TruthLaw.LOGICAL_LAW],
            TruthSystemType.EDUCATIONAL: [TruthLaw.LOGICAL_LAW, TruthLaw.NATURAL_LAW, TruthLaw.MORAL_LAW],
            TruthSystemType.POLITICAL: [TruthLaw.MORAL_LAW, TruthLaw.SOCIAL_LAW],
            TruthSystemType.ORGANIZATIONAL: [TruthLaw.SOCIAL_LAW, TruthLaw.MORAL_LAW],
            TruthSystemType.PERSONAL: [TruthLaw.MORAL_LAW, TruthLaw.SPIRITUAL_LAW]
        }
        
        required_types = essential_for_type.get(system_type, [])
        missing_types = [law_type for law_type in required_types if law_type not in active_law_types]
        
        gaps = []
        for missing_type in missing_types:
            gaps.append(f"Missing {missing_type.value.replace('_', ' ').title()} principles")
        
        return gaps
    
    def _identify_contradictions(self, principles: List[TruthPrinciple], 
                               practices: List[str]) -> List[str]:
        """Identify contradictions between stated principles and observed practices"""
        contradictions = []
        
        for principle in principles:
            if principle.contradictions_noted:
                for contradiction in principle.contradictions_noted:
                    contradictions.append(f"{principle.name}: {contradiction}")
        
        return contradictions
    
    def _calculate_truth_utilization(self, principles: List[TruthPrinciple], 
                                   consistency: Dict[str, Any], gaps: List[str], 
                                   contradictions: List[str]) -> float:
        """Calculate overall score for how well truth is being utilized"""
        if not principles:
            return 0.0
        
        # Base score from principle quality
        avg_universality = sum(p.universality_score for p in principles) / len(principles)
        avg_consistency = consistency["overall_consistency"]
        
        # Penalties for gaps and contradictions
        gap_penalty = len(gaps) * 0.1
        contradiction_penalty = len(contradictions) * 0.15
        
        score = (avg_universality + avg_consistency) / 2
        score -= gap_penalty
        score -= contradiction_penalty
        
        return max(0.0, min(1.0, score))
    
    def _calculate_universality(self, principle: str) -> float:
        """Calculate how universal/eternal a principle is"""
        # Divine and moral laws are most universal
        principle_lower = principle.lower()
        
        universal_indicators = ["love", "truth", "justice", "mercy", "honesty", "service"]
        score = sum(0.15 for indicator in universal_indicators if indicator in principle_lower)
        
        return min(1.0, score + 0.1)  # Base score of 0.1
    
    def _calculate_consistency_with_practices(self, principle: str, practices: List[str]) -> float:
        """Calculate how consistently a principle is applied in practice"""
        if not practices:
            return 0.5  # Neutral if no practices to evaluate
        
        principle_keywords = principle.lower().split()[:3]
        practice_text = ' '.join(practices).lower()
        
        matches = sum(1 for word in principle_keywords if word in practice_text)
        return min(1.0, matches / len(principle_keywords))
    
    def _determine_source_authority(self, principle: str, law_type: TruthLaw) -> str:
        """Determine the source of authority for a principle"""
        authority_map = {
            TruthLaw.DIVINE_LAW: "Scripture and revelation",
            TruthLaw.NATURAL_LAW: "Observation and scientific method",
            TruthLaw.MORAL_LAW: "Universal moral intuition and reasoning",
            TruthLaw.SPIRITUAL_LAW: "Spiritual experience and religious teaching",
            TruthLaw.SOCIAL_LAW: "Social contract and cultural agreement",
            TruthLaw.LOGICAL_LAW: "Rational thought and philosophical reasoning"
        }
        return authority_map.get(law_type, "Unknown authority")
    
    def _find_supporting_evidence(self, principle: str, practices: List[str]) -> List[str]:
        """Find evidence that supports the principle"""
        evidence = []
        principle_lower = principle.lower()
        
        # Look for practices that align with the principle
        for practice in practices:
            if any(word in practice.lower() for word in principle_lower.split()[:3]):
                evidence.append(f"Practice: {practice}")
        
        if not evidence:
            evidence.append("Principle stated but limited evidence in practices")
        
        return evidence[:3]  # Limit to top 3
    
    def _find_contradictions(self, principle: str, practices: List[str]) -> List[str]:
        """Find contradictions to the principle"""
        contradictions = []
        
        # This would need more sophisticated analysis
        # For now, return empty list
        return contradictions
    
    def _identify_applications(self, principle: str, practices: List[str]) -> List[str]:
        """Identify practical applications of the principle"""
        applications = []
        principle_lower = principle.lower()
        
        if "love" in principle_lower:
            applications.append("Express care and concern for others")
            applications.append("Serve those in need")
        elif "truth" in principle_lower:
            applications.append("Seek accurate information")
            applications.append("Speak honestly in communications")
        elif "justice" in principle_lower:
            applications.append("Treat people fairly and equally")
            applications.append("Stand up for the innocent")
        
        return applications[:3]  # Limit to top 3
    
    def _determine_verification_method(self, law_type: TruthLaw) -> str:
        """Determine how this type of law can be verified"""
        verification_methods = {
            TruthLaw.DIVINE_LAW: "Spiritual confirmation and scriptural consistency",
            TruthLaw.NATURAL_LAW: "Scientific experiment and observation",
            TruthLaw.MORAL_LAW: "Practical outcomes and universal consensus",
            TruthLaw.SPIRITUAL_LAW: "Personal experience and spiritual fruits",
            TruthLaw.SOCIAL_LAW: "Social outcomes and collective agreement",
            TruthLaw.LOGICAL_LAW: "Logical consistency and rational analysis"
        }
        return verification_methods.get(law_type, "Multiple verification methods")
    
    def _generate_recommendation(self, system_name: str, score: float, 
                               gaps: List[str], contradictions: List[str]) -> str:
        """Generate recommendations for improving truth utilization"""
        recommendation = f"Truth System Analysis for {system_name}:\n\n"
        
        if score >= 0.8:
            recommendation += "✅ EXCELLENT: Strong truth foundation and consistent application.\n"
        elif score >= 0.6:
            recommendation += "👍 GOOD: Solid truth utilization with room for improvement.\n"
        elif score >= 0.4:
            recommendation += "⚠️ MIXED: Some truth principles present but inconsistent application.\n"
        else:
            recommendation += "❌ CONCERNING: Weak truth foundation or poor utilization.\n"
        
        recommendation += f"Truth Utilization Score: {score:.2f}/1.0\n\n"
        
        if gaps:
            recommendation += "🎯 GAPS TO ADDRESS:\n"
            for gap in gaps[:3]:
                recommendation += f"• {gap}\n"
            recommendation += "\n"
        
        if contradictions:
            recommendation += "⚠️ CONTRADICTIONS TO RESOLVE:\n"
            for contradiction in contradictions[:3]:
                recommendation += f"• {contradiction}\n"
            recommendation += "\n"
        
        recommendation += "💡 RECOMMENDATIONS:\n"
        recommendation += "• Apply Russell Nelson heart pattern: regular nourishment, exercise, avoid toxins\n"
        recommendation += "• Ensure consistency between stated principles and actual practices\n"
        recommendation += "• Seek truth from the highest sources (divine revelation, natural law, moral intuition)\n"
        recommendation += "• Regularly evaluate and adjust based on outcomes and fruits\n"
        
        return recommendation
    
    def evaluate_russell_nelson_heart_system(self) -> SystemEvaluation:
        """Example evaluation of Russell Nelson's heart analogy system"""
        return self.evaluate_system(
            system_name="Russell Nelson Heart Analogy for Spiritual Health",
            system_type=TruthSystemType.RELIGIOUS,
            system_description="Just as the heart needs regular care - proper food, exercise, rest - the spirit needs regular spiritual nourishment, exercise of faith, and avoiding spiritual toxins",
            observed_practices=[
                "Daily scripture study and prayer",
                "Regular church attendance and service",
                "Avoiding harmful influences and behaviors", 
                "Sabbath day observance for renewal",
                "Community fellowship and support",
                "Continuous learning and growth"
            ],
            claimed_principles=[
                "Spiritual health requires regular nourishment",
                "Faith must be exercised to grow stronger",
                "Spiritual toxins weaken faith",
                "Rest and renewal are essential",
                "Community connection strengthens spirituality"
            ]
        )

def demonstrate_truth_system_evaluation():
    """Demonstrate the truth system evaluator"""
    evaluator = TruthSystemEvaluator()
    
    print("🔍 TRUTH SYSTEM EVALUATOR")
    print("=" * 60)
    print("Analyzing what truth laws are in place and how they're being used\n")
    
    # Evaluate Russell Nelson heart analogy
    evaluation = evaluator.evaluate_russell_nelson_heart_system()
    
    print("📊 SYSTEM EVALUATION REPORT")
    print("-" * 40)
    print(f"System: {evaluation.system_name}")
    print(f"Type: {evaluation.system_type.value}")
    print(f"Truth Foundation: {evaluation.truth_foundation}")
    print(f"Truth Utilization Score: {evaluation.truth_utilization_score:.2f}/1.0\n")
    
    print("⚖️ ACTIVE TRUTH PRINCIPLES:")
    for principle in evaluation.active_principles[:5]:
        print(f"• {principle.name} ({principle.law_type.value})")
        print(f"  Universality: {principle.universality_score:.2f}, Consistency: {principle.consistency_score:.2f}")
    
    print(f"\n📈 CONSISTENCY ANALYSIS:")
    print(f"Overall Consistency: {evaluation.consistency_analysis['overall_consistency']:.2f}/1.0")
    
    if evaluation.gaps_identified:
        print(f"\n🎯 GAPS IDENTIFIED:")
        for gap in evaluation.gaps_identified:
            print(f"• {gap}")
    
    if evaluation.contradictions_found:
        print(f"\n⚠️ CONTRADICTIONS FOUND:")
        for contradiction in evaluation.contradictions_found:
            print(f"• {contradiction}")
    
    print(f"\n{evaluation.recommendation}")
    
    return evaluator

if __name__ == "__main__":
    demonstrate_truth_system_evaluation()
