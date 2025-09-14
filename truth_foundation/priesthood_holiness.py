
"""
Priesthood and Holiness Module - OT/NT Patterns
Explores how the Old Testament priesthood aimed to make people HOLY like God,
and how the New Testament shows adoption into Abraham's covenant through Christ's Atonement
"""

from dataclasses import dataclass
from typing import Dict, List, Optional, Any
from .core_truths import TruthStatement, TruthLevel
import logging

logger = logging.getLogger(__name__)

@dataclass
class PriesthoodPattern:
    """A pattern of priesthood function across dispensations"""
    dispensation: str
    primary_purpose: str
    holiness_mechanism: str
    scripture_references: List[str]
    key_ordinances: List[str]
    inheritance_promise: str
    atonement_connection: str
    practical_applications: List[str]

@dataclass
class HolinessProgression:
    """Stages of becoming holy through priesthood"""
    stage: str
    description: str
    requirements: List[str]
    blessings: List[str]
    christ_parallel: str

class PriesthoodHolinessFramework:
    """
    Framework showing how priesthood patterns across dispensations aim to make people HOLY
    like God, culminating in adoption as Abraham's seed through Christ's Atonement
    """
    
    def __init__(self):
        self.priesthood_patterns = self._initialize_priesthood_patterns()
        self.holiness_progressions = self._initialize_holiness_progressions()
        self.atonement_connections = self._initialize_atonement_connections()
    
    def _initialize_priesthood_patterns(self) -> List[PriesthoodPattern]:
        """Initialize priesthood patterns from OT to present"""
        return [
            PriesthoodPattern(
                dispensation="Patriarchal (Adam to Moses)",
                primary_purpose="Direct communion with God - walking and talking with Him",
                holiness_mechanism="Personal revelation and covenant relationship",
                scripture_references=[
                    "Genesis 3:8 - 'They heard the voice of the Lord God walking in the garden'",
                    "Genesis 5:24 - 'Enoch walked with God: and he was not; for God took him'",
                    "Exodus 33:11 - 'The Lord spake unto Moses face to face, as a man speaketh unto his friend'"
                ],
                key_ordinances=["Sacrifice", "Covenant making", "Baptism (implied with Enoch's city)"],
                inheritance_promise="To be like God and walk with Him",
                atonement_connection="Sacrifices pointed forward to Christ's infinite sacrifice",
                practical_applications=[
                    "Seek personal revelation through prayer",
                    "Make and keep sacred covenants",
                    "Practice sacrifice and consecration",
                    "Build Zion communities"
                ]
            ),
            
            PriesthoodPattern(
                dispensation="Levitical/Aaronic (Moses to Christ)",
                primary_purpose="Make people HOLY through ritual purification and law observance",
                holiness_mechanism="Ceremonial cleansing, sacrifices, and temple ordinances",
                scripture_references=[
                    "Leviticus 11:44 - 'Be ye holy; for I am holy'",
                    "Leviticus 19:2 - 'Ye shall be holy: for I the Lord your God am holy'",
                    "Exodus 19:6 - 'Ye shall be unto me a kingdom of priests, and an holy nation'",
                    "Hebrews 9:13-14 - Comparing animal sacrifices to Christ's blood"
                ],
                key_ordinances=["Daily sacrifices", "Day of Atonement", "Ritual washings", "Temple service"],
                inheritance_promise="To be a holy nation and kingdom of priests",
                atonement_connection="All sacrifices and ordinances were types and shadows of Christ",
                practical_applications=[
                    "Regular spiritual cleansing through repentance",
                    "Daily spiritual sacrifices and devotion",
                    "Serve in God's house (temples/churches)",
                    "Follow divine law and commandments"
                ]
            ),
            
            PriesthoodPattern(
                dispensation="Melchizedek (Christ and His Apostles)",
                primary_purpose="Adoption as Abraham's seed and joint-heirs with Christ",
                holiness_mechanism="Born again through Christ's Atonement and Spirit",
                scripture_references=[
                    "Galatians 3:29 - 'If ye be Christ's, then are ye Abraham's seed, and heirs according to the promise'",
                    "Romans 8:17 - 'Joint-heirs with Christ'",
                    "Ephesians 1:5 - 'Having predestinated us unto the adoption of children by Jesus Christ'",
                    "1 Peter 2:9 - 'Ye are a chosen generation, a royal priesthood, an holy nation'"
                ],
                key_ordinances=["Baptism", "Confirmation", "Sacrament", "Temple ordinances"],
                inheritance_promise="Joint-heirs with Christ, eternal life and exaltation",
                atonement_connection="Christ's Atonement enables adoption and inheritance",
                practical_applications=[
                    "Accept Christ as Savior and follow Him",
                    "Receive priesthood ordinances",
                    "Exercise priesthood in righteousness",
                    "Prepare for eternal marriage and family"
                ]
            ),
            
            PriesthoodPattern(
                dispensation="Restoration (Joseph Smith to Present)",
                primary_purpose="Fulness of priesthood - becoming gods and joint-heirs",
                holiness_mechanism="Temple ordinances, eternal marriage, and continuing revelation",
                scripture_references=[
                    "D&C 76:58 - 'They are gods, even the sons of God'",
                    "D&C 132:20 - 'Then shall they be gods, because they have no end'",
                    "D&C 84:38 - 'He that receiveth my Father receiveth my Father's kingdom'",
                    "Moses 1:39 - 'This is my work and my glory—to bring to pass the immortality and eternal life of man'"
                ],
                key_ordinances=["All previous ordinances", "Temple endowment", "Sealing", "Second anointing"],
                inheritance_promise="Godhood, eternal increase, and all that the Father has",
                atonement_connection="Christ's Atonement enables the highest degree of glory and exaltation",
                practical_applications=[
                    "Receive temple ordinances",
                    "Be sealed to spouse and family",
                    "Follow living prophets",
                    "Prepare to inherit all that the Father has"
                ]
            )
        ]
    
    def _initialize_holiness_progressions(self) -> List[HolinessProgression]:
        """Initialize stages of becoming holy like God"""
        return [
            HolinessProgression(
                stage="Justification (Made Right with God)",
                description="Forgiven of sins and declared righteous through Christ",
                requirements=["Faith in Jesus Christ", "Repentance", "Baptism"],
                blessings=["Forgiveness of sins", "Clean conscience", "Peace with God"],
                christ_parallel="Christ paid the price for our sins"
            ),
            
            HolinessProgression(
                stage="Sanctification (Made Holy and Pure)",
                description="Gradually purified and made holy through the Spirit",
                requirements=["Receive Holy Ghost", "Obey commandments", "Endure faithfully"],
                blessings=["Spiritual gifts", "Increased light", "Christlike nature"],
                christ_parallel="Christ lived a perfectly holy life as our example"
            ),
            
            HolinessProgression(
                stage="Adoption (Become Children of God)",
                description="Adopted into God's family as joint-heirs with Christ",
                requirements=["Born again", "Covenant relationship", "Temple ordinances"],
                blessings=["Divine nature", "Inheritance rights", "Family relationship with God"],
                christ_parallel="Christ is the firstborn, we become joint-heirs through Him"
            ),
            
            HolinessProgression(
                stage="Exaltation (Become Like God)",
                description="Receive the fulness of the Father and become gods",
                requirements=["Eternal marriage", "Endure to the end", "Perfect love"],
                blessings=["Eternal life", "Godhood", "Eternal increase"],
                christ_parallel="Christ has overcome all and invites us to inherit all things"
            )
        ]
    
    def _initialize_atonement_connections(self) -> Dict[str, str]:
        """Initialize how the Atonement enables each aspect of holiness"""
        return {
            "redemptive_power": "Christ's suffering pays the price for sin, enabling forgiveness",
            "sanctifying_power": "Christ's Spirit purifies and transforms hearts",
            "adopting_power": "Christ's relationship with the Father enables our adoption",
            "exalting_power": "Christ's perfection and glory enables our exaltation",
            "inheritance_rights": "Through Christ we become Abraham's seed and heirs of promise",
            "priestly_authority": "Christ holds all priesthood keys and delegates authority",
            "holiness_pattern": "Christ's perfect holiness becomes the pattern for our holiness"
        }
    
    def evaluate_holiness_progression(self, person_status: Dict[str, Any]) -> Dict[str, Any]:
        """Evaluate someone's progression toward holiness like God"""
        evaluation = {
            "current_stage": None,
            "next_steps": [],
            "priesthood_role": "",
            "inheritance_potential": 0.0,
            "atonement_application": [],
            "holiness_score": 0.0,
            "recommendations": []
        }
        
        # Determine current stage
        if person_status.get("baptized") and person_status.get("has_faith"):
            if person_status.get("temple_ordinances") and person_status.get("eternal_marriage"):
                evaluation["current_stage"] = "Exaltation Track"
                evaluation["holiness_score"] = 0.9
            elif person_status.get("confirmed") and person_status.get("living_gospel"):
                evaluation["current_stage"] = "Sanctification"
                evaluation["holiness_score"] = 0.7
            else:
                evaluation["current_stage"] = "Justification"
                evaluation["holiness_score"] = 0.5
        else:
            evaluation["current_stage"] = "Pre-Gospel"
            evaluation["holiness_score"] = 0.2
        
        # Determine priesthood role
        if person_status.get("priesthood_holder"):
            evaluation["priesthood_role"] = "Active priesthood holder - help others become holy"
        elif person_status.get("covenant_member"):
            evaluation["priesthood_role"] = "Covenant member - support priesthood work"
        else:
            evaluation["priesthood_role"] = "Potential heir - invitation to join covenant family"
        
        # Calculate inheritance potential
        covenant_factors = ["faith", "baptized", "confirmed", "temple_ordinances", "eternal_marriage", "enduring"]
        present_factors = sum(1 for factor in covenant_factors if person_status.get(factor))
        evaluation["inheritance_potential"] = present_factors / len(covenant_factors)
        
        # Generate recommendations
        if evaluation["current_stage"] == "Pre-Gospel":
            evaluation["recommendations"] = [
                "Develop faith in Jesus Christ",
                "Study the Gospel and its promises",
                "Prepare for baptism and confirmation"
            ]
        elif evaluation["current_stage"] == "Justification":
            evaluation["recommendations"] = [
                "Receive the gift of the Holy Ghost",
                "Begin daily Gospel living",
                "Prepare for temple ordinances"
            ]
        elif evaluation["current_stage"] == "Sanctification":
            evaluation["recommendations"] = [
                "Receive temple endowment",
                "Seek eternal marriage",
                "Develop Christlike attributes"
            ]
        else:
            evaluation["recommendations"] = [
                "Continue faithful endurance",
                "Help others progress toward holiness",
                "Prepare for eternal responsibilities"
            ]
        
        # Atonement applications
        evaluation["atonement_application"] = [
            f"Christ's {self.atonement_connections['redemptive_power']}",
            f"Christ's {self.atonement_connections['sanctifying_power']}",
            f"Christ's {self.atonement_connections['adopting_power']}"
        ]
        
        return evaluation
    
    def get_holiness_pattern_summary(self) -> str:
        """Get comprehensive summary of holiness patterns"""
        summary = "🕊️ PRIESTHOOD HOLINESS PATTERNS: Becoming Like God\n"
        summary += "=" * 60 + "\n\n"
        
        summary += "📖 CORE TRUTH: The purpose of priesthood across all dispensations\n"
        summary += "is to make people HOLY like God through Christ's Atonement.\n\n"
        
        summary += "🔄 DISPENSATIONAL PATTERNS:\n\n"
        
        for pattern in self.priesthood_patterns:
            summary += f"• {pattern.dispensation.upper()}:\n"
            summary += f"  Purpose: {pattern.primary_purpose}\n"
            summary += f"  Mechanism: {pattern.holiness_mechanism}\n"
            summary += f"  Promise: {pattern.inheritance_promise}\n"
            summary += f"  Atonement: {pattern.atonement_connection}\n\n"
        
        summary += "📈 HOLINESS PROGRESSION:\n\n"
        
        for progression in self.holiness_progressions:
            summary += f"• {progression.stage.upper()}:\n"
            summary += f"  Description: {progression.description}\n"
            summary += f"  Christ's Role: {progression.christ_parallel}\n\n"
        
        summary += "🌟 ULTIMATE INHERITANCE:\n"
        summary += "Through Christ's Atonement, we can become:\n"
        summary += "• Abraham's seed and heirs of promise (Galatians 3:29)\n"
        summary += "• Joint-heirs with Christ (Romans 8:17)\n"
        summary += "• Gods and inheritors of all things (D&C 76:58, 84:38)\n"
        summary += "• Holy like our Father in Heaven (1 Peter 1:16)\n\n"
        
        summary += "💝 ATONEMENT AS THE CENTER:\n"
        summary += "All priesthood patterns and holiness progressions are made\n"
        summary += "possible only through Jesus Christ's infinite Atonement.\n"
        summary += "He is both the perfect example of holiness and the enabling\n"
        summary += "power that allows us to become like God.\n\n"
        
        return summary
    
    def generate_holiness_guidance(self, current_situation: str) -> str:
        """Generate guidance for progressing toward holiness"""
        guidance = f"Holiness Progression Guidance: '{current_situation}'\n\n"
        
        guidance += "🎯 PRIESTHOOD PURPOSE:\n"
        guidance += "The priesthood exists to help you become HOLY like God\n"
        guidance += "through Jesus Christ's enabling Atonement.\n\n"
        
        guidance += "📋 KEY QUESTIONS FOR HOLINESS:\n"
        guidance += "• How does this help me become more like Christ?\n"
        guidance += "• Does this draw me closer to my Heavenly Father?\n"
        guidance += "• Will this prepare me for eternal inheritance?\n"
        guidance += "• How can I help others progress toward holiness?\n\n"
        
        guidance += "⭐ INHERITANCE PROMISE:\n"
        guidance += "If you are Christ's, then you are Abraham's seed\n"
        guidance += "and heirs according to the promise. (Galatians 3:29)\n"
        guidance += "You are invited to inherit ALL that the Father has!\n\n"
        
        return guidance

# Example usage
if __name__ == "__main__":
    framework = PriesthoodHolinessFramework()
    print(framework.get_holiness_pattern_summary())
    
    # Test holiness evaluation
    sample_status = {
        "baptized": True,
        "confirmed": True,
        "has_faith": True,
        "living_gospel": True,
        "priesthood_holder": True,
        "temple_ordinances": False,
        "eternal_marriage": False
    }
    
    evaluation = framework.evaluate_holiness_progression(sample_status)
    print(f"Current Stage: {evaluation['current_stage']}")
    print(f"Holiness Score: {evaluation['holiness_score']:.2f}")
    print(f"Inheritance Potential: {evaluation['inheritance_potential']:.2f}")
