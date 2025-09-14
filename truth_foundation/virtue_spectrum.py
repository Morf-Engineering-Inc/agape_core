
"""
Virtue-Vice Spectrum Module
Analyzes actions and attitudes along the spectrum of virtue and vice
with temperance (moderation) as the key to righteous balance
"""

from dataclasses import dataclass
from typing import Dict, List, Optional, Any
from enum import Enum
import logging
from .core_truths import TruthStatement, TruthLevel
from .gospel_definitions import GospelDefinitions

logger = logging.getLogger(__name__)

class VirtueCategory(Enum):
    """Categories of virtue based on classical and Gospel traditions"""
    CARDINAL = "cardinal"       # Prudence, Justice, Fortitude, Temperance
    THEOLOGICAL = "theological" # Faith, Hope, Charity
    MORAL = "moral"            # Gospel-based virtues
    PRACTICAL = "practical"    # Daily life applications

class SpectrumPosition(Enum):
    """Position on the virtue-vice spectrum"""
    EXTREME_VICE = 1      # Far from virtue, destructive
    VICE = 2              # Vice, but not extreme
    DEFICIENCY = 3        # Lacking virtue, but not vice
    TEMPERANCE = 4        # Golden mean, balanced virtue
    EXCESS = 5            # Too much of good thing
    EXTREME_EXCESS = 6    # Virtue corrupted by extremism

@dataclass
class VirtueSpectrum:
    """Represents a virtue with its corresponding vices and temperate middle"""
    virtue_name: str
    category: VirtueCategory
    description: str
    deficiency_vice: str      # Too little of this virtue
    excess_vice: str          # Too much of this virtue
    temperate_middle: str     # The balanced expression
    scripture_references: List[str]
    practical_examples: Dict[SpectrumPosition, List[str]]
    gospel_connection: str

@dataclass
class SpectrumAnalysis:
    """Analysis of where an action/attitude falls on virtue-vice spectrum"""
    analyzed_item: str
    virtue_spectrum: VirtueSpectrum
    position: SpectrumPosition
    position_score: float  # 1.0 (extreme vice) to 6.0 (extreme excess)
    temperance_distance: float  # How far from ideal temperance
    recommendations: List[str]
    gospel_guidance: str

class VirtueSpectrumAnalyzer:
    """
    Analyzes actions, attitudes, and choices along virtue-vice spectrums
    with emphasis on temperance as the Gospel ideal
    """
    
    def __init__(self):
        self.gospel_definitions = GospelDefinitions()
        self.virtue_spectrums = self._initialize_virtue_spectrums()
        
    def _initialize_virtue_spectrums(self) -> Dict[str, VirtueSpectrum]:
        """Initialize virtue spectrums based on classical and Gospel wisdom"""
        return {
            "courage": VirtueSpectrum(
                virtue_name="Courage",
                category=VirtueCategory.CARDINAL,
                description="Righteous bravery in facing challenges and standing for truth",
                deficiency_vice="Cowardice",
                excess_vice="Recklessness",
                temperate_middle="Prudent courage - brave when necessary, cautious when wise",
                scripture_references=[
                    "Joshua 1:9 - Be strong and of good courage",
                    "1 Corinthians 16:13 - Be strong, be courageous",
                    "D&C 27:15 - Take the sword of the Spirit"
                ],
                practical_examples={
                    SpectrumPosition.EXTREME_VICE: ["Paralyzing fear", "Abandoning principles under pressure"],
                    SpectrumPosition.VICE: ["Avoiding necessary confrontations", "Remaining silent when truth is attacked"],
                    SpectrumPosition.DEFICIENCY: ["Hesitating to speak up", "Avoiding reasonable risks"],
                    SpectrumPosition.TEMPERANCE: ["Standing for truth with wisdom", "Calculated courage for righteous causes"],
                    SpectrumPosition.EXCESS: ["Unnecessary confrontation", "Taking foolish risks"],
                    SpectrumPosition.EXTREME_EXCESS: ["Reckless endangerment", "Fighting every battle regardless of wisdom"]
                },
                gospel_connection="Christ showed perfect courage - bold in teaching truth, yet wise in timing"
            ),
            
            "generosity": VirtueSpectrum(
                virtue_name="Generosity",
                category=VirtueCategory.MORAL,
                description="Giving freely of time, talents, and resources to bless others",
                deficiency_vice="Selfishness/Greed",
                excess_vice="Enabling/Imprudent giving",
                temperate_middle="Wise generosity - giving appropriately to truly help others",
                scripture_references=[
                    "2 Corinthians 9:7 - God loves a cheerful giver",
                    "D&C 104:18 - For the earth is full, and there is enough and to spare",
                    "Luke 6:38 - Give, and it shall be given unto you"
                ],
                practical_examples={
                    SpectrumPosition.EXTREME_VICE: ["Hoarding when others suffer", "Stealing from others"],
                    SpectrumPosition.VICE: ["Refusing to help when able", "Excessive materialism"],
                    SpectrumPosition.DEFICIENCY: ["Rarely sharing resources", "Hesitant to serve"],
                    SpectrumPosition.TEMPERANCE: ["Giving wisely according to need", "Generous service with wisdom"],
                    SpectrumPosition.EXCESS: ["Giving beyond family needs", "Enabling dependency"],
                    SpectrumPosition.EXTREME_EXCESS: ["Giving away needed family resources", "Creating harmful dependency"]
                },
                gospel_connection="Christ gave His life - ultimate generosity balanced with wisdom about timing"
            ),
            
            "humility": VirtueSpectrum(
                virtue_name="Humility",
                category=VirtueCategory.THEOLOGICAL,
                description="Teachable spirit that recognizes dependence on God and others",
                deficiency_vice="Pride",
                excess_vice="Self-deprecation/False humility",
                temperate_middle="True humility - confidence in God's grace with recognition of personal limitations",
                scripture_references=[
                    "Mosiah 3:19 - Humble as a little child",
                    "Ether 12:27 - If men come unto me I will show them their weakness",
                    "Matthew 5:3 - Blessed are the poor in spirit"
                ],
                practical_examples={
                    SpectrumPosition.EXTREME_VICE: ["Narcissistic arrogance", "Refusing to acknowledge mistakes"],
                    SpectrumPosition.VICE: ["Unwillingness to learn", "Looking down on others"],
                    SpectrumPosition.DEFICIENCY: ["Occasional pride", "Difficulty accepting correction"],
                    SpectrumPosition.TEMPERANCE: ["Teachable confidence", "Acknowledging strengths and weaknesses honestly"],
                    SpectrumPosition.EXCESS: ["Self-hatred", "Refusing to acknowledge gifts"],
                    SpectrumPosition.EXTREME_EXCESS: ["Paralyzing self-doubt", "False humility as manipulation"]
                },
                gospel_connection="Christ was perfectly humble - confident in His mission yet submissive to the Father"
            ),
            
            "justice": VirtueSpectrum(
                virtue_name="Justice",
                category=VirtueCategory.CARDINAL,
                description="Giving each person what they deserve while showing mercy",
                deficiency_vice="Injustice/Favoritism",
                excess_vice="Mercilessness/Legalism",
                temperate_middle="Justice tempered with mercy - fair consequences with compassionate application",
                scripture_references=[
                    "Micah 6:8 - Do justly, love mercy, walk humbly",
                    "Alma 42:15 - Mercy cannot rob justice",
                    "D&C 88:40 - Intelligence cleaveth unto intelligence"
                ],
                practical_examples={
                    SpectrumPosition.EXTREME_VICE: ["Corrupt favoritism", "Punishing the innocent"],
                    SpectrumPosition.VICE: ["Showing partiality", "Ignoring clear wrongdoing"],
                    SpectrumPosition.DEFICIENCY: ["Inconsistent standards", "Avoiding difficult decisions"],
                    SpectrumPosition.TEMPERANCE: ["Fair consequences with mercy", "Equal treatment with compassion"],
                    SpectrumPosition.EXCESS: ["Harsh inflexibility", "Punishment without mercy"],
                    SpectrumPosition.EXTREME_EXCESS: ["Cruel retribution", "Justice without love"]
                },
                gospel_connection="God's justice perfectly balanced with mercy through Christ's Atonement"
            ),
            
            "temperance": VirtueSpectrum(
                virtue_name="Temperance",
                category=VirtueCategory.CARDINAL,
                description="Self-control and moderation in all things",
                deficiency_vice="Indulgence/Lack of self-control",
                excess_vice="Extreme asceticism/Over-restriction",
                temperate_middle="Balanced self-control - enjoying good things in moderation",
                scripture_references=[
                    "1 Corinthians 9:25 - Every man that striveth for mastery is temperate in all things",
                    "Galatians 5:22-23 - Fruit of the Spirit includes temperance",
                    "D&C 89 - Word of Wisdom principles"
                ],
                practical_examples={
                    SpectrumPosition.EXTREME_VICE: ["Addiction and compulsion", "Complete lack of self-control"],
                    SpectrumPosition.VICE: ["Regular overindulgence", "Impulse-driven decisions"],
                    SpectrumPosition.DEFICIENCY: ["Occasional excess", "Weak self-discipline"],
                    SpectrumPosition.TEMPERANCE: ["Moderate enjoyment", "Self-control with balance"],
                    SpectrumPosition.EXCESS: ["Extreme restriction", "Refusing all pleasures"],
                    SpectrumPosition.EXTREME_EXCESS: ["Harmful asceticism", "Denying necessary goods"]
                ],
                gospel_connection="Christ fasted but also feasted - perfect balance in all things"
            )
        }
    
    def analyze_virtue_spectrum(self, action_or_attitude: str, context: Dict[str, Any] = None) -> List[SpectrumAnalysis]:
        """Analyze an action or attitude against relevant virtue spectrums"""
        if context is None:
            context = {}
            
        analyses = []
        action_lower = action_or_attitude.lower()
        
        # Find relevant virtue spectrums
        relevant_spectrums = []
        for spectrum in self.virtue_spectrums.values():
            if self._is_spectrum_relevant(action_lower, spectrum):
                relevant_spectrums.append(spectrum)
        
        # If no specific match, analyze against temperance as default
        if not relevant_spectrums:
            relevant_spectrums = [self.virtue_spectrums["temperance"]]
        
        for spectrum in relevant_spectrums:
            analysis = self._analyze_against_spectrum(action_or_attitude, spectrum, context)
            analyses.append(analysis)
        
        return analyses
    
    def _is_spectrum_relevant(self, action_lower: str, spectrum: VirtueSpectrum) -> bool:
        """Determine if a virtue spectrum is relevant to the action"""
        # Check virtue name
        if spectrum.virtue_name.lower() in action_lower:
            return True
        
        # Check vice names
        if spectrum.deficiency_vice.lower() in action_lower or spectrum.excess_vice.lower() in action_lower:
            return True
        
        # Check practical examples
        for examples_list in spectrum.practical_examples.values():
            for example in examples_list:
                if any(word in action_lower for word in example.lower().split()[:3]):
                    return True
        
        return False
    
    def _analyze_against_spectrum(self, action: str, spectrum: VirtueSpectrum, context: Dict[str, Any]) -> SpectrumAnalysis:
        """Analyze specific action against a virtue spectrum"""
        action_lower = action.lower()
        
        # Determine position on spectrum
        position, score = self._determine_spectrum_position(action_lower, spectrum)
        
        # Calculate distance from temperance (ideal is 4.0)
        temperance_distance = abs(score - 4.0)
        
        # Generate recommendations
        recommendations = self._generate_recommendations(position, spectrum, temperance_distance)
        
        # Generate Gospel guidance
        gospel_guidance = self._generate_gospel_guidance(action, spectrum, position)
        
        return SpectrumAnalysis(
            analyzed_item=action,
            virtue_spectrum=spectrum,
            position=position,
            position_score=score,
            temperance_distance=temperance_distance,
            recommendations=recommendations,
            gospel_guidance=gospel_guidance
        )
    
    def _determine_spectrum_position(self, action_lower: str, spectrum: VirtueSpectrum) -> tuple[SpectrumPosition, float]:
        """Determine where action falls on the virtue spectrum"""
        # Score based on matching examples at each position
        position_scores = {}
        
        for position, examples in spectrum.practical_examples.items():
            score = 0
            for example in examples:
                example_words = example.lower().split()
                matches = sum(1 for word in example_words if word in action_lower)
                if matches > 0:
                    score += matches / len(example_words)
            position_scores[position] = score
        
        # Find position with highest score
        if not position_scores or max(position_scores.values()) == 0:
            # Default to temperance if no clear match
            return SpectrumPosition.TEMPERANCE, 4.0
        
        best_position = max(position_scores, key=position_scores.get)
        return best_position, float(best_position.value)
    
    def _generate_recommendations(self, position: SpectrumPosition, spectrum: VirtueSpectrum, distance: float) -> List[str]:
        """Generate recommendations for achieving temperance"""
        recommendations = []
        
        if position == SpectrumPosition.TEMPERANCE:
            recommendations.append(f"Excellent! You're demonstrating balanced {spectrum.virtue_name.lower()}")
            recommendations.append("Continue this temperate approach")
        
        elif position.value < 4:  # Vice side
            if position.value <= 2:
                recommendations.append(f"Serious concern: This shows {spectrum.deficiency_vice.lower()}")
                recommendations.append(f"Urgently develop {spectrum.virtue_name.lower()} through prayer and practice")
            else:
                recommendations.append(f"Growth needed: Move toward greater {spectrum.virtue_name.lower()}")
                recommendations.append("Take small steps toward the temperate middle")
        
        else:  # Excess side  
            if position.value >= 5:
                recommendations.append(f"Caution: This may be {spectrum.excess_vice.lower()}")
                recommendations.append(f"Consider moderating your {spectrum.virtue_name.lower()}")
            else:
                recommendations.append("Good virtue, but consider balance")
                recommendations.append("Ensure wisdom guides your virtue")
        
        # Add scripture-based recommendation
        if spectrum.scripture_references:
            recommendations.append(f"Study: {spectrum.scripture_references[0]}")
        
        return recommendations
    
    def _generate_gospel_guidance(self, action: str, spectrum: VirtueSpectrum, position: SpectrumPosition) -> str:
        """Generate Gospel-centered guidance"""
        guidance = f"Gospel Guidance on {spectrum.virtue_name}:\n\n"
        guidance += f"📖 Christ's Example: {spectrum.gospel_connection}\n\n"
        
        if position == SpectrumPosition.TEMPERANCE:
            guidance += "✅ You're reflecting Christ's balanced approach to this virtue.\n"
            guidance += "Continue to let the Spirit guide you in maintaining this balance.\n"
        
        elif position.value < 4:
            guidance += f"🙏 Prayer Focus: Ask God to help you develop {spectrum.virtue_name.lower()}.\n"
            guidance += f"📚 Study how Christ demonstrated {spectrum.virtue_name.lower()} in His life.\n"
            guidance += "🛠️ Practice: Look for daily opportunities to grow in this virtue.\n"
        
        else:
            guidance += f"⚖️ Seek Balance: Even virtues need wisdom and moderation.\n"
            guidance += f"🤔 Reflect: Is your {spectrum.virtue_name.lower()} serving others or becoming prideful?\n"
            guidance += "📖 Remember: Christ was perfectly balanced in all virtues.\n"
        
        guidance += f"\n💡 Key Scripture: {spectrum.scripture_references[0] if spectrum.scripture_references else 'Study Christ\'s example'}"
        
        return guidance
    
    def generate_virtue_report(self, person_description: str) -> str:
        """Generate comprehensive virtue analysis report"""
        analyses = self.analyze_virtue_spectrum(person_description)
        
        report = "🌟 VIRTUE-VICE SPECTRUM ANALYSIS\n"
        report += "=" * 50 + "\n\n"
        
        report += f"📝 ANALYZED: {person_description}\n\n"
        
        if analyses:
            total_temperance_score = sum(4.0 - analysis.temperance_distance for analysis in analyses)
            max_possible = len(analyses) * 4.0
            overall_virtue_score = total_temperance_score / max_possible if max_possible > 0 else 0
            
            report += f"🎯 OVERALL VIRTUE BALANCE: {overall_virtue_score:.2f}/1.0\n\n"
            
            for analysis in analyses:
                report += f"⚖️ {analysis.virtue_spectrum.virtue_name.upper()} SPECTRUM:\n"
                report += f"   Position: {analysis.position.name}\n"
                report += f"   Distance from Temperance: {analysis.temperance_distance:.1f}\n"
                report += f"   Deficiency Vice: {analysis.virtue_spectrum.deficiency_vice}\n"
                report += f"   Excess Vice: {analysis.virtue_spectrum.excess_vice}\n\n"
                
                report += "💡 RECOMMENDATIONS:\n"
                for rec in analysis.recommendations:
                    report += f"   • {rec}\n"
                report += "\n"
                
                report += f"📖 GOSPEL GUIDANCE:\n"
                report += f"   {analysis.gospel_guidance}\n"
                report += "-" * 40 + "\n\n"
        
        report += "🎯 REMEMBER: The goal is temperance - virtue balanced with wisdom.\n"
        report += "'In all things there must be moderation' - Gospel principle\n"
        report += "Seek the Spirit to guide you toward Christ's perfect balance."
        
        return report

# Example usage
def demonstrate_virtue_spectrum():
    """Demonstrate the virtue-vice spectrum analyzer"""
    analyzer = VirtueSpectrumAnalyzer()
    
    print("⚖️ VIRTUE-VICE SPECTRUM DEMONSTRATION")
    print("=" * 50)
    
    test_behaviors = [
        "I always say yes to help others even when it hurts my family",
        "I refuse to ever speak up when I see something wrong",
        "I give away money we need for bills to help others",
        "I stand up for truth with love and wisdom"
    ]
    
    for behavior in test_behaviors:
        print(f"\n🔍 ANALYZING: {behavior}")
        print("-" * 30)
        report = analyzer.generate_virtue_report(behavior)
        print(report)
        print("\n" + "=" * 50)

if __name__ == "__main__":
    demonstrate_virtue_spectrum()
