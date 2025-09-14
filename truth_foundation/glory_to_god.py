
"""
Glory to God Module - Evaluating if something brings glory to God
Based on 1 Corinthians 10:31 "So whether you eat or drink or whatever you do, do it all for the glory of God"
"""

from dataclasses import dataclass
from typing import Dict, List, Optional, Any, Tuple
from enum import Enum
import logging
from .core_truths import TruthStatement, TruthLevel

logger = logging.getLogger(__name__)

class GloryLevel(Enum):
    """Levels of how something brings glory to God"""
    DISHONORS_GOD = -2      # Actively dishonors or blasphemes God
    NEUTRAL_SECULAR = 0     # Neither honors nor dishonors God
    ACKNOWLEDGES_GOD = 1    # Recognizes God's existence or role
    HONORS_GOD = 2          # Shows respect and reverence for God
    GLORIFIES_GOD = 3       # Actively brings praise and glory to God

@dataclass
class GloryAttribute:
    """An attribute of God that can be glorified"""
    attribute_name: str
    description: str
    scripture_references: List[str]
    how_to_glorify: List[str]
    recognition_indicators: List[str]
    opposite_behaviors: List[str]

@dataclass
class GloryEvaluation:
    """Result of evaluating how something brings glory to God"""
    glory_level: GloryLevel
    glory_score: float  # -1.0 to 1.0
    attributes_glorified: List[str]
    attributes_dishonored: List[str]
    specific_ways_glorified: List[str]
    improvement_suggestions: List[str]
    eternal_perspective: str

class GloryToGodEvaluator:
    """
    Evaluates whether actions, content, or decisions bring glory to God
    Based on revealing and honoring God's character and attributes
    """
    
    def __init__(self):
        self.god_attributes = self._initialize_god_attributes()
        self.glory_indicators = self._initialize_glory_indicators()
        self.dishonor_indicators = self._initialize_dishonor_indicators()
    
    def _initialize_god_attributes(self) -> List[GloryAttribute]:
        """Initialize key attributes of God that can be glorified"""
        return [
            GloryAttribute(
                attribute_name="Love",
                description="God's perfect, unconditional love for all creation",
                scripture_references=[
                    "1 John 4:8 - 'God is love'",
                    "John 3:16 - 'For God so loved the world'",
                    "Romans 8:38-39 - 'Nothing can separate us from God's love'"
                ],
                how_to_glorify=[
                    "Show sacrificial love for others",
                    "Love enemies and difficult people",
                    "Demonstrate unconditional acceptance",
                    "Put others' needs before your own"
                ],
                recognition_indicators=[
                    "Acts of selfless service",
                    "Forgiveness of wrongs",
                    "Compassion for the suffering",
                    "Love without expecting return"
                ],
                opposite_behaviors=[
                    "Hatred, revenge, malice",
                    "Conditional love based on performance",
                    "Selfishness and narcissism",
                    "Abandoning people when they struggle"
                ]
            ),
            
            GloryAttribute(
                attribute_name="Truth",
                description="God as the source and standard of all truth",
                scripture_references=[
                    "John 14:6 - 'I am the way, the truth, and the life'",
                    "John 8:32 - 'The truth shall make you free'",
                    "D&C 93:36 - 'The glory of God is intelligence, or light and truth'"
                ],
                how_to_glorify=[
                    "Speak truth even when difficult",
                    "Seek truth in all areas of life",
                    "Expose lies and deception",
                    "Live authentically and honestly"
                ],
                recognition_indicators=[
                    "Commitment to honesty",
                    "Pursuit of knowledge and understanding",
                    "Rejection of falsehood",
                    "Transparency in relationships"
                ],
                opposite_behaviors=[
                    "Lying, deception, fraud",
                    "Promoting false ideologies",
                    "Hiding truth for personal gain",
                    "Relativism that denies absolute truth"
                ]
            ),
            
            GloryAttribute(
                attribute_name="Justice",
                description="God's perfect fairness and moral righteousness",
                scripture_references=[
                    "Deuteronomy 32:4 - 'All his ways are just'",
                    "Psalm 89:14 - 'Righteousness and justice are the foundation of your throne'",
                    "Isaiah 30:18 - 'The Lord is a God of justice'"
                ],
                how_to_glorify=[
                    "Stand up for the oppressed",
                    "Treat all people fairly",
                    "Support righteous laws and governance",
                    "Oppose corruption and abuse"
                ],
                recognition_indicators=[
                    "Fair treatment of all people",
                    "Defense of the innocent",
                    "Equal application of standards",
                    "Opposition to corruption"
                ],
                opposite_behaviors=[
                    "Favoritism and bias",
                    "Oppression of the weak",
                    "Corruption and bribery",
                    "Ignoring injustice"
                ]
            ),
            
            GloryAttribute(
                attribute_name="Mercy",
                description="God's compassion and forgiveness toward sinners",
                scripture_references=[
                    "Psalm 103:8 - 'Compassionate and gracious, slow to anger'",
                    "Lamentations 3:22-23 - 'His mercies are new every morning'",
                    "Ephesians 2:4 - 'Rich in mercy'"
                ],
                how_to_glorify=[
                    "Forgive those who wrong you",
                    "Show compassion to the fallen",
                    "Give second chances",
                    "Help rather than punish when possible"
                ],
                recognition_indicators=[
                    "Forgiveness of offenses",
                    "Compassion for mistakes",
                    "Restoration over condemnation",
                    "Patience with human weakness"
                ],
                opposite_behaviors=[
                    "Merciless punishment",
                    "Refusing to forgive",
                    "Harsh judgment without compassion",
                    "Revenge and retaliation"
                ]
            ),
            
            GloryAttribute(
                attribute_name="Wisdom",
                description="God's perfect understanding and wise judgment",
                scripture_references=[
                    "Romans 11:33 - 'Oh, the depth of the riches of the wisdom of God'",
                    "James 1:5 - 'If any of you lacks wisdom, let him ask God'",
                    "Proverbs 2:6 - 'The Lord gives wisdom'"
                ],
                how_to_glorify=[
                    "Seek divine wisdom in decisions",
                    "Apply knowledge righteously",
                    "Show good judgment and discernment",
                    "Help others gain understanding"
                ],
                recognition_indicators=[
                    "Thoughtful decision-making",
                    "Long-term perspective",
                    "Learning from mistakes",
                    "Teaching and mentoring others"
                ],
                opposite_behaviors=[
                    "Foolish and reckless choices",
                    "Ignoring consequences",
                    "Pride that rejects counsel",
                    "Using knowledge for evil"
                ]
            ),
            
            GloryAttribute(
                attribute_name="Holiness",
                description="God's perfect purity and separation from sin",
                scripture_references=[
                    "Isaiah 6:3 - 'Holy, holy, holy is the Lord Almighty'",
                    "1 Peter 1:16 - 'Be holy, because I am holy'",
                    "Revelation 4:8 - 'Holy is the Lord God Almighty'"
                ],
                how_to_glorify=[
                    "Live a pure and righteous life",
                    "Separate from sin and corruption",
                    "Pursue moral excellence",
                    "Consecrate yourself to God's service"
                ],
                recognition_indicators=[
                    "Moral purity and integrity",
                    "Separation from worldly corruption",
                    "Consecration to sacred purposes",
                    "Reverence and worship"
                ],
                opposite_behaviors=[
                    "Moral corruption and sin",
                    "Profanity and irreverence",
                    "Desecration of sacred things",
                    "Living for selfish pleasures"
                ]
            ),
            
            GloryAttribute(
                attribute_name="Power",
                description="God's omnipotence and ability to accomplish all things",
                scripture_references=[
                    "Jeremiah 32:17 - 'Nothing is too hard for you'",
                    "Luke 1:37 - 'Nothing is impossible with God'",
                    "Ephesians 3:20 - 'Able to do immeasurably more than we ask'"
                ],
                how_to_glorify=[
                    "Accomplish great things through faith",
                    "Overcome seemingly impossible challenges",
                    "Demonstrate divine strength in weakness",
                    "Testify of God's miraculous power"
                ],
                recognition_indicators=[
                    "Achieving the seemingly impossible",
                    "Miraculous healings and interventions",
                    "Supernatural strength in trials",
                    "Divine assistance in challenges"
                ],
                opposite_behaviors=[
                    "Denying God's power",
                    "Relying solely on human strength",
                    "Attributing miracles to chance",
                    "Living as if God doesn't exist"
                ]
            )
        ]
    
    def _initialize_glory_indicators(self) -> List[str]:
        """Initialize general indicators that something brings glory to God"""
        return [
            "Acknowledges God as the source",
            "Points others toward God",
            "Demonstrates divine attributes",
            "Builds faith in God",
            "Reflects God's character",
            "Serves God's purposes",
            "Brings praise and worship to God",
            "Reveals God's goodness",
            "Advances God's kingdom",
            "Shows gratitude to God",
            "Obeys God's commandments",
            "Sacrifices for righteous purposes"
        ]
    
    def _initialize_dishonor_indicators(self) -> List[str]:
        """Initialize indicators that something dishonors God"""
        return [
            "Denies God's existence",
            "Blasphemes or mocks God",
            "Attributes God's work to others",
            "Contradicts God's character",
            "Promotes sin and corruption",
            "Leads people away from God",
            "Uses God's name in vain",
            "Rebels against divine law",
            "Takes credit for God's blessings",
            "Perverts sacred things",
            "Teaches false doctrine about God",
            "Lives as if God doesn't matter"
        ]
    
    def evaluate_glory_to_god(self, content: str, context: Dict[str, Any] = None) -> GloryEvaluation:
        """Evaluate how well something brings glory to God"""
        if context is None:
            context = {}
        
        content_lower = content.lower()
        
        # Calculate glory level and score
        glory_score = 0.0
        attributes_glorified = []
        attributes_dishonored = []
        specific_ways = []
        
        # Check for glory indicators
        for indicator in self.glory_indicators:
            if any(word in content_lower for word in indicator.lower().split()[:3]):
                glory_score += 0.1
                specific_ways.append(f"Shows: {indicator}")
        
        # Check for dishonor indicators
        for indicator in self.dishonor_indicators:
            if any(word in content_lower for word in indicator.lower().split()[:3]):
                glory_score -= 0.15
                specific_ways.append(f"Concerns: {indicator}")
        
        # Check specific God attributes
        for attribute in self.god_attributes:
            attribute_score = self._evaluate_attribute_glorification(content_lower, attribute)
            if attribute_score > 0.3:
                attributes_glorified.append(attribute.attribute_name)
                glory_score += attribute_score * 0.2
            elif attribute_score < -0.3:
                attributes_dishonored.append(attribute.attribute_name)
                glory_score += attribute_score * 0.2
        
        # Normalize score to -1.0 to 1.0 range
        glory_score = max(-1.0, min(1.0, glory_score))
        
        # Determine glory level
        if glory_score >= 0.6:
            glory_level = GloryLevel.GLORIFIES_GOD
        elif glory_score >= 0.3:
            glory_level = GloryLevel.HONORS_GOD
        elif glory_score >= 0.1:
            glory_level = GloryLevel.ACKNOWLEDGES_GOD
        elif glory_score >= -0.2:
            glory_level = GloryLevel.NEUTRAL_SECULAR
        else:
            glory_level = GloryLevel.DISHONORS_GOD
        
        # Generate improvement suggestions
        improvement_suggestions = self._generate_improvement_suggestions(
            glory_level, attributes_glorified, attributes_dishonored
        )
        
        # Generate eternal perspective
        eternal_perspective = self._generate_eternal_perspective(glory_level, content)
        
        return GloryEvaluation(
            glory_level=glory_level,
            glory_score=glory_score,
            attributes_glorified=attributes_glorified,
            attributes_dishonored=attributes_dishonored,
            specific_ways_glorified=specific_ways,
            improvement_suggestions=improvement_suggestions,
            eternal_perspective=eternal_perspective
        )
    
    def _evaluate_attribute_glorification(self, content_lower: str, attribute: GloryAttribute) -> float:
        """Evaluate how well content glorifies a specific attribute of God"""
        score = 0.0
        
        # Check for recognition indicators (positive)
        for indicator in attribute.recognition_indicators:
            if any(word in content_lower for word in indicator.lower().split()[:3]):
                score += 0.25
        
        # Check for how_to_glorify alignment
        for way in attribute.how_to_glorify:
            if any(word in content_lower for word in way.lower().split()[:3]):
                score += 0.2
        
        # Check for opposite behaviors (negative)
        for opposite in attribute.opposite_behaviors:
            if any(word in content_lower for word in opposite.lower().split()[:3]):
                score -= 0.3
        
        return max(-1.0, min(1.0, score))
    
    def _generate_improvement_suggestions(self, glory_level: GloryLevel, 
                                        glorified: List[str], dishonored: List[str]) -> List[str]:
        """Generate suggestions for how to better bring glory to God"""
        suggestions = []
        
        if glory_level == GloryLevel.DISHONORS_GOD:
            suggestions.extend([
                "Remove content that mocks or denies God",
                "Acknowledge God as the source of all good things",
                "Replace destructive messages with uplifting truth"
            ])
        
        elif glory_level == GloryLevel.NEUTRAL_SECULAR:
            suggestions.extend([
                "Find ways to acknowledge God's role or presence",
                "Connect content to eternal principles",
                "Show gratitude for divine blessings"
            ])
        
        elif glory_level in [GloryLevel.ACKNOWLEDGES_GOD, GloryLevel.HONORS_GOD]:
            suggestions.extend([
                "More explicitly point others toward God",
                "Demonstrate additional divine attributes",
                "Include testimony of God's goodness"
            ])
        
        # Add specific attribute suggestions
        all_attributes = [attr.attribute_name for attr in self.god_attributes]
        missing_attributes = set(all_attributes) - set(glorified)
        
        if missing_attributes:
            sample_missing = list(missing_attributes)[:2]
            suggestions.extend([
                f"Consider ways to reflect God's {attr.lower()}" for attr in sample_missing
            ])
        
        return suggestions[:5]  # Limit to top 5 suggestions
    
    def _generate_eternal_perspective(self, glory_level: GloryLevel, content: str) -> str:
        """Generate eternal perspective on bringing glory to God"""
        if glory_level == GloryLevel.GLORIFIES_GOD:
            return ("This content aligns with our eternal purpose to glorify God. "
                   "It will contribute to building God's kingdom and bringing souls to Christ.")
        
        elif glory_level == GloryLevel.HONORS_GOD:
            return ("This content shows respect for God and can be part of honoring Him. "
                   "With small adjustments, it could more powerfully glorify God.")
        
        elif glory_level == GloryLevel.ACKNOWLEDGES_GOD:
            return ("This content recognizes God's existence but could do more to actively glorify Him. "
                   "Consider how to make God's character more evident.")
        
        elif glory_level == GloryLevel.NEUTRAL_SECULAR:
            return ("This content is spiritually neutral. While not harmful, it misses opportunities "
                   "to point others toward God and His glory.")
        
        else:  # DISHONORS_GOD
            return ("This content actively works against God's glory and eternal purposes. "
                   "It may lead souls away from God rather than toward Him.")
    
    def generate_glory_report(self, content: str, context: Dict[str, Any] = None) -> str:
        """Generate a comprehensive report on how content brings glory to God"""
        evaluation = self.evaluate_glory_to_god(content, context)
        
        report = f"🙌 GLORY TO GOD EVALUATION\n"
        report += "=" * 50 + "\n\n"
        
        report += f"📊 CONTENT: {content[:100]}{'...' if len(content) > 100 else ''}\n\n"
        
        # Glory level and score
        report += f"✨ GLORY LEVEL: {evaluation.glory_level.name}\n"
        report += f"📈 GLORY SCORE: {evaluation.glory_score:.2f}/1.0\n\n"
        
        # Attributes glorified
        if evaluation.attributes_glorified:
            report += f"🌟 GOD'S ATTRIBUTES GLORIFIED:\n"
            for attr in evaluation.attributes_glorified:
                report += f"• {attr}\n"
            report += "\n"
        
        # Attributes dishonored
        if evaluation.attributes_dishonored:
            report += f"⚠️ GOD'S ATTRIBUTES DISHONORED:\n"
            for attr in evaluation.attributes_dishonored:
                report += f"• {attr}\n"
            report += "\n"
        
        # Specific ways glorified
        if evaluation.specific_ways_glorified:
            report += f"🎯 SPECIFIC WAYS:\n"
            for way in evaluation.specific_ways_glorified[:5]:
                report += f"• {way}\n"
            report += "\n"
        
        # Improvement suggestions
        if evaluation.improvement_suggestions:
            report += f"💡 SUGGESTIONS TO BETTER GLORIFY GOD:\n"
            for suggestion in evaluation.improvement_suggestions:
                report += f"• {suggestion}\n"
            report += "\n"
        
        # Eternal perspective
        report += f"🌅 ETERNAL PERSPECTIVE:\n{evaluation.eternal_perspective}\n\n"
        
        # Biblical foundation
        report += f"📖 BIBLICAL FOUNDATION:\n"
        report += f"'So whether you eat or drink or whatever you do, do it all for the glory of God.' - 1 Corinthians 10:31\n"
        report += f"'The chief end of man is to glorify God and enjoy Him forever.' - Westminster Catechism\n"
        
        return report

# Example usage and integration
def demonstrate_glory_evaluation():
    """Demonstrate the Glory to God evaluation system"""
    evaluator = GloryToGodEvaluator()
    
    print("🙌 GLORY TO GOD EVALUATION SYSTEM")
    print("=" * 60)
    print("Based on 1 Corinthians 10:31 - 'Do it all for the glory of God'\n")
    
    # Example content to evaluate
    examples = [
        "This amazing discovery shows how wonderfully God designed the universe",
        "I helped my neighbor fix their roof without expecting anything in return",
        "Science proves there is no God and religion is just superstition",
        "The stock market went up today",
        "Through Christ's strength, I was able to overcome this addiction"
    ]
    
    for example in examples:
        print(f"🔍 EVALUATING: {example}")
        print("-" * 50)
        
        report = evaluator.generate_glory_report(example)
        print(report)
        print("=" * 60 + "\n")

if __name__ == "__main__":
    demonstrate_glory_evaluation()
