
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
    All cycles point toward the Millennial reign of Christ as the ultimate reference point
    """
    
    def __init__(self):
        self.cycles: List[GospelCycle] = []
        self.patterns: Dict[str, CyclePattern] = {}
        self.dc_121_principles = self._initialize_dc_121_principles()
        self.millennial_prophecies = self._initialize_millennial_framework()
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
    
    def _initialize_millennial_framework(self) -> Dict[str, Any]:
        """Initialize the Millennial prophecy framework as ultimate reference point"""
        return {
            "prophetic_timeline": {
                "current_phase": "Restoration gathering (pre-Second Coming)",
                "next_phase": "Signs, tribulations, and preparation",
                "culmination": "Second Coming of Jesus Christ",
                "millennial_reign": "1000 years of peace under Christ's direct rule",
                "final_judgment": "End of mortality, final resurrection and judgment"
            },
            "millennial_characteristics": {
                "righteousness": "Satan bound, righteousness prevails (Rev 20:2)",
                "peace": "No war, lion lies with lamb (Isaiah 11:6-9)",
                "knowledge": "Earth filled with knowledge of God (Isaiah 11:9)",
                "justice": "Perfect justice under Christ's rule (Isaiah 9:6-7)",
                "healing": "No death, sickness, or sorrow until end (D&C 101:29-31)",
                "temple_work": "Work for the dead completed (D&C 138:58)",
                "unity": "One fold, one shepherd (John 10:16)"
            },
            "vineyard_completion": {
                "final_harvest": "Gathering of Israel completed before Second Coming",
                "burning": "Wicked destroyed at Second Coming (Malachi 4:1)",
                "preservation": "Righteous preserved and gathered (D&C 45:57)",
                "restoration": "Earth receives paradisiacal glory (Articles of Faith 1:10)",
                "perfect_fruit": "All remaining branches bear good fruit under Christ"
            },
            "reference_point_implications": {
                "all_cycles_point_forward": "Every historical cycle prepares for the Millennium",
                "ultimate_restoration": "All faithful will be gathered and perfected",
                "pattern_completion": "Pride cycles end permanently under Christ's rule",
                "perfect_law": "D&C 121 principles perfectly implemented globally",
                "eternal_perspective": "Temporal decisions evaluated by millennial standards"
            },
            "prophecy_indicators": {
                "gathering_acceleration": "Global missionary work and temple building",
                "knowledge_increase": "Daniel 12:4 - knowledge runs to and fro",
                "spiritual_gifts": "Joel 2:28-29 - Spirit poured out on all flesh",
                "signs_in_heaven": "Luke 21:25 - signs in sun, moon, stars",
                "restoration_completion": "All keys and authority restored",
                "gospel_to_all": "Matthew 24:14 - gospel preached to all nations"
            }
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
                olive_tree_stage="Massive grafting, global tending - preparing for final harvest",
                notes="Ongoing gathering & temple work; preparing for Second Coming",
                midpoint_year=1922.5, faithfulness_delta=65
            ),
            
            # Add prophesied Millennium as reference point
            GospelCycle(
                period="Millennium (Prophesied)",
                start_year=2030, end_year=3030, duration=1000,  # Approximate timing
                tradition=Tradition.RESTORATION, cycle_type=CycleType.RISE,
                faithfulness_start=90, faithfulness_end=100,
                dominant_weakness="none (Satan bound)",
                cultivated_strength="perfect righteousness, knowledge, peace",
                dominant_emotion="perfect joy, peace",
                olive_tree_stage="Perfect fruit under Master Gardener's direct presence",
                notes="Christ reigns personally; earth in paradisiacal glory",
                midpoint_year=2530.0, faithfulness_delta=10
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
    
    def analyze_olive_tree_patterns(self) -> Dict[str, Any]:
        """Analyze patterns using the Olive Tree/Vineyard allegory framework"""
        olive_tree_analysis = {
            "vineyard_stages": {},
            "pruning_cycles": [],
            "grafting_periods": [],
            "fruit_seasons": [],
            "burning_periods": [],
            "master_gardener_interventions": [],
            "current_vineyard_state": None
        }
        
        # Categorize periods by olive tree stages
        stage_categories = {
            "planting": ["Planting", "New planting", "Choice land"],
            "pruning": ["Pruning", "Heavy pruning", "Decay", "removal", "training"],
            "grafting": ["Grafting", "Massive grafting", "replanting"],
            "flourishing": ["full fruit", "Master Gardener", "prosperity"],
            "overgrowth": ["Overgrowth", "wild branches", "Neglect"],
            "burning": ["burned", "destruction", "lopping"]
        }
        
        for cycle in self.cycles:
            stage_lower = cycle.olive_tree_stage.lower()
            
            # Categorize each cycle
            for category, keywords in stage_categories.items():
                if any(keyword.lower() in stage_lower for keyword in keywords):
                    if category not in olive_tree_analysis["vineyard_stages"]:
                        olive_tree_analysis["vineyard_stages"][category] = []
                    olive_tree_analysis["vineyard_stages"][category].append({
                        "period": cycle.period,
                        "duration": cycle.duration,
                        "faithfulness_change": cycle.faithfulness_delta,
                        "weakness": cycle.dominant_weakness,
                        "strength": cycle.cultivated_strength,
                        "emotion": cycle.dominant_emotion
                    })
            
            # Identify specific patterns
            if "pruning" in stage_lower or "decay" in stage_lower:
                olive_tree_analysis["pruning_cycles"].append({
                    "period": cycle.period,
                    "pruning_type": "Heavy pruning" if cycle.faithfulness_delta < -20 else "Light pruning",
                    "recovery_potential": abs(cycle.faithfulness_delta),
                    "lessons": self._extract_pruning_lessons(cycle)
                })
            
            if "grafting" in stage_lower:
                olive_tree_analysis["grafting_periods"].append({
                    "period": cycle.period,
                    "grafting_success": cycle.faithfulness_delta,
                    "integration_challenges": cycle.dominant_weakness,
                    "new_strength": cycle.cultivated_strength
                })
            
            if "fruit" in stage_lower or cycle.faithfulness_end > 80:
                olive_tree_analysis["fruit_seasons"].append({
                    "period": cycle.period,
                    "fruit_quality": cycle.faithfulness_end,
                    "sustainability_factors": cycle.cultivated_strength,
                    "threats": cycle.dominant_weakness
                })
            
            if "Master Gardener" in cycle.olive_tree_stage:
                olive_tree_analysis["master_gardener_interventions"].append({
                    "period": cycle.period,
                    "intervention_type": "Direct presence",
                    "transformation_power": cycle.faithfulness_delta,
                    "lasting_impact": cycle.notes
                })
        
        # Current vineyard state analysis
        current_cycle = next((c for c in self.cycles if c.tradition == Tradition.RESTORATION), None)
        if current_cycle:
            olive_tree_analysis["current_vineyard_state"] = self._analyze_current_vineyard_state(current_cycle)
        
        return olive_tree_analysis
    
    def _extract_pruning_lessons(self, cycle: GospelCycle) -> List[str]:
        """Extract lessons from pruning periods"""
        lessons = []
        
        if "pride" in cycle.dominant_weakness.lower():
            lessons.append("Pride leads to spiritual decay requiring severe pruning")
        if "oppression" in cycle.dominant_weakness.lower():
            lessons.append("Oppression of others brings divine judgment")
        if "idolatry" in cycle.dominant_weakness.lower():
            lessons.append("Idolatry replaces good fruit with wild, bitter fruit")
        if cycle.faithfulness_delta < -30:
            lessons.append("Severe spiritual decline requires extended recovery time")
        
        # Add strength-building lessons
        strengths = cycle.cultivated_strength.lower()
        if "faith" in strengths:
            lessons.append("Pruning develops deeper faith and reliance on God")
        if "humility" in strengths:
            lessons.append("Suffering teaches humility and dependence on divine grace")
        
        return lessons
    
    def _analyze_current_vineyard_state(self, current_cycle: GospelCycle) -> Dict[str, Any]:
        """Analyze current state of the Lord's vineyard"""
        return {
            "stage": "Massive grafting, global tending",
            "global_scope": "Worldwide gathering of scattered Israel",
            "grafting_success": f"{current_cycle.faithfulness_start} → {current_cycle.faithfulness_end}",
            "current_challenges": [
                "Wild branches (apostasy) still present",
                "Some areas need heavy pruning (reformation)",
                "Grafted branches need strengthening (new converts)",
                "Soil preparation (missionary work) ongoing"
            ],
            "master_gardener_presence": "Through living prophets and continuing revelation",
            "fruit_prospects": "Preparing for final harvest",
            "warnings": [
                "Pride can cause good branches to go wild",
                "Neglect leads to overgrowth and loss",
                "Some branches may need removal if they corrupt others"
            ],
            "opportunities": [
                "Technology enables global grafting",
                "Temples provide spiritual nourishment",
                "Youth are 'choice branches' ready for service"
            ]
        }
    
    def get_olive_tree_timeline(self) -> str:
        """Generate a comprehensive Olive Tree timeline analysis"""
        timeline = "🌳 OLIVE TREE ALLEGORY TIMELINE - Lord's Vineyard Through History\n"
        timeline += "=" * 80 + "\n\n"
        
        timeline += "📖 BASED ON ISAIAH 5 & JACOB 5 (Book of Mormon)\n"
        timeline += "The Lord's vineyard represents His covenant people throughout history\n\n"
        
        # Sort cycles chronologically
        sorted_cycles = sorted(self.cycles, key=lambda x: x.start_year)
        
        for cycle in sorted_cycles:
            timeline += f"🕐 {cycle.period} ({cycle.start_year} to {cycle.end_year})\n"
            timeline += f"   🌳 Vineyard Stage: {cycle.olive_tree_stage}\n"
            timeline += f"   📊 Spiritual Health: {cycle.faithfulness_start} → {cycle.faithfulness_end}\n"
            timeline += f"   🪓 Pruning Needed: {cycle.dominant_weakness}\n"
            timeline += f"   🌱 New Growth: {cycle.cultivated_strength}\n"
            timeline += f"   💭 Gardener's Mood: {cycle.dominant_emotion}\n"
            timeline += f"   📝 Vineyard Notes: {cycle.notes}\n"
            
            # Add Jacob 5 insights
            stage_insights = self._get_jacob_5_insights(cycle.olive_tree_stage)
            if stage_insights:
                timeline += f"   💡 Jacob 5 Insight: {stage_insights}\n"
            
            timeline += "\n" + "-" * 60 + "\n\n"
        
        # Add pattern analysis
        olive_analysis = self.analyze_olive_tree_patterns()
        
        timeline += "🔍 VINEYARD PATTERN ANALYSIS:\n\n"
        
        if olive_analysis["pruning_cycles"]:
            timeline += "✂️ PRUNING CYCLES IDENTIFIED:\n"
            for pruning in olive_analysis["pruning_cycles"]:
                timeline += f"• {pruning['period']}: {pruning['pruning_type']}\n"
                timeline += f"  Recovery Potential: {pruning['recovery_potential']}\n"
                for lesson in pruning['lessons'][:2]:
                    timeline += f"  Lesson: {lesson}\n"
            timeline += "\n"
        
        if olive_analysis["grafting_periods"]:
            timeline += "🌿 GRAFTING PERIODS:\n"
            for grafting in olive_analysis["grafting_periods"]:
                timeline += f"• {grafting['period']}: Success rate {grafting['grafting_success']}\n"
                timeline += f"  New Strength: {grafting['new_strength']}\n"
            timeline += "\n"
        
        if olive_analysis["master_gardener_interventions"]:
            timeline += "👨‍🌾 MASTER GARDENER DIRECT INTERVENTIONS:\n"
            for intervention in olive_analysis["master_gardener_interventions"]:
                timeline += f"• {intervention['period']}: {intervention['intervention_type']}\n"
                timeline += f"  Impact: {intervention['transformation_power']} point change\n"
            timeline += "\n"
        
        # Current state
        if olive_analysis["current_vineyard_state"]:
            current = olive_analysis["current_vineyard_state"]
            timeline += "🌟 CURRENT VINEYARD STATE (Restoration Era):\n"
            timeline += f"Stage: {current['stage']}\n"
            timeline += f"Global Scope: {current['global_scope']}\n"
            timeline += f"Progress: {current['grafting_success']}\n"
            timeline += f"Master Gardener: {current['master_gardener_presence']}\n\n"
            
            timeline += "⚠️ CURRENT CHALLENGES:\n"
            for challenge in current['challenges'][:3]:
                timeline += f"• {challenge}\n"
            timeline += "\n"
            
            timeline += "💪 CURRENT OPPORTUNITIES:\n"
            for opportunity in current['opportunities']:
                timeline += f"• {opportunity}\n"
        
        timeline += "\n" + "=" * 80 + "\n"
        timeline += "🔮 VINEYARD PROPHECY: The final harvest approaches.\n"
        timeline += "Jacob 5:77 - 'And it came to pass that they did work, and did dig'\n"
        timeline += "about the trees, and they did nourish them; and the trees became good.'\n"
        
        return timeline
    
    def _get_jacob_5_insights(self, olive_tree_stage: str) -> str:
        """Get specific Jacob 5 insights for each vineyard stage"""
        stage_lower = olive_tree_stage.lower()
        
        insights = {
            "planting": "Jacob 5:3 - The Lord planted His vineyard in choice land",
            "pruning": "Jacob 5:4 - 'I will prune it, and dig about it, that perhaps it may bring forth good fruit'",
            "grafting": "Jacob 5:16-17 - Natural branches grafted into wild olive tree",
            "decay": "Jacob 5:32 - 'The wild fruit of the tree did overcome that part of the tree which brought forth good fruit'",
            "overgrowth": "Jacob 5:47 - 'And we have nourished it, and it hath brought forth much fruit, and there is none of it which is good'",
            "master gardener": "Jacob 5:71 - 'And the Lord of the vineyard said unto the servant: Let us go to and hew down the trees'",
            "burning": "Jacob 5:77 - Final attempt before burning the vineyard",
            "massive grafting": "Jacob 5:52 - 'Let us take of the branches of these which I have planted in the nethermost parts of my vineyard'"
        }
        
        for key, insight in insights.items():
            if key in stage_lower:
                return insight
        
        return ""
    
    def evaluate_millennial_proximity(self) -> Dict[str, Any]:
        """Evaluate how close we are to millennial conditions based on prophecy indicators"""
        indicators = self.millennial_prophecies["prophecy_indicators"]
        
        # Score current fulfillment of millennial indicators (simplified evaluation)
        indicator_scores = {
            "gathering_acceleration": 0.85,  # High global missionary activity, temple building
            "knowledge_increase": 0.95,     # Internet, AI, rapid information spread
            "spiritual_gifts": 0.70,        # Increasing spiritual experiences reported
            "signs_in_heaven": 0.60,        # Various astronomical phenomena
            "restoration_completion": 0.90,  # Most keys restored, ongoing revelation
            "gospel_to_all": 0.75           # Gospel reaching most nations
        }
        
        overall_proximity = sum(indicator_scores.values()) / len(indicator_scores)
        
        analysis = {
            "millennial_proximity_score": overall_proximity,
            "indicator_analysis": indicator_scores,
            "current_phase": self.millennial_prophecies["prophetic_timeline"]["current_phase"],
            "key_preparation_areas": [],
            "prophetic_patterns": [],
            "warning_signs": []
        }
        
        # Generate preparation recommendations
        if overall_proximity > 0.8:
            analysis["key_preparation_areas"] = [
                "Accelerate temple work and family history",
                "Strengthen individual and family righteousness",
                "Prepare temporally and spiritually for upheavals",
                "Increase missionary work and gathering"
            ]
        
        # Identify patterns that suggest we're in final restoration phase
        analysis["prophetic_patterns"] = [
            "Technology enabling global gospel spread",
            "Rapid temple construction worldwide", 
            "Increasing natural disasters and signs",
            "Growing polarization between good and evil",
            "Restoration of Israel and Jerusalem's importance"
        ]
        
        return analysis
    
    def predict_pre_millennial_cycles(self) -> Dict[str, Any]:
        """Predict remaining cycles before the Millennium"""
        millennial_analysis = self.evaluate_millennial_proximity()
        
        predictions = {
            "estimated_time_remaining": "Unknown, but signs suggest soon",
            "likely_pre_millennial_phases": [
                {
                    "phase": "Intensified Gathering",
                    "characteristics": "Accelerated missionary work, temple building",
                    "duration_estimate": "10-30 years",
                    "faithfulness_trajectory": "Rising among faithful, declining among rebellious"
                },
                {
                    "phase": "Great Divide/Polarization", 
                    "characteristics": "Clear separation between righteous and wicked",
                    "duration_estimate": "5-15 years",
                    "faithfulness_trajectory": "Extreme polarization"
                },
                {
                    "phase": "Tribulation and Signs",
                    "characteristics": "Natural disasters, wars, cleansing events",
                    "duration_estimate": "Variable, could be rapid",
                    "faithfulness_trajectory": "Testing of faith, purification"
                },
                {
                    "phase": "Second Coming Preparation",
                    "characteristics": "Final preparation, City of Zion, return to Jackson County",
                    "duration_estimate": "Final years before Second Coming",
                    "faithfulness_trajectory": "Righteous prepared, wicked destroyed"
                }
            ],
            "vineyard_implications": [
                "Final massive grafting of Israel",
                "Pruning of wicked branches (cleansing)",
                "Preparation of vineyard for Master's return",
                "Burning of chaff and preservation of wheat"
            ],
            "decision_making_guidance": [
                "Evaluate all choices by eternal/millennial standards",
                "Prioritize spiritual preparation over temporal security",
                "Focus on gathering and strengthening the faithful",
                "Prepare for both temporal trials and spiritual opportunities"
            ]
        }
        
        return predictions

    def get_cycle_summary(self) -> str:
        """Get a comprehensive summary of gospel cycles with Olive Tree framework"""
        summary = "🕊️ GOSPEL CYCLES ANALYSIS: God's Relationship with His People\n"
        summary += "🌳 Through the Lens of the Lord's Vineyard (Jacob 5)\n"
        summary += "👑 ULTIMATE REFERENCE POINT: The Millennium of Christ's Reign\n"
        summary += "=" * 70 + "\n\n"
        
        # Olive Tree pattern overview first
        summary += "🌳 VINEYARD OVERVIEW:\n"
        summary += "The Lord's vineyard (His covenant people) goes through cycles of:\n"
        summary += "• Planting (establishing covenants)\n"
        summary += "• Growth & pruning (trials that strengthen)\n" 
        summary += "• Grafting (bringing in new branches/people)\n"
        summary += "• Flourishing (righteousness bears good fruit)\n"
        summary += "• Decay/overgrowth (apostasy, wild branches dominate)\n"
        summary += "• Burning/renewal (judgment followed by restoration)\n\n"
        
        summary += "📊 HISTORICAL PATTERNS BASED ON D&C 121:40-45:\n\n"
        
        # Cycle statistics
        rise_cycles = [c for c in self.cycles if c.cycle_type == CycleType.RISE]
        fall_cycles = [c for c in self.cycles if c.cycle_type == CycleType.FALL]
        
        summary += f"📈 RISE CYCLES (Growth/Grafting): {len(rise_cycles)} periods\n"
        summary += f"   Average Duration: {sum(c.duration for c in rise_cycles) / len(rise_cycles):.0f} years\n"
        summary += f"   Average Faithfulness Gain: +{sum(c.faithfulness_delta for c in rise_cycles) / len(rise_cycles):.0f}\n\n"
        
        summary += f"📉 FALL CYCLES (Decay/Pruning): {len(fall_cycles)} periods\n"
        summary += f"   Average Duration: {sum(c.duration for c in fall_cycles) / len(fall_cycles):.0f} years\n"
        summary += f"   Average Faithfulness Loss: {sum(c.faithfulness_delta for c in fall_cycles) / len(fall_cycles):.0f}\n\n"
        
        # Olive Tree specific patterns
        olive_analysis = self.analyze_olive_tree_patterns()
        
        if olive_analysis["pruning_cycles"]:
            summary += f"✂️ PRUNING PERIODS: {len(olive_analysis['pruning_cycles'])} identified\n"
            heavy_pruning = sum(1 for p in olive_analysis["pruning_cycles"] if p["pruning_type"] == "Heavy pruning")
            summary += f"   Heavy Pruning Events: {heavy_pruning}\n"
            summary += f"   Pattern: Heavy pruning usually leads to stronger growth\n\n"
        
        if olive_analysis["grafting_periods"]:
            summary += f"🌿 GRAFTING PERIODS: {len(olive_analysis['grafting_periods'])} major grafting events\n"
            avg_success = sum(g["grafting_success"] for g in olive_analysis["grafting_periods"]) / len(olive_analysis["grafting_periods"])
            summary += f"   Average Success: +{avg_success:.0f} faithfulness points\n\n"
        
        # Current restoration analysis
        summary += "🌟 CURRENT RESTORATION CYCLE (Massive Grafting Era):\n"
        current = self.analyze_current_restoration_cycle()
        summary += f"Duration So Far: {current['duration_so_far']} years\n"
        summary += f"Trajectory: {current['faithfulness_trajectory']}\n"
        summary += f"Vineyard Stage: {current['olive_tree_stage']}\n"
        summary += f"Key Strengths: {', '.join(current['cultivated_strengths'])}\n\n"
        
        summary += "⚠️ VINEYARD WARNINGS (Based on Jacob 5 & D&C 121):\n"
        summary += "• Wild branches (apostasy) can overcome good fruit if not pruned\n"
        summary += "• Pride makes good branches go wild (D&C 121:37)\n"
        summary += "• Neglect leads to overgrowth and corruption\n"
        summary += "• The Master will burn the vineyard if it bears only evil fruit\n\n"
        
        summary += "💡 BEHAVIORAL PREDICTIONS FROM VINEYARD PATTERNS:\n"
        summary += "RIGHTEOUSNESS (Good Fruit) brings:\n"
        summary += "• Divine favor and protection\n"
        summary += "• Spiritual growth and revelation\n"
        summary += "• Prosperity and gathering (grafting success)\n"
        summary += "• Unity and Zion-like conditions\n\n"
        
        summary += "APOSTASY (Wild Fruit) brings:\n"
        summary += "• Loss of spiritual authority\n"
        summary += "• Heaven's withdrawal (pruning/cutting off)\n"
        summary += "• Scattering and destruction\n"
        summary += "• Risk of being burned with the chaff\n\n"
        
        summary += "🔮 JACOB 5 PROPHECY: We are in the 'last time' - final gathering before harvest\n"
        summary += "The Master Gardener works urgently to save as many branches as possible\n\n"
        
        # Add millennial proximity analysis
        millennial_analysis = self.evaluate_millennial_proximity()
        summary += "👑 MILLENNIAL PROXIMITY ANALYSIS:\n"
        summary += f"Overall Readiness Score: {millennial_analysis['millennial_proximity_score']:.2f}/1.0\n"
        summary += f"Current Phase: {millennial_analysis['current_phase']}\n\n"
        
        summary += "📊 PROPHECY FULFILLMENT INDICATORS:\n"
        for indicator, score in millennial_analysis['indicator_analysis'].items():
            status = "✅" if score > 0.8 else "⚡" if score > 0.6 else "🔄"
            summary += f"{status} {indicator.replace('_', ' ').title()}: {score:.2f}\n"
        
        summary += "\n🎯 KEY PREPARATION AREAS:\n"
        for area in millennial_analysis['key_preparation_areas']:
            summary += f"• {area}\n"
        
        summary += "\n👑 MILLENNIAL REFERENCE POINT FOR ALL DECISIONS:\n"
        summary += "• Will this choice prepare me/others for Christ's reign?\n"
        summary += "• Does this align with millennial righteousness standards?\n"
        summary += "• Am I helping gather Israel or scattering?\n"
        summary += "• Is this building Zion or Babylon?\n\n"
        
        summary += "🏁 ULTIMATE PROMISE: Christ will reign, righteousness will prevail,\n"
        summary += "and all faithful covenant keepers will inherit eternal glory.\n"
        
        return summary

# Example usage and demonstration
def demo_gospel_cycles():
    """Demonstrate the Gospel Cycles analyzer"""
    analyzer = GospelCyclesAnalyzer()
    
    print("🕊️ GOSPEL CYCLES ANALYSIS DEMONSTRATION")
    print("=" * 60)
    
    # Show cycle summary
    print(analyzer.get_cycle_summary())
    
    # Show millennial proximity analysis
    print("\n" + "=" * 60)
    print("👑 MILLENNIAL PROXIMITY & PRE-MILLENNIAL PREDICTIONS")
    print("-" * 60)
    
    millennial_analysis = analyzer.evaluate_millennial_proximity()
    print(f"🎯 Millennial Proximity Score: {millennial_analysis['millennial_proximity_score']:.2f}")
    print(f"📍 Current Phase: {millennial_analysis['current_phase']}")
    
    pre_millennial = analyzer.predict_pre_millennial_cycles()
    print(f"\n🔮 Estimated Time Frame: {pre_millennial['estimated_time_remaining']}")
    print("\n📋 Likely Pre-Millennial Phases:")
    for phase in pre_millennial['likely_pre_millennial_phases'][:2]:
        print(f"• {phase['phase']}: {phase['characteristics']}")
    
    print("\n💡 Decision-Making Guidance:")
    for guidance in pre_millennial['decision_making_guidance'][:2]:
        print(f"• {guidance}")
    
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
