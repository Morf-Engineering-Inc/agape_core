
"""
Gospel Cycles Analysis Module
Analyzes historical patterns of God's relationship with His chosen people
Based on D&C 121:40-45 principles of righteous power and influence
"""

from dataclasses import dataclass
from typing import Dict, List, Optional, Any, Tuple
from enum import Enum
import csv
import os
from pathlib import Path

class CycleType(Enum):
    RISE = "Up"
    FALL = "Down"
    STABLE = "Flat/Volatile"
    MIXED = "Mixed"

class Tradition(Enum):
    BIBLE_OT = "Bible-OT"
    BIBLE_NT = "Bible-NT"
    BIBLE_MIXED = "Bible-OT/NT"
    BOOK_OF_MORMON = "Book of Mormon"
    CHRISTIAN_ERA = "Christian Era"
    RESTORATION = "Restoration"

@dataclass
class GospelCycle:
    """Represents a cycle in gospel history"""
    period: str
    start_year: int
    end_year: int
    duration: int
    tradition: Tradition
    cycle_type: CycleType
    faithfulness_start: int
    faithfulness_end: int
    dominant_weakness: str
    cultivated_strength: str
    dominant_emotion: str
    olive_tree_stage: str
    notes: str
    midpoint_year: float
    faithfulness_delta: int

@dataclass
class CyclePattern:
    """Pattern analysis for cycle behavior"""
    pattern_name: str
    triggers: List[str]
    duration_range: Tuple[int, int]
    faithfulness_change_range: Tuple[int, int]
    common_weaknesses: List[str]
    required_strengths: List[str]
    typical_emotions: List[str]
    olive_tree_stages: List[str]
    dc_121_principle: str

class GospelCyclesAnalyzer:
    """
    Analyzes historical gospel cycles to understand God's relationship with His people
    Based on D&C 121:40-45 principles of righteous dominion
    """
    
    def __init__(self):
        self.cycles: List[GospelCycle] = []
        self.patterns: Dict[str, CyclePattern] = {}
        self.dc_121_principles = self._initialize_dc_121_principles()
        self.load_historical_data()
        self._analyze_patterns()
    
    def _initialize_dc_121_principles(self) -> Dict[str, str]:
        """Initialize D&C 121:40-45 principles for righteous dominion"""
        return {
            "authority_corruption": "That the rights of the priesthood are inseparably connected with the powers of heaven, and that the powers of heaven cannot be controlled nor handled only upon the principles of righteousness",
            "power_withdrawal": "That they may be conferred upon us, it is true; but when we undertake to cover our sins, or to gratify our pride, our vain ambition, or to exercise control or dominion or compulsion upon the souls of the children of men, in any degree of unrighteousness, behold, the heavens withdraw themselves",
            "spirit_grieved": "The Spirit of the Lord is grieved; and when it is withdrawn, Amen to the priesthood or the authority of that man",
            "natural_man": "Behold, ere he is aware, he is left unto himself, to kick against the pricks, to persecute the saints, and to fight against God",
            "righteous_power": "No power or influence can or ought to be maintained by virtue of the priesthood, only by persuasion, by long-suffering, by gentleness and meekness, and by love unfeigned",
            "warning_rebuke": "By kindness, and pure knowledge, which shall greatly enlarge the soul without hypocrisy, and without guile—Reproving betimes with sharpness, when moved upon by the Holy Ghost; and then showing forth afterwards an increase of love toward him whom thou hast reproved, lest he esteem thee to be his enemy",
            "confidence_wax": "That he may know that thy faithfulness is stronger than the cords of death"
        }
    
    def load_historical_data(self):
        """Load historical cycle data from attached files"""
        # This would load from your CSV data
        sample_cycles = [
            GospelCycle(
                period="Patriarchs (Abraham→Joseph)",
                start_year=-2000, end_year=-1600, duration=400,
                tradition=Tradition.BIBLE_OT, cycle_type=CycleType.RISE,
                faithfulness_start=35, faithfulness_end=65,
                dominant_weakness="idolatry around nations",
                cultivated_strength="covenant loyalty",
                dominant_emotion="hope emerging",
                olive_tree_stage="Planting & early pruning",
                notes="Covenants established; family line preserved",
                midpoint_year=-1800.0, faithfulness_delta=30
            ),
            GospelCycle(
                period="Divided Kingdom (Israel/Judah)",
                start_year=-930, end_year=-586, duration=344,
                tradition=Tradition.BIBLE_OT, cycle_type=CycleType.FALL,
                faithfulness_start=75, faithfulness_end=25,
                dominant_weakness="idolatry, injustice",
                cultivated_strength="prophetic calls",
                dominant_emotion="stubbornness",
                olive_tree_stage="Decay; removal of dead wood",
                notes="Leads to Assyrian/Babylonian exiles",
                midpoint_year=-758.0, faithfulness_delta=-50
            ),
            GospelCycle(
                period="Ministry of Jesus",
                start_year=-30, end_year=33, duration=63,
                tradition=Tradition.BIBLE_NT, cycle_type=CycleType.RISE,
                faithfulness_start=50, faithfulness_end=100,
                dominant_weakness="doubt, fear",
                cultivated_strength="faith, charity",
                dominant_emotion="joy, peace",
                olive_tree_stage="Master Gardener arrives",
                notes="Fullness of gospel, atonement",
                midpoint_year=1.5, faithfulness_delta=50
            ),
            GospelCycle(
                period="Great Apostasy (post-apostolic)",
                start_year=100, end_year=1820, duration=1720,
                tradition=Tradition.CHRISTIAN_ERA, cycle_type=CycleType.FALL,
                faithfulness_start=70, faithfulness_end=15,
                dominant_weakness="corruption, loss of authority",
                cultivated_strength="conscience, fragments of light",
                dominant_emotion="confusion→yearning",
                olive_tree_stage="Overgrowth / wild branches dominate",
                notes="Plain and precious truths lost (per LDS view)",
                midpoint_year=960.0, faithfulness_delta=-55
            ),
            GospelCycle(
                period="Restoration to Present",
                start_year=1820, end_year=2025, duration=205,
                tradition=Tradition.RESTORATION, cycle_type=CycleType.RISE,
                faithfulness_start=15, faithfulness_end=80,
                dominant_weakness="scattering, skepticism",
                cultivated_strength="revelation, ordinances, gathering Israel",
                dominant_emotion="hope, covenant confidence",
                olive_tree_stage="Massive grafting, global tending",
                notes="Ongoing gathering & temple work",
                midpoint_year=1922.5, faithfulness_delta=65
            )
        ]
        self.cycles = sample_cycles
    
    def _analyze_patterns(self):
        """Analyze historical patterns based on D&C 121 principles"""
        self.patterns = {
            "pride_cycle": CyclePattern(
                pattern_name="Pride Cycle",
                triggers=["prosperity", "success", "power", "wealth"],
                duration_range=(50, 200),
                faithfulness_change_range=(-60, -20),
                common_weaknesses=["pride", "inequality", "oppression", "forgetting God"],
                required_strengths=["humility", "charity", "service", "remembrance"],
                typical_emotions=["stubbornness", "hardness", "anger"],
                olive_tree_stages=["Overgrowth", "Wild branches dominate", "Decay"],
                dc_121_principle="gratify our pride, our vain ambition, or to exercise control or dominion"
            ),
            
            "persecution_purification": CyclePattern(
                pattern_name="Persecution Purification",
                triggers=["external threats", "suffering", "captivity", "exile"],
                duration_range=(20, 100),
                faithfulness_change_range=(10, 40),
                common_weaknesses=["fear", "doubt", "despair"],
                required_strengths=["faith", "endurance", "unity"],
                typical_emotions=["godly sorrow", "hope", "determination"],
                olive_tree_stages=["Heavy pruning", "Soil renewal", "Careful tending"],
                dc_121_principle="by long-suffering, by gentleness and meekness"
            ),
            
            "revelation_restoration": CyclePattern(
                pattern_name="Revelation Restoration",
                triggers=["prophetic calling", "divine visitation", "new scripture"],
                duration_range=(30, 100),
                faithfulness_change_range=(30, 65),
                common_weaknesses=["ignorance", "tradition", "hardness"],
                required_strengths=["revelation", "authority", "truth"],
                typical_emotions=["joy", "hope", "covenant confidence"],
                olive_tree_stages=["Grafting", "New planting", "Master Gardener arrives"],
                dc_121_principle="by pure knowledge, which shall greatly enlarge the soul"
            ),
            
            "apostasy_drift": CyclePattern(
                pattern_name="Apostasy Drift",
                triggers=["loss of authority", "corruption", "worldliness"],
                duration_range=(100, 1800),
                faithfulness_change_range=(-70, -10),
                common_weaknesses=["corruption", "loss of keys", "false doctrine"],
                required_strengths=["conscience", "fragments of light", "yearning"],
                typical_emotions=["confusion", "darkness", "spiritual hunger"],
                olive_tree_stages=["Wild branches", "Overgrowth", "Neglect"],
                dc_121_principle="the heavens withdraw themselves; The Spirit of the Lord is grieved"
            )
        }
    
    def predict_cycle_behavior(self, current_conditions: Dict[str, Any]) -> Dict[str, Any]:
        """Predict likely cycle behavior based on current conditions and D&C 121 principles"""
        prediction = {
            "likely_pattern": None,
            "cycle_direction": None,
            "duration_estimate": None,
            "key_warnings": [],
            "required_interventions": [],
            "dc_121_guidance": [],
            "confidence_score": 0.0
        }
        
        # Analyze current conditions against known patterns
        pattern_scores = {}
        
        for pattern_name, pattern in self.patterns.items():
            score = self._calculate_pattern_match(current_conditions, pattern)
            pattern_scores[pattern_name] = score
        
        # Find best matching pattern
        best_pattern = max(pattern_scores.items(), key=lambda x: x[1])
        if best_pattern[1] > 0.3:  # Threshold for confident prediction
            pattern = self.patterns[best_pattern[0]]
            prediction["likely_pattern"] = best_pattern[0]
            prediction["confidence_score"] = best_pattern[1]
            
            # Predict cycle direction
            if "fall" in pattern.pattern_name.lower() or "apostasy" in pattern.pattern_name.lower():
                prediction["cycle_direction"] = "Decline"
            else:
                prediction["cycle_direction"] = "Rise"
            
            # Estimate duration
            min_dur, max_dur = pattern.duration_range
            prediction["duration_estimate"] = f"{min_dur}-{max_dur} years"
            
            # Generate warnings based on D&C 121
            prediction["key_warnings"] = self._generate_dc_121_warnings(pattern)
            
            # Generate interventions
            prediction["required_interventions"] = self._generate_interventions(pattern)
            
            # D&C 121 guidance
            prediction["dc_121_guidance"] = self._generate_dc_121_guidance(pattern)
        
        return prediction
    
    def _calculate_pattern_match(self, conditions: Dict[str, Any], pattern: CyclePattern) -> float:
        """Calculate how well current conditions match a historical pattern"""
        score = 0.0
        total_factors = 0
        
        # Check triggers
        if "triggers" in conditions:
            trigger_matches = sum(1 for trigger in pattern.triggers 
                                if any(trigger.lower() in cond.lower() for cond in conditions["triggers"]))
            score += (trigger_matches / len(pattern.triggers)) * 0.3
            total_factors += 0.3
        
        # Check weaknesses
        if "weaknesses" in conditions:
            weakness_matches = sum(1 for weakness in pattern.common_weaknesses
                                 if any(weakness.lower() in weak.lower() for weak in conditions["weaknesses"]))
            score += (weakness_matches / len(pattern.common_weaknesses)) * 0.3
            total_factors += 0.3
        
        # Check emotions
        if "emotions" in conditions:
            emotion_matches = sum(1 for emotion in pattern.typical_emotions
                                if any(emotion.lower() in emo.lower() for emo in conditions["emotions"]))
            score += (emotion_matches / len(pattern.typical_emotions)) * 0.2
            total_factors += 0.2
        
        # Check strengths (inverse - lack of strengths increases match for negative patterns)
        if "strengths" in conditions:
            strength_deficit = len(pattern.required_strengths) - len(conditions["strengths"])
            if "apostasy" in pattern.pattern_name.lower() or "pride" in pattern.pattern_name.lower():
                score += max(0, strength_deficit / len(pattern.required_strengths)) * 0.2
            else:
                strength_matches = sum(1 for strength in pattern.required_strengths
                                     if any(strength.lower() in str_cond.lower() for str_cond in conditions["strengths"]))
                score += (strength_matches / len(pattern.required_strengths)) * 0.2
            total_factors += 0.2
        
        return score / total_factors if total_factors > 0 else 0.0
    
    def _generate_dc_121_warnings(self, pattern: CyclePattern) -> List[str]:
        """Generate warnings based on D&C 121 principles"""
        warnings = []
        
        if "pride" in pattern.pattern_name.lower():
            warnings.extend([
                "PRIDE WARNING: 'when we undertake to gratify our pride, our vain ambition'",
                "DOMINION WARNING: 'exercise control or dominion or compulsion upon the souls of men'",
                "HEAVEN'S WITHDRAWAL: 'behold, the heavens withdraw themselves'"
            ])
        
        if "apostasy" in pattern.pattern_name.lower():
            warnings.extend([
                "SPIRIT GRIEVED: 'The Spirit of the Lord is grieved; and when it is withdrawn'",
                "AUTHORITY LOST: 'Amen to the priesthood or the authority of that man'",
                "LEFT ALONE: 'he is left unto himself, to kick against the pricks'"
            ])
        
        if "persecution" in pattern.pattern_name.lower():
            warnings.extend([
                "FAITHFULNESS TEST: 'that he may know that thy faithfulness is stronger than the cords of death'",
                "LONG-SUFFERING REQUIRED: 'by long-suffering, by gentleness and meekness'"
            ])
        
        return warnings
    
    def _generate_interventions(self, pattern: CyclePattern) -> List[str]:
        """Generate required interventions based on pattern"""
        interventions = []
        
        for strength in pattern.required_strengths:
            if strength == "humility":
                interventions.append("Cultivate humility through service and submission to God's will")
            elif strength == "charity":
                interventions.append("Develop pure love of Christ through serving others")
            elif strength == "revelation":
                interventions.append("Seek personal revelation and follow living prophets")
            elif strength == "unity":
                interventions.append("Build Zion through consecration and common purpose")
            elif strength == "faith":
                interventions.append("Strengthen faith through prayer, scripture study, and obedience")
        
        return interventions
    
    def _generate_dc_121_guidance(self, pattern: CyclePattern) -> List[str]:
        """Generate specific D&C 121 guidance for the pattern"""
        guidance = []
        
        # Always include the core righteous dominion principle
        guidance.append("RIGHTEOUS POWER: 'by persuasion, by long-suffering, by gentleness and meekness, and by love unfeigned'")
        
        if "pride" in pattern.pattern_name.lower():
            guidance.append("KNOWLEDGE WITH KINDNESS: 'by kindness, and pure knowledge, which shall greatly enlarge the soul'")
            guidance.append("NO HYPOCRISY: 'without hypocrisy, and without guile'")
        
        if any(word in pattern.pattern_name.lower() for word in ["persecution", "suffering"]):
            guidance.append("REPROOF WITH LOVE: 'Reproving betimes with sharpness, when moved upon by the Holy Ghost'")
            guidance.append("INCREASE LOVE: 'then showing forth afterwards an increase of love'")
        
        guidance.append("FAITHFUL UNTO DEATH: 'that thy faithfulness is stronger than the cords of death'")
        
        return guidance
    
    def analyze_current_restoration_cycle(self) -> Dict[str, Any]:
        """Analyze the current Restoration cycle for patterns and predictions"""
        current_cycle = next((c for c in self.cycles if c.tradition == Tradition.RESTORATION), None)
        
        if not current_cycle:
            return {"error": "Current restoration cycle not found"}
        
        analysis = {
            "current_phase": "Restoration Rise",
            "duration_so_far": 2025 - 1820,
            "faithfulness_trajectory": f"{current_cycle.faithfulness_start} → {current_cycle.faithfulness_end}",
            "current_weaknesses": current_cycle.dominant_weakness.split(", "),
            "cultivated_strengths": current_cycle.cultivated_strength.split(", "),
            "emotional_state": current_cycle.dominant_emotion,
            "olive_tree_stage": current_cycle.olive_tree_stage,
            "historical_parallels": [],
            "potential_threats": [],
            "strengthening_opportunities": []
        }
        
        # Find historical parallels
        similar_cycles = [c for c in self.cycles 
                         if c.cycle_type == CycleType.RISE and c.tradition != Tradition.RESTORATION]
        
        for cycle in similar_cycles:
            if abs(cycle.faithfulness_delta - current_cycle.faithfulness_delta) < 20:
                analysis["historical_parallels"].append({
                    "period": cycle.period,
                    "pattern": f"Similar rise pattern (+{cycle.faithfulness_delta})",
                    "outcome": cycle.notes
                })
        
        # Identify potential threats based on D&C 121
        analysis["potential_threats"] = [
            "Pride from prosperity and growth",
            "Institutionalization leading to loss of Spirit",
            "Worldly influences and secular pressures",
            "Internal apostasy and false teachings",
            "Persecution leading to compromise"
        ]
        
        # Strengthening opportunities
        analysis["strengthening_opportunities"] = [
            "Continue global gathering of Israel",
            "Strengthen families and youth",
            "Increase temple work and ordinances",
            "Develop Christlike attributes through service",
            "Follow living prophets and revelation"
        ]
        
        return analysis
    
    def get_cycle_summary(self) -> str:
        """Get a comprehensive summary of gospel cycles"""
        summary = "🕊️ GOSPEL CYCLES ANALYSIS: God's Relationship with His People\n"
        summary += "=" * 70 + "\n\n"
        
        summary += "📊 HISTORICAL PATTERNS BASED ON D&C 121:40-45:\n\n"
        
        # Cycle statistics
        rise_cycles = [c for c in self.cycles if c.cycle_type == CycleType.RISE]
        fall_cycles = [c for c in self.cycles if c.cycle_type == CycleType.FALL]
        
        summary += f"📈 RISE CYCLES: {len(rise_cycles)} periods\n"
        summary += f"   Average Duration: {sum(c.duration for c in rise_cycles) / len(rise_cycles):.0f} years\n"
        summary += f"   Average Faithfulness Gain: +{sum(c.faithfulness_delta for c in rise_cycles) / len(rise_cycles):.0f}\n\n"
        
        summary += f"📉 FALL CYCLES: {len(fall_cycles)} periods\n"
        summary += f"   Average Duration: {sum(c.duration for c in fall_cycles) / len(fall_cycles):.0f} years\n"
        summary += f"   Average Faithfulness Loss: {sum(c.faithfulness_delta for c in fall_cycles) / len(fall_cycles):.0f}\n\n"
        
        # Key patterns
        summary += "🔄 KEY PATTERNS IDENTIFIED:\n\n"
        for pattern_name, pattern in self.patterns.items():
            summary += f"• {pattern.pattern_name.upper()}:\n"
            summary += f"  Triggers: {', '.join(pattern.triggers[:3])}\n"
            summary += f"  D&C 121 Connection: {pattern.dc_121_principle[:50]}...\n"
            summary += f"  Duration: {pattern.duration_range[0]}-{pattern.duration_range[1]} years\n\n"
        
        # Current restoration analysis
        summary += "🌟 CURRENT RESTORATION CYCLE:\n"
        current = self.analyze_current_restoration_cycle()
        summary += f"Duration So Far: {current['duration_so_far']} years\n"
        summary += f"Trajectory: {current['faithfulness_trajectory']}\n"
        summary += f"Stage: {current['olive_tree_stage']}\n"
        summary += f"Key Strengths: {', '.join(current['cultivated_strengths'])}\n\n"
        
        summary += "⚠️ KEY D&C 121 WARNINGS FOR CURRENT CYCLE:\n"
        summary += "• Pride and vain ambition lead to heaven's withdrawal\n"
        summary += "• Authority must be exercised in righteousness\n"
        summary += "• Power comes through persuasion and love, not compulsion\n"
        summary += "• Knowledge must be coupled with kindness and humility\n\n"
        
        summary += "💡 BEHAVIORAL PREDICTIONS:\n"
        summary += "Based on historical patterns, righteousness brings:\n"
        summary += "• Divine favor and protection\n"
        summary += "• Spiritual growth and revelation\n"
        summary += "• Prosperity and gathering\n"
        summary += "• Unity and Zion-like conditions\n\n"
        
        summary += "Apostasy/wickedness brings:\n"
        summary += "• Loss of spiritual authority\n"
        summary += "• Heaven's withdrawal\n"
        summary += "• Scattering and destruction\n"
        summary += "• Bondage and suffering\n\n"
        
        return summary

# Example usage and demonstration
def demo_gospel_cycles():
    """Demonstrate the Gospel Cycles analyzer"""
    analyzer = GospelCyclesAnalyzer()
    
    print("🕊️ GOSPEL CYCLES ANALYSIS DEMONSTRATION")
    print("=" * 60)
    
    # Show cycle summary
    print(analyzer.get_cycle_summary())
    
    # Test prediction with sample conditions
    print("\n" + "=" * 60)
    print("🔮 BEHAVIORAL PREDICTION EXAMPLE")
    print("-" * 30)
    
    current_conditions = {
        "triggers": ["prosperity", "growth", "success"],
        "weaknesses": ["pride", "inequality", "worldliness"],
        "strengths": ["revelation", "gathering"],
        "emotions": ["confidence", "some stubbornness"]
    }
    
    prediction = analyzer.predict_cycle_behavior(current_conditions)
    
    print(f"Sample Conditions: {current_conditions}")
    print(f"\nPredicted Pattern: {prediction['likely_pattern']}")
    print(f"Confidence: {prediction['confidence_score']:.2f}")
    print(f"Likely Direction: {prediction['cycle_direction']}")
    print(f"Duration Estimate: {prediction['duration_estimate']}")
    
    if prediction["key_warnings"]:
        print(f"\n⚠️ D&C 121 Warnings:")
        for warning in prediction["key_warnings"][:2]:
            print(f"• {warning}")
    
    if prediction["dc_121_guidance"]:
        print(f"\n💡 D&C 121 Guidance:")
        for guidance in prediction["dc_121_guidance"][:2]:
            print(f"• {guidance}")

if __name__ == "__main__":
    demo_gospel_cycles()
