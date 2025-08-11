
"""
Truth Discerner - Media Analysis Engine
Evaluates movies, books, and cultural content against biblical truth standards
"""

from dataclasses import dataclass
from typing import Dict, List, Optional, Any
from enum import Enum
import logging

# Import from parent Agape Core
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from truth_foundation.gospel_truth import GospelTruthEngine
    from truth_foundation.core_truths import TruthFoundation, TruthLevel
except ImportError:
    # Fallback if modules not available
    GospelTruthEngine = None
    TruthFoundation = None

logger = logging.getLogger(__name__)

class ContentType(Enum):
    MOVIE = "movie"
    TV_SHOW = "tv_show"
    BOOK = "book"
    SOCIAL_MEDIA = "social_media"
    NEWS_ARTICLE = "news_article"
    MUSIC = "music"
    VIDEO_GAME = "video_game"

class TruthAlignment(Enum):
    PURE_TRUTH = 4      # Aligns with biblical principles
    MIXED_TRUTH = 3     # Good elements with concerning messages
    DECEPTIVE = 2       # Contrary to biblical truth
    ACTIVELY_HARMFUL = 1 # Designed to undermine faith

@dataclass
class ContentElement:
    """Represents an element of content for analysis"""
    title: str
    description: str
    content_type: ContentType
    target_audience: str
    cultural_influence: str
    key_themes: List[str]
    explicit_messages: List[str]
    implicit_messages: List[str]

@dataclass
class WorldviewIndicator:
    """Identifies specific worldview being promoted"""
    worldview_type: str
    evidence: List[str]
    strength: float  # 0.0 to 1.0
    impact_level: str

@dataclass
class TruthDiscernmentReport:
    """Comprehensive analysis report"""
    content_title: str
    truth_score: int  # 0-100
    truth_alignment: TruthAlignment
    positive_elements: List[str]
    concerning_elements: List[str]
    biblical_parallels: List[str]
    worldview_analysis: List[WorldviewIndicator]
    cultural_impact: str
    recommendation: str
    discussion_questions: List[str]
    gospel_evaluation: Dict[str, Any]

class MediaAnalyzer:
    """
    Core engine for analyzing media content against biblical truth standards
    """
    
    def __init__(self):
        self.gospel_engine = GospelTruthEngine() if GospelTruthEngine else None
        self.truth_foundation = TruthFoundation() if TruthFoundation else None
        
        # Initialize worldview detection patterns
        self._initialize_worldview_patterns()
        
        # Initialize biblical themes
        self._initialize_biblical_themes()
    
    def _initialize_worldview_patterns(self):
        """Initialize patterns for detecting different worldviews"""
        self.worldview_patterns = {
            "secular_humanism": [
                "human reason ultimate authority",
                "science explains everything",
                "religion is outdated",
                "humans decide morality",
                "progress through reason alone"
            ],
            "materialism": [
                "only physical world exists",
                "no afterlife or spirit",
                "consciousness from brain only",
                "meaning from matter alone",
                "death is final end"
            ],
            "relativism": [
                "your truth my truth",
                "no absolute morality",
                "all views equally valid",
                "cultural determines truth",
                "tolerance above truth"
            ],
            "hedonism": [
                "pleasure is life purpose",
                "avoid pain seek pleasure",
                "instant gratification good",
                "self-indulgence promoted",
                "consequences don't matter"
            ],
            "progressive_ideology": [
                "traditional values oppressive",
                "constant change is progress",
                "past was worse than present",
                "authority structures unjust",
                "revolution brings improvement"
            ],
            "new_age_spirituality": [
                "you are your own god",
                "create your own reality",
                "all paths lead to god",
                "inner divinity concept",
                "karma and reincarnation"
            ]
        }
    
    def _initialize_biblical_themes(self):
        """Initialize biblical themes for positive identification"""
        self.biblical_themes = {
            "love_and_sacrifice": [
                "self-sacrifice for others",
                "unconditional love",
                "putting others first",
                "redemptive suffering",
                "laying down life for friends"
            ],
            "truth_and_honesty": [
                "truth matters",
                "honesty in relationships",
                "integrity under pressure",
                "speaking truth in love",
                "transparency and authenticity"
            ],
            "justice_and_mercy": [
                "fighting for the oppressed",
                "mercy toward enemies",
                "forgiveness after wrong",
                "protection of innocent",
                "fairness and equality"
            ],
            "faith_and_hope": [
                "trust in higher power",
                "hope in difficult times",
                "faith over sight",
                "perseverance through trial",
                "purpose beyond circumstances"
            ],
            "wisdom_and_humility": [
                "learning from mistakes",
                "seeking wise counsel",
                "admitting when wrong",
                "respecting authority",
                "growing in understanding"
            ]
        }
    
    def analyze_content(self, content: ContentElement) -> TruthDiscernmentReport:
        """
        Main analysis function that evaluates content against biblical truth
        """
        logger.info(f"Analyzing content: {content.title}")
        
        # Perform various analysis components
        positive_elements = self._identify_positive_elements(content)
        concerning_elements = self._identify_concerning_elements(content)
        biblical_parallels = self._find_biblical_parallels(content)
        worldview_analysis = self._analyze_worldviews(content)
        truth_score = self._calculate_truth_score(content, positive_elements, concerning_elements)
        truth_alignment = self._determine_truth_alignment(truth_score)
        
        # Get Gospel-specific evaluation if available
        gospel_evaluation = {}
        if self.gospel_engine:
            context = {
                "content_type": content.content_type.value,
                "themes": content.key_themes,
                "messages": content.explicit_messages + content.implicit_messages
            }
            gospel_evaluation = self.gospel_engine.evaluate_against_gospel(
                f"Consuming media with themes: {', '.join(content.key_themes)}", 
                context
            )
        
        # Generate recommendations and discussion questions
        recommendation = self._generate_recommendation(truth_score, truth_alignment, content)
        discussion_questions = self._generate_discussion_questions(content, positive_elements, concerning_elements)
        
        return TruthDiscernmentReport(
            content_title=content.title,
            truth_score=truth_score,
            truth_alignment=truth_alignment,
            positive_elements=positive_elements,
            concerning_elements=concerning_elements,
            biblical_parallels=biblical_parallels,
            worldview_analysis=worldview_analysis,
            cultural_impact=content.cultural_influence,
            recommendation=recommendation,
            discussion_questions=discussion_questions,
            gospel_evaluation=gospel_evaluation
        )
    
    def _identify_positive_elements(self, content: ContentElement) -> List[str]:
        """Identify elements that align with biblical truth"""
        positive_elements = []
        
        # Check for biblical themes in content
        all_content = " ".join([
            content.description,
            " ".join(content.key_themes),
            " ".join(content.explicit_messages),
            " ".join(content.implicit_messages)
        ]).lower()
        
        for theme_name, patterns in self.biblical_themes.items():
            for pattern in patterns:
                if any(word in all_content for word in pattern.lower().split()):
                    positive_elements.append(f"Promotes {theme_name.replace('_', ' ')}: {pattern}")
                    break
        
        return list(set(positive_elements))
    
    def _identify_concerning_elements(self, content: ContentElement) -> List[str]:
        """Identify elements that contradict biblical truth"""
        concerning_elements = []
        
        all_content = " ".join([
            content.description,
            " ".join(content.key_themes),
            " ".join(content.explicit_messages),
            " ".join(content.implicit_messages)
        ]).lower()
        
        # Check for anti-biblical patterns
        concerning_patterns = [
            ("Violence as primary solution", ["violence solves problems", "killing is heroic", "revenge is justified"]),
            ("Sexual immorality normalized", ["casual sex", "adultery", "promiscuity", "sexual liberation"]),
            ("Authority rebellion promoted", ["reject all authority", "parents are wrong", "rebellion is good"]),
            ("Materialism emphasized", ["money brings happiness", "possessions define worth", "greed is good"]),
            ("Occult/supernatural powers", ["magic", "witchcraft", "supernatural powers", "dark forces"]),
            ("Mockery of faith", ["religion is stupid", "believers are fools", "faith is weakness"])
        ]
        
        for concern_name, patterns in concerning_patterns:
            for pattern in patterns:
                if pattern in all_content:
                    concerning_elements.append(f"{concern_name}: {pattern}")
                    break
        
        return concerning_elements
    
    def _find_biblical_parallels(self, content: ContentElement) -> List[str]:
        """Find biblical parallels and connections"""
        parallels = []
        
        # Common biblical narrative patterns
        narrative_patterns = {
            "redemption story": "Christ's redemption of humanity",
            "sacrifice for others": "Greater love has no one than this (John 15:13)",
            "truth revelation": "Truth sets you free (John 8:32)",
            "forgiveness theme": "Forgive as you have been forgiven (Ephesians 4:32)",
            "good vs evil": "Light vs. darkness (John 1:5)",
            "transformation": "New creation in Christ (2 Corinthians 5:17)",
            "suffering with purpose": "All things work together for good (Romans 8:28)"
        }
        
        all_content = " ".join([
            content.description,
            " ".join(content.key_themes)
        ]).lower()
        
        for pattern, verse in narrative_patterns.items():
            if any(word in all_content for word in pattern.split()):
                parallels.append(f"{pattern.title()}: {verse}")
        
        return parallels
    
    def _analyze_worldviews(self, content: ContentElement) -> List[WorldviewIndicator]:
        """Detect and analyze worldviews promoted in content"""
        worldviews = []
        
        all_content = " ".join([
            content.description,
            " ".join(content.key_themes),
            " ".join(content.explicit_messages),
            " ".join(content.implicit_messages)
        ]).lower()
        
        for worldview_type, patterns in self.worldview_patterns.items():
            evidence = []
            matches = 0
            
            for pattern in patterns:
                if any(word in all_content for word in pattern.split()):
                    evidence.append(pattern)
                    matches += 1
            
            if matches > 0:
                strength = min(1.0, matches / len(patterns))
                impact_level = "High" if strength > 0.6 else "Medium" if strength > 0.3 else "Low"
                
                worldviews.append(WorldviewIndicator(
                    worldview_type=worldview_type.replace('_', ' ').title(),
                    evidence=evidence,
                    strength=strength,
                    impact_level=impact_level
                ))
        
        return worldviews
    
    def _calculate_truth_score(self, content: ContentElement, positive_elements: List[str], concerning_elements: List[str]) -> int:
        """Calculate overall truth score (0-100)"""
        base_score = 50  # Neutral starting point
        
        # Add points for positive elements
        base_score += len(positive_elements) * 10
        
        # Subtract points for concerning elements
        base_score -= len(concerning_elements) * 15
        
        # Adjust based on content type
        if content.content_type in [ContentType.SOCIAL_MEDIA, ContentType.NEWS_ARTICLE]:
            # Social media and news have higher impact, so stricter standards
            base_score -= 5
        
        # Adjust based on target audience
        if "children" in content.target_audience.lower():
            # Stricter standards for children's content
            base_score -= len(concerning_elements) * 5
        
        return max(0, min(100, base_score))
    
    def _determine_truth_alignment(self, truth_score: int) -> TruthAlignment:
        """Determine truth alignment category based on score"""
        if truth_score >= 80:
            return TruthAlignment.PURE_TRUTH
        elif truth_score >= 60:
            return TruthAlignment.MIXED_TRUTH
        elif truth_score >= 30:
            return TruthAlignment.DECEPTIVE
        else:
            return TruthAlignment.ACTIVELY_HARMFUL
    
    def _generate_recommendation(self, truth_score: int, alignment: TruthAlignment, content: ContentElement) -> str:
        """Generate viewing/consumption recommendation"""
        recommendations = {
            TruthAlignment.PURE_TRUTH: f"✅ RECOMMENDED: This content aligns well with biblical principles and can be enjoyed with confidence.",
            TruthAlignment.MIXED_TRUTH: f"⚠️ USE DISCERNMENT: Contains good elements but also concerning messages. Great for discussion about truth vs. error.",
            TruthAlignment.DECEPTIVE: f"⚡ CAUTION ADVISED: Promotes worldviews contrary to biblical truth. Only consume with strong biblical foundation and critical thinking.",
            TruthAlignment.ACTIVELY_HARMFUL: f"🚨 AVOID: This content actively undermines biblical truth and faith. Not recommended for consumption."
        }
        
        base_recommendation = recommendations[alignment]
        
        # Add specific guidance based on content type
        if content.content_type == ContentType.SOCIAL_MEDIA:
            base_recommendation += " Be especially careful with social media's addictive design and influence on thinking patterns."
        elif "children" in content.target_audience.lower():
            base_recommendation += " Extra caution advised for children's developing worldview."
        
        return base_recommendation
    
    def _generate_discussion_questions(self, content: ContentElement, positive_elements: List[str], concerning_elements: List[str]) -> List[str]:
        """Generate discussion questions for families/groups"""
        questions = [
            f"What worldview does '{content.title}' promote, and how does it compare to a biblical worldview?",
            "Which characters or actions in this content demonstrate biblical virtues? Which ones don't?",
            "How might this content influence someone's thinking about God, relationships, or moral choices?"
        ]
        
        if positive_elements:
            questions.append("What positive messages or biblical parallels can we find in this content?")
        
        if concerning_elements:
            questions.append("What concerning messages does this content promote, and how should we respond as believers?")
        
        if content.content_type == ContentType.SOCIAL_MEDIA:
            questions.append("How does consuming this type of social media content affect our thoughts and behaviors?")
        
        return questions

def analyze_movie_example():
    """Example usage analyzing a movie"""
    # Example: Analyzing "The Matrix" (1999)
    matrix_content = ContentElement(
        title="The Matrix",
        description="A computer hacker discovers reality is a simulation and joins a rebellion to free humanity from machines",
        content_type=ContentType.MOVIE,
        target_audience="Teen and Adult",
        cultural_influence="High - influential sci-fi philosophy",
        key_themes=["reality vs illusion", "choice and free will", "sacrifice for others", "truth seeking"],
        explicit_messages=["Question everything you believe", "The truth will set you free", "Choose difficult truth over comfortable lies"],
        implicit_messages=["Authority structures may be deceptive", "Individual awakening is necessary", "Reality may not be what it seems"]
    )
    
    analyzer = MediaAnalyzer()
    report = analyzer.analyze_content(matrix_content)
    
    print(f"CONTENT: {report.content_title}")
    print(f"TRUTH SCORE: {report.truth_score}/100")
    print(f"ALIGNMENT: {report.truth_alignment.name}")
    print(f"\nPOSITIVE ELEMENTS:")
    for element in report.positive_elements:
        print(f"✅ {element}")
    print(f"\nCONCERNING ELEMENTS:")
    for element in report.concerning_elements:
        print(f"⚠️ {element}")
    print(f"\nBIBLICAL PARALLELS:")
    for parallel in report.biblical_parallels:
        print(f"📖 {parallel}")
    print(f"\nRECOMMENDATION: {report.recommendation}")

if __name__ == "__main__":
    analyze_movie_example()
