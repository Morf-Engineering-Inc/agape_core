
"""
Atonement Supreme Truth Module - The central reference point for all truth evaluation
The Atonement of Jesus Christ as the ultimate truth that grounds all other truths
"""

from dataclasses import dataclass
from typing import Dict, List, Optional, Any
from .core_truths import TruthStatement, TruthLevel
import logging

logger = logging.getLogger(__name__)

@dataclass
class AtonementAspect:
    """Specific aspect of the Atonement with its implications"""
    aspect: str
    description: str
    scripture_references: List[str]
    truth_implications: List[str]
    practical_applications: List[str]
    grounding_power: str

class AtonementSupremeTruth:
    """
    The Atonement of Jesus Christ as the supreme truth that grounds all other truths
    His death, resurrection, and suffering for sins forms the ultimate reference point
    """
    
    def __init__(self):
        self.supreme_truth = self._initialize_supreme_truth()
        self.atonement_aspects = self._initialize_atonement_aspects()
        self.grounding_principles = self._initialize_grounding_principles()
    
    def _initialize_supreme_truth(self) -> TruthStatement:
        """Initialize the supreme truth of the Atonement"""
        return TruthStatement(
            statement="The Atonement of Jesus Christ - His death, resurrection, and suffering for the sins of all mankind - is the supreme act of love and the foundation of all truth and redemption",
            level=TruthLevel.GOSPEL_TRUTH,
            authority_source="Scripture - John 3:16, 1 Corinthians 15:3-4, 2 Nephi 9:7-9, Alma 34:8-16",
            confidence=1.0,
            context="Supreme foundational reality",
            supporting_evidence=[
                "Christ's perfect life and divine nature",
                "Prophetic testimonies throughout history", 
                "Resurrection witnessed by hundreds",
                "Transformative power in human lives",
                "Universal need for redemption",
                "Infinite scope of suffering and love"
            ],
            implications=[
                "All truth derives its meaning from Christ's redemptive work",
                "Human worth is established by Christ's sacrifice for each soul",
                "Hope and redemption are possible for all through the Atonement",
                "Love is supreme because it motivated the Atonement",
                "Justice and mercy are perfectly balanced in Christ",
                "All moral evaluation must reference the Atonement"
            ]
        )
    
    def _initialize_atonement_aspects(self) -> List[AtonementAspect]:
        """Initialize the key aspects of the Atonement"""
        return [
            AtonementAspect(
                aspect="Infinite Suffering",
                description="Christ suffered for the sins, pains, and infirmities of all mankind",
                scripture_references=[
                    "Alma 7:11-12 - 'He will take upon him their infirmities'",
                    "D&C 19:16-19 - 'Which suffering caused myself... to tremble'",
                    "Isaiah 53:4-5 - 'Surely he hath borne our griefs'"
                ],
                truth_implications=[
                    "No human suffering is unknown to Christ",
                    "Every person has infinite worth to justify infinite suffering",
                    "Pain and trials have redemptive potential through Christ"
                ],
                practical_applications=[
                    "Comfort others knowing Christ understands their pain",
                    "Find meaning in suffering through Christ's example",
                    "Never dismiss someone's pain as insignificant"
                ],
                grounding_power="Establishes that all human experience has been sanctified by Christ's suffering"
            ),
            
            AtonementAspect(
                aspect="Perfect Justice Satisfied",
                description="Christ paid the full price for sin, satisfying divine justice",
                scripture_references=[
                    "Alma 42:22-25 - 'The plan of redemption could not be brought about'",
                    "Romans 3:25-26 - 'To declare his righteousness'",
                    "2 Nephi 9:26 - 'The atonement satisfieth the demands of justice'"
                ],
                truth_implications=[
                    "Moral law is absolute and must be satisfied",
                    "Justice is a divine attribute that cannot be compromised",
                    "All wrongdoing requires payment or punishment"
                ],
                practical_applications=[
                    "Uphold moral standards without compromise",
                    "Seek justice while offering mercy through Christ",
                    "Acknowledge personal accountability for choices"
                ],
                grounding_power="Validates absolute moral standards while enabling forgiveness"
            ),
            
            AtonementAspect(
                aspect="Perfect Mercy Extended",
                description="Christ's sacrifice enables infinite mercy for the repentant",
                scripture_references=[
                    "Alma 42:22-25 - 'Mercy claimeth the penitent'",
                    "1 John 1:9 - 'He is faithful and just to forgive'",
                    "Moroni 6:8 - 'As oft as they repented... they were forgiven'"
                ],
                truth_implications=[
                    "No sin is too great for Christ's atonement",
                    "Repentance is the key to accessing mercy",
                    "Divine love seeks redemption, not condemnation"
                ],
                practical_applications=[
                    "Offer forgiveness as Christ forgives",
                    "Maintain hope for redemption of all people",
                    "Focus on restoration rather than punishment"
                ],
                grounding_power="Enables hope and second chances while maintaining moral accountability"
            ),
            
            AtonementAspect(
                aspect="Victory Over Death",
                description="Christ's resurrection conquered death and enables eternal life",
                scripture_references=[
                    "1 Corinthians 15:54-57 - 'Death is swallowed up in victory'",
                    "Alma 11:42-45 - 'All shall be raised from the dead'",
                    "John 11:25 - 'I am the resurrection, and the life'"
                ],
                truth_implications=[
                    "Death is not the end of existence",
                    "Physical and spiritual resurrection are real",
                    "Eternal perspective should guide temporal decisions"
                ],
                practical_applications=[
                    "Comfort the grieving with resurrection hope",
                    "Make decisions with eternal consequences in mind",
                    "Value life knowing it continues beyond death"
                ],
                grounding_power="Provides ultimate hope and eternal perspective on all truth claims"
            ),
            
            AtonementAspect(
                aspect="Enabling Grace",
                description="Christ's grace enables us to become more than we could alone",
                scripture_references=[
                    "2 Corinthians 12:9 - 'My grace is sufficient for thee'",
                    "Ether 12:27 - 'My grace is sufficient for all men'",
                    "Moroni 10:32-33 - 'Come unto Christ... his grace is sufficient'"
                ],
                truth_implications=[
                    "Human effort alone is insufficient for perfection",
                    "Divine help is available to become better",
                    "Weakness can become strength through Christ"
                ],
                practical_applications=[
                    "Rely on divine help in moral improvement",
                    "Encourage others that change is possible",
                    "Maintain humility about personal achievements"
                ],
                grounding_power="Establishes that moral progress and truth-seeking require divine assistance"
            )
        ]
    
    def _initialize_grounding_principles(self) -> List[str]:
        """Initialize principles for how the Atonement grounds all truth"""
        return [
            "All truth claims must be evaluated in light of Christ's redemptive mission",
            "The supreme act of love (Atonement) validates love as the highest principle",
            "Christ's perfect justice and mercy provide the standard for all moral reasoning",
            "The reality of sin and redemption frames all human moral choices",
            "Eternal perspective from resurrection grounds temporal decision-making",
            "Divine grace enables truth-seeking and moral improvement beyond human capacity"
        ]
    
    def evaluate_through_atonement_lens(self, truth_claim: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Evaluate any truth claim through the lens of the Atonement"""
        evaluation = {
            "atonement_alignment_score": 0.0,
            "relevant_aspects": [],
            "grounding_analysis": "",
            "redemptive_potential": 0.0,
            "eternal_perspective": "",
            "atonement_guidance": ""
        }
        
        claim_lower = truth_claim.lower()
        
        # Evaluate alignment with each Atonement aspect
        total_score = 0.0
        relevant_count = 0
        
        for aspect in self.atonement_aspects:
            relevance = self._calculate_aspect_relevance(claim_lower, aspect)
            if relevance > 0.3:
                relevant_count += 1
                alignment = self._calculate_aspect_alignment(claim_lower, aspect)
                total_score += alignment
                evaluation["relevant_aspects"].append({
                    "aspect": aspect.aspect,
                    "relevance": relevance,
                    "alignment": alignment,
                    "grounding_power": aspect.grounding_power
                })
        
        evaluation["atonement_alignment_score"] = total_score / relevant_count if relevant_count > 0 else 0.0
        
        # Evaluate redemptive potential
        redemptive_indicators = ["heal", "restore", "forgive", "redeem", "hope", "love", "serve"]
        redemptive_score = sum(1 for indicator in redemptive_indicators if indicator in claim_lower)
        evaluation["redemptive_potential"] = min(1.0, redemptive_score / 4)
        
        # Generate analysis
        evaluation["grounding_analysis"] = self._generate_grounding_analysis(truth_claim, evaluation)
        evaluation["eternal_perspective"] = self._generate_eternal_perspective(truth_claim)
        evaluation["atonement_guidance"] = self._generate_atonement_guidance(truth_claim, evaluation)
        
        return evaluation
    
    def _calculate_aspect_relevance(self, claim_lower: str, aspect: AtonementAspect) -> float:
        """Calculate how relevant an Atonement aspect is to a truth claim"""
        relevance = 0.0
        
        # Check aspect keywords
        aspect_keywords = aspect.aspect.lower().split() + aspect.description.lower().split()[:5]
        claim_keywords = claim_lower.split()
        matching_keywords = set(aspect_keywords) & set(claim_keywords)
        relevance += len(matching_keywords) * 0.2
        
        # Check truth implications
        for implication in aspect.truth_implications:
            if any(word in claim_lower for word in implication.lower().split()[:3]):
                relevance += 0.3
        
        return min(1.0, relevance)
    
    def _calculate_aspect_alignment(self, claim_lower: str, aspect: AtonementAspect) -> float:
        """Calculate how well a claim aligns with an Atonement aspect"""
        alignment = 0.0
        
        # Check positive alignment with truth implications
        for implication in aspect.truth_implications:
            if any(word in claim_lower for word in implication.lower().split()[:4]):
                alignment += 0.25
        
        # Check practical applications alignment
        for application in aspect.practical_applications:
            if any(word in claim_lower for word in application.lower().split()[:3]):
                alignment += 0.2
        
        # Check for contradictions to Atonement principles
        anti_atonement = ["hopeless", "worthless", "unforgivable", "meaningless", "purposeless"]
        if any(indicator in claim_lower for indicator in anti_atonement):
            alignment -= 0.5
        
        return max(-1.0, min(1.0, alignment))
    
    def _generate_grounding_analysis(self, truth_claim: str, evaluation: Dict[str, Any]) -> str:
        """Generate analysis of how the Atonement grounds this truth claim"""
        analysis = f"Atonement Grounding Analysis for: '{truth_claim}'\n\n"
        
        if evaluation["atonement_alignment_score"] > 0.7:
            analysis += "✅ STRONG ATONEMENT FOUNDATION: This truth is well-grounded in Christ's redemptive work.\n"
        elif evaluation["atonement_alignment_score"] > 0.4:
            analysis += "⚠️ PARTIAL GROUNDING: Consider how this relates more fully to the Atonement.\n"
        else:
            analysis += "❌ WEAK GROUNDING: This truth claim needs clearer connection to Christ's Atonement.\n"
        
        if evaluation["relevant_aspects"]:
            analysis += "\n🎯 RELEVANT ATONEMENT ASPECTS:\n"
            for aspect in evaluation["relevant_aspects"][:3]:
                analysis += f"• {aspect['aspect']}: {aspect['grounding_power']}\n"
        
        return analysis
    
    def _generate_eternal_perspective(self, truth_claim: str) -> str:
        """Generate eternal perspective based on resurrection reality"""
        return (f"Eternal Perspective: Given that Christ's resurrection proves eternal existence, "
                f"this truth claim should be evaluated for its eternal significance and "
                f"how it helps souls progress toward eternal life and exaltation.")
    
    def _generate_atonement_guidance(self, truth_claim: str, evaluation: Dict[str, Any]) -> str:
        """Generate comprehensive guidance grounded in the Atonement"""
        guidance = f"Atonement-Grounded Guidance for: '{truth_claim}'\n\n"
        
        guidance += "🕊️ SUPREME TRUTH FOUNDATION:\n"
        guidance += "The Atonement of Jesus Christ - His death, resurrection, and infinite suffering - "
        guidance += "is the supreme act that gives meaning to all other truths.\n\n"
        
        guidance += f"📊 ATONEMENT ALIGNMENT: {evaluation['atonement_alignment_score']:.2f}/1.0\n"
        guidance += f"💝 REDEMPTIVE POTENTIAL: {evaluation['redemptive_potential']:.2f}/1.0\n\n"
        
        guidance += "🎯 KEY GROUNDING QUESTIONS:\n"
        guidance += "• How does this truth relate to Christ's redemptive mission?\n"
        guidance += "• Does this honor the infinite worth demonstrated by Christ's sacrifice?\n"
        guidance += "• Will this contribute to the redemption and exaltation of souls?\n"
        guidance += "• Does this reflect the perfect balance of justice and mercy in the Atonement?\n"
        guidance += "• How does the eternal perspective from resurrection inform this truth?\n\n"
        
        guidance += f"{evaluation['eternal_perspective']}\n"
        
        return guidance
    
    def get_supreme_truth(self) -> TruthStatement:
        """Get the supreme truth statement"""
        return self.supreme_truth
    
    def ground_all_truth_in_atonement(self, truth_system) -> str:
        """Method to demonstrate how all truth is grounded in the Atonement"""
        grounding_explanation = """
        🕊️ THE ATONEMENT AS SUPREME TRUTH FOUNDATION 🕊️
        
        The Atonement of Jesus Christ serves as the supreme reference point for all truth because:
        
        1. SUPREME ACT OF LOVE: The Atonement is the greatest demonstration of love ever made,
           validating love as the highest principle by which all truth is measured.
        
        2. PERFECT JUSTICE: Christ's satisfaction of justice establishes absolute moral standards
           while simultaneously enabling mercy and redemption.
        
        3. INFINITE WORTH DEMONSTRATED: The infinite suffering Christ endured for each soul
           establishes the infinite worth and dignity of every human being.
        
        4. VICTORY OVER DEATH: The resurrection proves eternal existence and provides ultimate
           hope, giving eternal perspective to all temporal truth claims.
        
        5. ENABLING GRACE: Christ's grace enables moral progress and truth-seeking beyond
           human capacity, making spiritual growth and enlightenment possible.
        
        6. UNIVERSAL REDEMPTION: The Atonement offers hope and second chances to all,
           establishing restoration and forgiveness as divine principles.
        
        Therefore, any truth claim, moral principle, or decision should be evaluated by asking:
        • Does this honor the infinite worth demonstrated by Christ's sacrifice?
        • Does this reflect the love that motivated the Atonement?
        • Does this contribute to the redemption and exaltation of souls?
        • Is this consistent with the perfect justice and mercy balanced in Christ?
        • Does this maintain the eternal perspective provided by the resurrection?
        
        The Atonement grounds all truth because it is the supreme manifestation of divine love,
        justice, mercy, and power - the ultimate reality that gives meaning to all existence.
        """
        return grounding_explanation

# Example usage and integration
if __name__ == "__main__":
    atonement_truth = AtonementSupremeTruth()
    
    # Test evaluation
    test_claim = "helping others is important"
    evaluation = atonement_truth.evaluate_through_atonement_lens(test_claim, {})
    print(evaluation["atonement_guidance"])
    
    # Show grounding explanation
    print(atonement_truth.ground_all_truth_in_atonement(None))
