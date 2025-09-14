
"""
Family Truth and Agenda Analysis Module
Analyzes media content for hidden agendas that build or destroy family as designed by God
Uses LDS Proclamation on the Family as the eternal truth standard
"""

from dataclasses import dataclass
from typing import Dict, List, Optional, Any
from enum import Enum
import logging

# Import existing truth foundation components
from .gospel_definitions import GospelDefinitions
from .core_truths import TruthFoundation
from .atonement_supreme import AtonementSupremeTruth

logger = logging.getLogger(__name__)

class FamilyImpact(Enum):
    BUILDS_FAMILY = 4      # Strengthens God's family design
    SUPPORTS_FAMILY = 3    # Generally supportive of family values
    NEUTRAL = 2            # No clear impact on family
    UNDERMINES_FAMILY = 1  # Subtly attacks family structure
    DESTROYS_FAMILY = 0    # Actively works to destroy family

class AgendaIntensity(Enum):
    NO_AGENDA = 0          # No detectable agenda
    SUBTLE_INFLUENCE = 1   # Gentle persuasion
    CLEAR_MESSAGING = 2    # Obvious agenda
    ACTIVE_PROPAGANDA = 3  # Aggressive agenda pushing
    SOCIAL_ENGINEERING = 4 # Systematic worldview replacement

@dataclass
class AgendaDetection:
    """Detected agenda with its characteristics"""
    agenda_type: str
    description: str
    intensity: AgendaIntensity
    evidence: List[str]
    target_audience: str
    persuasion_methods: List[str]
    desired_behavior_change: str
    worldview_promoted: str

@dataclass
class FamilyTruthEvaluation:
    """Evaluation against eternal family truths"""
    proclamation_alignment: float  # 0.0 to 1.0
    family_impact: FamilyImpact
    gender_truth_score: float
    marriage_truth_score: float
    parenting_truth_score: float
    divine_design_alignment: float
    concerning_elements: List[str]
    supporting_elements: List[str]

@dataclass
class AgendaAnalysisReport:
    """Comprehensive agenda and family truth analysis"""
    content_title: str
    detected_agendas: List[AgendaDetection]
    family_evaluation: FamilyTruthEvaluation
    overall_agenda_score: float  # 0.0 to 1.0 (higher = more agenda-driven)
    thought_modification_tactics: List[str]
    behavior_targets: List[str]
    proclamation_violations: List[str]
    family_protection_guidance: str
    discussion_questions: List[str]

class FamilyAgendaAnalyzer:
    """
    Core analyzer for detecting agendas that target family structures
    and evaluating content against the Proclamation on the Family
    """
    
    def __init__(self):
        self.gospel_definitions = GospelDefinitions()
        self.truth_foundation = TruthFoundation()
        self.atonement_supreme = AtonementSupremeTruth()
        
        # Initialize Proclamation standards
        self._initialize_proclamation_standards()
        
        # Initialize agenda detection patterns
        self._initialize_agenda_patterns()
        
        # Initialize persuasion tactics
        self._initialize_persuasion_tactics()
    
    def _initialize_proclamation_standards(self):
        """Initialize standards from the Proclamation on the Family"""
        self.proclamation_standards = {
            "marriage": {
                "divine_truth": "Marriage between a man and a woman is ordained of God",
                "violations": [
                    "same-sex marriage promoted as equal",
                    "marriage redefined beyond man-woman",
                    "traditional marriage mocked or deprecated",
                    "marriage portrayed as optional or outdated"
                ],
                "supporting_elements": [
                    "husband and wife partnership celebrated",
                    "marriage as sacred covenant",
                    "complementary roles of man and woman",
                    "eternal nature of marriage bonds"
                ]
            },
            "gender": {
                "divine_truth": "Gender is an eternal characteristic and essential to identity",
                "violations": [
                    "gender fluidity promoted",
                    "biological sex vs gender separation",
                    "transgender ideology normalized",
                    "gender confusion in children encouraged"
                ],
                "supporting_elements": [
                    "clear masculine and feminine roles",
                    "biological reality of male and female",
                    "gender-specific strengths celebrated",
                    "divine design of two genders"
                ]
            },
            "family_structure": {
                "divine_truth": "The family is central to the Creator's plan for eternal destiny",
                "violations": [
                    "alternative family structures promoted as equal",
                    "nuclear family portrayed negatively",
                    "parental authority undermined",
                    "family bonds shown as restrictive"
                ],
                "supporting_elements": [
                    "mother-father-children as ideal",
                    "family unity and loyalty",
                    "parental love and guidance",
                    "family as source of happiness"
                ]
            },
            "parenting": {
                "divine_truth": "Parents have primary responsibility for their children",
                "violations": [
                    "state/experts know better than parents",
                    "children's autonomy over parental guidance",
                    "parents portrayed as incompetent",
                    "family values vs progressive values conflict"
                ],
                "supporting_elements": [
                    "parental authority respected",
                    "mother-father complementary roles",
                    "teaching children righteousness",
                    "family traditions and values"
                ]
            },
            "procreation": {
                "divine_truth": "Sacred powers of procreation are to be employed within marriage",
                "violations": [
                    "casual sex normalized",
                    "promiscuity without consequences",
                    "sexuality separated from marriage",
                    "reproductive technologies without marriage"
                ],
                "supporting_elements": [
                    "intimacy within marriage blessed",
                    "children as heritage from the Lord",
                    "sacred nature of creating life",
                    "sexual purity promoted"
                ]
            }
        }
    
    def _initialize_agenda_patterns(self):
        """Initialize patterns for detecting specific agendas"""
        self.agenda_patterns = {
            "lgbtq_normalization": {
                "description": "Normalize LGBTQ+ relationships and identities as equal to traditional family",
                "indicators": [
                    "same-sex couples with children",
                    "transgender characters as positive role models",
                    "traditional families shown as inferior",
                    "coming out stories celebrated",
                    "pride flags and symbols prominently displayed"
                ],
                "persuasion_methods": [
                    "emotional storytelling",
                    "sympathetic character portrayal",
                    "traditional families as villains",
                    "repetitive positive exposure"
                ],
                "behavior_target": "Accept LGBTQ+ as normal and equal family structures"
            },
            "gender_ideology": {
                "description": "Promote gender fluidity and transgender ideology especially to children",
                "indicators": [
                    "gender-neutral language forced",
                    "biological sex minimized",
                    "children questioning gender identity",
                    "transition stories as heroic",
                    "traditional gender roles mocked"
                ],
                "persuasion_methods": [
                    "confusion of children",
                    "expert authority claims",
                    "compassion manipulation",
                    "social pressure tactics"
                ],
                "behavior_target": "Question traditional gender roles and biological reality"
            },
            "family_deconstruction": {
                "description": "Break down traditional family structures and parental authority",
                "indicators": [
                    "parents as obstacles to children's happiness",
                    "individual autonomy over family loyalty",
                    "traditional values as oppressive",
                    "experts/institutions as better guides than parents",
                    "family traditions as outdated"
                ],
                "persuasion_methods": [
                    "generational conflict storylines",
                    "parents portrayed as ignorant",
                    "freedom vs family responsibility",
                    "progressive values as enlightened"
                ],
                "behavior_target": "Reject parental guidance and traditional family values"
            },
            "sexual_liberation": {
                "description": "Normalize sexual activity outside marriage and casual relationships",
                "indicators": [
                    "casual sex without consequences",
                    "multiple partners as normal",
                    "marriage as restrictive",
                    "sexual exploration encouraged",
                    "promiscuity as empowering"
                ],
                "persuasion_methods": [
                    "consequences minimized",
                    "pleasure without responsibility",
                    "peer pressure modeling",
                    "liberation language"
                ],
                "behavior_target": "Engage in sexual activity outside marriage bonds"
            },
            "progressive_values": {
                "description": "Replace traditional values with progressive ideology",
                "indicators": [
                    "traditional values as backward",
                    "social justice as highest virtue",
                    "systemic oppression narratives",
                    "collective guilt for past",
                    "constant change as progress"
                ],
                "persuasion_methods": [
                    "moral superiority positioning",
                    "shame for traditional beliefs",
                    "peer pressure conformity",
                    "authority figure endorsement"
                ],
                "behavior_target": "Adopt progressive worldview and reject traditional values"
            }
        }
    
    def _initialize_persuasion_tactics(self):
        """Initialize common tactics used to modify thoughts and behaviors"""
        self.persuasion_tactics = {
            "emotional_manipulation": [
                "sympathetic character portrayal",
                "heartstring-pulling storylines",
                "victim narrative creation",
                "guilt and shame induction"
            ],
            "normalization_techniques": [
                "repetitive positive exposure",
                "casual background inclusion",
                "expert authority endorsement",
                "peer group modeling"
            ],
            "traditional_value_undermining": [
                "strawman traditional characters",
                "outdated/ignorant portrayal",
                "negative consequences for traditional choices",
                "progressive characters as enlightened"
            ],
            "authority_replacement": [
                "parents/religion as ignorant",
                "experts/institutions as wise",
                "individual feelings as ultimate authority",
                "peer opinion over family guidance"
            ],
            "consequence_minimization": [
                "no negative outcomes shown",
                "problems solved easily",
                "support systems always available",
                "realistic consequences avoided"
            ]
        }
    
    def analyze_content_agenda(self, title: str, description: str, 
                              character_analysis: Dict[str, Any],
                              plot_elements: List[str],
                              target_audience: str = "General") -> AgendaAnalysisReport:
        """
        Main analysis function for detecting agendas and family truth alignment
        """
        logger.info(f"Analyzing agenda and family truth for: {title}")
        
        # Detect agendas
        detected_agendas = self._detect_agendas(description, character_analysis, plot_elements)
        
        # Evaluate against Proclamation standards
        family_evaluation = self._evaluate_family_truth(description, character_analysis, plot_elements)
        
        # Calculate overall agenda score
        overall_agenda_score = self._calculate_agenda_score(detected_agendas)
        
        # Identify thought modification tactics
        thought_tactics = self._identify_thought_modification_tactics(
            description, character_analysis, plot_elements
        )
        
        # Identify behavior targets
        behavior_targets = self._identify_behavior_targets(detected_agendas)
        
        # Check Proclamation violations
        proclamation_violations = self._check_proclamation_violations(family_evaluation)
        
        # Generate family protection guidance
        protection_guidance = self._generate_family_protection_guidance(
            detected_agendas, family_evaluation, target_audience
        )
        
        # Generate discussion questions
        discussion_questions = self._generate_family_discussion_questions(
            title, detected_agendas, family_evaluation
        )
        
        return AgendaAnalysisReport(
            content_title=title,
            detected_agendas=detected_agendas,
            family_evaluation=family_evaluation,
            overall_agenda_score=overall_agenda_score,
            thought_modification_tactics=thought_tactics,
            behavior_targets=behavior_targets,
            proclamation_violations=proclamation_violations,
            family_protection_guidance=protection_guidance,
            discussion_questions=discussion_questions
        )
    
    def _detect_agendas(self, description: str, characters: Dict[str, Any], 
                       plot_elements: List[str]) -> List[AgendaDetection]:
        """Detect specific agendas in the content"""
        detected_agendas = []
        full_content = f"{description} {' '.join(plot_elements)} {str(characters)}"
        content_lower = full_content.lower()
        
        for agenda_type, pattern in self.agenda_patterns.items():
            evidence = []
            intensity_score = 0
            
            # Check for indicators
            for indicator in pattern["indicators"]:
                if self._indicator_present(content_lower, indicator):
                    evidence.append(f"Contains: {indicator}")
                    intensity_score += 1
            
            if evidence:  # Agenda detected
                # Determine intensity
                intensity_level = AgendaIntensity.SUBTLE_INFLUENCE
                if intensity_score >= 4:
                    intensity_level = AgendaIntensity.SOCIAL_ENGINEERING
                elif intensity_score >= 3:
                    intensity_level = AgendaIntensity.ACTIVE_PROPAGANDA
                elif intensity_score >= 2:
                    intensity_level = AgendaIntensity.CLEAR_MESSAGING
                
                # Identify persuasion methods used
                used_methods = []
                for method in pattern["persuasion_methods"]:
                    if self._persuasion_method_present(content_lower, method):
                        used_methods.append(method)
                
                detected_agendas.append(AgendaDetection(
                    agenda_type=agenda_type.replace('_', ' ').title(),
                    description=pattern["description"],
                    intensity=intensity_level,
                    evidence=evidence,
                    target_audience="Children and families",
                    persuasion_methods=used_methods,
                    desired_behavior_change=pattern["behavior_target"],
                    worldview_promoted=self._identify_worldview(agenda_type)
                ))
        
        return detected_agendas
    
    def _evaluate_family_truth(self, description: str, characters: Dict[str, Any], 
                              plot_elements: List[str]) -> FamilyTruthEvaluation:
        """Evaluate content against Proclamation on the Family standards"""
        full_content = f"{description} {' '.join(plot_elements)} {str(characters)}"
        content_lower = full_content.lower()
        
        # Evaluate each Proclamation area
        marriage_score = self._evaluate_proclamation_area(content_lower, "marriage")
        gender_score = self._evaluate_proclamation_area(content_lower, "gender")
        family_structure_score = self._evaluate_proclamation_area(content_lower, "family_structure")
        parenting_score = self._evaluate_proclamation_area(content_lower, "parenting")
        procreation_score = self._evaluate_proclamation_area(content_lower, "procreation")
        
        # Calculate overall alignment
        scores = [marriage_score, gender_score, family_structure_score, parenting_score, procreation_score]
        proclamation_alignment = sum(scores) / len(scores)
        
        # Determine family impact
        if proclamation_alignment >= 0.8:
            family_impact = FamilyImpact.BUILDS_FAMILY
        elif proclamation_alignment >= 0.6:
            family_impact = FamilyImpact.SUPPORTS_FAMILY
        elif proclamation_alignment >= 0.4:
            family_impact = FamilyImpact.NEUTRAL
        elif proclamation_alignment >= 0.2:
            family_impact = FamilyImpact.UNDERMINES_FAMILY
        else:
            family_impact = FamilyImpact.DESTROYS_FAMILY
        
        # Identify concerning and supporting elements
        concerning_elements = self._identify_concerning_elements(content_lower)
        supporting_elements = self._identify_supporting_elements(content_lower)
        
        return FamilyTruthEvaluation(
            proclamation_alignment=proclamation_alignment,
            family_impact=family_impact,
            gender_truth_score=gender_score,
            marriage_truth_score=marriage_score,
            parenting_truth_score=parenting_score,
            divine_design_alignment=(marriage_score + gender_score) / 2,
            concerning_elements=concerning_elements,
            supporting_elements=supporting_elements
        )
    
    def _evaluate_proclamation_area(self, content_lower: str, area: str) -> float:
        """Evaluate content against a specific Proclamation area"""
        standards = self.proclamation_standards[area]
        score = 0.5  # Start neutral
        
        # Check for violations
        for violation in standards["violations"]:
            if self._indicator_present(content_lower, violation):
                score -= 0.15
        
        # Check for supporting elements
        for support in standards["supporting_elements"]:
            if self._indicator_present(content_lower, support):
                score += 0.15
        
        return max(0.0, min(1.0, score))
    
    def _indicator_present(self, content_lower: str, indicator: str) -> bool:
        """Check if an indicator is present in the content"""
        # Simple keyword matching - could be enhanced with NLP
        indicator_words = indicator.lower().split()
        return any(word in content_lower for word in indicator_words[:3])
    
    def _persuasion_method_present(self, content_lower: str, method: str) -> bool:
        """Check if a persuasion method is being used"""
        method_keywords = {
            "emotional storytelling": ["emotional", "heartbreaking", "touching", "moving"],
            "sympathetic character portrayal": ["sympathetic", "likeable", "relatable", "victim"],
            "traditional families as villains": ["traditional", "conservative", "religious", "backward"],
            "expert authority claims": ["expert", "scientist", "doctor", "professional"],
            "confusion of children": ["question", "explore", "discover", "experiment"],
            "peer pressure modeling": ["everyone", "normal", "accepted", "popular"]
        }
        
        keywords = method_keywords.get(method, method.split())
        return any(keyword in content_lower for keyword in keywords)
    
    def _identify_worldview(self, agenda_type: str) -> str:
        """Identify the worldview being promoted by an agenda"""
        worldview_map = {
            "lgbtq_normalization": "Sexual and gender relativism",
            "gender_ideology": "Gender fluidity and social construction",
            "family_deconstruction": "Individualism over family authority",
            "sexual_liberation": "Sexual freedom without moral constraints",
            "progressive_values": "Progressive ideology over traditional values"
        }
        return worldview_map.get(agenda_type, "Secular humanism")
    
    def _calculate_agenda_score(self, detected_agendas: List[AgendaDetection]) -> float:
        """Calculate overall agenda score (0.0 = no agenda, 1.0 = heavy agenda)"""
        if not detected_agendas:
            return 0.0
        
        total_intensity = sum(agenda.intensity.value for agenda in detected_agendas)
        max_possible = len(detected_agendas) * 4  # Max intensity value
        
        return total_intensity / max_possible if max_possible > 0 else 0.0
    
    def _identify_thought_modification_tactics(self, description: str, 
                                             characters: Dict[str, Any], 
                                             plot_elements: List[str]) -> List[str]:
        """Identify specific tactics used to modify thoughts"""
        full_content = f"{description} {' '.join(plot_elements)} {str(characters)}"
        content_lower = full_content.lower()
        
        identified_tactics = []
        
        for tactic_category, tactics in self.persuasion_tactics.items():
            for tactic in tactics:
                if self._persuasion_method_present(content_lower, tactic):
                    identified_tactics.append(f"{tactic_category}: {tactic}")
        
        return identified_tactics
    
    def _identify_behavior_targets(self, detected_agendas: List[AgendaDetection]) -> List[str]:
        """Identify what behavior changes the content is trying to achieve"""
        return [agenda.desired_behavior_change for agenda in detected_agendas]
    
    def _check_proclamation_violations(self, family_evaluation: FamilyTruthEvaluation) -> List[str]:
        """Check for specific violations of Proclamation principles"""
        violations = []
        
        if family_evaluation.marriage_truth_score < 0.3:
            violations.append("Undermines marriage as ordained between man and woman")
        
        if family_evaluation.gender_truth_score < 0.3:
            violations.append("Contradicts eternal nature of gender identity")
        
        if family_evaluation.parenting_truth_score < 0.3:
            violations.append("Undermines parental authority and responsibility")
        
        if family_evaluation.proclamation_alignment < 0.3:
            violations.append("Generally opposes the divine plan for families")
        
        return violations
    
    def _identify_concerning_elements(self, content_lower: str) -> List[str]:
        """Identify specific concerning elements for families"""
        concerning_patterns = {
            "Same-sex parenting normalized": ["two mothers", "two fathers", "gay parents"],
            "Gender confusion promoted": ["gender identity", "questioning gender", "transitioning"],
            "Traditional marriage mocked": ["traditional marriage", "heteronormative", "old-fashioned"],
            "Parental authority undermined": ["parents don't understand", "experts know better", "your choice"],
            "Sexual content for children": ["sexual exploration", "romantic relationships", "physical intimacy"]
        }
        
        concerning = []
        for concern, keywords in concerning_patterns.items():
            if any(keyword in content_lower for keyword in keywords):
                concerning.append(concern)
        
        return concerning
    
    def _identify_supporting_elements(self, content_lower: str) -> List[str]:
        """Identify elements that support family truth"""
        supporting_patterns = {
            "Strong mother-father partnership": ["husband and wife", "mother and father", "married couple"],
            "Clear gender roles celebrated": ["masculine", "feminine", "gender differences"],
            "Family unity promoted": ["family loyalty", "family bonds", "family traditions"],
            "Parental wisdom respected": ["parents guidance", "family values", "parental love"],
            "Marriage as sacred covenant": ["sacred marriage", "eternal marriage", "covenant relationship"]
        }
        
        supporting = []
        for support, keywords in supporting_patterns.items():
            if any(keyword in content_lower for keyword in keywords):
                supporting.append(support)
        
        return supporting
    
    def _generate_family_protection_guidance(self, detected_agendas: List[AgendaDetection],
                                           family_evaluation: FamilyTruthEvaluation,
                                           target_audience: str) -> str:
        """Generate guidance for protecting families from harmful agendas"""
        guidance = f"🛡️ FAMILY PROTECTION GUIDANCE\n\n"
        
        if family_evaluation.family_impact in [FamilyImpact.DESTROYS_FAMILY, FamilyImpact.UNDERMINES_FAMILY]:
            guidance += "🚨 HIGH ALERT: This content actively works against God's plan for families.\n\n"
            guidance += "PROTECTION STRATEGIES:\n"
            guidance += "• Pre-screening recommended before family viewing\n"
            guidance += "• Prepare counteractive discussions based on Proclamation truths\n"
            guidance += "• Consider alternative content that builds family values\n"
            guidance += "• Use as teaching moment about worldly vs eternal perspectives\n\n"
        
        elif family_evaluation.family_impact == FamilyImpact.NEUTRAL:
            guidance += "⚠️ CAUTION: Mixed messages - use discernment and discussion.\n\n"
        
        else:
            guidance += "✅ FAMILY-FRIENDLY: Supports or builds family according to divine design.\n\n"
        
        if detected_agendas:
            guidance += "DETECTED AGENDAS TO DISCUSS:\n"
            for agenda in detected_agendas[:3]:
                guidance += f"• {agenda.agenda_type}: {agenda.desired_behavior_change}\n"
            guidance += "\n"
        
        guidance += "PROCLAMATION TRUTH REMINDERS:\n"
        guidance += "• Marriage between man and woman is ordained of God\n"
        guidance += "• Gender is eternal and essential to identity and purpose\n"
        guidance += "• Family is central to Creator's plan for eternal destiny\n"
        guidance += "• Parents have primary responsibility for their children\n\n"
        
        return guidance
    
    def _generate_family_discussion_questions(self, title: str,
                                            detected_agendas: List[AgendaDetection],
                                            family_evaluation: FamilyTruthEvaluation) -> List[str]:
        """Generate discussion questions for families"""
        questions = [
            f"How does '{title}' align with or contradict the Proclamation on the Family?",
            "What view of marriage and family does this content promote?",
            "How are traditional family roles portrayed compared to alternative structures?",
            "What messages about gender and identity does this content send?"
        ]
        
        if detected_agendas:
            questions.extend([
                "What agenda or worldview is this content trying to promote?",
                "How might this content influence children's understanding of family?",
                "What behavior changes is this content encouraging?"
            ])
        
        if family_evaluation.concerning_elements:
            questions.append("What concerning elements should we discuss as a family?")
        
        questions.extend([
            "How can we use eternal truths to evaluate what we watch/read?",
            "What does God's plan teach us about the purposes of family and gender?"
        ])
        
        return questions

def demonstrate_buzz_lightyear_analysis():
    """Demonstrate analysis using the Buzz Lightyear example mentioned"""
    analyzer = FamilyAgendaAnalyzer()
    
    # Simulate Buzz Lightyear content analysis
    buzz_analysis = analyzer.analyze_content_agenda(
        title="Lightyear (2022)",
        description="Space ranger Buzz Lightyear's origin story with time travel adventure",
        character_analysis={
            "buzz_lightyear": "Main character, space ranger, heroic figure",
            "hawthorne": "Female space ranger, romantic relationship with another woman",
            "hawthorne_partner": "Female partner, married to Hawthorne, raising child together",
            "supporting_characters": "Various diverse crew members and civilians"
        },
        plot_elements=[
            "space exploration mission",
            "time travel consequences", 
            "redemption arc for main character",
            "same-sex marriage and family prominently featured",
            "child raised by two female parents shown positively",
            "traditional family structures not prominently featured"
        ],
        target_audience="Children and families"
    )
    
    print("🎬 FAMILY AGENDA ANALYSIS: Lightyear (2022)")
    print("=" * 60)
    
    print(f"\n📊 OVERALL AGENDA SCORE: {buzz_analysis.overall_agenda_score:.2f}/1.0")
    print(f"👨‍👩‍👧‍👦 FAMILY IMPACT: {buzz_analysis.family_evaluation.family_impact.name}")
    print(f"📜 PROCLAMATION ALIGNMENT: {buzz_analysis.family_evaluation.proclamation_alignment:.2f}/1.0")
    
    print(f"\n🎯 DETECTED AGENDAS:")
    for agenda in buzz_analysis.detected_agendas:
        print(f"• {agenda.agenda_type} (Intensity: {agenda.intensity.name})")
        print(f"  Goal: {agenda.desired_behavior_change}")
        print(f"  Evidence: {', '.join(agenda.evidence[:2])}")
    
    print(f"\n⚠️ PROCLAMATION VIOLATIONS:")
    for violation in buzz_analysis.proclamation_violations:
        print(f"• {violation}")
    
    print(f"\n💡 CONCERNING ELEMENTS:")
    for element in buzz_analysis.family_evaluation.concerning_elements:
        print(f"• {element}")
    
    print(f"\n🛡️ FAMILY PROTECTION GUIDANCE:")
    print(buzz_analysis.family_protection_guidance)
    
    print(f"\n❓ FAMILY DISCUSSION QUESTIONS:")
    for i, question in enumerate(buzz_analysis.discussion_questions[:5], 1):
        print(f"{i}. {question}")
    
    return buzz_analysis

if __name__ == "__main__":
    demonstrate_buzz_lightyear_analysis()
