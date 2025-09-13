
"""
Advice Credibility Analysis Framework
Evaluates the trustworthiness, context, and applicability of advice from experts and authority figures
"""

from dataclasses import dataclass
from typing import Dict, List, Optional, Any
from enum import Enum
import logging

# Import from core truth foundation
try:
    from truth_foundation.gospel_truth import GospelTruthEngine
    from truth_foundation.core_truths import TruthFoundation, TruthLevel
except ImportError:
    GospelTruthEngine = None
    TruthFoundation = None

logger = logging.getLogger(__name__)

class AdviceSource(Enum):
    BUSINESS_LEADER = "business_leader"
    ACADEMIC_EXPERT = "academic_expert"
    RELIGIOUS_AUTHORITY = "religious_authority"
    GOVERNMENT_OFFICIAL = "government_official"
    CELEBRITY_INFLUENCER = "celebrity_influencer"
    PEER_ADVISOR = "peer_advisor"
    AI_SYSTEM = "ai_system"
    UNKNOWN_SOURCE = "unknown_source"

class CredibilityLevel(Enum):
    HIGHLY_TRUSTWORTHY = 5    # Well-founded, consistent, proven advice
    GENERALLY_RELIABLE = 4    # Good track record with minor concerns
    MIXED_CREDIBILITY = 3     # Some good points, some questionable
    LOW_CREDIBILITY = 2       # Significant concerns or contradictions
    UNTRUSTWORTHY = 1         # Harmful, deceptive, or consistently wrong

class ContextDependency(Enum):
    UNIVERSAL = 1             # Applies in all contexts
    HIGHLY_CONTEXTUAL = 2     # Only applies in specific situations
    CONTRADICTORY = 3         # May contradict other valid advice
    TEMPORAL = 4              # Was true then, may not be now

@dataclass
class ExpertProfile:
    """Profile of advice giver for credibility assessment"""
    name: str
    source_type: AdviceSource
    expertise_domains: List[str]
    track_record: Dict[str, Any]
    potential_biases: List[str]
    incentives: List[str]  # What motivates their advice
    credibility_history: float  # 0.0 to 1.0 based on past accuracy

@dataclass
class AdviceContext:
    """Context in which advice was given"""
    time_period: str
    audience: str
    situation_specifics: str
    market_conditions: str
    constraints: List[str]
    assumptions: List[str]

@dataclass
class AdviceStatement:
    """Represents a piece of advice to be analyzed"""
    advice_text: str
    expert: ExpertProfile
    context: AdviceContext
    claimed_benefits: List[str]
    implicit_assumptions: List[str]
    contradicts_other_advice: List[str]

@dataclass
class CredibilityAnalysis:
    """Comprehensive credibility assessment"""
    advice: str
    credibility_score: float  # 0.0 to 1.0
    credibility_level: CredibilityLevel
    context_dependency: ContextDependency
    expert_assessment: Dict[str, Any]
    truth_alignment: Dict[str, Any]
    contradictions_identified: List[str]
    applicability_factors: List[str]
    warning_flags: List[str]
    recommendation: str
    gospel_evaluation: Dict[str, Any]

class AdviceCredibilityAnalyzer:
    """
    Core engine for analyzing the credibility and applicability of expert advice
    """
    
    def __init__(self):
        self.gospel_engine = GospelTruthEngine() if GospelTruthEngine else None
        self.truth_foundation = TruthFoundation() if TruthFoundation else None
        
        # Initialize credibility factors
        self._initialize_credibility_factors()
        
        # Initialize warning patterns
        self._initialize_warning_patterns()
        
        # Initialize context patterns
        self._initialize_context_patterns()
    
    def _initialize_credibility_factors(self):
        """Initialize factors that affect advice credibility"""
        self.credibility_factors = {
            "track_record": {
                "weight": 0.3,
                "indicators": [
                    "proven success in domain",
                    "consistent performance",
                    "peer recognition",
                    "measurable outcomes"
                ]
            },
            "transparency": {
                "weight": 0.2,
                "indicators": [
                    "acknowledges limitations",
                    "shows reasoning process",
                    "admits uncertainty",
                    "cites sources"
                ]
            },
            "consistency": {
                "weight": 0.2,
                "indicators": [
                    "advice aligns with principles",
                    "doesn't contradict own statements",
                    "coherent worldview",
                    "logical reasoning"
                ]
            },
            "incentive_alignment": {
                "weight": 0.15,
                "indicators": [
                    "no obvious conflicts of interest",
                    "aligned with advisee's interests",
                    "not self-serving",
                    "genuine care for outcomes"
                ]
            },
            "domain_expertise": {
                "weight": 0.15,
                "indicators": [
                    "deep knowledge in relevant area",
                    "current with developments",
                    "understands nuances",
                    "recognizes edge cases"
                ]
            }
        }
    
    def _initialize_warning_patterns(self):
        """Initialize patterns that indicate potentially problematic advice"""
        self.warning_patterns = {
            "absolute_claims": [
                "always works",
                "never fails",
                "guaranteed success",
                "100% effective",
                "works for everyone"
            ],
            "urgency_manipulation": [
                "act now or miss out",
                "limited time only",
                "everyone else is doing it",
                "you'll regret not doing this"
            ],
            "oversimplification": [
                "just do this one thing",
                "simple secret to success",
                "easy solution",
                "no downsides",
                "risk-free"
            ],
            "appeal_to_authority": [
                "trust me, I'm successful",
                "because I said so",
                "my experience proves",
                "I'm the expert here"
            ],
            "contradiction_indicators": [
                "but also",
                "however sometimes",
                "except when",
                "unless you",
                "it depends"
            ]
        }
    
    def _initialize_context_patterns(self):
        """Initialize patterns for understanding context dependency"""
        self.context_patterns = {
            "startup_advice": {
                "highly_contextual": [
                    "stage-dependent strategy",
                    "market-specific approach",
                    "resource-dependent decision",
                    "timing-sensitive action"
                ],
                "universal_principles": [
                    "customer focus",
                    "financial discipline",
                    "team building",
                    "product quality"
                ],
                "phase_dependent_synthesis": {
                    "discovery_phase": ["don't scale", "get close to users", "manual processes"],
                    "interpretation_phase": ["design insight", "user intuition", "synthesis"],
                    "scaling_phase": ["infrastructure", "systems", "operations", "mass market"]
                }
            },
            "business_strategy": {
                "temporal_factors": [
                    "market cycles",
                    "technology evolution",
                    "regulatory changes",
                    "competitive landscape"
                ]
            },
            "synthesis_indicators": [
                "phase by phase",
                "different stages",
                "sequential approach",
                "first... then...",
                "over time",
                "as you grow"
            ]
        }
    
    def analyze_advice(self, advice_statement: AdviceStatement) -> CredibilityAnalysis:
        """
        Main analysis function that evaluates advice credibility
        """
        logger.info(f"Analyzing advice: {advice_statement.advice_text[:100]}...")
        
        # Analyze expert credibility
        expert_assessment = self._assess_expert_credibility(advice_statement.expert)
        
        # Check for warning flags
        warning_flags = self._identify_warning_flags(advice_statement)
        
        # Analyze context dependency
        context_dependency = self._analyze_context_dependency(advice_statement)
        
        # Check for contradictions
        contradictions = self._identify_contradictions(advice_statement)
        
        # Evaluate against truth foundation
        truth_alignment = self._evaluate_truth_alignment(advice_statement)
        
        # Calculate overall credibility score
        credibility_score = self._calculate_credibility_score(
            expert_assessment, warning_flags, truth_alignment, contradictions
        )
        
        # Determine credibility level
        credibility_level = self._determine_credibility_level(credibility_score)
        
        # Generate applicability factors
        applicability_factors = self._generate_applicability_factors(advice_statement)
        
        # Get Gospel evaluation if available
        gospel_evaluation = {}
        if self.gospel_engine:
            gospel_evaluation = self.gospel_engine.evaluate_against_gospel(
                advice_statement.advice_text,
                {"context": advice_statement.context.__dict__}
            )
        
        # Generate recommendation
        recommendation = self._generate_recommendation(
            credibility_level, context_dependency, warning_flags, advice_statement
        )
        
        return CredibilityAnalysis(
            advice=advice_statement.advice_text,
            credibility_score=credibility_score,
            credibility_level=credibility_level,
            context_dependency=context_dependency,
            expert_assessment=expert_assessment,
            truth_alignment=truth_alignment,
            contradictions_identified=contradictions,
            applicability_factors=applicability_factors,
            warning_flags=warning_flags,
            recommendation=recommendation,
            gospel_evaluation=gospel_evaluation
        )
    
    def _assess_expert_credibility(self, expert: ExpertProfile) -> Dict[str, Any]:
        """Assess the credibility of the advice giver"""
        assessment = {
            "source_type": expert.source_type.value,
            "expertise_match": 0.0,
            "track_record_score": expert.credibility_history,
            "bias_concerns": expert.potential_biases,
            "incentive_alignment": 0.0,
            "overall_expert_score": 0.0
        }
        
        # Calculate expertise match (simplified)
        if expert.expertise_domains:
            assessment["expertise_match"] = min(1.0, len(expert.expertise_domains) * 0.3)
        
        # Assess incentive alignment
        problematic_incentives = ["financial gain", "self-promotion", "book sales", "consulting fees"]
        alignment_score = 1.0
        for incentive in expert.incentives:
            if any(prob in incentive.lower() for prob in problematic_incentives):
                alignment_score -= 0.2
        assessment["incentive_alignment"] = max(0.0, alignment_score)
        
        # Calculate overall expert score
        assessment["overall_expert_score"] = (
            expert.credibility_history * 0.4 +
            assessment["expertise_match"] * 0.3 +
            assessment["incentive_alignment"] * 0.3
        )
        
        return assessment
    
    def _identify_warning_flags(self, advice_statement: AdviceStatement) -> List[str]:
        """Identify warning flags in the advice"""
        flags = []
        advice_lower = advice_statement.advice_text.lower()
        
        # Check for warning patterns
        for warning_type, patterns in self.warning_patterns.items():
            for pattern in patterns:
                if pattern in advice_lower:
                    flags.append(f"{warning_type.replace('_', ' ').title()}: '{pattern}'")
        
        # Check for vague language
        vague_terms = ["probably", "might work", "could help", "maybe try"]
        if any(term in advice_lower for term in vague_terms):
            flags.append("Vague language: Lacks specificity or confidence")
        
        # Check for missing context
        if not advice_statement.context.constraints:
            flags.append("Missing constraints: No mention of limitations or conditions")
        
        return flags
    
    def _analyze_context_dependency(self, advice_statement: AdviceStatement) -> ContextDependency:
        """Analyze how context-dependent the advice is"""
        advice_lower = advice_statement.advice_text.lower()
        
        # Check for universal principles
        universal_indicators = ["always", "fundamental", "principle", "core truth", "universal"]
        if any(indicator in advice_lower for indicator in universal_indicators):
            return ContextDependency.UNIVERSAL
        
        # Check for highly contextual language
        contextual_indicators = ["depends", "situation", "context", "specific", "sometimes", "when"]
        contextual_count = sum(1 for indicator in contextual_indicators if indicator in advice_lower)
        
        if contextual_count >= 3:
            return ContextDependency.HIGHLY_CONTEXTUAL
        elif contextual_count >= 1:
            return ContextDependency.CONTRADICTORY
        
        # Check for temporal indicators
        temporal_indicators = ["now", "currently", "today", "this era", "right now"]
        if any(indicator in advice_lower for indicator in temporal_indicators):
            return ContextDependency.TEMPORAL
        
        return ContextDependency.HIGHLY_CONTEXTUAL  # Default for most business advice
    
    def _identify_contradictions(self, advice_statement: AdviceStatement) -> List[str]:
        """Identify contradictions with other known advice or principles"""
        contradictions = []
        
        # Use provided contradictions
        contradictions.extend(advice_statement.contradicts_other_advice)
        
        # Check for internal contradictions
        advice_lower = advice_statement.advice_text.lower()
        contradiction_pairs = [
            ("scale", "don't scale"),
            ("move fast", "be careful"),
            ("focus", "diversify"),
            ("save money", "spend money"),
            ("plan ahead", "be flexible")
        ]
        
        for concept1, concept2 in contradiction_pairs:
            if concept1 in advice_lower and concept2 in advice_lower:
                contradictions.append(f"Internal contradiction: mentions both '{concept1}' and '{concept2}'")
        
        return contradictions
    
    def _evaluate_truth_alignment(self, advice_statement: AdviceStatement) -> Dict[str, Any]:
        """Evaluate how well advice aligns with foundational truths"""
        alignment = {"score": 0.5, "concerns": [], "supports": []}
        
        if self.truth_foundation:
            context = {
                "advice_context": advice_statement.context.__dict__,
                "expert_info": advice_statement.expert.__dict__
            }
            alignment["score"] = self.truth_foundation.evaluate_truth_claim(
                advice_statement.advice_text, 
                context
            )
        
        # Check alignment with moral principles
        advice_lower = advice_statement.advice_text.lower()
        
        # Positive moral indicators
        positive_indicators = ["honest", "integrity", "serve others", "help", "benefit", "ethical"]
        for indicator in positive_indicators:
            if indicator in advice_lower:
                alignment["supports"].append(f"Promotes {indicator}")
        
        # Concerning indicators
        concerning_indicators = ["deceive", "exploit", "manipulate", "harm", "cheat"]
        for indicator in concerning_indicators:
            if indicator in advice_lower:
                alignment["concerns"].append(f"May promote {indicator}")
        
        return alignment
    
    def _calculate_credibility_score(
        self, 
        expert_assessment: Dict[str, Any], 
        warning_flags: List[str], 
        truth_alignment: Dict[str, Any],
        contradictions: List[str]
    ) -> float:
        """Calculate overall credibility score"""
        base_score = 0.5  # Neutral starting point
        
        # Expert credibility contribution (40%)
        base_score += expert_assessment["overall_expert_score"] * 0.4
        
        # Truth alignment contribution (30%)
        base_score += truth_alignment["score"] * 0.3
        
        # Warning flags penalty (up to -30%)
        warning_penalty = min(0.3, len(warning_flags) * 0.1)
        base_score -= warning_penalty
        
        # Contradictions penalty (up to -20%)
        contradiction_penalty = min(0.2, len(contradictions) * 0.05)
        base_score -= contradiction_penalty
        
        # Concerns from truth alignment
        concern_penalty = min(0.1, len(truth_alignment.get("concerns", [])) * 0.05)
        base_score -= concern_penalty
        
        return max(0.0, min(1.0, base_score))
    
    def _determine_credibility_level(self, credibility_score: float) -> CredibilityLevel:
        """Determine credibility level based on score"""
        if credibility_score >= 0.8:
            return CredibilityLevel.HIGHLY_TRUSTWORTHY
        elif credibility_score >= 0.65:
            return CredibilityLevel.GENERALLY_RELIABLE
        elif credibility_score >= 0.45:
            return CredibilityLevel.MIXED_CREDIBILITY
        elif credibility_score >= 0.25:
            return CredibilityLevel.LOW_CREDIBILITY
        else:
            return CredibilityLevel.UNTRUSTWORTHY
    
    def _generate_applicability_factors(self, advice_statement: AdviceStatement) -> List[str]:
        """Generate factors that affect when/how advice applies"""
        factors = []
        
        # Context-specific factors
        if advice_statement.context.situation_specifics:
            factors.append(f"Situation: {advice_statement.context.situation_specifics}")
        
        if advice_statement.context.market_conditions:
            factors.append(f"Market conditions: {advice_statement.context.market_conditions}")
        
        # Resource requirements
        if advice_statement.context.constraints:
            factors.extend([f"Constraint: {constraint}" for constraint in advice_statement.context.constraints])
        
        # Assumptions
        if advice_statement.implicit_assumptions:
            factors.extend([f"Assumes: {assumption}" for assumption in advice_statement.implicit_assumptions])
        
        # Temporal factors
        factors.append(f"Time period: {advice_statement.context.time_period}")
        
        return factors
    
    def _generate_recommendation(
        self,
        credibility_level: CredibilityLevel,
        context_dependency: ContextDependency,
        warning_flags: List[str],
        advice_statement: AdviceStatement
    ) -> str:
        """Generate overall recommendation for the advice"""
        
        recommendations = {
            CredibilityLevel.HIGHLY_TRUSTWORTHY: "✅ HIGHLY RECOMMENDED: This advice appears well-founded and trustworthy.",
            CredibilityLevel.GENERALLY_RELIABLE: "👍 GENERALLY GOOD: This advice seems reliable with minor concerns.",
            CredibilityLevel.MIXED_CREDIBILITY: "⚠️ USE CAUTION: This advice has both strengths and significant concerns.",
            CredibilityLevel.LOW_CREDIBILITY: "⚡ BE SKEPTICAL: This advice has major credibility issues.",
            CredibilityLevel.UNTRUSTWORTHY: "🚨 AVOID: This advice appears untrustworthy or potentially harmful."
        }
        
        base_recommendation = recommendations[credibility_level]
        
        # Add context dependency guidance
        if context_dependency == ContextDependency.HIGHLY_CONTEXTUAL:
            base_recommendation += " IMPORTANT: This advice is highly context-specific - ensure your situation matches."
        elif context_dependency == ContextDependency.CONTRADICTORY:
            base_recommendation += " NOTE: This advice may contradict other valid advice - consider the specific context."
        elif context_dependency == ContextDependency.TEMPORAL:
            base_recommendation += " TIMING: This advice may be time-sensitive and might not apply in different eras."
        
        # Add warning flag guidance
        if len(warning_flags) > 2:
            base_recommendation += f" WARNING: Multiple red flags detected ({len(warning_flags)} issues identified)."
        
        return base_recommendation

def analyze_jobs_yc_scaling_synthesis():
    """Analyze how Jobs, YC, and scaling advice work together rather than contradict"""
    
    # This example demonstrates CONTEXT-DEPENDENT COMPATIBILITY
    # Three pieces of advice that seem contradictory but actually complement each other
    
    analyzer = AdviceCredibilityAnalyzer()
    
    print("🔍 SYNTHESIS ANALYSIS: Jobs + YC + Scaling Concerns")
    print("=" * 70)
    print("This demonstrates how seemingly contradictory advice can be COMPLEMENTARY")
    print("when understood in proper context and sequence.\n")
    
    # Analyze each piece in context
    contexts = [
        {
            "phase": "Early exploration",
            "advice": "Do things that don't scale - get close to users, learn directly",
            "purpose": "Discovery and validation",
            "timeline": "Weeks to months"
        },
        {
            "phase": "Product definition", 
            "advice": "Customers don't know what they want until you show them",
            "purpose": "Interpretation and design insight",
            "timeline": "Months of iteration"
        },
        {
            "phase": "Growth execution",
            "advice": "Startups fail when they can't scale - build infrastructure",
            "purpose": "Mass market delivery",
            "timeline": "Years of execution"
        }
    ]
    
    print("📋 PHASE-BY-PHASE ANALYSIS:")
    for i, context in enumerate(contexts, 1):
        print(f"\n{i}. {context['phase'].upper()}")
        print(f"   💡 Advice: {context['advice']}")
        print(f"   🎯 Purpose: {context['purpose']}")
        print(f"   ⏱️  Timeline: {context['timeline']}")
    
    print(f"\n🔗 SYNTHESIS INSIGHT:")
    print("These aren't contradictory - they're SEQUENTIAL MUSCLES:")
    print("• DISCOVER (don't scale) → INTERPRET (Jobs insight) → SCALE (infrastructure)")
    print("• Each phase requires different approaches and mindsets")
    print("• The 'contradiction' dissolves when you understand WHEN each applies")
    
    print(f"\n⚖️ CREDIBILITY IMPACT:")
    print("✅ HIGH: When advice acknowledges phase-dependency")
    print("⚠️  MEDIUM: When advice claims universal application") 
    print("❌ LOW: When advice ignores context or timing")
    
    print(f"\n💡 KEY LESSON FOR AI DECISION-MAKING:")
    print("Context and timing are CRUCIAL for evaluating advice credibility.")
    print("What appears contradictory may actually be complementary when")
    print("properly sequenced and applied to appropriate situations.")
    
    return {
        "synthesis_type": "phase_dependent_compatibility",
        "credibility_insight": "Context dissolves apparent contradictions",
        "practical_application": "Always ask WHEN and WHERE advice applies"
    }

def analyze_sam_altman_example():
    """Analyze the Sam Altman scaling advice example"""
    
    # Create expert profile for Sam Altman
    sam_altman = ExpertProfile(
        name="Sam Altman",
        source_type=AdviceSource.BUSINESS_LEADER,
        expertise_domains=["startups", "technology", "venture capital", "AI"],
        track_record={
            "successes": ["Y Combinator leadership", "OpenAI", "multiple successful investments"],
            "experience": "15+ years in startup ecosystem"
        },
        potential_biases=["Silicon Valley perspective", "high-growth focus", "tech industry bias"],
        incentives=["Y Combinator success", "startup ecosystem growth", "thought leadership"],
        credibility_history=0.8  # Generally high credibility
    )
    
    # Create context for the advice
    context = AdviceContext(
        time_period="Early 2010s startup era",
        audience="Early-stage startup founders",
        situation_specifics="Pre-product-market-fit startups",
        market_conditions="High VC funding availability, tech boom",
        constraints=["Limited resources", "Need to validate market"],
        assumptions=["Fast iteration is possible", "Manual processes can be automated later", "Product-market fit is priority"]
    )
    
    # Create the advice statement
    advice = AdviceStatement(
        advice_text="Build things that don't scale - focus on doing things manually and personally at first, worry about scaling later",
        expert=sam_altman,
        context=context,
        claimed_benefits=["Faster validation", "Better customer understanding", "Resource efficiency"],
        implicit_assumptions=["You will eventually need to scale", "Manual approach is temporary", "Learning is more important than efficiency initially"],
        contradicts_other_advice=["Startups fail because they cannot scale", "Build scalable systems from day one", "Focus on operational efficiency"]
    )
    
    # Analyze the advice
    analyzer = AdviceCredibilityAnalyzer()
    analysis = analyzer.analyze_advice(advice)
    
    print("🔍 ADVICE CREDIBILITY ANALYSIS")
    print("=" * 60)
    print(f"📝 ADVICE: {analysis.advice}")
    print(f"🎯 CREDIBILITY LEVEL: {analysis.credibility_level.name}")
    print(f"📊 CREDIBILITY SCORE: {analysis.credibility_score:.2f}/1.0")
    print(f"🌍 CONTEXT DEPENDENCY: {analysis.context_dependency.name}")
    
    print(f"\n👤 EXPERT ASSESSMENT:")
    for key, value in analysis.expert_assessment.items():
        if isinstance(value, float):
            print(f"• {key.replace('_', ' ').title()}: {value:.2f}")
        else:
            print(f"• {key.replace('_', ' ').title()}: {value}")
    
    print(f"\n⚠️ WARNING FLAGS ({len(analysis.warning_flags)}):")
    for flag in analysis.warning_flags:
        print(f"• {flag}")
    
    print(f"\n🔄 CONTRADICTIONS IDENTIFIED:")
    for contradiction in analysis.contradictions_identified:
        print(f"• {contradiction}")
    
    print(f"\n📋 APPLICABILITY FACTORS:")
    for factor in analysis.applicability_factors:
        print(f"• {factor}")
    
    print(f"\n💡 RECOMMENDATION:")
    print(analysis.recommendation)
    
    print(f"\n🎯 KEY INSIGHT:")
    print("This advice is HIGHLY CONTEXTUAL - it applies specifically to early-stage startups")
    print("seeking product-market fit, but contradicts advice for growth-stage companies that")
    print("need operational efficiency and scalability. The contradiction exists because")
    print("different advice applies at different stages of company development.")
    
    return analysis

if __name__ == "__main__":
    # First show the synthesis analysis
    print("🎯 PART 1: SYNTHESIS ANALYSIS")
    analyze_jobs_yc_scaling_synthesis()
    
    print("\n" + "=" * 70)
    print("🎯 PART 2: DETAILED CREDIBILITY ANALYSIS")
    analyze_sam_altman_example()
