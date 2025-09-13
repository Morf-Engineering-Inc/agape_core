
"""
Righteous Power and Influence Module - D&C 121:39-45
Core principles for how power and influence should be exercised
according to divine patterns revealed through Joseph Smith
"""

from dataclasses import dataclass
from typing import Dict, List, Optional, Any
from .core_truths import TruthStatement, TruthLevel
import logging

logger = logging.getLogger(__name__)

@dataclass
class PowerPrinciple:
    """A principle about righteous exercise of power"""
    principle: str
    scripture_reference: str
    description: str
    positive_attributes: List[str]
    warning_against: List[str]
    practical_applications: List[str]

class RighteousPowerFramework:
    """
    Framework for evaluating power and influence based on D&C 121:39-45
    Establishes divine patterns for leadership and authority
    """
    
    def __init__(self):
        self.power_principles = self._initialize_power_principles()
        self.unrighteous_dominion_warnings = self._initialize_warnings()
        self.righteous_power_attributes = self._initialize_righteous_attributes()
    
    def _initialize_power_principles(self) -> List[PowerPrinciple]:
        """Initialize core principles from D&C 121"""
        return [
            PowerPrinciple(
                principle="No Power or Influence by Virtue of Priesthood",
                scripture_reference="D&C 121:41",
                description="True authority cannot be maintained by force, coercion, or position alone",
                positive_attributes=[
                    "Persuasion",
                    "Long-suffering", 
                    "Gentleness",
                    "Meekness",
                    "Love unfeigned"
                ],
                warning_against=[
                    "Exercising control or dominion",
                    "Compulsion",
                    "Force",
                    "Using position for personal gain"
                ],
                practical_applications=[
                    "Lead by example rather than command",
                    "Invite rather than compel participation",
                    "Show genuine care for those you lead",
                    "Exercise patience when others make mistakes",
                    "Admit your own limitations and errors"
                ]
            ),
            
            PowerPrinciple(
                principle="Kindness and Pure Knowledge",
                scripture_reference="D&C 121:42",
                description="Influence comes through kindness and understanding truth",
                positive_attributes=[
                    "Kindness",
                    "Pure knowledge",
                    "Charity",
                    "Virtue",
                    "Understanding"
                ],
                warning_against=[
                    "Harsh correction",
                    "Public humiliation",
                    "Acting without understanding",
                    "Selfishness in correction"
                ],
                practical_applications=[
                    "Seek to understand before seeking to be understood",
                    "Correct in private when possible",
                    "Show genuine concern for others' wellbeing",
                    "Base decisions on truth and principle",
                    "Act with pure motives"
                ]
            ),
            
            PowerPrinciple(
                principle="Reproving with Sharpness When Moved Upon",
                scripture_reference="D&C 121:43",
                description="Sometimes firm correction is necessary, but only when prompted by the Spirit",
                positive_attributes=[
                    "Spiritual discernment",
                    "Timing",
                    "Courage to act",
                    "Immediate love after correction",
                    "Clear communication"
                ],
                warning_against=[
                    "Acting in anger",
                    "Correction without love",
                    "Personal vengeance",
                    "Continuing harshness after correction"
                ],
                practical_applications=[
                    "Pray before difficult conversations",
                    "Ensure correction serves the person's growth",
                    "Show increased love immediately after correction",
                    "Focus on behavior, not attacking character",
                    "Ensure the person knows you care about them"
                ]
            ),
            
            PowerPrinciple(
                principle="Garnish Thoughts with Virtue",
                scripture_reference="D&C 121:45",
                description="Pure thoughts and virtue create confidence before God and man",
                positive_attributes=[
                    "Virtue",
                    "Pure thoughts",
                    "Confidence",
                    "Integrity",
                    "Moral courage"
                ],
                warning_against=[
                    "Impure thoughts",
                    "Hidden sin",
                    "Moral compromise",
                    "Duplicity"
                ],
                practical_applications=[
                    "Maintain personal purity in thought and action",
                    "Be the same person in private as in public",
                    "Develop genuine moral courage",
                    "Let virtue guide all decisions",
                    "Build confidence through righteous living"
                ]
            )
        ]
    
    def _initialize_warnings(self) -> List[str]:
        """Initialize warnings about unrighteous dominion from D&C 121:39"""
        return [
            "It is the nature and disposition of almost all men to exercise unrighteous dominion",
            "When men receive authority, they immediately begin to exercise dominion",
            "Human tendency is to control others when given power",
            "Most people cannot handle authority without becoming prideful",
            "Power tends to corrupt unless constrained by righteousness"
        ]
    
    def _initialize_righteous_attributes(self) -> Dict[str, str]:
        """Initialize the divine attributes that enable righteous power"""
        return {
            "persuasion": "Convincing through reason and truth, not force",
            "long_suffering": "Patient endurance with others' weaknesses",
            "gentleness": "Tender care and consideration for others",
            "meekness": "Strength under control, teachable spirit",
            "love_unfeigned": "Genuine, sincere care for others' welfare",
            "kindness": "Consistent goodness and compassion",
            "pure_knowledge": "Understanding truth without selfish motive",
            "charity": "Pure love of Christ for all people",
            "virtue": "Moral excellence and integrity",
            "confidence": "Assurance that comes from righteousness"
        }
    
    def evaluate_power_exercise(self, leadership_scenario: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Evaluate how power is being exercised against D&C 121 principles"""
        evaluation = {
            "righteousness_score": 0.0,
            "aligned_principles": [],
            "concerning_patterns": [],
            "recommendations": [],
            "attribute_assessment": {}
        }
        
        scenario_lower = leadership_scenario.lower()
        
        # Check for righteous attributes
        righteous_indicators = 0
        total_attributes = len(self.righteous_power_attributes)
        
        for attribute, description in self.righteous_power_attributes.items():
            if self._scenario_demonstrates_attribute(scenario_lower, attribute):
                evaluation["aligned_principles"].append(f"Demonstrates {attribute}: {description}")
                righteous_indicators += 1
                evaluation["attribute_assessment"][attribute] = "PRESENT"
            else:
                evaluation["attribute_assessment"][attribute] = "NOT_EVIDENT"
        
        # Check for unrighteous dominion patterns
        dominion_patterns = [
            ("force", "using force or compulsion"),
            ("control", "exercising unrighteous control"),
            ("dominion", "seeking to dominate others"),
            ("compel", "compelling rather than inviting"),
            ("harsh", "harsh or unkind treatment"),
            ("power", "using position for personal gain")
        ]
        
        for pattern, description in dominion_patterns:
            if pattern in scenario_lower:
                evaluation["concerning_patterns"].append(f"Warning: {description}")
        
        evaluation["righteousness_score"] = righteous_indicators / total_attributes
        
        # Generate recommendations
        if evaluation["righteousness_score"] > 0.7:
            evaluation["recommendations"].append("Leadership approach aligns well with D&C 121 principles")
        elif evaluation["righteousness_score"] > 0.4:
            evaluation["recommendations"].append("Good foundation but could better embody Gospel leadership")
        else:
            evaluation["recommendations"].append("Significant alignment needed with D&C 121 principles")
        
        if evaluation["concerning_patterns"]:
            evaluation["recommendations"].append("Address patterns of unrighteous dominion")
        
        # Specific D&C 121 recommendations
        evaluation["recommendations"].extend([
            "Lead by persuasion rather than compulsion",
            "Show genuine love and concern for those you lead",
            "Maintain personal virtue and pure motives",
            "Exercise authority only when moved upon by the Spirit"
        ])
        
        return evaluation
    
    def _scenario_demonstrates_attribute(self, scenario_lower: str, attribute: str) -> bool:
        """Check if a scenario demonstrates a specific righteous attribute"""
        attribute_indicators = {
            "persuasion": ["convince", "reason", "explain", "invite", "encourage"],
            "long_suffering": ["patient", "endure", "tolerate", "wait", "forbear"],
            "gentleness": ["gentle", "tender", "soft", "kind", "careful"],
            "meekness": ["humble", "teachable", "submissive", "modest", "quiet"],
            "love_unfeigned": ["genuine", "sincere", "authentic", "real love", "truly care"],
            "kindness": ["kind", "compassionate", "considerate", "thoughtful", "caring"],
            "pure_knowledge": ["truth", "understanding", "wisdom", "insight", "discernment"],
            "charity": ["love", "serve", "sacrifice", "selfless", "others first"],
            "virtue": ["integrity", "honest", "pure", "righteous", "moral"],
            "confidence": ["confident", "assured", "certain", "bold", "courageous"]
        }
        
        indicators = attribute_indicators.get(attribute, [])
        return any(indicator in scenario_lower for indicator in indicators)
    
    def generate_leadership_guidance(self, leadership_challenge: str) -> str:
        """Generate D&C 121-based guidance for leadership challenges"""
        evaluation = self.evaluate_power_exercise(leadership_challenge, {})
        
        guidance = f"🏛️ D&C 121 LEADERSHIP GUIDANCE\n"
        guidance += f"Challenge: '{leadership_challenge}'\n\n"
        
        guidance += f"📊 RIGHTEOUSNESS ASSESSMENT: {evaluation['righteousness_score']:.2f}/1.0\n\n"
        
        if evaluation["aligned_principles"]:
            guidance += "✅ RIGHTEOUS PATTERNS IDENTIFIED:\n"
            for principle in evaluation["aligned_principles"][:3]:
                guidance += f"• {principle}\n"
            guidance += "\n"
        
        if evaluation["concerning_patterns"]:
            guidance += "⚠️ UNRIGHTEOUS DOMINION WARNINGS:\n"
            for warning in evaluation["concerning_patterns"]:
                guidance += f"• {warning}\n"
            guidance += "\n"
        
        guidance += "🎯 D&C 121 PRINCIPLES TO APPLY:\n"
        guidance += "• No power or influence can be maintained by virtue of position alone (v. 41)\n"
        guidance += "• Lead by persuasion, long-suffering, gentleness, and meekness (v. 41)\n"
        guidance += "• Show kindness and charity, let virtue garnish thy thoughts (v. 42, 45)\n"
        guidance += "• If correction is needed, let it be followed by increased love (v. 43-44)\n\n"
        
        guidance += "💡 PRACTICAL RECOMMENDATIONS:\n"
        for rec in evaluation["recommendations"][:4]:
            guidance += f"• {rec}\n"
        
        guidance += "\n📖 KEY SCRIPTURE: D&C 121:41-45\n"
        guidance += "\"No power or influence can or ought to be maintained by virtue of the priesthood, "
        guidance += "only by persuasion, by long-suffering, by gentleness and meekness, and by love unfeigned\"\n"
        
        return guidance
    
    def get_power_principle_by_verse(self, verse_number: int) -> Optional[PowerPrinciple]:
        """Get specific principle by D&C 121 verse number"""
        verse_mapping = {
            41: self.power_principles[0],  # No power by virtue of priesthood
            42: self.power_principles[1],  # Kindness and pure knowledge
            43: self.power_principles[2],  # Reproving with sharpness
            45: self.power_principles[3]   # Garnish thoughts with virtue
        }
        return verse_mapping.get(verse_number)

# Example usage
if __name__ == "__main__":
    framework = RighteousPowerFramework()
    
    # Test leadership scenario
    scenario = "A manager needs to correct an employee's poor performance but wants to do it righteously"
    guidance = framework.generate_leadership_guidance(scenario)
    print(guidance)
