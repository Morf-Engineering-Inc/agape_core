
"""
New Testament Story Analyzer
Focuses on analyzing and understanding core NT stories, particularly:
1. The Golden Rule (Matthew 7:12, Luke 6:31)
2. The Good Samaritan (Luke 10:25-37)
"""

from dataclasses import dataclass
from typing import Dict, List, Optional, Any
from enum import Enum
import logging

logger = logging.getLogger(__name__)

class StoryType(Enum):
    PARABLE = "parable"
    TEACHING = "teaching"
    MIRACLE = "miracle"
    HISTORICAL = "historical"

@dataclass
class NTStory:
    """Represents a New Testament story with analysis"""
    title: str
    story_type: StoryType
    scripture_references: List[str]
    context: str
    main_characters: List[str]
    central_message: str
    moral_lessons: List[str]
    practical_applications: List[str]
    cultural_background: str
    connection_to_love_commands: str

@dataclass
class StoryAnalysis:
    """Analysis results for NT stories"""
    story: NTStory
    relevance_score: float
    modern_parallels: List[str]
    application_scenarios: List[str]
    discussion_questions: List[str]
    related_verses: List[str]

class NTStoryAnalyzer:
    """
    Analyzer for New Testament stories with focus on Golden Rule and Good Samaritan
    """
    
    def __init__(self):
        self.core_stories = self._initialize_core_stories()
        self.story_patterns = self._initialize_story_patterns()
    
    def _initialize_core_stories(self) -> Dict[str, NTStory]:
        """Initialize the two core stories for analysis"""
        return {
            "golden_rule": NTStory(
                title="The Golden Rule",
                story_type=StoryType.TEACHING,
                scripture_references=["Matthew 7:12", "Luke 6:31"],
                context="Part of the Sermon on the Mount/Plain - Jesus teaching about relationships",
                main_characters=["Jesus", "Disciples", "Crowd"],
                central_message="Treat others as you would want to be treated",
                moral_lessons=[
                    "Empathy is the foundation of morality",
                    "Active love requires putting yourself in others' shoes",
                    "This principle summarizes the Law and Prophets",
                    "It's a positive command, not just avoiding harm"
                ],
                practical_applications=[
                    "Before speaking, ask: 'How would I want to be spoken to?'",
                    "In business dealings, consider the other person's perspective",
                    "When making decisions affecting others, imagine being in their position",
                    "Practice proactive kindness, not just avoiding meanness",
                    "Use this as a test for all interpersonal actions"
                ],
                cultural_background="Rabbis had taught negative forms ('don't do to others...'), but Jesus gave the positive, active form",
                connection_to_love_commands="Direct application of 'love your neighbor as yourself' - assumes proper self-love and extends it outward"
            ),
            
            "good_samaritan": NTStory(
                title="The Good Samaritan",
                story_type=StoryType.PARABLE,
                scripture_references=["Luke 10:25-37"],
                context="Response to lawyer's question 'Who is my neighbor?' after discussing the greatest commandments",
                main_characters=[
                    "Lawyer (expert in religious law)",
                    "Jesus",
                    "Traveler (victim)",
                    "Priest",
                    "Levite",
                    "Samaritan"
                ],
                central_message="Your neighbor is anyone in need, regardless of race, religion, or social status",
                moral_lessons=[
                    "Mercy transcends religious and ethnic boundaries",
                    "Actions matter more than religious position",
                    "Love requires sacrifice and inconvenience",
                    "Prejudice can blind us to moral duty",
                    "True neighborliness is shown, not just felt"
                ],
                practical_applications=[
                    "Help those in need regardless of their background",
                    "Don't let religious activity excuse lack of compassion",
                    "Be willing to be inconvenienced to help others",
                    "Challenge your own prejudices and biases",
                    "Look for opportunities to show mercy daily",
                    "Use resources (time, money, skills) to serve others"
                ],
                cultural_background="Jews and Samaritans had deep ethnic and religious hatred; priest and Levite would have religious duties that helping might complicate",
                connection_to_love_commands="Defines 'neighbor' broadly and shows love of neighbor in concrete action - mercy, sacrifice, ongoing care"
            )
        }
    
    def _initialize_story_patterns(self) -> Dict[str, List[str]]:
        """Initialize patterns for identifying story elements"""
        return {
            "love_themes": [
                "compassion", "mercy", "kindness", "care", "sacrifice",
                "empathy", "understanding", "service", "help", "neighbor"
            ],
            "justice_themes": [
                "fairness", "equality", "righteousness", "impartiality",
                "judgment", "law", "right", "wrong", "moral"
            ],
            "practical_action": [
                "do", "act", "help", "serve", "give", "care", "visit",
                "heal", "feed", "clothe", "comfort", "rescue"
            ],
            "universal_application": [
                "all", "everyone", "whoever", "anyone", "every person",
                "all people", "humanity", "world", "nations"
            ]
        }
    
    def analyze_story(self, story_key: str) -> StoryAnalysis:
        """Analyze a specific story and return comprehensive analysis"""
        if story_key not in self.core_stories:
            raise ValueError(f"Story '{story_key}' not found")
        
        story = self.core_stories[story_key]
        
        # Calculate relevance score
        relevance_score = self._calculate_relevance_score(story)
        
        # Generate modern parallels
        modern_parallels = self._generate_modern_parallels(story)
        
        # Generate application scenarios
        application_scenarios = self._generate_application_scenarios(story)
        
        # Generate discussion questions
        discussion_questions = self._generate_discussion_questions(story)
        
        # Find related verses
        related_verses = self._find_related_verses(story)
        
        return StoryAnalysis(
            story=story,
            relevance_score=relevance_score,
            modern_parallels=modern_parallels,
            application_scenarios=application_scenarios,
            discussion_questions=discussion_questions,
            related_verses=related_verses
        )
    
    def _calculate_relevance_score(self, story: NTStory) -> float:
        """Calculate how relevant this story is to modern life"""
        score = 0.0
        
        # Base relevance for core teachings
        if story.title in ["The Golden Rule", "The Good Samaritan"]:
            score += 0.9
        
        # Add points for practical applications
        score += min(0.5, len(story.practical_applications) * 0.1)
        
        # Add points for universal themes
        universal_themes = ["love", "compassion", "mercy", "justice", "equality"]
        for theme in universal_themes:
            if any(theme in lesson.lower() for lesson in story.moral_lessons):
                score += 0.1
        
        return min(1.0, score)
    
    def _generate_modern_parallels(self, story: NTStory) -> List[str]:
        """Generate modern day parallels for the story"""
        if story.title == "The Golden Rule":
            return [
                "Customer service: Treat customers as you'd want to be treated as a customer",
                "Social media: Post only what you'd want posted about you",
                "Workplace conflicts: Address issues as you'd want your issues addressed",
                "Parenting: Discipline children as you'd want to be corrected",
                "Road rage: Drive as you'd want others to drive around your family",
                "Online reviews: Write reviews as fairly as you'd want your business reviewed"
            ]
        
        elif story.title == "The Good Samaritan":
            return [
                "Helping someone of a different political party who's stranded",
                "A Christian helping a Muslim family in crisis",
                "Stopping to help in a 'bad' neighborhood despite personal risk",
                "Religious leaders ignoring homeless while rushing to church",
                "Immigrant helping native-born citizen despite facing discrimination",
                "Atheist showing more practical love than church members"
            ]
        
        return []
    
    def _generate_application_scenarios(self, story: NTStory) -> List[str]:
        """Generate specific scenarios where the story applies"""
        if story.title == "The Golden Rule":
            return [
                "Before sending that harsh email, ask: 'How would I want to receive criticism?'",
                "When tempted to gossip, consider: 'Would I want this said about me?'",
                "In negotiations, think: 'What would feel fair if I were on the other side?'",
                "When disciplining children: 'How did I want to be corrected when I made mistakes?'",
                "In marriage conflicts: 'How would I want my spouse to approach this issue?'"
            ]
        
        elif story.title == "The Good Samaritan":
            return [
                "Stopping to help someone whose car broke down, even when late for church",
                "Caring for a difficult neighbor who everyone else avoids",
                "Helping someone from a group you politically disagree with",
                "Using your skills/resources to help someone who can't repay you",
                "Showing ongoing care, not just one-time help"
            ]
        
        return []
    
    def _generate_discussion_questions(self, story: NTStory) -> List[str]:
        """Generate thought-provoking questions about the story"""
        if story.title == "The Golden Rule":
            return [
                "How does this principle challenge modern 'looking out for #1' mentality?",
                "What's the difference between the Golden Rule and just being 'nice'?",
                "How do we apply this when we have different preferences than others?",
                "Why did Jesus make this the summary of 'the Law and Prophets'?",
                "How does proper self-love enable us to love others well?",
                "What are practical ways to remember this principle in daily life?"
            ]
        
        elif story.title == "The Good Samaritan":
            return [
                "Who are the 'Samaritans' in our society - those we might prejudge?",
                "What 'religious duties' might keep us from showing mercy today?",
                "How do we balance wisdom/safety with the call to help others?",
                "What does it mean that the Samaritan 'had compassion' - emotion vs. action?",
                "How does this parable expand our definition of 'neighbor'?",
                "What would have happened if the Samaritan had just prayed for the victim?"
            ]
        
        return []
    
    def _find_related_verses(self, story: NTStory) -> List[str]:
        """Find related Bible verses that connect to the story's themes"""
        if story.title == "The Golden Rule":
            return [
                "Leviticus 19:18 - Love your neighbor as yourself",
                "Philippians 2:3-4 - Consider others' interests above your own",
                "1 Corinthians 10:24 - Seek the good of others",
                "Romans 12:15 - Rejoice with those who rejoice, weep with those who weep",
                "Galatians 6:2 - Bear one another's burdens"
            ]
        
        elif story.title == "The Good Samaritan":
            return [
                "James 2:14-17 - Faith without works is dead",
                "1 John 3:17-18 - Love in deed and truth, not just words",
                "Matthew 25:35-40 - Whatever you did for the least of these",
                "Galatians 3:28 - No distinction in Christ",
                "Isaiah 58:6-7 - True fasting includes caring for others"
            ]
        
        return []
    
    def compare_stories(self) -> Dict[str, Any]:
        """Compare the two core stories and find connections"""
        golden_rule = self.core_stories["golden_rule"]
        good_samaritan = self.core_stories["good_samaritan"]
        
        comparison = {
            "common_themes": [
                "Love of neighbor",
                "Practical application of love",
                "Moving beyond self-interest",
                "Universal application",
                "Active (not passive) virtue"
            ],
            "differences": {
                "golden_rule": "Universal principle for all relationships",
                "good_samaritan": "Specific example of neighbor love in action"
            },
            "complementary_nature": [
                "Golden Rule provides the principle",
                "Good Samaritan provides the example",
                "Together they show both the 'what' and 'how' of neighbor love",
                "Both expand our understanding beyond traditional boundaries"
            ],
            "practical_integration": [
                "Use Golden Rule to test your motivations",
                "Use Good Samaritan to guide your actions",
                "Both require empathy and sacrifice",
                "Both challenge societal norms and prejudices"
            ]
        }
        
        return comparison
    
    def generate_teaching_outline(self, story_key: str) -> str:
        """Generate a teaching outline for the story"""
        analysis = self.analyze_story(story_key)
        story = analysis.story
        
        outline = f"# Teaching Outline: {story.title}\n\n"
        
        outline += f"## I. Context and Background\n"
        outline += f"- **Scripture:** {', '.join(story.scripture_references)}\n"
        outline += f"- **Setting:** {story.context}\n"
        outline += f"- **Cultural Background:** {story.cultural_background}\n\n"
        
        outline += f"## II. The Story/Teaching\n"
        outline += f"- **Main Characters:** {', '.join(story.main_characters)}\n"
        outline += f"- **Central Message:** {story.central_message}\n\n"
        
        outline += f"## III. Key Lessons\n"
        for i, lesson in enumerate(story.moral_lessons, 1):
            outline += f"{i}. {lesson}\n"
        outline += "\n"
        
        outline += f"## IV. Modern Applications\n"
        for i, app in enumerate(story.practical_applications, 1):
            outline += f"{i}. {app}\n"
        outline += "\n"
        
        outline += f"## V. Modern Parallels\n"
        for i, parallel in enumerate(analysis.modern_parallels, 1):
            outline += f"{i}. {parallel}\n"
        outline += "\n"
        
        outline += f"## VI. Discussion Questions\n"
        for i, question in enumerate(analysis.discussion_questions, 1):
            outline += f"{i}. {question}\n"
        outline += "\n"
        
        outline += f"## VII. Related Scriptures\n"
        for verse in analysis.related_verses:
            outline += f"- {verse}\n"
        outline += "\n"
        
        outline += f"## VIII. Connection to Great Commandments\n"
        outline += f"{story.connection_to_love_commands}\n\n"
        
        return outline
    
    def get_story_summary(self) -> str:
        """Get a comprehensive summary of both stories"""
        comparison = self.compare_stories()
        
        summary = "# The Two Most Common New Testament Stories: Analysis Summary\n\n"
        
        summary += "## Overview\n"
        summary += "The Golden Rule and the Good Samaritan parable represent two of the most frequently referenced and influential teachings from the New Testament. Together, they provide both the principle and practice of Jesus's command to 'love your neighbor as yourself.'\n\n"
        
        summary += "## Why These Two Stories?\n"
        summary += "1. **Universal Recognition** - Known even by non-Christians\n"
        summary += "2. **Practical Application** - Clear guidance for daily life\n"
        summary += "3. **Moral Foundation** - Basis for ethics across cultures\n"
        summary += "4. **Jesus's Priority** - Central to His teaching\n"
        summary += "5. **Timeless Relevance** - Apply to every era and culture\n\n"
        
        summary += "## Common Themes\n"
        for theme in comparison["common_themes"]:
            summary += f"- {theme}\n"
        summary += "\n"
        
        summary += "## How They Work Together\n"
        for point in comparison["complementary_nature"]:
            summary += f"- {point}\n"
        summary += "\n"
        
        summary += "## Practical Integration\n"
        for point in comparison["practical_integration"]:
            summary += f"- {point}\n"
        summary += "\n"
        
        return summary

# Usage example
def demo_analyzer():
    """Demonstrate the NT Story Analyzer"""
    analyzer = NTStoryAnalyzer()
    
    print("=== NEW TESTAMENT STORY ANALYZER ===\n")
    
    # Analyze each story
    for story_key in ["golden_rule", "good_samaritan"]:
        analysis = analyzer.analyze_story(story_key)
        print(f"Story: {analysis.story.title}")
        print(f"Relevance Score: {analysis.relevance_score:.2f}")
        print(f"Central Message: {analysis.story.central_message}")
        print(f"Modern Parallel Example: {analysis.modern_parallels[0] if analysis.modern_parallels else 'None'}")
        print("-" * 50)
    
    # Show comparison
    print("\n=== STORY COMPARISON ===")
    comparison = analyzer.compare_stories()
    print("Common Themes:")
    for theme in comparison["common_themes"][:3]:
        print(f"- {theme}")
    
    # Generate teaching outline for Golden Rule
    print("\n=== SAMPLE TEACHING OUTLINE ===")
    outline = analyzer.generate_teaching_outline("golden_rule")
    print(outline[:500] + "...")

if __name__ == "__main__":
    demo_analyzer()
