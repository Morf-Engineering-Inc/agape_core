
"""
Gospel Definitions Module - Core definitions for Gospel concepts
Provides scriptural and doctrinal definitions for key Gospel terms
"""

from dataclasses import dataclass
from typing import List, Dict, Any
from .core_truths import TruthStatement, TruthLevel

@dataclass
class GospelDefinition:
    """A Gospel concept with its definition and applications"""
    term: str
    definition: str
    scripture_references: List[str]
    characteristics: List[str]
    practical_applications: List[str]
    christ_connection: str
    how_it_helps_others_come_unto_christ: str

class GospelDefinitions:
    """
    Core Gospel definitions that establish meaning for key concepts
    in the context of coming unto Christ and testifying of Him
    """
    
    def __init__(self):
        self.definitions = self._initialize_definitions()
    
    def _initialize_definitions(self) -> Dict[str, GospelDefinition]:
        """Initialize core Gospel definitions"""
        return {
            "good": GospelDefinition(
                term="good",
                definition="That which is of God, aligned with His nature and will, and leads others to Christ",
                scripture_references=[
                    "Moroni 7:12-13 - 'All things which are good cometh of God'",
                    "Matthew 19:17 - 'There is none good but one, that is, God'",
                    "3 Nephi 14:17 - 'Every good tree bringeth forth good fruit'",
                    "James 1:17 - 'Every good gift and every perfect gift is from above'"
                ],
                characteristics=[
                    "Comes from God as the source",
                    "Draws people closer to Christ",
                    "Inspires faith, hope, and charity",
                    "Builds up rather than tears down",
                    "Serves others selflessly",
                    "Aligns with eternal principles",
                    "Bears good fruit over time",
                    "Testifies of Christ's reality and love"
                ],
                practical_applications=[
                    "Actions that serve others without seeking reward",
                    "Teaching truth with love and patience",
                    "Defending the innocent and vulnerable",
                    "Sharing the Gospel through word and example",
                    "Forgiving others as Christ forgives",
                    "Sacrificing for others' wellbeing",
                    "Creating beauty, art, and culture that uplifts",
                    "Using talents and resources to bless others"
                ],
                christ_connection="All good originates from Christ as the light and life of the world",
                how_it_helps_others_come_unto_christ=(
                    "Good acts serve as a testimony of Christ's reality and love. When we do good, "
                    "we reflect His character and draw others to want to know the source of that goodness. "
                    "Our good works become a light that helps others see Christ and desire to follow Him."
                )
            ),
            
            "testify_of_christ": GospelDefinition(
                term="testify_of_christ",
                definition="To bear witness of Jesus Christ through word, deed, and the Spirit's confirmation",
                scripture_references=[
                    "John 15:27 - 'Ye also shall bear witness, because ye have been with me'",
                    "Acts 1:8 - 'Ye shall be witnesses unto me'",
                    "1 John 5:9 - 'The witness of God is greater'",
                    "Revelation 19:10 - 'The testimony of Jesus is the spirit of prophecy'"
                ],
                characteristics=[
                    "Speaks truth about Christ's divine nature",
                    "Shares personal experiences with Christ",
                    "Lives in a way that reflects Christ's teachings",
                    "Invites the Spirit to confirm truth",
                    "Declares Christ's atonement and resurrection",
                    "Shows Christ's love through service",
                    "Defends Christ's name and doctrine",
                    "Points others to Christ as their Savior"
                ],
                practical_applications=[
                    "Sharing conversion experiences and spiritual witnesses",
                    "Teaching from the scriptures about Christ",
                    "Serving others as Christ would serve",
                    "Defending Christ's teachings when challenged",
                    "Living Gospel principles consistently",
                    "Expressing gratitude for Christ's atonement",
                    "Missionary work and Gospel sharing",
                    "Creating art, music, or literature that glorifies Christ"
                ],
                christ_connection="Christ is both the subject and the power behind all true testimony",
                how_it_helps_others_come_unto_christ=(
                    "Testimony of Christ creates faith in the hearts of hearers. When we testify "
                    "with the Spirit's power, it penetrates hearts and opens minds to Gospel truth. "
                    "Our witness becomes a catalyst for others' spiritual awakening and conversion."
                )
            ),
            
            "come_unto_christ": GospelDefinition(
                term="come_unto_christ",
                definition="The process of accepting Christ as Savior, following His teachings, and becoming like Him",
                scripture_references=[
                    "Matthew 11:28 - 'Come unto me, all ye that labour and are heavy laden'",
                    "3 Nephi 12:48 - 'Be ye therefore perfect, even as your Father in heaven is perfect'",
                    "Ether 12:27 - 'Come unto Christ, and be perfected in him'",
                    "Moroni 10:32 - 'Come unto Christ, and be perfected in him'"
                ],
                characteristics=[
                    "Requires faith in Jesus Christ",
                    "Involves repentance and change of heart",
                    "Includes making and keeping covenants",
                    "Demands following Christ's example",
                    "Brings peace and spiritual healing",
                    "Leads to eternal life and exaltation",
                    "Transforms character and desires",
                    "Creates unity with God and others"
                ],
                practical_applications=[
                    "Daily prayer and scripture study",
                    "Regular church attendance and worship",
                    "Serving others in Christ's name",
                    "Keeping Gospel covenants faithfully",
                    "Forgiving others as Christ forgives",
                    "Seeking to become more like Christ daily",
                    "Sharing the Gospel with others",
                    "Enduring to the end with faith"
                ],
                christ_connection="Christ is the way, the truth, and the life - the only path to the Father",
                how_it_helps_others_come_unto_christ=(
                    "As we come unto Christ ourselves, we become examples and guides for others. "
                    "Our transformation testifies of Christ's power to change lives, making others "
                    "want to experience that same peace and joy that comes from following Him."
                )
            )
        }
    
    def get_definition(self, term: str) -> GospelDefinition:
        """Get a specific Gospel definition"""
        return self.definitions.get(term.lower().replace(" ", "_"))
    
    def evaluate_goodness(self, action: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Evaluate whether an action qualifies as 'good' by Gospel standards"""
        good_def = self.definitions["good"]
        evaluation = {
            "is_good": False,
            "goodness_score": 0.0,
            "alignment_factors": [],
            "testimony_potential": 0.0,
            "christ_invitation_score": 0.0,
            "recommendations": []
        }
        
        action_lower = action.lower()
        
        # Evaluate against characteristics of good
        alignment_count = 0
        for characteristic in good_def.characteristics:
            if self._action_aligns_with_characteristic(action_lower, characteristic):
                alignment_count += 1
                evaluation["alignment_factors"].append(f"Aligns with: {characteristic}")
        
        evaluation["goodness_score"] = alignment_count / len(good_def.characteristics)
        evaluation["is_good"] = evaluation["goodness_score"] > 0.5
        
        # Evaluate testimony potential
        testimony_indicators = ["teach", "share", "testify", "witness", "example", "serve"]
        testimony_score = sum(1 for indicator in testimony_indicators if indicator in action_lower)
        evaluation["testimony_potential"] = min(1.0, testimony_score / 3)
        
        # Evaluate how it helps others come unto Christ
        christ_indicators = ["love", "serve", "help", "bless", "heal", "forgive", "teach"]
        christ_score = sum(1 for indicator in christ_indicators if indicator in action_lower)
        evaluation["christ_invitation_score"] = min(1.0, christ_score / 3)
        
        # Generate recommendations
        if evaluation["is_good"]:
            evaluation["recommendations"].append("This action appears to be good by Gospel standards")
            if evaluation["testimony_potential"] < 0.5:
                evaluation["recommendations"].append("Consider how this could better testify of Christ")
            if evaluation["christ_invitation_score"] < 0.5:
                evaluation["recommendations"].append("Look for ways this could help others come unto Christ")
        else:
            evaluation["recommendations"].append("Consider how to better align this action with Gospel goodness")
            evaluation["recommendations"].append("Ask: Does this come from God and lead others to Christ?")
        
        return evaluation
    
    def _action_aligns_with_characteristic(self, action_lower: str, characteristic: str) -> bool:
        """Check if an action aligns with a characteristic of goodness"""
        # Simple keyword matching - could be enhanced
        char_lower = characteristic.lower()
        
        alignment_patterns = {
            "comes from god": ["pray", "inspired", "spiritual", "divine"],
            "draws people closer": ["invite", "encourage", "inspire", "uplift"],
            "inspires faith": ["faith", "hope", "believe", "trust"],
            "builds up": ["build", "strengthen", "support", "encourage"],
            "serves others": ["serve", "help", "assist", "support"],
            "aligns with eternal": ["eternal", "truth", "principle", "righteous"],
            "bears good fruit": ["result", "outcome", "blessing", "benefit"],
            "testifies of christ": ["testify", "witness", "christ", "example"]
        }
        
        for pattern_key, keywords in alignment_patterns.items():
            if pattern_key in char_lower:
                return any(keyword in action_lower for keyword in keywords)
        
        return False
    
    def generate_goodness_guidance(self, proposed_action: str) -> str:
        """Generate guidance on how to make an action truly 'good' in Gospel terms"""
        evaluation = self.evaluate_goodness(proposed_action, {})
        good_def = self.definitions["good"]
        
        guidance = f"Gospel Goodness Analysis: '{proposed_action}'\n\n"
        
        guidance += f"✅ GOODNESS SCORE: {evaluation['goodness_score']:.2f}/1.0\n"
        guidance += f"📖 TESTIMONY POTENTIAL: {evaluation['testimony_potential']:.2f}/1.0\n"
        guidance += f"💝 CHRIST INVITATION: {evaluation['christ_invitation_score']:.2f}/1.0\n\n"
        
        guidance += "📋 GOSPEL DEFINITION OF GOOD:\n"
        guidance += f"{good_def.definition}\n\n"
        
        if evaluation["alignment_factors"]:
            guidance += "✅ POSITIVE ALIGNMENTS:\n"
            for factor in evaluation["alignment_factors"][:3]:
                guidance += f"• {factor}\n"
            guidance += "\n"
        
        guidance += "💡 TO INCREASE GOODNESS:\n"
        for rec in evaluation["recommendations"]:
            guidance += f"• {rec}\n"
        
        guidance += "\n🎯 KEY QUESTIONS FOR TRUE GOODNESS:\n"
        guidance += "• Does this action come from God and align with His will?\n"
        guidance += "• Will this help others come unto Christ?\n"
        guidance += "• Does this testify of Christ's reality and love?\n"
        guidance += "• Will this bear good fruit over time?\n"
        
        return guidance

# Example usage
if __name__ == "__main__":
    definitions = GospelDefinitions()
    
    # Test goodness evaluation
    test_action = "teach someone about the Gospel with love and patience"
    guidance = definitions.generate_goodness_guidance(test_action)
    print(guidance)
