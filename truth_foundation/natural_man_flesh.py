
"""
Natural Man and Works of the Flesh Module
Analyzes human tendencies toward sin and provides Gospel-centered solutions
Based on Galatians 5:19-21, 1 John 2:16, and Mosiah 3:19
"""

from dataclasses import dataclass
from typing import Dict, List, Optional, Any
from enum import Enum
import logging
from .core_truths import TruthStatement, TruthLevel
from .gospel_definitions import GospelDefinitions

logger = logging.getLogger(__name__)

class FleshCategory(Enum):
    """Categories of fleshly desires and works"""
    SEXUAL_SINS = "sexual_sins"
    RELIGIOUS_SINS = "religious_sins" 
    RELATIONAL_SINS = "relational_sins"
    INTEMPERANCE = "intemperance"
    PRIDE_OF_LIFE = "pride_of_life"
    LUST_OF_EYES = "lust_of_eyes"

class SeverityLevel(Enum):
    """Severity levels of fleshly tendencies"""
    EXTREME = 5      # Destroys souls and relationships
    HIGH = 4         # Serious spiritual damage
    MODERATE = 3     # Significant concern
    LOW = 2          # Warning signs
    TENDENCY = 1     # Natural inclination

@dataclass
class FleshWork:
    """Represents a specific work of the flesh"""
    name: str
    category: FleshCategory
    description: str
    scripture_references: List[str]
    severity: SeverityLevel
    warning_signs: List[str]
    spiritual_consequences: List[str]
    gospel_remedy: str
    virtue_opposite: str
    practical_overcome_steps: List[str]

@dataclass
class FleshAnalysis:
    """Analysis of fleshly tendencies in behavior or content"""
    analyzed_item: str
    detected_works: List[FleshWork]
    severity_score: float  # 1.0 to 5.0
    primary_category: FleshCategory
    spiritual_danger_level: str
    gospel_remedies: List[str]
    virtue_recommendations: List[str]
    scriptural_guidance: List[str]

class NaturalManAnalyzer:
    """
    Analyzes content, behaviors, and attitudes for works of the flesh
    Provides Gospel-centered remedies and virtue development
    """
    
    def __init__(self):
        self.gospel_definitions = GospelDefinitions()
        self.flesh_works = self._initialize_flesh_works()
        
    def _initialize_flesh_works(self) -> Dict[str, FleshWork]:
        """Initialize the comprehensive catalog of works of the flesh"""
        return {
            # SEXUAL SINS
            "sexual_immorality": FleshWork(
                name="Sexual Immorality (Fornication)",
                category=FleshCategory.SEXUAL_SINS,
                description="Any sexual activity outside the covenant of marriage",
                scripture_references=[
                    "Galatians 5:19",
                    "1 Corinthians 6:18 - Flee fornication",
                    "Alma 39:9 - Go no more after the lusts of your eyes"
                ],
                severity=SeverityLevel.HIGH,
                warning_signs=[
                    "Justifying sexual activity outside marriage",
                    "Viewing pornography",
                    "Inappropriate physical intimacy",
                    "Sexualizing relationships"
                ],
                spiritual_consequences=[
                    "Loss of Spirit's influence",
                    "Spiritual numbness", 
                    "Damaged ability to feel God's love",
                    "Broken covenant relationship with God"
                ],
                gospel_remedy="Repentance through Christ's Atonement, keeping the Law of Chastity",
                virtue_opposite="Chastity and sexual purity",
                practical_overcome_steps=[
                    "Confess to appropriate priesthood leader",
                    "Remove tempting influences and media",
                    "Strengthen relationship with God through prayer",
                    "Focus on developing Christ-like love",
                    "Seek professional help if needed"
                ]
            ),
            
            "impurity": FleshWork(
                name="Impurity",
                category=FleshCategory.SEXUAL_SINS,
                description="Moral uncleanness, especially in sexual context",
                scripture_references=[
                    "Galatians 5:19",
                    "Matthew 5:8 - Blessed are the pure in heart",
                    "D&C 88:86 - Abide the law to abide the glory"
                ],
                severity=SeverityLevel.MODERATE,
                warning_signs=[
                    "Impure thoughts and fantasies",
                    "Inappropriate humor or conversation",
                    "Consuming immoral media",
                    "Compromising moral standards gradually"
                ],
                spiritual_consequences=[
                    "Cannot abide celestial glory",
                    "Weakened spiritual discernment",
                    "Difficulty feeling the Spirit",
                    "Corrupted view of relationships"
                ],
                gospel_remedy="Purification through Christ's blood, virtue in thoughts",
                virtue_opposite="Purity of heart and mind",
                practical_overcome_steps=[
                    "Control thoughts and media consumption",
                    "Practice virtue in all interactions",
                    "Study scriptures daily to purify mind",
                    "Serve others to redirect focus",
                    "Fast and pray for spiritual cleansing"
                ]
            ),
            
            "sensuality": FleshWork(
                name="Sensuality (Lewdness)",
                category=FleshCategory.SEXUAL_SINS,
                description="Indulging in sexual pleasures without restraint",
                scripture_references=[
                    "Galatians 5:19",
                    "1 Peter 4:3 - Time past of our life may suffice us",
                    "2 Peter 2:18 - Allure through lusts of the flesh"
                ],
                severity=SeverityLevel.HIGH,
                warning_signs=[
                    "Obsession with physical pleasure",
                    "Lack of self-control in physical desires",
                    "Promoting or encouraging lewdness",
                    "Objectifying others"
                ],
                spiritual_consequences=[
                    "Spiritual death",
                    "Cannot inherit kingdom of God",
                    "Enslaved to physical desires",
                    "Loss of divine nature"
                ],
                gospel_remedy="Self-mastery through Christ's power, temperance",
                virtue_opposite="Self-control and temperance",
                practical_overcome_steps=[
                    "Practice fasting to gain self-mastery",
                    "Avoid situations that trigger sensuality",
                    "Develop spiritual disciplines",
                    "Focus on eternal rather than temporal",
                    "Seek the Spirit's help in moments of temptation"
                ]
            ),
            
            # RELIGIOUS SINS
            "idolatry": FleshWork(
                name="Idolatry",
                category=FleshCategory.RELIGIOUS_SINS,
                description="Worshipping anything or anyone other than the one true God",
                scripture_references=[
                    "Galatians 5:20",
                    "1 John 5:21 - Keep yourselves from idols",
                    "Exodus 20:3 - Thou shalt have no other gods before me"
                ],
                severity=SeverityLevel.EXTREME,
                warning_signs=[
                    "Putting money, career, or possessions before God",
                    "Worshipping celebrities or leaders",
                    "Making anything more important than God",
                    "Relying on worldly things for security"
                ],
                spiritual_consequences=[
                    "Spiritual death",
                    "Cannot receive revelation",
                    "Loss of eternal perspective",
                    "Bondage to false gods"
                ],
                gospel_remedy="Put God first in all things, worship only Him",
                virtue_opposite="Worship and devotion to God",
                practical_overcome_steps=[
                    "Examine what you spend most time thinking about",
                    "Put God first in priorities and time",
                    "Regular worship and temple attendance",
                    "Remove idolatrous influences",
                    "Practice gratitude to God for all blessings"
                ]
            ),
            
            "sorcery": FleshWork(
                name="Sorcery (Witchcraft/Pharmakeia)",
                category=FleshCategory.RELIGIOUS_SINS,
                description="Use of magic, occult practices, or mind-altering substances",
                scripture_references=[
                    "Galatians 5:20",
                    "Revelation 21:8 - Sorcerers shall have their part in the lake of fire",
                    "D&C 89 - Word of Wisdom principles"
                ],
                severity=SeverityLevel.EXTREME,
                warning_signs=[
                    "Involvement in occult practices",
                    "Seeking power through dark means",
                    "Drug use or abuse",
                    "Fortune telling or seeking forbidden knowledge"
                ],
                spiritual_consequences=[
                    "Opens soul to evil influences",
                    "Loss of agency and spiritual freedom",
                    "Cannot inherit celestial kingdom",
                    "Bondage to Satan"
                ],
                gospel_remedy="Complete rejection of occult, reliance on God's power only",
                virtue_opposite="Faith in God's power and wisdom",
                practical_overcome_steps=[
                    "Completely abandon all occult practices",
                    "Remove all occult materials and influences",
                    "Seek priesthood blessings for protection",
                    "Study scriptures to understand God's power",
                    "Pray for deliverance and protection"
                ]
            ),
            
            # RELATIONAL SINS
            "enmity": FleshWork(
                name="Enmity (Hatred)",
                category=FleshCategory.RELATIONAL_SINS,
                description="Hostility and animosity toward others",
                scripture_references=[
                    "Galatians 5:20",
                    "1 John 4:20 - He that loveth not his brother whom he hath seen",
                    "3 Nephi 11:29 - He that hath the spirit of contention is not of me"
                ],
                severity=SeverityLevel.HIGH,
                warning_signs=[
                    "Harboring hatred toward others",
                    "Refusing to forgive",
                    "Seeking revenge or harm",
                    "Enjoying others' failures"
                ],
                spiritual_consequences=[
                    "Cannot love God while hating others",
                    "Prayers hindered",
                    "Loss of charity and Christ-like love",
                    "Spiritual darkness"
                ],
                gospel_remedy="Love enemies, forgive all men, develop charity",
                virtue_opposite="Love and charity",
                practical_overcome_steps=[
                    "Pray for those you struggle to love",
                    "Serve those you have conflicts with",
                    "Practice forgiveness daily",
                    "Look for good in others",
                    "Remember Christ's love for all"
                ]
            ),
            
            "strife": FleshWork(
                name="Strife (Contention)",
                category=FleshCategory.RELATIONAL_SINS,
                description="Quarrels and disputes that destroy unity",
                scripture_references=[
                    "Galatians 5:20",
                    "3 Nephi 11:29 - Spirit of contention is not of me",
                    "Proverbs 13:10 - Only by pride cometh contention"
                ],
                severity=SeverityLevel.MODERATE,
                warning_signs=[
                    "Always arguing or debating",
                    "Creating division in groups",
                    "Inability to disagree peacefully",
                    "Stirring up conflict"
                ],
                spiritual_consequences=[
                    "Drives away the Spirit",
                    "Destroys relationships",
                    "Creates division in families/church",
                    "Prevents unity and peace"
                ],
                gospel_remedy="Seek peace, be a peacemaker, speak with kindness",
                virtue_opposite="Peace and unity",
                practical_overcome_steps=[
                    "Practice listening before speaking",
                    "Seek to understand rather than win",
                    "Apologize quickly when wrong",
                    "Focus on common ground",
                    "Pray for peace in relationships"
                ]
            ),
            
            "jealousy": FleshWork(
                name="Jealousy",
                category=FleshCategory.RELATIONAL_SINS,
                description="Resentment of others' possessions, success, or advantages",
                scripture_references=[
                    "Galatians 5:20",
                    "James 3:14-16 - Where envying and strife is, there is confusion",
                    "D&C 67:10 - Casting away jealousy and fears"
                ],
                severity=SeverityLevel.MODERATE,
                warning_signs=[
                    "Feeling bad when others succeed",
                    "Comparing yourself constantly to others",
                    "Gossiping about others' success",
                    "Unable to celebrate others' blessings"
                ],
                spiritual_consequences=[
                    "Prevents gratitude and contentment",
                    "Destroys joy and peace",
                    "Weakens relationships",
                    "Invites evil spirits"
                ],
                gospel_remedy="Gratitude for own blessings, rejoicing in others' success",
                virtue_opposite="Gratitude and contentment",
                practical_overcome_steps=[
                    "Daily gratitude practice",
                    "Celebrate others' successes genuinely",
                    "Focus on your own progress",
                    "Serve those you're jealous of",
                    "Remember God's individual plan for you"
                ]
            ),
            
            "fits_of_anger": FleshWork(
                name="Fits of Anger (Wrath)",
                category=FleshCategory.RELATIONAL_SINS,
                description="Uncontrolled outbursts of rage",
                scripture_references=[
                    "Galatians 5:20",
                    "Ephesians 4:26 - Be ye angry, and sin not",
                    "Alma 38:12 - Bridle all your passions"
                ],
                severity=SeverityLevel.HIGH,
                warning_signs=[
                    "Explosive temper",
                    "Verbal or physical aggression",
                    "Road rage or similar outbursts",
                    "Inability to control emotional reactions"
                ],
                spiritual_consequences=[
                    "Damages relationships severely",
                    "Creates fear in others",
                    "Loss of Spirit's influence",
                    "May lead to violence"
                ],
                gospel_remedy="Self-control, bridling passions, patience",
                virtue_opposite="Patience and self-control",
                practical_overcome_steps=[
                    "Identify anger triggers",
                    "Practice breathing and counting before reacting",
                    "Remove yourself from trigger situations",
                    "Seek professional anger management if needed",
                    "Fast and pray for self-mastery"
                ]
            ),
            
            # INTEMPERANCE
            "drunkenness": FleshWork(
                name="Drunkenness",
                category=FleshCategory.INTEMPERANCE,
                description="Excessive consumption of alcohol",
                scripture_references=[
                    "Galatians 5:21",
                    "D&C 89:7 - Strong drinks are not for the belly",
                    "1 Corinthians 6:10 - Drunkards shall not inherit kingdom"
                ],
                severity=SeverityLevel.HIGH,
                warning_signs=[
                    "Regular alcohol consumption",
                    "Drinking to escape problems",
                    "Unable to stop drinking",
                    "Alcohol affecting relationships or work"
                ],
                spiritual_consequences=[
                    "Loss of self-control and agency",
                    "Cannot inherit kingdom of God",
                    "Weakened spiritual discernment",
                    "Physical and spiritual addiction"
                ],
                gospel_remedy="Complete abstinence, Word of Wisdom obedience",
                virtue_opposite="Temperance and self-control",
                practical_overcome_steps=[
                    "Commit to complete abstinence",
                    "Remove alcohol from environment",
                    "Find healthy coping mechanisms",
                    "Join support groups if needed",
                    "Seek priesthood blessings and professional help"
                ]
            ),
            
            # PRIDE OF LIFE
            "pride_of_life": FleshWork(
                name="Pride of Life",
                category=FleshCategory.PRIDE_OF_LIFE,
                description="Desire for personal greatness, recognition, and self-glorification",
                scripture_references=[
                    "1 John 2:16",
                    "Proverbs 16:18 - Pride goeth before destruction",
                    "Ether 12:27 - I give unto men weakness that they may be humble"
                ],
                severity=SeverityLevel.HIGH,
                warning_signs=[
                    "Seeking praise and recognition",
                    "Comparing yourself to others",
                    "Difficulty accepting correction",
                    "Boasting about accomplishments"
                ],
                spiritual_consequences=[
                    "God resisteth the proud",
                    "Cannot receive revelation",
                    "Spiritual blindness",
                    "Loss of teachable spirit"
                ],
                gospel_remedy="Humility, recognizing dependence on God",
                virtue_opposite="Humility and meekness",
                practical_overcome_steps=[
                    "Daily practice gratitude to God for abilities",
                    "Serve others without recognition",
                    "Accept correction gracefully", 
                    "Focus on others' needs",
                    "Remember your weaknesses and God's grace"
                ]
            ),
            
            # LUST OF EYES
            "lust_of_eyes": FleshWork(
                name="Lust of the Eyes",
                category=FleshCategory.LUST_OF_EYES,
                description="Desire for what we see - possessions, wealth, status",
                scripture_references=[
                    "1 John 2:16",
                    "Luke 12:15 - A man's life consisteth not in abundance",
                    "Jacob 2:18 - Before ye seek for riches, seek ye for the kingdom"
                ],
                severity=SeverityLevel.MODERATE,
                warning_signs=[
                    "Constantly wanting what others have",
                    "Materialism and consumerism",
                    "Covetousness and greed",
                    "Status-seeking behavior"
                ],
                spiritual_consequences=[
                    "Never satisfied or content",
                    "Worship of material things",
                    "Neglect of spiritual matters",
                    "Anxiety about temporal security"
                ],
                gospel_remedy="Contentment, gratitude, seeking first God's kingdom",
                virtue_opposite="Contentment and spiritual focus",
                practical_overcome_steps=[
                    "Practice gratitude for what you have",
                    "Limit exposure to advertising and social media",
                    "Focus on experiences over possessions",
                    "Give generously to others",
                    "Remember eternal vs temporal perspective"
                ]
            )
        }
    
    def analyze_flesh_tendencies(self, content: str, context: Dict[str, Any] = None) -> FleshAnalysis:
        """Analyze content for works of the flesh and provide Gospel remedies"""
        if context is None:
            context = {}
            
        content_lower = content.lower()
        detected_works = []
        
        # Check each flesh work for indicators
        for flesh_work in self.flesh_works.values():
            if self._detect_flesh_work(content_lower, flesh_work):
                detected_works.append(flesh_work)
        
        # Calculate severity score
        severity_score = self._calculate_severity_score(detected_works)
        
        # Determine primary category
        primary_category = self._determine_primary_category(detected_works)
        
        # Determine spiritual danger level
        spiritual_danger_level = self._assess_spiritual_danger(severity_score)
        
        # Generate Gospel remedies
        gospel_remedies = self._generate_gospel_remedies(detected_works)
        
        # Generate virtue recommendations
        virtue_recommendations = self._generate_virtue_recommendations(detected_works)
        
        # Generate scriptural guidance
        scriptural_guidance = self._generate_scriptural_guidance(detected_works)
        
        return FleshAnalysis(
            analyzed_item=content,
            detected_works=detected_works,
            severity_score=severity_score,
            primary_category=primary_category,
            spiritual_danger_level=spiritual_danger_level,
            gospel_remedies=gospel_remedies,
            virtue_recommendations=virtue_recommendations,
            scriptural_guidance=scriptural_guidance
        )
    
    def _detect_flesh_work(self, content_lower: str, flesh_work: FleshWork) -> bool:
        """Detect if content contains indicators of a specific flesh work"""
        # Check name and description
        if flesh_work.name.lower() in content_lower:
            return True
            
        # Check warning signs
        for sign in flesh_work.warning_signs:
            sign_words = sign.lower().split()
            if len(sign_words) <= 3:  # Simple phrases
                if all(word in content_lower for word in sign_words):
                    return True
            else:  # Longer descriptions, check for key words
                key_words = sign_words[:3]  # First 3 words
                if any(word in content_lower for word in key_words):
                    return True
        
        return False
    
    def _calculate_severity_score(self, detected_works: List[FleshWork]) -> float:
        """Calculate overall severity score"""
        if not detected_works:
            return 0.0
            
        total_severity = sum(work.severity.value for work in detected_works)
        average_severity = total_severity / len(detected_works)
        
        # Weight by number of works detected
        multiplier = min(2.0, 1.0 + (len(detected_works) - 1) * 0.2)
        
        return min(5.0, average_severity * multiplier)
    
    def _determine_primary_category(self, detected_works: List[FleshWork]) -> FleshCategory:
        """Determine the primary category of flesh works detected"""
        if not detected_works:
            return FleshCategory.INTEMPERANCE  # Default
            
        # Count by category
        category_counts = {}
        for work in detected_works:
            category = work.category
            category_counts[category] = category_counts.get(category, 0) + 1
        
        # Return most common category
        return max(category_counts, key=category_counts.get)
    
    def _assess_spiritual_danger(self, severity_score: float) -> str:
        """Assess spiritual danger level based on severity score"""
        if severity_score >= 4.5:
            return "EXTREME SPIRITUAL DANGER"
        elif severity_score >= 3.5:
            return "HIGH SPIRITUAL DANGER" 
        elif severity_score >= 2.5:
            return "MODERATE SPIRITUAL CONCERN"
        elif severity_score >= 1.5:
            return "LOW SPIRITUAL RISK"
        else:
            return "MINIMAL CONCERN"
    
    def _generate_gospel_remedies(self, detected_works: List[FleshWork]) -> List[str]:
        """Generate Gospel remedies for detected works of the flesh"""
        remedies = []
        
        # Add unique remedies from detected works
        for work in detected_works[:3]:  # Limit to top 3
            if work.gospel_remedy not in remedies:
                remedies.append(work.gospel_remedy)
        
        # Add general remedies
        if detected_works:
            remedies.extend([
                "Daily prayer and scripture study",
                "Regular temple attendance",
                "Seek guidance from priesthood leaders",
                "Fast for spiritual strength",
                "Apply the Atonement of Jesus Christ"
            ])
        
        return remedies[:5]  # Limit to 5 remedies
    
    def _generate_virtue_recommendations(self, detected_works: List[FleshWork]) -> List[str]:
        """Generate virtue recommendations to overcome detected works"""
        virtues = []
        
        for work in detected_works:
            if work.virtue_opposite not in virtues:
                virtues.append(work.virtue_opposite)
        
        return virtues
    
    def _generate_scriptural_guidance(self, detected_works: List[FleshWork]) -> List[str]:
        """Generate scriptural guidance for detected issues"""
        scriptures = []
        
        for work in detected_works[:3]:  # Top 3 works
            if work.scripture_references:
                scriptures.append(work.scripture_references[0])  # First scripture for each
        
        # Add general scriptures about overcoming the flesh
        scriptures.extend([
            "Mosiah 3:19 - Put off the natural man",
            "Romans 8:13 - If ye live after the flesh, ye shall die", 
            "Galatians 5:24 - They that are Christ's have crucified the flesh"
        ])
        
        return list(set(scriptures))  # Remove duplicates
    
    def generate_flesh_report(self, content: str) -> str:
        """Generate comprehensive report on works of the flesh analysis"""
        analysis = self.analyze_flesh_tendencies(content)
        
        report = "🔥 WORKS OF THE FLESH ANALYSIS\n"
        report += "=" * 50 + "\n\n"
        
        report += f"📝 ANALYZED: {content}\n\n"
        
        report += f"⚠️ SPIRITUAL DANGER LEVEL: {analysis.spiritual_danger_level}\n"
        report += f"📊 SEVERITY SCORE: {analysis.severity_score:.2f}/5.0\n"
        report += f"🎯 PRIMARY CATEGORY: {analysis.primary_category.value.replace('_', ' ').title()}\n\n"
        
        if analysis.detected_works:
            report += "🚨 DETECTED WORKS OF THE FLESH:\n"
            for work in analysis.detected_works:
                report += f"   • {work.name} ({work.category.value.replace('_', ' ').title()})\n"
                report += f"     Severity: {work.severity.name}\n"
                report += f"     Description: {work.description}\n\n"
        
        if analysis.gospel_remedies:
            report += "💊 GOSPEL REMEDIES:\n"
            for remedy in analysis.gospel_remedies:
                report += f"   • {remedy}\n"
            report += "\n"
        
        if analysis.virtue_recommendations:
            report += "⭐ VIRTUES TO DEVELOP:\n"
            for virtue in analysis.virtue_recommendations:
                report += f"   • {virtue}\n"
            report += "\n"
        
        if analysis.scriptural_guidance:
            report += "📖 SCRIPTURAL GUIDANCE:\n"
            for scripture in analysis.scriptural_guidance:
                report += f"   • {scripture}\n"
            report += "\n"
        
        report += "🙏 REMEMBER: Through Christ's Atonement, all works of the flesh can be overcome.\n"
        report += "'Put off the natural man and become a saint through the atonement of Christ.'\n"
        report += "- Mosiah 3:19"
        
        return report

# Example usage and demonstration
def demonstrate_flesh_analyzer():
    """Demonstrate the natural man and works of flesh analyzer"""
    analyzer = NaturalManAnalyzer()
    
    print("🔥 WORKS OF THE FLESH ANALYZER DEMONSTRATION")
    print("=" * 50)
    
    test_content = [
        "I can't stop looking at inappropriate content online",
        "I hate my coworker and want them to fail",
        "I drink every weekend to forget my problems", 
        "I deserve more recognition than others get",
        "I want everything I see on social media"
    ]
    
    for content in test_content:
        print(f"\n🔍 ANALYZING: {content}")
        print("-" * 30)
        report = analyzer.generate_flesh_report(content)
        print(report)
        print("\n" + "=" * 50)

if __name__ == "__main__":
    demonstrate_flesh_analyzer()
