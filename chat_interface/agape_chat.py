#!/usr/bin/env python3
"""
Agape Chat Interface - Interactive decision guidance system
Allows users to ask questions and receive Gospel-based decision guidance
"""

import json
import logging
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from datetime import datetime

# Import core Agape system
try:
    from main import AgapeCore, Decision
    from truth_foundation.gospel_truth import GospelTruthEngine
    from value_theory.beta import ValueImpactCalculator
    from human_potential.developmentship import HumanPotentialCalculator
except ImportError:
    # Fallback for testing
    AgapeCore = None

logger = logging.getLogger(__name__)

@dataclass
class ChatMessage:
    """Represents a chat message with metadata"""
    timestamp: datetime
    user_input: str
    ai_response: str
    decision_data: Optional[Dict[str, Any]] = None
    confidence_score: float = 0.0

@dataclass
class QuestionTemplate:
    """Template for guided questions to help users think through decisions"""
    category: str
    question: str
    follow_up_questions: List[str]
    context_hints: List[str]

@dataclass
class QuickAction:
    """Represents a quick action button in the chat interface"""
    action_id: str
    title: str
    description: str
    icon: str
    example_input: str

class AgapeChatInterface:
    """
    Interactive chat interface for Agape Core AI decision-making
    Provides conversational guidance based on Gospel truth and ethical frameworks
    """

    def __init__(self):
        self.agape_core = AgapeCore() if AgapeCore else None
        self.chat_history: List[ChatMessage] = []
        self.current_context: Dict[str, Any] = {}
        self.question_templates = self._initialize_question_templates()
        self.quick_actions = self._initialize_quick_actions()

    def _initialize_question_templates(self) -> List[QuestionTemplate]:
        """Initialize guided question templates"""
        return [
            QuestionTemplate(
                category="Personal Decision",
                question="What personal decision are you facing?",
                follow_up_questions=[
                    "How might this decision affect your relationship with God?",
                    "Who else could be impacted by this choice?",
                    "What are the potential long-term consequences?",
                    "What does your conscience tell you about this?"
                ],
                context_hints=["personal", "individual", "character", "integrity"]
            ),
            QuestionTemplate(
                category="Relationship Issue",
                question="What relationship challenge are you dealing with?",
                follow_up_questions=[
                    "How can you show love and respect in this situation?",
                    "What would it look like to 'love your neighbor as yourself' here?",
                    "How can you pursue peace and reconciliation?",
                    "What boundaries might be needed while still showing love?"
                ],
                context_hints=["family", "friend", "conflict", "forgiveness", "marriage"]
            ),
            QuestionTemplate(
                category="Work/Career Decision",
                question="What work or career decision do you need guidance on?",
                follow_up_questions=[
                    "How does this align with using your talents to serve others?",
                    "What impact will this have on your ability to provide for your family?",
                    "How might this affect your integrity and witness?",
                    "What opportunities does this create to love and serve others?"
                ],
                context_hints=["job", "career", "work", "business", "employment"]
            ),
            QuestionTemplate(
                category="Financial Decision",
                question="What financial decision are you considering?",
                follow_up_questions=[
                    "How does this demonstrate good stewardship?",
                    "What impact will this have on your ability to be generous?",
                    "Are you being motivated by contentment or greed?",
                    "How might this affect your dependence on God vs. money?"
                ],
                context_hints=["money", "purchase", "investment", "giving", "budget"]
            ),
            QuestionTemplate(
                category="Moral Dilemma",
                question="What moral or ethical situation are you facing?",
                follow_up_questions=[
                    "What would happen if everyone made this same choice?",
                    "How does this align with Biblical principles?",
                    "What would Jesus do in this situation?",
                    "How can you choose truth and love simultaneously?"
                ],
                context_hints=["right", "wrong", "ethical", "moral", "conscience"]
            )
        ]

    def _initialize_quick_actions(self) -> List[QuickAction]:
        """Initialize quick action buttons"""
        return [
            QuickAction(
                action_id="discern_truth",
                title="🔍 Discern Truth",
                description="Evaluate content, URLs, or statements for truth alignment",
                icon="🔍",
                example_input="Paste URL or describe content to evaluate"
            ),
            QuickAction(
                action_id="seekgood_media",
                title="📺 SeekGood Media",
                description="Analyze media content against Philippians 4:8 standards",
                icon="📺",
                example_input="Enter movie title, TV show, or media description"
            ),
            QuickAction(
                action_id="family_agenda",
                title="👨‍👩‍👧‍👦 Family Impact",
                description="Analyze content for family agenda alignment",
                icon="👨‍👩‍👧‍👦",
                example_input="Describe content to check against family values"
            ),
            QuickAction(
                action_id="glory_to_god",
                title="✨ Glory to God",
                description="Evaluate if content brings glory to God",
                icon="✨",
                example_input="Enter content to evaluate for God-glorifying elements"
            ),
            QuickAction(
                action_id="system_truth",
                title="⚖️ System Truth",
                description="Analyze what truth laws are in place in a system",
                icon="⚖️",
                example_input="Describe an organization, process, or system"
            ),
            QuickAction(
                action_id="gospel_guidance",
                title="📖 Gospel Guidance",
                description="Get guidance based on Gospel principles",
                icon="📖",
                example_input="Describe your situation or decision"
            )
        ]

    def start_conversation(self) -> str:
        """Start a new conversation with welcome message"""
        quick_actions_text = "\n\n✨ **Quick Actions:**\n"
        for action in self.quick_actions:
            quick_actions_text += f"• **{action.title}**: {action.description} (e.g., `{action.example_input}`)\n"

        welcome_message = f"""
🤍 Welcome to Agape Core AI Chat Interface!

I'm here to help you make decisions guided by the two Great Commandments:
1. Love God with all your heart, soul, mind, and strength
2. Love your neighbor as yourself

You can:
• Ask me about any decision you're facing
• Describe a situation you need wisdom on
• Request guidance on moral or ethical questions
• Get help thinking through relationships, work, or personal choices
{quick_actions_text}
What decision or situation would you like guidance on today?

(Type 'help' for guided questions or 'examples' for sample scenarios)
        """
        return welcome_message.strip()

    def process_user_input(self, user_input: str) -> str:
        """Process user input and generate appropriate response"""
        user_input = user_input.strip()

        # Handle special commands
        if user_input.lower() == 'help':
            return self._show_help()
        elif user_input.lower() == 'examples':
            return self._show_examples()
        elif user_input.lower() == 'history':
            return self._show_history()
        elif user_input.lower().startswith('clear'):
            return self._clear_history()
        
        # Handle quick actions
        for action in self.quick_actions:
            if user_input.lower().startswith(action.action_id.replace("_", " ")):
                return self._handle_quick_action(action, user_input)

        # Detect question category and provide targeted guidance
        category = self._detect_question_category(user_input)

        # Extract context from user input
        context = self._extract_context(user_input, category)

        # Generate decision analysis if Agape Core is available
        decision_analysis = None
        if self.agape_core:
            try:
                decision_analysis = self.agape_core.evaluate_decision(user_input, context)
            except Exception as e:
                logger.error(f"Error in decision analysis: {e}")

        # Generate response
        response = self._generate_response(user_input, category, context, decision_analysis)

        # Save to chat history
        self._save_to_history(user_input, response, decision_analysis)

        return response

    def _handle_quick_action(self, action: QuickAction, user_input: str) -> str:
        """Handle a specific quick action"""
        if action.action_id == "discern_truth":
            # Extract URL or content from user input
            content_to_evaluate = user_input[len(action.action_id.replace("_", " ")):].strip()
            if not content_to_evaluate:
                return "Please provide a URL or content to evaluate for truth."
            
            # Placeholder for actual truth discernment logic
            # In a real application, this would involve more sophisticated analysis
            # For now, we'll simulate a response.
            if "http" in content_to_evaluate:
                return f"Analyzing URL: {content_to_evaluate}... This appears to be a valid URL. Evaluating its truthfulness requires deeper analysis."
            else:
                return f"Analyzing content: '{content_to_evaluate}'... Evaluating this content for truth alignment requires specific algorithms."
        
        elif action.action_id == "seekgood_media":
            media_title = user_input[len(action.action_id.replace("_", " ")):].strip()
            if not media_title:
                return "Please provide a media title or description."
            return f"Analyzing media: '{media_title}' against Philippians 4:8 standards. This requires a media analysis module."
        
        elif action.action_id == "family_agenda":
            content = user_input[len(action.action_id.replace("_", " ")):].strip()
            if not content:
                return "Please describe the content to check against family values."
            return f"Analyzing content for family agenda alignment: '{content}'. This requires a family values assessment module."
        
        elif action.action_id == "glory_to_god":
            content = user_input[len(action.action_id.replace("_", " ")):].strip()
            if not content:
                return "Please describe the content to evaluate for God-glorifying elements."
            return f"Evaluating content for God-glorifying elements: '{content}'. This requires spiritual discernment logic."
        
        elif action.action_id == "system_truth":
            system_description = user_input[len(action.action_id.replace("_", " ")):].strip()
            if not system_description:
                return "Please describe the organization, process, or system."
            return f"Analyzing truth laws in system: '{system_description}'. This requires a legal and systemic analysis capability."
        
        elif action.action_id == "gospel_guidance":
            situation = user_input[len(action.action_id.replace("_", " ")):].strip()
            if not situation:
                return "Please describe your situation or decision."
            return self.process_user_input(situation) # Delegate to regular processing

        else:
            return "Sorry, I don't know how to handle that quick action yet."


    def _detect_question_category(self, user_input: str) -> Optional[QuestionTemplate]:
        """Detect which question category best fits the user input"""
        user_lower = user_input.lower()

        for template in self.question_templates:
            # Check if any context hints match
            hint_matches = sum(1 for hint in template.context_hints if hint in user_lower)
            if hint_matches > 0:
                return template

        # Default to moral dilemma if no specific category detected
        return self.question_templates[-1]  # Moral Dilemma template

    def _extract_context(self, user_input: str, category: Optional[QuestionTemplate]) -> Dict[str, Any]:
        """Extract context information from user input"""
        context = {
            "user_question": user_input,
            "category": category.category if category else "General",
            "urgency": "medium",  # Default
            "scope": "individual"  # Default
        }

        # Extract urgency indicators
        urgent_words = ["urgent", "immediate", "asap", "quickly", "emergency"]
        if any(word in user_input.lower() for word in urgent_words):
            context["urgency"] = "high"

        # Extract scope indicators
        if any(word in user_input.lower() for word in ["family", "team", "group", "community"]):
            context["scope"] = "group"
        elif any(word in user_input.lower() for word in ["everyone", "public", "all people"]):
            context["scope"] = "public"

        # Extract emotional context
        emotional_words = {
            "anxiety": ["worried", "anxious", "stressed", "concerned"],
            "fear": ["afraid", "scared", "fearful", "terrified"],
            "anger": ["angry", "mad", "frustrated", "upset"],
            "sadness": ["sad", "depressed", "grieving", "hurt"],
            "joy": ["happy", "excited", "grateful", "blessed"]
        }

        for emotion, words in emotional_words.items():
            if any(word in user_input.lower() for word in words):
                context["emotional_state"] = emotion
                break

        return context

    def _generate_response(self, user_input: str, category: Optional[QuestionTemplate], 
                          context: Dict[str, Any], decision_analysis: Optional[Decision]) -> str:
        """Generate comprehensive response with Gospel-based guidance"""

        response = f"Thank you for sharing your situation. Let me provide some guidance based on Gospel principles.\n\n"

        # Add category-specific guidance
        if category:
            response += f"📋 **{category.category} Guidance:**\n"
            response += f"This appears to be a {category.category.lower()}. Here are some key questions to consider:\n\n"

            for i, question in enumerate(category.follow_up_questions[:3], 1):
                response += f"{i}. {question}\n"
            response += "\n"

        # Add decision analysis if available
        if decision_analysis:
            response += "🎯 **Gospel Truth Analysis:**\n"
            response += f"• Overall Gospel Alignment: {decision_analysis.overall_score:.2f}/1.0\n"
            response += f"• Love God Score: {decision_analysis.love_god_score:.2f}/1.0\n"
            response += f"• Love Neighbor Score: {decision_analysis.love_neighbor_score:.2f}/1.0\n\n"

            # Add value impact if available
            if hasattr(decision_analysis, 'value_impact') and decision_analysis.value_impact:
                impact = decision_analysis.value_impact
                response += f"📊 **Impact Assessment:**\n"
                response += f"• People Affected: {impact.number_of_people:,}\n"
                response += f"• Total Impact Score: {impact.total_impact:.1f}\n\n"

            # Add recommendations
            if decision_analysis.overall_score > 0.7:
                response += "✅ **RECOMMENDED:** This path strongly aligns with Gospel principles.\n\n"
            elif decision_analysis.overall_score > 0.4:
                response += "⚠️ **PROCEED THOUGHTFULLY:** This has mixed alignment - consider the guidance above.\n\n"
            else:
                response += "❌ **RECONSIDER:** This path conflicts with Gospel principles. Consider alternatives.\n\n"

        # Add Biblical wisdom
        response += self._add_biblical_wisdom(user_input, context)

        # Add practical next steps
        response += "\n🎯 **Next Steps:**\n"
        response += "1. **Pray for wisdom** - 'If any of you lacks wisdom, ask God' (James 1:5)\n"
        response += "2. **Seek counsel** - Consider talking with trusted Christian friends or mentors\n"
        response += "3. **Test against Scripture** - Does this align with Biblical principles?\n"
        response += "4. **Consider consequences** - How will this affect your witness and relationships?\n\n"

        response += "Would you like me to explore any specific aspect of this decision further?"

        return response

    def _add_biblical_wisdom(self, user_input: str, context: Dict[str, Any]) -> str:
        """Add relevant Biblical wisdom based on the situation"""
        wisdom_map = {
            "decision": "Trust in the Lord with all your heart and lean not on your own understanding (Proverbs 3:5-6)",
            "fear": "Have I not commanded you? Be strong and courageous. Do not be afraid (Joshua 1:9)",
            "relationship": "Above all, love each other deeply, because love covers over a multitude of sins (1 Peter 4:8)",
            "work": "Whatever you do, work at it with all your heart, as working for the Lord (Colossians 3:23)",
            "money": "Keep your life free from love of money, and be content with what you have (Hebrews 13:5)",
            "forgiveness": "Be kind and compassionate to one another, forgiving each other (Ephesians 4:32)",
            "wisdom": "The fear of the Lord is the beginning of wisdom (Proverbs 9:10)",
            "peace": "Let the peace of Christ rule in your hearts (Colossians 3:15)"
        }

        user_lower = user_input.lower()
        relevant_verse = None

        for key, verse in wisdom_map.items():
            if key in user_lower:
                relevant_verse = verse
                break

        if not relevant_verse:
            relevant_verse = wisdom_map["decision"]  # Default

        return f"📖 **Biblical Wisdom:**\n*{relevant_verse}*\n"

    def _show_help(self) -> str:
        """Show help with guided questions"""
        help_text = """
🤝 **How to Get the Best Guidance:**

**Question Categories I Can Help With:**
• Personal decisions and character choices
• Relationship issues and conflicts
• Work and career decisions
• Financial and stewardship questions
• Moral and ethical dilemmas

**For Better Results:**
• Be specific about your situation
• Include relevant context (who's involved, timeline, etc.)
• Mention any constraints or concerns you have
• Ask follow-up questions for deeper exploration

**Sample Questions:**
• "Should I take this job offer that pays more but requires travel away from family?"
• "How should I handle a conflict with my friend who borrowed money and won't pay it back?"
• "I'm struggling with whether to confront someone about their behavior - what should I consider?"

**Commands:**
• 'examples' - See example scenarios
• 'history' - View recent conversation
• 'clear' - Start fresh conversation

What specific situation would you like guidance on?
        """
        return help_text.strip()

    def _show_examples(self) -> str:
        """Show example scenarios"""
        examples = """
💡 **Example Scenarios I Can Help With:**

**Personal Ethics:**
"I found out my coworker is stealing supplies. Should I report them or talk to them first?"

**Family Relationships:**
"My adult child is making destructive choices. How do I balance love with boundaries?"

**Financial Stewardship:**
"We want to buy a bigger house but it would limit our giving. How do we decide?"

**Work Integrity:**
"My boss asked me to bend the truth to a client. How should I handle this?"

**Friendship Conflicts:**
"My friend constantly complains but never listens to advice. Should I distance myself?"

**Community Service:**
"I'm overwhelmed with volunteer commitments. How do I prioritize without letting people down?"

Simply describe your situation in your own words, and I'll provide guidance based on Gospel principles and practical wisdom.

What situation are you facing?
        """
        return examples.strip()

    def _show_history(self) -> str:
        """Show recent conversation history"""
        if not self.chat_history:
            return "No conversation history yet. Start by asking a question!"

        history_text = "📝 **Recent Conversation History:**\n\n"
        for i, msg in enumerate(self.chat_history[-5:], 1):  # Show last 5 messages
            history_text += f"**Q{i}:** {msg.user_input[:100]}{'...' if len(msg.user_input) > 100 else ''}\n"
            if msg.decision_data and 'overall_score' in msg.decision_data:
                score = msg.decision_data['overall_score']
                history_text += f"*Gospel Alignment: {score:.2f}/1.0*\n\n"

        return history_text.strip()

    def _clear_history(self) -> str:
        """Clear conversation history"""
        self.chat_history.clear()
        self.current_context.clear()
        return "🗑️ Conversation history cleared. What new situation would you like guidance on?"

    def _save_to_history(self, user_input: str, response: str, decision_analysis: Optional[Decision]):
        """Save conversation to history"""
        decision_data = None
        confidence = 0.0

        if decision_analysis:
            decision_data = {
                'overall_score': decision_analysis.overall_score,
                'love_god_score': decision_analysis.love_god_score,
                'love_neighbor_score': decision_analysis.love_neighbor_score,
                'harm_assessment': decision_analysis.harm_assessment
            }
            confidence = decision_analysis.overall_score

        message = ChatMessage(
            timestamp=datetime.now(),
            user_input=user_input,
            ai_response=response,
            decision_data=decision_data,
            confidence_score=confidence
        )

        self.chat_history.append(message)

        # Keep only last 20 messages to manage memory
        if len(self.chat_history) > 20:
            self.chat_history = self.chat_history[-20:]

def main():
    """Demo of the chat interface"""
    print("🤍 Agape Core AI - Chat Interface Demo")
    print("=" * 50)

    chat = AgapeChatInterface()
    print(chat.start_conversation())

    # Interactive chat loop
    while True:
        try:
            user_input = input("\n> ").strip()
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("\n🙏 May God bless your decisions! Goodbye!")
                break

            if user_input:
                response = chat.process_user_input(user_input)
                print(f"\n{response}")

        except KeyboardInterrupt:
            print("\n\n🙏 May God bless your decisions! Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")
            print("Please try rephrasing your question.")

if __name__ == "__main__":
    main()