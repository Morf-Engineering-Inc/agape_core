
"""
SeekGood Evaluation System
Evaluates literature, media, books, and ideas against Gospel standards of goodness
Based on LDS Article of Faith 13 and Philippians 4:8 - seeking "anything of good report"
"""

from dataclasses import dataclass
from typing import List, Dict, Any, Optional
from enum import Enum
import logging

# Import from existing truth foundation
from .gospel_definitions import GospelDefinitions
from .core_truths import TruthFoundation
from .atonement_supreme import AtonementSupremeTruth

logger = logging.getLogger(__name__)

class ContentCategory(Enum):
    BOOK = "book"
    MOVIE = "movie"
    MUSIC = "music"
    ART = "art"
    IDEA = "idea"
    ARTICLE = "article"
    DOCUMENTARY = "documentary"

class GoodnessLevel(Enum):
    EXCELLENT = 5      # Highly recommended - exemplifies Gospel virtues
    GOOD = 4          # Recommended - aligns well with Gospel principles
    MIXED = 3         # Use discernment - contains both good and concerning elements
    QUESTIONABLE = 2  # Caution advised - more concerning than beneficial
    AVOID = 1         # Not recommended - contrary to Gospel goodness

@dataclass
class SeekGoodCriteria:
    """The 8 criteria from Philippians 4:8 and Article of Faith 13"""
    true: float = 0.0          # "whatsoever things are true"
    honest: float = 0.0        # "whatsoever things are honest"
    just: float = 0.0          # "whatsoever things are just"
    pure: float = 0.0          # "whatsoever things are pure"
    lovely: float = 0.0        # "whatsoever things are lovely"
    good_report: float = 0.0   # "whatsoever things are of good report"
    virtuous: float = 0.0      # "if there be any virtue"
    praiseworthy: float = 0.0  # "if there be anything worthy of praise"

@dataclass
class ContentEvaluation:
    """Complete evaluation of content for goodness"""
    title: str
    category: ContentCategory
    description: str
    seek_good_scores: SeekGoodCriteria
    overall_goodness: GoodnessLevel
    goodness_score: float  # 0.0 - 5.0
    positive_elements: List[str]
    concerning_elements: List[str]
    gospel_alignment: Dict[str, Any]
    recommendation: str
    good_report_summary: str
    discussion_questions: List[str]

class SeekGoodEvaluator:
    """
    Main evaluation engine for determining if content meets Gospel standards of goodness
    """
    
    def __init__(self):
        self.gospel_definitions = GospelDefinitions()
        self.truth_foundation = TruthFoundation()
        self.atonement_supreme = AtonementSupremeTruth()
        
        # Initialize evaluation patterns
        self._initialize_goodness_patterns()
    
    def _initialize_goodness_patterns(self):
        """Initialize patterns for evaluating the 8 criteria of goodness"""
        self.goodness_patterns = {
            "true": {
                "positive": ["accurate", "factual", "honest", "reliable", "authentic", "genuine", "verified"],
                "negative": ["false", "deceptive", "misleading", "fabricated", "propaganda", "lies"]
            },
            "honest": {
                "positive": ["integrity", "transparent", "sincere", "trustworthy", "forthright", "candid"],
                "negative": ["dishonest", "manipulative", "deceitful", "hidden agenda", "propaganda"]
            },
            "just": {
                "positive": ["fair", "righteous", "equitable", "moral", "ethical", "principled"],
                "negative": ["unfair", "biased", "prejudiced", "discriminatory", "unjust", "corrupt"]
            },
            "pure": {
                "positive": ["clean", "innocent", "wholesome", "modest", "chaste", "moral"],
                "negative": ["impure", "vulgar", "crude", "sexual", "profane", "obscene"]
            },
            "lovely": {
                "positive": ["beautiful", "uplifting", "inspiring", "peaceful", "harmonious", "elegant"],
                "negative": ["ugly", "depressing", "disturbing", "chaotic", "violent", "grotesque"]
            },
            "good_report": {
                "positive": ["reputable", "respected", "acclaimed", "beneficial", "constructive", "positive"],
                "negative": ["notorious", "controversial", "harmful", "destructive", "negative influence"]
            },
            "virtuous": {
                "positive": ["moral excellence", "courage", "temperance", "justice", "wisdom", "charity"],
                "negative": ["vice", "corruption", "selfishness", "greed", "pride", "hatred"]
            },
            "praiseworthy": {
                "positive": ["excellent", "admirable", "commendable", "noteworthy", "exemplary", "meritorious"],
                "negative": ["shameful", "disgraceful", "contemptible", "unworthy", "deplorable"]
            }
        }
    
    def evaluate_content(self, title: str, category: ContentCategory, description: str, 
                        additional_context: Dict[str, Any] = None) -> ContentEvaluation:
        """
        Main evaluation function that applies Gospel standards of goodness
        """
        if additional_context is None:
            additional_context = {}
        
        logger.info(f"Evaluating {category.value}: {title}")
        
        # Evaluate against the 8 criteria
        seek_good_scores = self._evaluate_seek_good_criteria(description, additional_context)
        
        # Calculate overall goodness
        overall_score = self._calculate_overall_goodness(seek_good_scores)
        goodness_level = self._determine_goodness_level(overall_score)
        
        # Identify specific elements
        positive_elements = self._identify_positive_elements(description, additional_context)
        concerning_elements = self._identify_concerning_elements(description, additional_context)
        
        # Get Gospel alignment
        gospel_alignment = self.gospel_definitions.evaluate_goodness(
            f"Consuming {category.value}: {title} - {description}", 
            additional_context
        )
        
        # Generate recommendation and summary
        recommendation = self._generate_recommendation(goodness_level, overall_score, category)
        good_report_summary = self._generate_good_report_summary(title, seek_good_scores, positive_elements)
        discussion_questions = self._generate_discussion_questions(title, category, seek_good_scores)
        
        return ContentEvaluation(
            title=title,
            category=category,
            description=description,
            seek_good_scores=seek_good_scores,
            overall_goodness=goodness_level,
            goodness_score=overall_score,
            positive_elements=positive_elements,
            concerning_elements=concerning_elements,
            gospel_alignment=gospel_alignment,
            recommendation=recommendation,
            good_report_summary=good_report_summary,
            discussion_questions=discussion_questions
        )
    
    def _evaluate_seek_good_criteria(self, description: str, context: Dict[str, Any]) -> SeekGoodCriteria:
        """Evaluate content against the 8 criteria from Philippians 4:8"""
        description_lower = description.lower()
        context_text = " ".join(str(v) for v in context.values()).lower()
        full_text = f"{description_lower} {context_text}"
        
        scores = {}
        
        for criterion, patterns in self.goodness_patterns.items():
            positive_count = sum(1 for word in patterns["positive"] if word in full_text)
            negative_count = sum(1 for word in patterns["negative"] if word in full_text)
            
            # Calculate score (0.0 to 1.0)
            if positive_count + negative_count == 0:
                score = 0.5  # Neutral if no indicators
            else:
                score = positive_count / (positive_count + negative_count)
            
            scores[criterion] = score
        
        return SeekGoodCriteria(**scores)
    
    def _calculate_overall_goodness(self, scores: SeekGoodCriteria) -> float:
        """Calculate overall goodness score (0.0 - 5.0)"""
        # Weight the criteria (some are more important)
        weights = {
            'true': 1.2,        # Truth is foundational
            'honest': 1.1,      # Honesty is crucial
            'just': 1.1,        # Justice matters
            'pure': 1.3,        # Purity is highly valued
            'lovely': 0.9,      # Beauty is important but secondary
            'good_report': 1.0, # Reputation matters
            'virtuous': 1.2,    # Virtue is essential
            'praiseworthy': 1.0 # Excellence is good
        }
        
        total_weighted_score = 0
        total_weight = 0
        
        for criterion, weight in weights.items():
            score = getattr(scores, criterion)
            total_weighted_score += score * weight
            total_weight += weight
        
        average_score = total_weighted_score / total_weight
        return average_score * 5.0  # Scale to 0-5
    
    def _determine_goodness_level(self, score: float) -> GoodnessLevel:
        """Determine goodness level based on score"""
        if score >= 4.0:
            return GoodnessLevel.EXCELLENT
        elif score >= 3.2:
            return GoodnessLevel.GOOD
        elif score >= 2.4:
            return GoodnessLevel.MIXED
        elif score >= 1.6:
            return GoodnessLevel.QUESTIONABLE
        else:
            return GoodnessLevel.AVOID
    
    def _identify_positive_elements(self, description: str, context: Dict[str, Any]) -> List[str]:
        """Identify specific positive elements"""
        positive_elements = []
        full_text = f"{description} {' '.join(str(v) for v in context.values())}".lower()
        
        positive_indicators = {
            "Teaches moral lessons": ["moral", "lesson", "virtue", "character", "integrity"],
            "Promotes family values": ["family", "marriage", "children", "parents", "love"],
            "Inspires hope and faith": ["hope", "faith", "believe", "inspire", "uplift"],
            "Shows consequences of choices": ["consequence", "choice", "decision", "result", "outcome"],
            "Demonstrates service": ["service", "help", "charity", "kindness", "sacrifice"],
            "Portrays heroic virtue": ["hero", "courage", "brave", "noble", "righteous"],
            "Creates beauty": ["beautiful", "artistic", "creative", "aesthetic", "harmony"],
            "Seeks truth": ["truth", "seek", "discover", "learn", "wisdom"]
        }
        
        for element, keywords in positive_indicators.items():
            if any(keyword in full_text for keyword in keywords):
                positive_elements.append(element)
        
        return positive_elements
    
    def _identify_concerning_elements(self, description: str, context: Dict[str, Any]) -> List[str]:
        """Identify specific concerning elements"""
        concerning_elements = []
        full_text = f"{description} {' '.join(str(v) for v in context.values())}".lower()
        
        concerning_indicators = {
            "Contains explicit content": ["explicit", "graphic", "sexual", "nudity", "inappropriate"],
            "Promotes moral relativism": ["relative", "subjective", "no absolute", "your truth"],
            "Glorifies violence": ["violence", "killing", "murder", "torture", "brutality"],
            "Mocks faith or religion": ["mock", "ridicule", "religion", "faith", "god", "stupid"],
            "Promotes rebellion": ["rebel", "authority", "disobey", "reject", "revolution"],
            "Normalizes harmful behavior": ["normalize", "acceptable", "natural", "everyone does"],
            "Creates addiction patterns": ["addictive", "binge", "obsessive", "compulsive"],
            "Spreads fear or despair": ["fear", "despair", "hopeless", "doom", "anxiety"]
        }
        
        for element, keywords in concerning_indicators.items():
            if any(keyword in full_text for keyword in keywords):
                concerning_elements.append(element)
        
        return concerning_elements
    
    def _generate_recommendation(self, level: GoodnessLevel, score: float, category: ContentCategory) -> str:
        """Generate specific recommendation based on evaluation"""
        recommendations = {
            GoodnessLevel.EXCELLENT: f"✅ HIGHLY RECOMMENDED: This {category.value} exemplifies Gospel virtues and is excellent for personal growth and family enjoyment.",
            GoodnessLevel.GOOD: f"👍 RECOMMENDED: This {category.value} aligns well with Gospel principles and can be enjoyed with confidence.",
            GoodnessLevel.MIXED: f"⚠️ USE DISCERNMENT: This {category.value} contains both good and concerning elements. Great for discussion about applying Gospel standards.",
            GoodnessLevel.QUESTIONABLE: f"⚡ CAUTION ADVISED: This {category.value} has more concerning than beneficial elements. Only consume with strong Gospel foundation.",
            GoodnessLevel.AVOID: f"🚨 NOT RECOMMENDED: This {category.value} does not meet Gospel standards of goodness and should be avoided."
        }
        
        base_rec = recommendations[level]
        
        # Add specific guidance based on category
        if category == ContentCategory.BOOK:
            base_rec += " Consider reading with family or study group for added benefit."
        elif category == ContentCategory.MOVIE:
            base_rec += " Preview before family viewing if needed."
        elif category == ContentCategory.IDEA:
            base_rec += " Test this idea against Gospel truth before implementing."
        
        return base_rec
    
    def _generate_good_report_summary(self, title: str, scores: SeekGoodCriteria, 
                                    positive_elements: List[str]) -> str:
        """Generate summary for 'good report' purposes"""
        summary = f"GOOD REPORT ANALYSIS: '{title}'\n\n"
        
        # Highlight strongest criteria
        criteria_scores = {
            "Truth": scores.true,
            "Honesty": scores.honest,
            "Justice": scores.just,
            "Purity": scores.pure,
            "Loveliness": scores.lovely,
            "Good Report": scores.good_report,
            "Virtue": scores.virtuous,
            "Praiseworthiness": scores.praiseworthy
        }
        
        top_criteria = sorted(criteria_scores.items(), key=lambda x: x[1], reverse=True)[:3]
        
        summary += "📊 STRONGEST QUALITIES:\n"
        for criterion, score in top_criteria:
            percentage = int(score * 100)
            summary += f"• {criterion}: {percentage}%\n"
        
        if positive_elements:
            summary += f"\n✅ POSITIVE ELEMENTS:\n"
            for element in positive_elements[:3]:
                summary += f"• {element}\n"
        
        return summary
    
    def _generate_discussion_questions(self, title: str, category: ContentCategory, 
                                     scores: SeekGoodCriteria) -> List[str]:
        """Generate discussion questions for families/groups"""
        questions = [
            f"How does '{title}' align with the standard 'if there be anything virtuous, lovely, or of good report'?",
            f"What can we learn from this {category.value} that helps us become better disciples of Christ?",
            "Which of the 8 criteria (true, honest, just, pure, lovely, good report, virtuous, praiseworthy) does this exemplify best?"
        ]
        
        # Add category-specific questions
        if category == ContentCategory.BOOK:
            questions.append("How do the ideas in this book align with Gospel truth?")
        elif category == ContentCategory.MOVIE:
            questions.append("What values and worldviews are being promoted in this film?")
        elif category == ContentCategory.IDEA:
            questions.append("How can we test this idea against revealed truth?")
        
        return questions

    def evaluate_1001_ideas_example(self) -> ContentEvaluation:
        """Example evaluation of '1001 Ideas' book"""
        return self.evaluate_content(
            title="1001 Ideas That Changed the Way We Think",
            category=ContentCategory.BOOK,
            description="A comprehensive collection of history's most influential ideas, concepts, and discoveries that have shaped human civilization and thought",
            additional_context={
                "genre": "Philosophy/History of Ideas",
                "target_audience": "General adult education",
                "content_focus": "Intellectual history and important concepts",
                "approach": "Educational survey of significant ideas"
            }
        )

# Example usage and integration with Truth Rivers system
def demonstrate_seekgood_system():
    """Demonstrate the SeekGood evaluation system"""
    evaluator = SeekGoodEvaluator()
    
    # Example: Evaluate "1001 Ideas" book
    print("🔍 SEEKGOOD EVALUATION SYSTEM")
    print("=" * 50)
    
    evaluation = evaluator.evaluate_1001_ideas_example()
    
    print(f"📚 BOOK: {evaluation.title}")
    print(f"🎯 GOODNESS LEVEL: {evaluation.overall_goodness.name}")
    print(f"📊 GOODNESS SCORE: {evaluation.goodness_score:.2f}/5.0")
    
    print(f"\n📋 SEEK GOOD CRITERIA SCORES:")
    criteria_dict = evaluation.seek_good_scores.__dict__
    for criterion, score in criteria_dict.items():
        percentage = int(score * 100)
        print(f"• {criterion.replace('_', ' ').title()}: {percentage}%")
    
    print(f"\n✅ POSITIVE ELEMENTS:")
    for element in evaluation.positive_elements:
        print(f"• {element}")
    
    print(f"\n💡 RECOMMENDATION:")
    print(evaluation.recommendation)
    
    print(f"\n📖 GOOD REPORT SUMMARY:")
    print(evaluation.good_report_summary)
    
    return evaluation

if __name__ == "__main__":
    demonstrate_seekgood_system()
