
"""
Temple Laws Module - Sacred Ordinances and Covenants
Handles the higher laws revealed in temples that enable exaltation
and progression toward becoming like God through Christ's Atonement
"""

from dataclasses import dataclass
from typing import Dict, List, Optional, Any
from .core_truths import TruthStatement, TruthLevel
from .atonement_supreme import AtonementSupremeTruth
import logging

logger = logging.getLogger(__name__)

@dataclass
class TempleLaw:
    """A sacred law or principle taught in the temple"""
    law_name: str
    description: str
    scripture_references: List[str]
    covenant_requirements: List[str]
    blessings_promised: List[str]
    practical_applications: List[str]
    christ_connection: str
    progression_toward_godhood: str

@dataclass
class TempleAssessment:
    """Assessment of temple law observance and progression"""
    laws_being_lived: List[str]
    areas_for_growth: List[str]
    covenant_faithfulness_score: float
    progression_score: float
    recommendations: List[str]
    eternal_perspective: str

class TempleLawsFramework:
    """
    Framework for understanding and applying temple laws that enable
    progression toward eternal life and exaltation through Christ
    """
    
    def __init__(self):
        self.atonement_truth = AtonementSupremeTruth()
        self.temple_laws = self._initialize_temple_laws()
        self.progression_levels = self._initialize_progression_levels()
    
    def _initialize_temple_laws(self) -> Dict[str, TempleLaw]:
        """Initialize sacred temple laws and principles"""
        return {
            "law_of_obedience": TempleLaw(
                law_name="Law of Obedience",
                description="Complete obedience to God's commandments and His anointed servants",
                scripture_references=[
                    "D&C 130:20-21 - 'There is a law, irrevocably decreed... upon which all blessings are predicated'",
                    "1 Samuel 15:22 - 'To obey is better than sacrifice'",
                    "D&C 82:10 - 'I, the Lord, am bound when ye do what I say'"
                ],
                covenant_requirements=[
                    "Willingness to obey all of God's commandments",
                    "Submission to priesthood authority",
                    "Faithful observance of all Gospel ordinances",
                    "Complete dedication to building God's kingdom"
                ],
                blessings_promised=[
                    "All blessings predicated upon obedience",
                    "Divine protection and guidance",
                    "Spiritual power and authority",
                    "Progress toward eternal life"
                ],
                practical_applications=[
                    "Keep all commandments without picking and choosing",
                    "Sustain Church leaders and follow prophetic counsel",
                    "Attend church and fulfill callings faithfully",
                    "Live Gospel principles in all aspects of life"
                ],
                christ_connection="Christ was perfectly obedient to the Father in all things",
                progression_toward_godhood="Obedience is the first law of heaven - essential for godhood"
            ),
            
            "law_of_sacrifice": TempleLaw(
                law_name="Law of Sacrifice",
                description="Willingness to sacrifice all things for the Gospel, even life if necessary",
                scripture_references=[
                    "Lectures on Faith 6:7 - 'A religion that does not require the sacrifice of all things never has power sufficient to produce the faith necessary unto life and salvation'",
                    "Luke 14:26 - 'If any man come to me, and hate not... his own life also, he cannot be my disciple'",
                    "D&C 98:13 - 'It is my will that you should forsake all evil and cleave unto all good'"
                ],
                covenant_requirements=[
                    "Consecrate all possessions to the Lord",
                    "Put God's kingdom before personal interests",
                    "Willingness to give up anything God requires",
                    "Sacrifice time, talents, and resources for others"
                ],
                blessings_promised=[
                    "Faith sufficient for eternal life",
                    "Power to overcome all obstacles",
                    "Spiritual strength and testimony",
                    "Eternal rewards and inheritance"
                ],
                practical_applications=[
                    "Pay tithes and offerings generously",
                    "Serve missions and callings despite cost",
                    "Put family and Gospel before career advancement",
                    "Live modestly and share with those in need"
                ],
                christ_connection="Christ sacrificed His life and all things for our salvation",
                progression_toward_godhood="Gods must be willing to sacrifice all for their children"
            ),
            
            "law_of_gospel": TempleLaw(
                law_name="Law of the Gospel",
                description="Living by faith, repentance, baptism, and receiving the Holy Ghost",
                scripture_references=[
                    "3 Nephi 27:13-21 - Christ's definition of His Gospel",
                    "2 Nephi 31:17-21 - The doctrine of Christ",
                    "D&C 84:27 - 'The power of godliness is manifest'"
                ],
                covenant_requirements=[
                    "Exercise faith in Jesus Christ",
                    "Repent of all sins continually",
                    "Honor baptismal covenant daily",
                    "Follow promptings of the Holy Ghost"
                ],
                blessings_promised=[
                    "Remission of sins",
                    "Born again through the Spirit",
                    "Power of godliness manifest",
                    "Eternal life through Christ"
                ],
                practical_applications=[
                    "Daily prayer and scripture study",
                    "Weekly sacrament participation",
                    "Regular repentance and course correction",
                    "Seek and follow spiritual promptings"
                ],
                christ_connection="Christ is the Gospel - the way, truth, and life",
                progression_toward_godhood="The Gospel is the path to become like Christ"
            ),
            
            "law_of_chastity": TempleLaw(
                law_name="Law of Chastity",
                description="Sexual purity and fidelity according to God's design for eternal families",
                scripture_references=[
                    "1 Corinthians 6:18-20 - 'Flee fornication... glorify God in your body'",
                    "D&C 42:22-24 - 'Thou shalt love thy wife with all thy heart'",
                    "The Family: A Proclamation to the World"
                ],
                covenant_requirements=[
                    "Sexual relations only within legal marriage",
                    "Complete fidelity to spouse",
                    "Purity in thought, word, and deed",
                    "Respect the sacred power of procreation"
                ],
                blessings_promised=[
                    "Strong eternal marriage and family",
                    "Spiritual sensitivity and power",
                    "Self-respect and divine approval",
                    "Ability to create eternal families"
                ],
                practical_applications=[
                    "Guard thoughts and avoid tempting situations",
                    "Honor marriage covenants completely",
                    "Teach children proper principles",
                    "Support and strengthen families"
                ],
                christ_connection="Christ's pure love provides the pattern for marital love",
                progression_toward_godhood="Eternal marriage is essential for exaltation and godhood"
            ),
            
            "law_of_consecration": TempleLaw(
                law_name="Law of Consecration",
                description="Complete dedication of time, talents, and possessions to God's kingdom",
                scripture_references=[
                    "D&C 42:30-32 - 'All things shall be done with an eye single to the glory of God'",
                    "D&C 78:17-18 - 'The earth is the Lord's, and the fulness thereof'",
                    "Mosiah 2:17 - 'When ye are in the service of your fellow beings ye are only in the service of your God'"
                ],
                covenant_requirements=[
                    "Consecrate all possessions to the Lord",
                    "Use talents and abilities to build the kingdom",
                    "Serve others with pure motives",
                    "Have no selfish ambitions"
                ],
                blessings_promised=[
                    "Fulness of the earth",
                    "Spiritual and temporal prosperity",
                    "Unity with God's purposes",
                    "Eternal inheritance and exaltation"
                ],
                practical_applications=[
                    "Use all resources to bless others",
                    "Magnify callings and opportunities to serve",
                    "Live United Order principles in heart",
                    "See all possessions as stewardships from God"
                ],
                christ_connection="Christ consecrated His entire life and mission to the Father",
                progression_toward_godhood="Gods live the law of consecration perfectly"
            ),
            
            "broken_heart_contrite_spirit": TempleLaw(
                law_name="Broken Heart and Contrite Spirit",
                description="Complete humility, surrender to God's will, and spiritual rebirth",
                scripture_references=[
                    "3 Nephi 9:20 - 'Offer for a sacrifice unto me a broken heart and a contrite spirit'",
                    "2 Nephi 2:7 - 'Redemption cometh through the Holy Messiah'",
                    "Psalm 51:17 - 'A broken and a contrite heart, O God, thou wilt not despise'"
                ],
                covenant_requirements=[
                    "Complete humility before God",
                    "Surrender personal will to God's will",
                    "Genuine sorrow for sin",
                    "Willingness to be spiritually reborn"
                ],
                blessings_promised=[
                    "Spiritual rebirth and renewal",
                    "Remission of sins",
                    "Peace of conscience",
                    "Power to overcome natural man"
                ],
                practical_applications=[
                    "Daily examination of conscience",
                    "Sincere confession and repentance",
                    "Submit to God's timing and methods",
                    "Accept trials as refining experiences"
                ],
                christ_connection="Christ suffered with perfect submission to enable our redemption",
                progression_toward_godhood="Broken heart precedes spiritual rebirth necessary for godhood"
            )
        }
    
    def _initialize_progression_levels(self) -> Dict[str, Dict[str, Any]]:
        """Initialize levels of temple law progression"""
        return {
            "preparation": {
                "description": "Learning and preparing to make temple covenants",
                "requirements": ["Basic Gospel understanding", "Worthy of temple recommend"],
                "focus_laws": ["law_of_obedience", "law_of_gospel"]
            },
            "covenant_making": {
                "description": "Making sacred temple covenants",
                "requirements": ["Temple endowment", "Understanding covenant significance"],
                "focus_laws": ["law_of_sacrifice", "law_of_chastity"]
            },
            "covenant_keeping": {
                "description": "Faithfully living temple covenants",
                "requirements": ["Daily covenant observance", "Temple service"],
                "focus_laws": ["law_of_consecration", "broken_heart_contrite_spirit"]
            },
            "covenant_perfecting": {
                "description": "Perfecting covenant living toward exaltation",
                "requirements": ["Perfect love", "Complete consecration"],
                "focus_laws": ["All laws in perfect harmony"]
            }
        }
    
    def assess_temple_law_living(self, person_data: Dict[str, Any]) -> TempleAssessment:
        """Assess how well someone is living temple laws"""
        
        laws_being_lived = []
        areas_for_growth = []
        total_score = 0.0
        
        # Evaluate each temple law
        for law_name, law in self.temple_laws.items():
            score = self._evaluate_law_observance(law_name, person_data)
            total_score += score
            
            if score > 0.7:
                laws_being_lived.append(law_name.replace('_', ' ').title())
            elif score < 0.5:
                areas_for_growth.append(law_name.replace('_', ' ').title())
        
        covenant_faithfulness = total_score / len(self.temple_laws)
        
        # Determine progression level
        if covenant_faithfulness > 0.9:
            progression = 0.9
        elif covenant_faithfulness > 0.7:
            progression = 0.7
        elif covenant_faithfulness > 0.5:
            progression = 0.5
        else:
            progression = 0.3
        
        # Generate recommendations
        recommendations = self._generate_temple_recommendations(
            covenant_faithfulness, areas_for_growth, person_data
        )
        
        # Generate eternal perspective
        eternal_perspective = self._generate_eternal_perspective(covenant_faithfulness)
        
        return TempleAssessment(
            laws_being_lived=laws_being_lived,
            areas_for_growth=areas_for_growth,
            covenant_faithfulness_score=covenant_faithfulness,
            progression_score=progression,
            recommendations=recommendations,
            eternal_perspective=eternal_perspective
        )
    
    def _evaluate_law_observance(self, law_name: str, person_data: Dict[str, Any]) -> float:
        """Evaluate observance of a specific temple law"""
        
        law_indicators = {
            "law_of_obedience": ["follows_commandments", "sustains_leaders", "faithful_service"],
            "law_of_sacrifice": ["pays_tithing", "serves_missions", "sacrifices_for_others"],
            "law_of_gospel": ["daily_prayer", "scripture_study", "sacrament_attendance"],
            "law_of_chastity": ["moral_purity", "marital_fidelity", "appropriate_thoughts"],
            "law_of_consecration": ["serves_others", "uses_talents_for_good", "consecrated_living"],
            "broken_heart_contrite_spirit": ["humble", "repentant", "submissive_to_god"]
        }
        
        indicators = law_indicators.get(law_name, [])
        if not indicators:
            return 0.5
        
        present_indicators = sum(1 for indicator in indicators if person_data.get(indicator, False))
        return present_indicators / len(indicators)
    
    def _generate_temple_recommendations(self, faithfulness_score: float, 
                                       growth_areas: List[str], 
                                       person_data: Dict[str, Any]) -> List[str]:
        """Generate specific recommendations for temple law living"""
        recommendations = []
        
        if faithfulness_score > 0.8:
            recommendations.append("Continue faithful covenant keeping - you're on the path to exaltation")
            recommendations.append("Look for opportunities to help others make and keep temple covenants")
        elif faithfulness_score > 0.6:
            recommendations.append("Good foundation in covenant living - focus on areas needing growth")
            recommendations.append("Increase temple attendance for spiritual strength")
        else:
            recommendations.append("Begin with basics: daily prayer, scripture study, and obedience")
            recommendations.append("Prepare worthily for temple worship and covenant making")
        
        # Specific recommendations for growth areas
        for area in growth_areas[:2]:
            if "obedience" in area.lower():
                recommendations.append("Focus on complete obedience to all commandments")
            elif "sacrifice" in area.lower():
                recommendations.append("Practice consecration by sacrificing for others")
            elif "chastity" in area.lower():
                recommendations.append("Strengthen moral purity in thought and action")
            elif "consecration" in area.lower():
                recommendations.append("Use talents and resources to build God's kingdom")
        
        return recommendations
    
    def _generate_eternal_perspective(self, faithfulness_score: float) -> str:
        """Generate eternal perspective based on covenant faithfulness"""
        if faithfulness_score > 0.8:
            return ("You are progressing toward exaltation and eternal life. Continue faithfully "
                   "and you will inherit all that the Father has.")
        elif faithfulness_score > 0.6:
            return ("You are on the covenant path with good progress. Focus on faithful "
                   "endurance to receive eternal promises.")
        else:
            return ("The path to eternal life is before you. Begin with faith and obedience, "
                   "and God will help you progress toward exaltation.")
    
    def generate_temple_law_guidance(self, assessment: TempleAssessment) -> str:
        """Generate comprehensive temple law guidance"""
        
        guidance = "🏛️ TEMPLE LAW GUIDANCE\n"
        guidance += "Sacred Covenants and Eternal Progression\n"
        guidance += "=" * 60 + "\n\n"
        
        guidance += f"📊 COVENANT FAITHFULNESS: {assessment.covenant_faithfulness_score:.2f}/1.0\n"
        guidance += f"📈 PROGRESSION SCORE: {assessment.progression_score:.2f}/1.0\n\n"
        
        if assessment.laws_being_lived:
            guidance += "✅ TEMPLE LAWS BEING LIVED:\n"
            for law in assessment.laws_being_lived:
                guidance += f"• {law}\n"
            guidance += "\n"
        
        if assessment.areas_for_growth:
            guidance += "🎯 AREAS FOR GROWTH:\n"
            for area in assessment.areas_for_growth:
                guidance += f"• {area}\n"
            guidance += "\n"
        
        guidance += "💡 RECOMMENDATIONS:\n"
        for rec in assessment.recommendations:
            guidance += f"• {rec}\n"
        guidance += "\n"
        
        guidance += "🌟 ETERNAL PERSPECTIVE:\n"
        guidance += f"{assessment.eternal_perspective}\n\n"
        
        guidance += "📖 REMEMBER:\n"
        guidance += "Temple covenants are the pathway to eternal life and exaltation.\n"
        guidance += "Through Christ's Atonement, you can become joint-heirs with Him\n"
        guidance += "and inherit all that the Father has. Stay faithful to your covenants!\n\n"
        
        guidance += "🕊️ ULTIMATE PROMISE:\n"
        guidance += "\"Then shall they be gods, because they have no end; therefore shall they be\n"
        guidance += "from everlasting to everlasting, because they continue\" - D&C 132:20\n"
        
        return guidance
    
    def get_temple_law_details(self, law_name: str) -> Optional[TempleLaw]:
        """Get detailed information about a specific temple law"""
        return self.temple_laws.get(law_name)
    
    def get_all_temple_laws_summary(self) -> str:
        """Get summary of all temple laws"""
        summary = "🏛️ TEMPLE LAWS FOR ETERNAL PROGRESSION\n"
        summary += "=" * 55 + "\n\n"
        
        summary += "These sacred laws, when lived faithfully, enable progression\n"
        summary += "toward eternal life and exaltation through Christ's Atonement.\n\n"
        
        for i, (key, law) in enumerate(self.temple_laws.items(), 1):
            summary += f"{i}. {law.law_name.upper()}\n"
            summary += f"   Description: {law.description}\n"
            summary += f"   Progression: {law.progression_toward_godhood}\n"
            summary += f"   Key reference: {law.scripture_references[0]}\n\n"
        
        summary += "🌟 ULTIMATE GOAL:\n"
        summary += "To become joint-heirs with Christ and inherit all that the Father has\n"
        summary += "through faithful observance of sacred temple covenants.\n\n"
        
        summary += "💝 ATONEMENT CONNECTION:\n"
        summary += "All temple laws and ordinances derive their power from Christ's\n"
        summary += "infinite Atonement, which enables our exaltation and eternal life.\n"
        
        return summary

# Example usage and demonstration
def demonstrate_temple_laws():
    """Demonstrate the temple laws system"""
    framework = TempleLawsFramework()
    
    print("🏛️ TEMPLE LAWS SYSTEM")
    print("=" * 40)
    
    # Example person assessment
    example_person = {
        "follows_commandments": True,
        "sustains_leaders": True,
        "faithful_service": True,
        "pays_tithing": True,
        "serves_missions": False,
        "daily_prayer": True,
        "scripture_study": True,
        "moral_purity": True,
        "serves_others": True,
        "humble": True,
        "repentant": True
    }
    
    assessment = framework.assess_temple_law_living(example_person)
    guidance = framework.generate_temple_law_guidance(assessment)
    
    print(guidance)
    
    print("\n" + "=" * 40)
    print("📚 ALL TEMPLE LAWS SUMMARY:")
    print(framework.get_all_temple_laws_summary())
    
    return framework

if __name__ == "__main__":
    demonstrate_temple_laws()
