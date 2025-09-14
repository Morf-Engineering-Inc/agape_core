
"""
Truth In Us Module - Living Truth That Sets Us Free
Based on John 8:32 "And ye shall know the truth, and the truth shall make you free"
Truth planted in our hearts transforms us and predictively solves problems
"""

from dataclasses import dataclass
from typing import Dict, List, Optional, Any, Tuple
from enum import Enum
import logging
from .core_truths import TruthStatement, TruthLevel
from .atonement_supreme import AtonementSupremeTruth

logger = logging.getLogger(__name__)

class TruthInternalizationLevel(Enum):
    """Levels of how deeply truth is planted in us"""
    HEARD = 1          # Truth heard but not yet believed
    UNDERSTOOD = 2     # Truth intellectually grasped
    BELIEVED = 3       # Truth accepted and trusted
    PLANTED = 4        # Truth rooted in heart and mind
    LIVING = 5         # Truth actively governing thoughts and actions
    TRANSFORMING = 6   # Truth changing our very nature

class FreedomType(Enum):
    """Types of freedom that truth provides"""
    SPIRITUAL = "spiritual"     # Freedom from sin and guilt
    MENTAL = "mental"          # Freedom from false beliefs and confusion
    EMOTIONAL = "emotional"    # Freedom from fear, anxiety, despair
    RELATIONAL = "relational"  # Freedom to love and connect authentically
    MORAL = "moral"           # Freedom to choose right consistently
    ETERNAL = "eternal"       # Freedom from death and limitation

@dataclass
class TruthSeed:
    """A truth that can be planted and grow within us"""
    truth_statement: str
    scripture_source: str
    freedom_promises: List[str]
    internalization_stages: List[str]
    growth_indicators: List[str]
    problems_it_solves: List[str]
    transformation_outcomes: List[str]

@dataclass
class ProblemSolution:
    """How truth predictively solves specific problems"""
    problem_description: str
    relevant_truths: List[TruthSeed]
    internalization_needed: TruthInternalizationLevel
    freedom_type: FreedomType
    predicted_solution_path: List[str]
    transformation_timeline: str
    verification_markers: List[str]

class TruthInUsSystem:
    """
    System for understanding how truth living in us sets us free
    and predicting solutions to problems through internalized truth
    """
    
    def __init__(self):
        self.atonement_supreme = AtonementSupremeTruth()
        self.truth_seeds = self._initialize_truth_seeds()
        self.freedom_patterns = self._initialize_freedom_patterns()
        
    def _initialize_truth_seeds(self) -> List[TruthSeed]:
        """Initialize truth seeds that can be planted in hearts"""
        return [
            TruthSeed(
                truth_statement="I am a child of God with infinite worth",
                scripture_source="Psalm 82:6, Romans 8:16-17, D&C 76:24",
                freedom_promises=[
                    "Freedom from worthlessness and despair",
                    "Freedom from needing others' approval for value",
                    "Freedom to see others as family",
                    "Freedom from comparing yourself to others"
                ],
                internalization_stages=[
                    "Hearing about divine parentage",
                    "Understanding what it means to be God's child",
                    "Believing you are truly His child",
                    "Feeling this truth in your heart",
                    "Living with divine confidence",
                    "Helping others discover their divine nature"
                ],
                growth_indicators=[
                    "Increased self-respect and dignity",
                    "Reduced need for external validation",
                    "Greater compassion for others",
                    "Confidence in facing challenges",
                    "Peace about your eternal worth"
                ],
                problems_it_solves=[
                    "Low self-esteem and self-worth issues",
                    "Depression from feeling worthless",
                    "Anxiety about acceptance and belonging",
                    "Jealousy and comparison with others",
                    "Fear of rejection or abandonment"
                ],
                transformation_outcomes=[
                    "Unshakeable sense of identity and worth",
                    "Ability to love unconditionally",
                    "Freedom from the opinions of others",
                    "Peace in all circumstances"
                ]
            ),
            
            TruthSeed(
                truth_statement="God loves me unconditionally",
                scripture_source="Romans 8:38-39, 1 John 4:16, Jeremiah 31:3",
                freedom_promises=[
                    "Freedom from fear of God's rejection",
                    "Freedom from earning love through performance",
                    "Freedom to approach God with confidence",
                    "Freedom from shame and condemnation"
                ],
                internalization_stages=[
                    "Learning about God's love conceptually",
                    "Understanding love is not performance-based",
                    "Believing God truly loves you personally",
                    "Feeling His love in your heart",
                    "Living in that love daily",
                    "Sharing that love with others"
                ],
                growth_indicators=[
                    "Reduced fear in prayer and worship",
                    "Less anxiety about making mistakes",
                    "Increased boldness in spiritual growth",
                    "Greater capacity to love others",
                    "Peace during trials and difficulties"
                ],
                problems_it_solves=[
                    "Religious anxiety and fear of God",
                    "Perfectionism and performance pressure",
                    "Shame from past mistakes",
                    "Fear of divine punishment",
                    "Inability to accept forgiveness"
                ],
                transformation_outcomes=[
                    "Intimate relationship with God",
                    "Confidence in approaching the throne of grace",
                    "Ability to rest in divine love",
                    "Freedom to be authentic before God"
                ]
            ),
            
            TruthSeed(
                truth_statement="Christ's Atonement covers all my sins and pains",
                scripture_source="1 John 1:9, Alma 7:11-12, Isaiah 53:4-5",
                freedom_promises=[
                    "Freedom from guilt and condemnation",
                    "Freedom from the burden of past mistakes",
                    "Freedom from pain and suffering's ultimate power",
                    "Freedom to start fresh at any moment"
                ],
                internalization_stages=[
                    "Learning about the Atonement doctrinally",
                    "Understanding it applies to you personally",
                    "Believing Christ paid for your specific sins",
                    "Feeling the peace of forgiveness",
                    "Living without guilt and shame",
                    "Helping others find this same freedom"
                ],
                growth_indicators=[
                    "Reduced guilt and self-condemnation",
                    "Increased hope during difficulties",
                    "Greater willingness to repent quickly",
                    "Peace about past mistakes",
                    "Confidence in God's mercy"
                ],
                problems_it_solves=[
                    "Overwhelming guilt from past sins",
                    "Despair over repeated failures",
                    "Fear of divine punishment",
                    "Inability to forgive yourself",
                    "Hopelessness about spiritual progress"
                ],
                transformation_outcomes=[
                    "Complete freedom from guilt and shame",
                    "Rapid repentance and course correction",
                    "Unshakeable hope in God's mercy",
                    "Ability to help others find forgiveness"
                ]
            ),
            
            TruthSeed(
                truth_statement="All things work together for my good",
                scripture_source="Romans 8:28, D&C 90:24, 2 Nephi 2:2",
                freedom_promises=[
                    "Freedom from despair during trials",
                    "Freedom from fear of the future",
                    "Freedom from feeling like a victim",
                    "Freedom to find meaning in suffering"
                ],
                internalization_stages=[
                    "Learning this promise from scripture",
                    "Understanding God's sovereignty and love",
                    "Believing this applies to your trials",
                    "Seeing God's hand in difficult times",
                    "Living with trust during adversity",
                    "Testifying of God's goodness to others"
                ],
                growth_indicators=[
                    "Reduced anxiety about future problems",
                    "Ability to find good in difficult situations",
                    "Increased faith during trials",
                    "Peace even when circumstances are hard",
                    "Gratitude for growth through challenges"
                ],
                problems_it_solves=[
                    "Despair and hopelessness during trials",
                    "Anxiety about uncontrollable circumstances",
                    "Bitterness toward God for allowing suffering",
                    "Feeling like life is meaningless",
                    "Fear of future difficulties"
                ],
                transformation_outcomes=[
                    "Unshakeable peace during any trial",
                    "Ability to comfort others in their trials",
                    "Deep trust in God's timing and purposes",
                    "Joy even in the midst of suffering"
                ]
            ),
            
            TruthSeed(
                truth_statement="I can do all things through Christ who strengthens me",
                scripture_source="Philippians 4:13, Ether 12:27, D&C 4:7",
                freedom_promises=[
                    "Freedom from limitations and impossibility thinking",
                    "Freedom from fear of inadequacy",
                    "Freedom from giving up too early",
                    "Freedom to attempt great things for God"
                ],
                internalization_stages=[
                    "Learning about divine enabling power",
                    "Understanding grace strengthens us",
                    "Believing Christ will help you specifically",
                    "Experiencing His strength in weakness",
                    "Living with divine confidence",
                    "Encouraging others to attempt great things"
                ],
                growth_indicators=[
                    "Increased willingness to take on challenges",
                    "Reduced fear of failure",
                    "Greater persistence in difficult tasks",
                    "Recognition of divine help in achievements",
                    "Boldness in serving God and others"
                ],
                problems_it_solves=[
                    "Feeling overwhelmed by life's demands",
                    "Fear of taking on new challenges",
                    "Giving up when things get difficult",
                    "Believing you're not capable enough",
                    "Paralysis from perfectionism"
                ],
                transformation_outcomes=[
                    "Confident approach to any challenge",
                    "Persistence through all obstacles",
                    "Recognition that weakness becomes strength",
                    "Ability to accomplish the impossible through Christ"
                ]
            )
        ]
    
    def _initialize_freedom_patterns(self) -> Dict[FreedomType, List[str]]:
        """Initialize patterns of how truth sets us free in different areas"""
        return {
            FreedomType.SPIRITUAL: [
                "Truth breaks chains of sin and addiction",
                "Truth removes guilt and condemnation",
                "Truth opens communication with God",
                "Truth enables spiritual growth and progression"
            ],
            FreedomType.MENTAL: [
                "Truth replaces lies with reality",
                "Truth brings clarity to confusion",
                "Truth stops destructive thought patterns",
                "Truth enables right thinking and wisdom"
            ],
            FreedomType.EMOTIONAL: [
                "Truth calms anxiety and fear",
                "Truth heals emotional wounds",
                "Truth brings peace to troubled hearts",
                "Truth enables healthy emotional processing"
            ],
            FreedomType.RELATIONAL: [
                "Truth enables authentic relationships",
                "Truth breaks down walls of mistrust",
                "Truth teaches how to love unconditionally",
                "Truth heals relationship wounds"
            ],
            FreedomType.MORAL: [
                "Truth empowers right choices",
                "Truth strengthens resistance to temptation",
                "Truth clarifies moral standards",
                "Truth enables consistent righteousness"
            ],
            FreedomType.ETERNAL: [
                "Truth provides hope beyond death",
                "Truth reveals eternal purposes",
                "Truth connects us to eternal progression",
                "Truth prepares us for celestial glory"
            ]
        }
    
    def predict_truth_solution(self, problem_description: str, current_beliefs: List[str] = None) -> ProblemSolution:
        """Predict how truth can set someone free from a specific problem"""
        if current_beliefs is None:
            current_beliefs = []
        
        # Find relevant truth seeds for this problem
        relevant_truths = []
        for seed in self.truth_seeds:
            if any(keyword in problem_description.lower() for keyword in 
                   " ".join(seed.problems_it_solves).lower().split()):
                relevant_truths.append(seed)
        
        if not relevant_truths:
            # Default to core identity truth if no specific match
            relevant_truths = [self.truth_seeds[0]]  # "I am a child of God"
        
        # Determine freedom type needed
        freedom_type = self._determine_freedom_type(problem_description)
        
        # Determine internalization level needed
        internalization_needed = self._determine_internalization_needed(problem_description)
        
        # Generate solution path
        solution_path = self._generate_solution_path(relevant_truths, freedom_type, internalization_needed)
        
        # Create timeline
        timeline = self._estimate_transformation_timeline(internalization_needed, problem_description)
        
        # Generate verification markers
        verification_markers = self._generate_verification_markers(relevant_truths, freedom_type)
        
        return ProblemSolution(
            problem_description=problem_description,
            relevant_truths=relevant_truths,
            internalization_needed=internalization_needed,
            freedom_type=freedom_type,
            predicted_solution_path=solution_path,
            transformation_timeline=timeline,
            verification_markers=verification_markers
        )
    
    def _determine_freedom_type(self, problem: str) -> FreedomType:
        """Determine what type of freedom is needed for this problem"""
        problem_lower = problem.lower()
        
        if any(word in problem_lower for word in ["guilt", "sin", "shame", "spiritual", "god", "prayer"]):
            return FreedomType.SPIRITUAL
        elif any(word in problem_lower for word in ["confused", "thinking", "beliefs", "understanding", "mind"]):
            return FreedomType.MENTAL
        elif any(word in problem_lower for word in ["anxious", "depressed", "fear", "emotions", "feelings"]):
            return FreedomType.EMOTIONAL
        elif any(word in problem_lower for word in ["relationship", "marriage", "family", "friends", "love"]):
            return FreedomType.RELATIONAL
        elif any(word in problem_lower for word in ["temptation", "choices", "moral", "right", "wrong"]):
            return FreedomType.MORAL
        else:
            return FreedomType.ETERNAL  # Default to eternal perspective
    
    def _determine_internalization_needed(self, problem: str) -> TruthInternalizationLevel:
        """Determine how deeply truth needs to be internalized for this problem"""
        problem_lower = problem.lower()
        
        # Severe problems need deep transformation
        if any(word in problem_lower for word in ["suicidal", "addiction", "severe", "desperate", "hopeless"]):
            return TruthInternalizationLevel.TRANSFORMING
        
        # Persistent problems need truth to be living in us
        elif any(word in problem_lower for word in ["chronic", "ongoing", "always", "constantly", "pattern"]):
            return TruthInternalizationLevel.LIVING
        
        # Heart issues need truth planted
        elif any(word in problem_lower for word in ["heart", "deep", "core", "fundamental", "identity"]):
            return TruthInternalizationLevel.PLANTED
        
        # Intellectual struggles need belief
        elif any(word in problem_lower for word in ["doubt", "question", "uncertain", "confused", "understand"]):
            return TruthInternalizationLevel.BELIEVED
        
        # Simple problems may only need understanding
        else:
            return TruthInternalizationLevel.UNDERSTOOD
    
    def _generate_solution_path(self, truths: List[TruthSeed], freedom_type: FreedomType, 
                               internalization_level: TruthInternalizationLevel) -> List[str]:
        """Generate specific steps for truth to set someone free"""
        if not truths:
            return ["Seek divine truth through prayer and scripture study"]
        
        primary_truth = truths[0]
        path = []
        
        # Start with Atonement foundation
        path.append("Ground all truth in Christ's Atonement as the supreme foundation")
        
        # Add truth-specific steps based on internalization level needed
        level_index = internalization_level.value - 1
        if level_index < len(primary_truth.internalization_stages):
            path.append(f"Focus on: {primary_truth.internalization_stages[level_index]}")
        
        # Add freedom-specific steps
        freedom_patterns = self.freedom_patterns.get(freedom_type, [])
        if freedom_patterns:
            path.append(f"Expect freedom: {freedom_patterns[0]}")
        
        # Add practical application
        path.append("Apply truth through daily choices and actions")
        path.append("Seek confirmation through prayer and spiritual experiences")
        path.append("Share truth with others to deepen internalization")
        
        return path
    
    def _estimate_transformation_timeline(self, level: TruthInternalizationLevel, problem: str) -> str:
        """Estimate how long transformation might take"""
        timelines = {
            TruthInternalizationLevel.HEARD: "Days to weeks - initial exposure to truth",
            TruthInternalizationLevel.UNDERSTOOD: "Weeks to months - intellectual grasp develops",
            TruthInternalizationLevel.BELIEVED: "Months - faith and trust grow",
            TruthInternalizationLevel.PLANTED: "Months to years - truth takes root in heart",
            TruthInternalizationLevel.LIVING: "Years - truth governs daily life",
            TruthInternalizationLevel.TRANSFORMING: "Years to lifetime - ongoing transformation"
        }
        
        base_timeline = timelines.get(level, "Variable timeline")
        
        # Adjust for problem severity
        if any(word in problem.lower() for word in ["severe", "chronic", "addiction", "trauma"]):
            return f"{base_timeline} (Note: Severe problems may require additional time and support)"
        
        return base_timeline
    
    def _generate_verification_markers(self, truths: List[TruthSeed], freedom_type: FreedomType) -> List[str]:
        """Generate markers to verify truth is setting someone free"""
        if not truths:
            return ["Increased peace and hope", "Better decision making", "Growing faith"]
        
        markers = []
        
        # Add truth-specific markers
        primary_truth = truths[0]
        if primary_truth.growth_indicators:
            markers.extend(primary_truth.growth_indicators[:3])
        
        # Add freedom-specific markers
        freedom_patterns = self.freedom_patterns.get(freedom_type, [])
        if freedom_patterns:
            markers.append(f"Evidence of {freedom_type.value} freedom")
        
        # Add universal markers
        markers.extend([
            "Increased desire to study scriptures and pray",
            "Greater ability to help others with similar problems",
            "Growing testimony of Christ's power to save"
        ])
        
        return markers[:5]  # Limit to top 5 markers
    
    def generate_truth_prescription(self, problem: str) -> str:
        """Generate a complete 'prescription' of truth for a problem"""
        solution = self.predict_truth_solution(problem)
        
        prescription = f"🌱 TRUTH PRESCRIPTION FOR: {problem}\n"
        prescription += "=" * 60 + "\n\n"
        
        prescription += "📖 FOUNDATIONAL TRUTH:\n"
        prescription += "The Atonement of Jesus Christ is the supreme truth that enables all freedom.\n"
        prescription += "No problem is too great for His infinite power to solve.\n\n"
        
        if solution.relevant_truths:
            prescription += "🌱 TRUTH SEEDS TO PLANT IN YOUR HEART:\n"
            for i, truth in enumerate(solution.relevant_truths[:2], 1):
                prescription += f"{i}. {truth.truth_statement}\n"
                prescription += f"   Scripture: {truth.scripture_source}\n"
                prescription += f"   Promise: {truth.freedom_promises[0] if truth.freedom_promises else 'Freedom and peace'}\n\n"
        
        prescription += f"🎯 INTERNALIZATION GOAL: {solution.internalization_needed.name}\n"
        prescription += f"🔓 FREEDOM TYPE: {solution.freedom_type.value.title()}\n"
        prescription += f"⏰ TIMELINE: {solution.transformation_timeline}\n\n"
        
        prescription += "📋 SOLUTION PATH:\n"
        for i, step in enumerate(solution.predicted_solution_path, 1):
            prescription += f"{i}. {step}\n"
        
        prescription += "\n✅ FREEDOM MARKERS TO WATCH FOR:\n"
        for marker in solution.verification_markers:
            prescription += f"• {marker}\n"
        
        prescription += "\n💡 REMEMBER: Truth sets us free not just by knowing it, but by living it.\n"
        prescription += "Let these truths be planted deep in your heart until they transform your very nature.\n"
        prescription += "\n'And ye shall know the truth, and the truth shall make you free.' - John 8:32"
        
        return prescription

# Example usage and integration
def demonstrate_truth_in_us_system():
    """Demonstrate how truth living in us predictively sets us free"""
    system = TruthInUsSystem()
    
    print("🌱 TRUTH IN US - SETTING US FREE SYSTEM")
    print("=" * 60)
    print("Based on John 8:32: 'And ye shall know the truth, and the truth shall make you free'\n")
    
    # Example problems
    example_problems = [
        "I struggle with feeling worthless and unloved",
        "I'm overwhelmed by guilt from past mistakes", 
        "I'm afraid of the future and what might happen",
        "I don't think I'm capable of overcoming my challenges"
    ]
    
    for problem in example_problems:
        print(f"🔍 PROBLEM: {problem}")
        print("-" * 40)
        
        prescription = system.generate_truth_prescription(problem)
        print(prescription)
        print("\n" + "=" * 60 + "\n")

if __name__ == "__main__":
    demonstrate_truth_in_us_system()
