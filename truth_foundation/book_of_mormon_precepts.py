
"""
Book of Mormon Precepts Module - Drawing Nearer to God
Core precepts from the Book of Mormon that help people come closer to God
through loving God and loving neighbor, leading to sanctification and holiness
"""

from dataclasses import dataclass
from typing import Dict, List, Optional, Any
from enum import Enum
from .core_truths import TruthStatement, TruthLevel
from .gospel_definitions import GospelDefinitions
import logging

logger = logging.getLogger(__name__)

class SanctificationLevel(Enum):
    """Levels of spiritual progression toward becoming holy like God"""
    NATURAL_MAN = 1        # Before conversion, enemy to God
    AWAKENING = 2          # Beginning to feel/recognize truth
    CONVERSION = 3         # Born again through Christ
    SANCTIFICATION = 4     # Being made holy through the Spirit
    PERFECTION = 5         # Eventually perfect in Christ

@dataclass
class BookOfMormonPrecept:
    """A specific precept from the Book of Mormon that draws us closer to God"""
    precept: str
    primary_references: List[str]
    how_it_draws_closer: str
    love_god_connection: str
    love_neighbor_connection: str
    sanctification_power: str
    practical_applications: List[str]
    warning_against_opposites: List[str]
    world_peace_contribution: str

@dataclass
class SanctificationAssessment:
    """Assessment of someone's progress in becoming holy like God"""
    current_level: SanctificationLevel
    active_precepts: List[str]
    needed_precepts: List[str]
    love_god_score: float  # 0.0 to 1.0
    love_neighbor_score: float  # 0.0 to 1.0
    holiness_progression: float  # 0.0 to 1.0
    recommendations: List[str]
    peace_contribution: List[str]

class BookOfMormonPreceptsFramework:
    """
    Framework for applying Book of Mormon precepts to draw nearer to God
    and become sanctified through loving God and neighbor
    """
    
    def __init__(self):
        self.gospel_definitions = GospelDefinitions()
        self.precepts = self._initialize_precepts()
        self.sanctification_patterns = self._initialize_sanctification_patterns()
    
    def _initialize_precepts(self) -> Dict[str, BookOfMormonPrecept]:
        """Initialize the core Book of Mormon precepts"""
        return {
            "faith_in_christ": BookOfMormonPrecept(
                precept="Faith in Jesus Christ",
                primary_references=[
                    "2 Nephi 25:26 - 'We talk of Christ, we rejoice in Christ'",
                    "Alma 32 - Alma's discourse on faith",
                    "Ether 12 - Faith precedes the miracle"
                ],
                how_it_draws_closer="Trust in Christ's power begins the covenant path to God",
                love_god_connection="Faith demonstrates trust in God's goodness and power",
                love_neighbor_connection="Faith in Christ motivates service and compassion for others",
                sanctification_power="Faith opens the heart to receive God's transforming grace",
                practical_applications=[
                    "Trust God's promises even when circumstances are difficult",
                    "Act on spiritual promptings with confidence",
                    "Believe in Christ's power to heal and transform",
                    "Exercise faith through prayer and scripture study"
                ],
                warning_against_opposites=["Doubt", "Fear", "Cynicism", "Self-reliance without God"],
                world_peace_contribution="Faith in Christ unites believers across all divisions"
            ),
            
            "charity_pure_love": BookOfMormonPrecept(
                precept="Charity (Pure Love of Christ)",
                primary_references=[
                    "Moroni 7:45-48 - 'Charity is the pure love of Christ'",
                    "Ether 12:34 - 'Because thou hast seen thy weakness thou shalt be made strong'"
                ],
                how_it_draws_closer="Charity transforms us to become like Christ in love",
                love_god_connection="Charity reflects God's perfect love and makes us like Him",
                love_neighbor_connection="Charity is the pure expression of loving neighbors as ourselves",
                sanctification_power="Charity purifies the heart and makes us perfect in love",
                practical_applications=[
                    "See others as God sees them - with infinite worth",
                    "Serve without expectation of reward or recognition",
                    "Forgive completely and repeatedly",
                    "Sacrifice personal desires for others' welfare",
                    "Judge not, but seek to understand and help"
                ],
                warning_against_opposites=["Selfishness", "Judgment", "Conditional love", "Pride"],
                world_peace_contribution="Charity dissolves prejudice, hatred, and conflict"
            ),
            
            "prayer_communion": BookOfMormonPrecept(
                precept="Prayer and Personal Communion with God",
                primary_references=[
                    "Enos 1 - Enos's mighty prayer and forgiveness",
                    "Alma 34 - Amulek on prayer",
                    "3 Nephi 18 - Christ's teachings on prayer"
                ],
                how_it_draws_closer="Prayer creates direct, personal relationship with God",
                love_god_connection="Prayer expresses love, gratitude, and dependence on God",
                love_neighbor_connection="Praying for others increases love and service toward them",
                sanctification_power="Prayer invites God's Spirit to purify and guide",
                practical_applications=[
                    "Pray morning and evening with real intent",
                    "Pray for enemies and those who despitefully use you",
                    "Express gratitude in all circumstances",
                    "Seek God's will, not just personal desires",
                    "Listen for God's voice and promptings"
                ],
                warning_against_opposites=["Prayerlessness", "Vain repetitions", "Self-sufficiency"],
                world_peace_contribution="Prayer for all people increases universal love and understanding"
            ),
            
            "scripture_feasting": BookOfMormonPrecept(
                precept="Feasting Upon the Word of God",
                primary_references=[
                    "2 Nephi 32:3 - 'Feast upon the words of Christ'",
                    "Mosiah 1:7 - 'Search the scriptures diligently'",
                    "1 Nephi 15:24 - 'The word of God... leadeth to the fountain of living waters'"
                ],
                how_it_draws_closer="God's word nourishes faith and prevents spiritual forgetfulness",
                love_god_connection="Studying God's word shows reverence and desire to know Him",
                love_neighbor_connection="Scripture teaches how to love and serve others",
                sanctification_power="God's word sanctifies and cleanses from sin",
                practical_applications=[
                    "Daily scripture study with pondering and prayer",
                    "Apply scriptures to personal circumstances",
                    "Share scriptural insights with family and friends",
                    "Memorize key passages for strength",
                    "Seek the Spirit while reading"
                ],
                warning_against_opposites=["Spiritual laziness", "Secular learning only", "Neglect of revelation"],
                world_peace_contribution="Shared understanding of God's word unites hearts in truth"
            ),
            
            "service_poor": BookOfMormonPrecept(
                precept="Service and Care for the Poor",
                primary_references=[
                    "Mosiah 2:17 - 'When ye are in the service of your fellow beings ye are only in the service of your God'",
                    "Mosiah 4:26 - 'Impart of your substance to the poor'",
                    "Alma 34:28 - 'If ye turn away the needy... your prayer is vain'"
                ],
                how_it_draws_closer="Serving others serves God and develops Christlike love",
                love_god_connection="Service demonstrates love for God through love of His children",
                love_neighbor_connection="Direct application of loving neighbor through action",
                sanctification_power="Service purifies motives and develops charity",
                practical_applications=[
                    "Regularly serve in community and church",
                    "Give generously to those in need",
                    "Visit the sick, lonely, and struggling",
                    "Use talents and skills to bless others",
                    "Sacrifice time and resources for others' welfare"
                ],
                warning_against_opposites=["Selfishness", "Ignoring the needy", "Pride", "Materialism"],
                world_peace_contribution="Service creates communities of care and mutual support"
            ),
            
            "repentance_change": BookOfMormonPrecept(
                precept="Repentance and Change of Heart",
                primary_references=[
                    "Mosiah 3:12-13 - 'Salvation through the blood of Christ'",
                    "Alma 34:15-17 - 'Cry unto him for mercy'",
                    "Alma 5:14 - 'Have ye experienced this mighty change in your hearts?'"
                ],
                how_it_draws_closer="Repentance removes barriers between us and God",
                love_god_connection="Repentance shows humility and desire to please God",
                love_neighbor_connection="Repentance includes making amends and treating others better",
                sanctification_power="Repentance through Christ cleanses and renews the heart",
                practical_applications=[
                    "Daily examination of conscience and correction",
                    "Confess sins and seek forgiveness",
                    "Make restitution where possible",
                    "Forsake sin completely",
                    "Accept Christ's atoning grace"
                ],
                warning_against_opposites=["Pride", "Justification of sin", "Hardheartedness"],
                world_peace_contribution="Repentance enables forgiveness and reconciliation between people"
            ),
            
            "obedience_commandments": BookOfMormonPrecept(
                precept="Obedience to God's Commandments",
                primary_references=[
                    "Mosiah 2:41 - 'If ye do keep his commandments he doth bless you'",
                    "Alma 37:13 - 'O remember, remember that these things are true'",
                    "1 Nephi 3:7 - 'I will go and do the things which the Lord hath commanded'"
                ],
                how_it_draws_closer="Obedience aligns our will with God's will",
                love_god_connection="Obedience demonstrates love and trust in God's wisdom",
                love_neighbor_connection="God's commandments teach us how to love and treat others",
                sanctification_power="Obedience invites God's Spirit and blessings",
                practical_applications=[
                    "Keep the Sabbath day holy",
                    "Live the law of chastity",
                    "Pay honest tithes and offerings",
                    "Be honest in all dealings",
                    "Honor parents and family responsibilities"
                ],
                warning_against_opposites=["Rebellion", "Selective obedience", "Rationalization"],
                world_peace_contribution="Obedience to divine law creates just and peaceful societies"
            ),
            
            "endurance_steadfastness": BookOfMormonPrecept(
                precept="Endurance and Steadfastness to the End",
                primary_references=[
                    "2 Nephi 31:20 - 'Ye must press forward with a steadfastness in Christ'",
                    "3 Nephi 15:9 - 'He that endureth to the end shall be saved'",
                    "Mosiah 5:15 - 'Be steadfast and immovable'"
                ],
                how_it_draws_closer="Consistent discipleship over time deepens relationship with God",
                love_god_connection="Endurance shows persistent love despite trials",
                love_neighbor_connection="Steadfastness enables continued service through difficulties",
                sanctification_power="Endurance through trials purifies and perfects faith",
                practical_applications=[
                    "Maintain faith during trials and adversity",
                    "Continue serving even when discouraged",
                    "Persist in righteous habits and practices",
                    "Stay committed to covenants",
                    "Help others endure their challenges"
                ],
                warning_against_opposites=["Giving up", "Spiritual drift", "Discouragement"],
                world_peace_contribution="Enduring faith provides stability and hope to communities"
            )
        }
    
    def _initialize_sanctification_patterns(self) -> Dict[SanctificationLevel, Dict[str, Any]]:
        """Initialize patterns for spiritual progression toward holiness"""
        return {
            SanctificationLevel.NATURAL_MAN: {
                "description": "Enemy to God, yields to temptations of the flesh",
                "characteristics": ["Self-centered", "Spiritually dead", "Resistant to God"],
                "needed_precepts": ["faith_in_christ", "repentance_change"],
                "primary_scripture": "Mosiah 3:19 - 'The natural man is an enemy to God'"
            },
            SanctificationLevel.AWAKENING: {
                "description": "Beginning to feel and recognize spiritual truth",
                "characteristics": ["Spiritual stirrings", "Questioning", "Seeking"],
                "needed_precepts": ["prayer_communion", "scripture_feasting", "faith_in_christ"],
                "primary_scripture": "Alma 32:27 - 'Awake and arouse your faculties'"
            },
            SanctificationLevel.CONVERSION: {
                "description": "Born again through Christ, mighty change of heart",
                "characteristics": ["Forgiveness", "Peace", "New desires", "Love for God"],
                "needed_precepts": ["service_poor", "obedience_commandments"],
                "primary_scripture": "Alma 5:14 - 'Have ye experienced this mighty change?'"
            },
            SanctificationLevel.SANCTIFICATION: {
                "description": "Being made holy through the Spirit, growing in charity",
                "characteristics": ["Christlike love", "Spiritual gifts", "Desire to serve"],
                "needed_precepts": ["charity_pure_love", "endurance_steadfastness"],
                "primary_scripture": "Moroni 7:48 - 'Pray unto the Father with all energy of heart'"
            },
            SanctificationLevel.PERFECTION: {
                "description": "Perfect in Christ, full of love like God",
                "characteristics": ["Perfect love", "No condemnation", "At one with God"],
                "needed_precepts": ["All precepts in perfect harmony"],
                "primary_scripture": "Moroni 10:32-33 - 'Come unto Christ, and be perfected in him'"
            }
        }
    
    def assess_sanctification_progress(self, person_data: Dict[str, Any]) -> SanctificationAssessment:
        """Assess someone's progress in becoming holy through Book of Mormon precepts"""
        
        # Determine current sanctification level
        current_level = self._determine_sanctification_level(person_data)
        
        # Assess love scores
        love_god_score = self._assess_love_of_god(person_data)
        love_neighbor_score = self._assess_love_of_neighbor(person_data)
        
        # Determine active and needed precepts
        active_precepts = self._identify_active_precepts(person_data)
        needed_precepts = self._identify_needed_precepts(current_level, active_precepts)
        
        # Calculate overall holiness progression
        holiness_progression = (love_god_score + love_neighbor_score) / 2
        
        # Generate recommendations
        recommendations = self._generate_sanctification_recommendations(
            current_level, needed_precepts, love_god_score, love_neighbor_score
        )
        
        # Determine peace contribution
        peace_contribution = self._assess_peace_contribution(active_precepts)
        
        return SanctificationAssessment(
            current_level=current_level,
            active_precepts=active_precepts,
            needed_precepts=needed_precepts,
            love_god_score=love_god_score,
            love_neighbor_score=love_neighbor_score,
            holiness_progression=holiness_progression,
            recommendations=recommendations,
            peace_contribution=peace_contribution
        )
    
    def _determine_sanctification_level(self, person_data: Dict[str, Any]) -> SanctificationLevel:
        """Determine current level of sanctification"""
        
        # Check for conversion indicators
        if person_data.get("born_again", False) and person_data.get("mighty_change", False):
            if person_data.get("perfect_love", False):
                return SanctificationLevel.PERFECTION
            elif person_data.get("charity_developed", False):
                return SanctificationLevel.SANCTIFICATION
            else:
                return SanctificationLevel.CONVERSION
        elif person_data.get("spiritual_stirrings", False) or person_data.get("seeking_truth", False):
            return SanctificationLevel.AWAKENING
        else:
            return SanctificationLevel.NATURAL_MAN
    
    def _assess_love_of_god(self, person_data: Dict[str, Any]) -> float:
        """Assess love of God based on precept implementation"""
        love_indicators = [
            "prayer_regular", "scripture_study", "obedience_willing", 
            "gratitude_expressed", "worship_sincere", "faith_strong"
        ]
        
        present_indicators = sum(1 for indicator in love_indicators if person_data.get(indicator, False))
        return present_indicators / len(love_indicators)
    
    def _assess_love_of_neighbor(self, person_data: Dict[str, Any]) -> float:
        """Assess love of neighbor based on service and charity"""
        neighbor_love_indicators = [
            "service_regular", "charity_giving", "forgiveness_practiced",
            "kindness_shown", "patience_developed", "judgment_withheld"
        ]
        
        present_indicators = sum(1 for indicator in neighbor_love_indicators if person_data.get(indicator, False))
        return present_indicators / len(neighbor_love_indicators)
    
    def _identify_active_precepts(self, person_data: Dict[str, Any]) -> List[str]:
        """Identify which precepts are currently being practiced"""
        active = []
        
        precept_indicators = {
            "faith_in_christ": ["faith_strong", "trust_christ", "testimony_firm"],
            "charity_pure_love": ["charity_giving", "love_unconditional", "service_selfless"],
            "prayer_communion": ["prayer_regular", "prayer_sincere", "communion_god"],
            "scripture_feasting": ["scripture_study", "word_pondered", "revelation_sought"],
            "service_poor": ["service_regular", "poor_helped", "needs_met"],
            "repentance_change": ["repentance_genuine", "change_heart", "sin_forsaken"],
            "obedience_commandments": ["obedience_willing", "commandments_kept", "covenants_honored"],
            "endurance_steadfastness": ["endurance_shown", "steadfast_trials", "persistent_faith"]
        }
        
        for precept, indicators in precept_indicators.items():
            if any(person_data.get(indicator, False) for indicator in indicators):
                active.append(precept)
        
        return active
    
    def _identify_needed_precepts(self, current_level: SanctificationLevel, active_precepts: List[str]) -> List[str]:
        """Identify which precepts need focus for next level of growth"""
        level_patterns = self.sanctification_patterns[current_level]
        recommended_precepts = level_patterns["needed_precepts"]
        
        # Return precepts that are recommended but not yet active
        return [precept for precept in recommended_precepts if precept not in active_precepts]
    
    def _generate_sanctification_recommendations(self, level: SanctificationLevel, 
                                               needed: List[str], love_god: float, love_neighbor: float) -> List[str]:
        """Generate specific recommendations for spiritual growth"""
        recommendations = []
        
        # Level-specific guidance
        if level == SanctificationLevel.NATURAL_MAN:
            recommendations.append("Begin with faith in Jesus Christ - He can change your heart")
            recommendations.append("Start daily prayer to develop relationship with God")
        elif level == SanctificationLevel.AWAKENING:
            recommendations.append("Continue nurturing spiritual feelings through prayer and scripture")
            recommendations.append("Seek baptism and the gift of the Holy Ghost")
        elif level == SanctificationLevel.CONVERSION:
            recommendations.append("Focus on developing charity - the pure love of Christ")
            recommendations.append("Increase service to others as expression of love")
        elif level == SanctificationLevel.SANCTIFICATION:
            recommendations.append("Perfect your love through continued endurance and service")
            recommendations.append("Help others progress toward conversion and sanctification")
        
        # Love-specific recommendations
        if love_god < 0.7:
            recommendations.append("Strengthen love of God through more consistent prayer and scripture study")
        if love_neighbor < 0.7:
            recommendations.append("Increase love of neighbor through regular service and charity")
        
        # Precept-specific recommendations
        for precept in needed[:2]:  # Focus on top 2 needed precepts
            if precept in self.precepts:
                app = self.precepts[precept].practical_applications[0]
                recommendations.append(f"Focus on {precept.replace('_', ' ')}: {app}")
        
        return recommendations
    
    def _assess_peace_contribution(self, active_precepts: List[str]) -> List[str]:
        """Assess how active precepts contribute to world peace"""
        contributions = []
        
        for precept in active_precepts:
            if precept in self.precepts:
                contribution = self.precepts[precept].world_peace_contribution
                contributions.append(f"{precept.replace('_', ' ').title()}: {contribution}")
        
        return contributions
    
    def generate_sanctification_guidance(self, assessment: SanctificationAssessment) -> str:
        """Generate comprehensive guidance for becoming holy like God"""
        
        guidance = "🕊️ BOOK OF MORMON SANCTIFICATION GUIDANCE\n"
        guidance += "Drawing Nearer to God Through Gospel Living\n"
        guidance += "=" * 60 + "\n\n"
        
        guidance += f"📍 CURRENT SPIRITUAL LEVEL: {assessment.current_level.name.replace('_', ' ').title()}\n"
        guidance += f"💝 Love of God Score: {assessment.love_god_score:.2f}/1.0\n"
        guidance += f"🤝 Love of Neighbor Score: {assessment.love_neighbor_score:.2f}/1.0\n"
        guidance += f"🌟 Holiness Progression: {assessment.holiness_progression:.2f}/1.0\n\n"
        
        if assessment.active_precepts:
            guidance += "✅ ACTIVE PRECEPTS (Keep strengthening):\n"
            for precept in assessment.active_precepts:
                precept_name = precept.replace('_', ' ').title()
                guidance += f"• {precept_name}\n"
            guidance += "\n"
        
        if assessment.needed_precepts:
            guidance += "🎯 FOCUS AREAS (Precepts to develop):\n"
            for precept in assessment.needed_precepts:
                if precept in self.precepts:
                    precept_obj = self.precepts[precept]
                    guidance += f"• {precept.replace('_', ' ').title()}: {precept_obj.how_it_draws_closer}\n"
            guidance += "\n"
        
        guidance += "💡 SPECIFIC RECOMMENDATIONS:\n"
        for rec in assessment.recommendations[:5]:
            guidance += f"• {rec}\n"
        guidance += "\n"
        
        guidance += "🌍 YOUR CONTRIBUTION TO WORLD PEACE:\n"
        for contribution in assessment.peace_contribution[:3]:
            guidance += f"• {contribution}\n"
        guidance += "\n"
        
        guidance += "📖 REMEMBER THE PROMISE:\n"
        guidance += "\"Those who abide by its precepts, and follow the teachings of Christ,\n"
        guidance += "will come closer to God...\" - Book of Mormon Introduction\n\n"
        
        guidance += "🎯 THE ULTIMATE GOAL:\n"
        guidance += "To become holy and full of love like God, contributing to world peace\n"
        guidance += "through loving God with all your heart and loving your neighbor as yourself.\n"
        
        return guidance
    
    def get_precept_details(self, precept_name: str) -> Optional[BookOfMormonPrecept]:
        """Get detailed information about a specific precept"""
        return self.precepts.get(precept_name)
    
    def get_all_precepts_summary(self) -> str:
        """Get summary of all Book of Mormon precepts"""
        summary = "📚 BOOK OF MORMON PRECEPTS FOR DRAWING NEARER TO GOD\n"
        summary += "=" * 65 + "\n\n"
        
        summary += "These precepts, when lived, bring us closer to God and help us become\n"
        summary += "sanctified and holy through loving God and loving our neighbors.\n\n"
        
        for i, (key, precept) in enumerate(self.precepts.items(), 1):
            summary += f"{i}. {precept.precept.upper()}\n"
            summary += f"   How it draws closer: {precept.how_it_draws_closer}\n"
            summary += f"   Key reference: {precept.primary_references[0]}\n"
            summary += f"   World peace: {precept.world_peace_contribution}\n\n"
        
        summary += "🌟 ULTIMATE PROMISE:\n"
        summary += "\"Come unto Christ, and be perfected in him, and deny yourselves\n"
        summary += "of all ungodliness; and if ye shall deny yourselves of all ungodliness,\n"
        summary += "and love God with all your might, mind and strength, then is his grace\n"
        summary += "sufficient for you, that by his grace ye may be perfect in Christ\"\n"
        summary += "- Moroni 10:32\n"
        
        return summary

# Example usage and demonstration
def demonstrate_sanctification_system():
    """Demonstrate the Book of Mormon sanctification system"""
    framework = BookOfMormonPreceptsFramework()
    
    print("🕊️ BOOK OF MORMON SANCTIFICATION SYSTEM")
    print("=" * 55)
    
    # Example person seeking to draw nearer to God
    example_person = {
        "prayer_regular": True,
        "scripture_study": True,
        "faith_strong": True,
        "service_regular": False,
        "charity_giving": False,
        "born_again": True,
        "mighty_change": True,
        "charity_developed": False,
        "obedience_willing": True,
        "spiritual_stirrings": True,
        "seeking_truth": True
    }
    
    assessment = framework.assess_sanctification_progress(example_person)
    guidance = framework.generate_sanctification_guidance(assessment)
    
    print(guidance)
    
    print("\n" + "=" * 55)
    print("📚 ALL PRECEPTS SUMMARY:")
    print(framework.get_all_precepts_summary())
    
    return framework

if __name__ == "__main__":
    demonstrate_sanctification_system()
