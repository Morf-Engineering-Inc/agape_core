"""
Gilgamesh RAG Evaluator
=======================
Uses a Retrieval-Augmented Generation (RAG) approach to evaluate the Epic of
Gilgamesh (English version) against the Agape Core Gospel Truth framework.

Pipeline:
  1. Load content  -- built-in tablet summaries OR a user-supplied text file
  2. Chunk         -- split into tablet/section chunks
  3. Evaluate      -- run each chunk through SeekGoodEvaluator + MediaAnalyzer
  4. Aggregate     -- combine per-chunk scores into a final verdict

Run directly:
    python gilgamesh_evaluator/gilgamesh_rag_evaluator.py
    python gilgamesh_evaluator/gilgamesh_rag_evaluator.py --file /path/to/gilgamesh.txt
"""

import os
import sys
import argparse
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional, Tuple

# Allow imports from the project root
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from truth_foundation.seekgood import SeekGoodEvaluator, ContentCategory, ContentEvaluation
from truth_discerner.media_analyzer import MediaAnalyzer, ContentElement, ContentType, TruthDiscernmentReport


# ---------------------------------------------------------------------------
# Built-in Tablet Knowledge Base
# Each tablet is a "document" in our knowledge base.
# ---------------------------------------------------------------------------

GILGAMESH_TABLETS: List[Dict[str, Any]] = [
    {
        "id": "Tablet I",
        "title": "The Introduction of Gilgamesh",
        "summary": (
            "Gilgamesh is introduced as king of Uruk — two-thirds god, one-third man. "
            "He is described as the greatest of heroes: powerful, wise, builder of mighty walls. "
            "However, he is also a tyrant who abuses his people, taking what he wants by force. "
            "The gods hear the people's cries and create Enkidu, a wild man who lives among animals, "
            "as a counterbalance to Gilgamesh's unchecked power."
        ),
        "themes": [
            "Pride and power", "Tyranny", "Divine response to injustice",
            "Creation of a companion", "Human vs divine nature"
        ],
        "explicit_messages": [
            "A king can be both great and corrupt",
            "The gods hear the cries of the oppressed",
            "Power without restraint leads to abuse"
        ],
        "implicit_messages": [
            "Divine accountability exists for rulers",
            "Human greatness does not justify tyranny"
        ]
    },
    {
        "id": "Tablet II",
        "title": "Enkidu and Shamhat — Civilizing the Wild Man",
        "summary": (
            "Enkidu is seduced by the temple harlot Shamhat, who initiates him into civilization "
            "through sexual relations over seven days. After this encounter, the animals flee from "
            "him and he loses his wild nature. Shamhat teaches him clothing, bread, and beer. "
            "He travels to Uruk where he challenges Gilgamesh. After a great wrestling match, "
            "they become fast friends."
        ),
        "themes": [
            "Civilization vs wilderness", "Sexual initiation", "Transformation",
            "Friendship", "Loss of innocence", "Temple prostitution"
        ],
        "explicit_messages": [
            "Sexual experience separates man from the animal world",
            "Civilization is gained through sensual knowledge",
            "Conflict can forge friendship"
        ],
        "implicit_messages": [
            "Sacred prostitution is normalized",
            "Sensual pleasure is a path to enlightenment"
        ]
    },
    {
        "id": "Tablet III",
        "title": "Preparation for the Cedar Forest Journey",
        "summary": (
            "Gilgamesh proposes an expedition to the Cedar Forest to slay the demon guardian "
            "Humbaba and win eternal fame. Enkidu warns that Humbaba is a fearsome monster "
            "appointed by the god Enlil. The elders of Uruk counsel caution. "
            "Gilgamesh's mother Ninsun prays to the sun god Shamash on their behalf. "
            "Enkidu is adopted by Ninsun as her son. They prepare weapons and depart."
        ),
        "themes": [
            "Quest for glory and immortal fame", "Courage vs recklessness",
            "Seeking divine protection", "Brotherhood", "Overcoming fear"
        ],
        "explicit_messages": [
            "Fame is worth risking death",
            "Prayer is offered before dangerous journeys",
            "Wise counsel should be heeded"
        ],
        "implicit_messages": [
            "Human glory-seeking can override wise counsel",
            "A mother's prayer has power with the gods"
        ]
    },
    {
        "id": "Tablet IV",
        "title": "The Journey to the Cedar Forest",
        "summary": (
            "Gilgamesh and Enkidu make their way to the Cedar Forest. Each night Gilgamesh "
            "performs rituals and receives five ominous dreams which Enkidu interprets as "
            "favorable omens — though some interpretations seem forced. "
            "The sun god Shamash speaks to Gilgamesh and encourages the heroes. "
            "They push through their fears and reach the edge of the Cedar Forest."
        ),
        "themes": [
            "Divine dreams and omens", "Faith and courage", "Perseverance",
            "Fear of death", "Seeking divine guidance"
        ],
        "explicit_messages": [
            "Dreams are messages from the gods",
            "Divine support matters for great undertakings",
            "Perseverance through fear is heroic"
        ],
        "implicit_messages": [
            "Truth in dreams can be interpreted selectively to justify what we want",
            "Faith enables courage"
        ]
    },
    {
        "id": "Tablet V",
        "title": "The Battle with Humbaba",
        "summary": (
            "Gilgamesh and Enkidu enter the sacred Cedar Forest and confront Humbaba, its monstrous "
            "guardian. After a fierce battle, Humbaba is defeated and pleads for mercy. "
            "Enkidu urges Gilgamesh to kill him despite his pleas; Humbaba curses them before dying. "
            "They cut down the greatest cedar trees and fashion a great door for Enlil's temple. "
            "Their victory is great but carries a shadow — they killed a guardian of the sacred forest."
        ),
        "themes": [
            "Victory over evil", "Mercy denied", "Consequences of killing",
            "Desecration of sacred places", "Hubris in victory"
        ],
        "explicit_messages": [
            "Heroes defeat fearsome monsters",
            "Refusing mercy to a defeated enemy has moral weight",
            "Great deeds can carry grave consequences"
        ],
        "implicit_messages": [
            "Killing without mercy stains even heroic victories",
            "Hubris invites divine retribution"
        ]
    },
    {
        "id": "Tablet VI",
        "title": "Ishtar's Proposal and the Bull of Heaven",
        "summary": (
            "The goddess Ishtar offers Gilgamesh her love; he brutally rejects her, mocking her "
            "past lovers whom she destroyed. Enraged, Ishtar convinces the sky god Anu to send "
            "the Bull of Heaven to punish Uruk. The bull creates chaos and kills hundreds. "
            "Gilgamesh and Enkidu slay the bull together. Enkidu tears off the bull's hindquarter "
            "and throws it in Ishtar's face. Uruk celebrates, but the gods are deeply offended."
        ),
        "themes": [
            "Sexual temptation and rejection", "Divine wrath", "Pride and insult",
            "Human defiance of gods", "Consequences of hubris"
        ],
        "explicit_messages": [
            "Rejecting a goddess's advances brings terrible consequences",
            "Heroes can defeat even divine monsters",
            "Insulting the divine brings judgment"
        ],
        "implicit_messages": [
            "Sexual immorality and divine anger are connected",
            "Prideful defiance of authority leads to destruction"
        ]
    },
    {
        "id": "Tablet VII",
        "title": "The Death of Enkidu",
        "summary": (
            "The gods decree that one of the heroes must die for slaying Humbaba and the Bull of "
            "Heaven. Enkidu is chosen. He falls ill, suffers in agony, and dies. Before dying he "
            "curses Shamhat who first civilized him, then blesses her after the sun god Shamash "
            "reminds him of all the good that came from it. Enkidu's death leaves Gilgamesh "
            "utterly devastated, weeping and refusing to accept mortality."
        ),
        "themes": [
            "Death and grief", "Divine justice and mortality", "Friendship loss",
            "Suffering", "Blessing vs cursing", "Acceptance of consequences"
        ],
        "explicit_messages": [
            "Actions have consequences that cannot be escaped",
            "Grief over a dear friend is profound and real",
            "Gratitude can replace bitterness even at death's door"
        ],
        "implicit_messages": [
            "Mortality is the great equalizer",
            "Love transforms how we view suffering"
        ]
    },
    {
        "id": "Tablet VIII",
        "title": "Gilgamesh Mourns Enkidu",
        "summary": (
            "Gilgamesh gives a long lament for Enkidu, commissioning a great statue and funeral "
            "offerings. He mourns for seven days, refusing to let Enkidu be buried until a maggot "
            "falls from his nose. Gilgamesh is consumed by grief and terror at the reality of death. "
            "He abandons his kingly robes, dons animal skins, and sets out on a quest to find "
            "the secret of eternal life."
        ),
        "themes": [
            "Grief and lamentation", "Love expressed through mourning",
            "Fear of death driving action", "Quest for immortality begins",
            "Transformation through loss"
        ],
        "explicit_messages": [
            "Deep friendship creates deep grief",
            "Witnessing death can transform a person",
            "The desire to overcome death is universal"
        ],
        "implicit_messages": [
            "Even the greatest men are undone by death",
            "Loss can redirect the entire purpose of a life"
        ]
    },
    {
        "id": "Tablet IX",
        "title": "The Quest Begins — Scorpion Men and Mashu",
        "summary": (
            "Gilgamesh wanders the wilderness wearing animal skins, driven by fear of death. "
            "He reaches the twin mountains of Mashu, guarded by fearsome scorpion-people. "
            "He convinces them to let him pass through the tunnel beneath the mountain where "
            "the sun travels at night. After twelve leagues of total darkness he emerges into "
            "a paradise garden with trees bearing jewels as fruit."
        ),
        "themes": [
            "Quest through darkness", "Confronting the impossible",
            "Perseverance of will", "Paradise imagery", "Journey through death's domain"
        ],
        "explicit_messages": [
            "Terror of death can drive extraordinary journeys",
            "Darkness must be endured before reaching light",
            "Even monsters can show compassion"
        ],
        "implicit_messages": [
            "The path to life runs through death's shadow",
            "Paradise imagery reflects longing for immortality"
        ]
    },
    {
        "id": "Tablet X",
        "title": "The Tavern Keeper Siduri and the Boatman Urshanabi",
        "summary": (
            "Gilgamesh reaches the tavern keeper Siduri at the edge of the world. She counsels "
            "him to accept mortality and enjoy life's pleasures — food, family, festivity. "
            "Gilgamesh refuses and presses on. She directs him to the boatman Urshanabi who "
            "ferries him across the Waters of Death to reach Utnapishtim, the only mortal "
            "who was granted eternal life by the gods."
        ),
        "themes": [
            "Accepting mortality", "Earthly pleasure as consolation", "Perseverance",
            "The journey beyond death's boundary", "Wisdom from unexpected sources"
        ],
        "explicit_messages": [
            "Wisdom counsels accepting mortality and enjoying life's gifts",
            "Refusing wise counsel has consequences",
            "Family and daily life are precious gifts"
        ],
        "implicit_messages": [
            "Pleasure-seeking is offered as an answer to the fear of death",
            "The wisdom of this world cannot satisfy the longing for eternity"
        ]
    },
    {
        "id": "Tablet XI",
        "title": "Utnapishtim, the Flood, and the Plant of Life",
        "summary": (
            "Utnapishtim tells Gilgamesh the story of the great flood — nearly identical to Noah's "
            "ark account — in which the gods sent a flood to destroy humanity and Utnapishtim built "
            "a boat and saved all living things. The gods granted him immortality as reward. "
            "Utnapishtim challenges Gilgamesh to stay awake for seven days; Gilgamesh fails. "
            "As a consolation, Utnapishtim reveals a plant of rejuvenation at the sea's bottom. "
            "Gilgamesh retrieves it but a serpent steals it while he sleeps, leaving him with nothing. "
            "He returns to Uruk with only the great walls he built."
        ),
        "themes": [
            "The great flood narrative", "Immortality and its cost", "Human failure",
            "Serpent as thief of blessing", "Accepting limits", "Legacy through works"
        ],
        "explicit_messages": [
            "The flood story preserves a universal memory of divine judgment",
            "Immortality is not for mortal man to seize",
            "The serpent robs humanity of rejuvenation"
        ],
        "implicit_messages": [
            "Parallel to Genesis: flood, serpent, loss of paradise blessing",
            "God's gifts cannot be kept through human effort alone",
            "Legacy in earthly works is what remains"
        ]
    },
    {
        "id": "Tablet XII",
        "title": "The Underworld — Enkidu's Ghost",
        "summary": (
            "In this later appended tablet, Gilgamesh drops objects into the underworld and Enkidu "
            "volunteers to retrieve them. Despite warnings, Enkidu breaks the rules of the underworld "
            "and is trapped there. Gilgamesh begs the gods to release Enkidu's ghost. "
            "Enkidu's spirit rises and describes the grim reality of the underworld — the dead exist "
            "as shadows, and their afterlife quality depends on how many sons they had and how they died. "
            "The epic ends without resolution of Gilgamesh's quest."
        ),
        "themes": [
            "Death and the afterlife", "Disobedience has permanent consequences",
            "The grim nature of the underworld", "No resurrection or redemption offered",
            "Legacy through descendants"
        ],
        "explicit_messages": [
            "Breaking divine rules imprisons the soul",
            "The afterlife is bleak and offers little hope",
            "Sons and honored death bring better standing"
        ],
        "implicit_messages": [
            "A worldview without resurrection offers only shadow existence after death",
            "The absence of a redeemer leaves death undefeated"
        ]
    }
]


# ---------------------------------------------------------------------------
# Data Structures
# ---------------------------------------------------------------------------

@dataclass
class TabletEvaluation:
    tablet_id: str
    tablet_title: str
    seekgood_score: float
    seekgood_level: str
    truth_score: int
    truth_alignment: str
    positive_elements: List[str]
    concerning_elements: List[str]
    biblical_parallels: List[str]
    recommendation: str


@dataclass
class GilgameshVerdict:
    overall_seekgood_score: float
    overall_truth_score: float
    final_rating: str
    final_recommendation: str
    strongest_tablets: List[str]
    weakest_tablets: List[str]
    key_positives: List[str]
    key_concerns: List[str]
    biblical_connections: List[str]
    discussion_questions: List[str]
    tablet_evaluations: List[TabletEvaluation]


# ---------------------------------------------------------------------------
# RAG Chunker
# ---------------------------------------------------------------------------

class GilgameshChunker:
    """
    Turns source material into evaluatable chunks.
    If a text file is provided, it is split by tablet headers.
    Otherwise the built-in knowledge base is used.
    """

    def load_builtin(self) -> List[Dict[str, Any]]:
        return GILGAMESH_TABLETS

    def load_from_file(self, file_path: str) -> List[Dict[str, Any]]:
        """
        Load and chunk a raw text file of Gilgamesh.
        Splits on lines containing 'Tablet' followed by a Roman numeral or number.
        Falls back to fixed-size chunks if no tablet markers are found.
        """
        with open(file_path, "r", encoding="utf-8", errors="replace") as f:
            raw_text = f.read()

        import re
        tablet_pattern = re.compile(
            r"(Tablet\s+[IVXivx\d]+.*)",
            re.IGNORECASE
        )
        splits = tablet_pattern.split(raw_text)

        chunks: List[Dict[str, Any]] = []

        if len(splits) > 1:
            # Pair up header + body
            i = 1
            while i < len(splits):
                header = splits[i].strip()
                body = splits[i + 1].strip() if i + 1 < len(splits) else ""
                chunks.append({
                    "id": header,
                    "title": header,
                    "summary": body[:2000],
                    "themes": [],
                    "explicit_messages": [],
                    "implicit_messages": []
                })
                i += 2
        else:
            # No tablet markers — use 1500-character chunks
            words = raw_text.split()
            chunk_size = 300
            for idx in range(0, len(words), chunk_size):
                chunk_words = words[idx: idx + chunk_size]
                body = " ".join(chunk_words)
                chunks.append({
                    "id": f"Chunk {idx // chunk_size + 1}",
                    "title": f"Section {idx // chunk_size + 1}",
                    "summary": body,
                    "themes": [],
                    "explicit_messages": [],
                    "implicit_messages": []
                })

        return chunks if chunks else self.load_builtin()


# ---------------------------------------------------------------------------
# Core Evaluator
# ---------------------------------------------------------------------------

class GilgameshRAGEvaluator:
    """
    Main RAG evaluation engine for the Epic of Gilgamesh.
    """

    def __init__(self):
        self.seekgood = SeekGoodEvaluator()
        self.media_analyzer = MediaAnalyzer()
        self.chunker = GilgameshChunker()

    def _evaluate_tablet(self, tablet: Dict[str, Any]) -> TabletEvaluation:
        """Run one tablet through both evaluation engines and return combined result."""

        # --- SeekGood evaluation ---
        context = {
            "themes": ", ".join(tablet.get("themes", [])),
            "explicit_messages": "; ".join(tablet.get("explicit_messages", [])),
            "implicit_messages": "; ".join(tablet.get("implicit_messages", []))
        }
        sg_eval: ContentEvaluation = self.seekgood.evaluate_content(
            title=tablet["title"],
            category=ContentCategory.BOOK,
            description=tablet["summary"],
            additional_context=context
        )

        # --- MediaAnalyzer evaluation ---
        content_element = ContentElement(
            title=tablet["title"],
            description=tablet["summary"],
            content_type=ContentType.BOOK,
            target_audience="Adult — Academic / Literary",
            cultural_influence="High — oldest surviving written epic",
            key_themes=tablet.get("themes", []),
            explicit_messages=tablet.get("explicit_messages", []),
            implicit_messages=tablet.get("implicit_messages", [])
        )
        ma_report: TruthDiscernmentReport = self.media_analyzer.analyze_content(content_element)

        return TabletEvaluation(
            tablet_id=tablet["id"],
            tablet_title=tablet["title"],
            seekgood_score=sg_eval.goodness_score,
            seekgood_level=sg_eval.overall_goodness.name,
            truth_score=ma_report.truth_score,
            truth_alignment=ma_report.truth_alignment.name,
            positive_elements=sg_eval.positive_elements + ma_report.positive_elements,
            concerning_elements=sg_eval.concerning_elements + ma_report.concerning_elements,
            biblical_parallels=ma_report.biblical_parallels,
            recommendation=sg_eval.recommendation
        )

    def evaluate(self, file_path: Optional[str] = None) -> GilgameshVerdict:
        """
        Full RAG evaluation pipeline.
        Loads chunks → evaluates each → aggregates verdict.
        """
        if file_path:
            print(f"\n📂 Loading text file: {file_path}")
            tablets = self.chunker.load_from_file(file_path)
        else:
            print("\n📚 Using built-in Gilgamesh knowledge base (12 tablets)")
            tablets = self.chunker.load_builtin()

        print(f"   → {len(tablets)} sections to evaluate\n")

        tablet_evals: List[TabletEvaluation] = []
        for tablet in tablets:
            print(f"   Evaluating: {tablet['id']} — {tablet['title']} ...")
            result = self._evaluate_tablet(tablet)
            tablet_evals.append(result)

        return self._aggregate(tablet_evals)

    def _aggregate(self, evals: List[TabletEvaluation]) -> GilgameshVerdict:
        """Combine per-tablet results into a single final verdict."""

        if not evals:
            raise ValueError("No tablet evaluations to aggregate.")

        avg_seekgood = sum(e.seekgood_score for e in evals) / len(evals)
        avg_truth = sum(e.truth_score for e in evals) / len(evals)

        # Rank tablets
        ranked_sg = sorted(evals, key=lambda e: e.seekgood_score, reverse=True)
        strongest = [f"{e.tablet_id}: {e.tablet_title}" for e in ranked_sg[:3]]
        weakest = [f"{e.tablet_id}: {e.tablet_title}" for e in ranked_sg[-3:]]

        # Pool all positives, concerns, biblical parallels
        all_positives: List[str] = []
        all_concerns: List[str] = []
        all_parallels: List[str] = []
        for e in evals:
            all_positives.extend(e.positive_elements)
            all_concerns.extend(e.concerning_elements)
            all_parallels.extend(e.biblical_parallels)

        key_positives = list(dict.fromkeys(all_positives))[:8]
        key_concerns = list(dict.fromkeys(all_concerns))[:8]
        biblical_connections = list(dict.fromkeys(all_parallels))[:6]

        # Final rating
        combined = (avg_seekgood / 5.0 * 50) + (avg_truth / 100.0 * 50)  # 0-100
        if combined >= 75:
            final_rating = "RECOMMENDED — Good with Discernment"
            recommendation = (
                "The Epic of Gilgamesh earns a positive overall rating through this framework. "
                "It contains profound themes of friendship, grief, mortality, and even a striking "
                "parallel to the Genesis flood account. It is best read with mature discernment "
                "given its pagan worldview, scenes of sexual initiation, and a bleak view of the afterlife. "
                "Academically and spiritually, it is valuable for understanding the ancient world's "
                "hunger for answers that only the Gospel fully provides."
            )
        elif combined >= 55:
            final_rating = "MIXED — Use Scholarly Discernment"
            recommendation = (
                "The Epic of Gilgamesh scores in the mixed range. It carries genuine literary and "
                "spiritual value — its themes of mortality, friendship, grief, and the flood narrative "
                "parallel Gospel truths powerfully. However, its pagan worldview, sexual content in Tablet II, "
                "and a hopeless afterlife vision lower its score. Recommended for mature, spiritually "
                "grounded readers who can engage critically and redemptively."
            )
        elif combined >= 35:
            final_rating = "CAUTION — For Scholarly Use Only"
            recommendation = (
                "Gilgamesh presents significant concerns from a Gospel lens. While containing valuable "
                "historical parallels (especially the flood narrative), its pagan theology, sexual initiation "
                "scenes, and absence of redemption make it unsuitable for general consumption. "
                "Approach only with strong biblical grounding and scholarly purpose."
            )
        else:
            final_rating = "AVOID — Contrary to Gospel Standards"
            recommendation = (
                "The text does not meet Gospel standards of goodness overall. "
                "While it has historical importance, the overall content is not recommended."
            )

        discussion_questions = [
            "How does the Gilgamesh flood narrative (Tablet XI) compare to the account of Noah in Genesis? What does the similarity tell us?",
            "Gilgamesh's quest for immortality ends in failure. How does the Gospel of Jesus Christ answer the question of death that Gilgamesh could not solve?",
            "The serpent in Tablet XI steals the plant of eternal life. What biblical parallel does this bring to mind?",
            "What does the deep friendship between Gilgamesh and Enkidu teach us about love, loyalty, and grief?",
            "Tablet X offers earthly pleasure as the answer to death's terror. How does the Gospel offer a better answer?",
            "The epic ends without resurrection or hope. How does Christ's resurrection change everything about how believers face death?",
            "How should a disciple of Christ approach great ancient literature that contains both truth and error?"
        ]

        return GilgameshVerdict(
            overall_seekgood_score=round(avg_seekgood, 2),
            overall_truth_score=round(avg_truth, 1),
            final_rating=final_rating,
            final_recommendation=recommendation,
            strongest_tablets=strongest,
            weakest_tablets=weakest,
            key_positives=key_positives,
            key_concerns=key_concerns,
            biblical_connections=biblical_connections,
            discussion_questions=discussion_questions,
            tablet_evaluations=evals
        )


# ---------------------------------------------------------------------------
# Report Printer
# ---------------------------------------------------------------------------

def print_verdict(verdict: GilgameshVerdict, verbose: bool = False):
    DIVIDER = "=" * 65

    print(f"\n{DIVIDER}")
    print("  AGAPE CORE — GILGAMESH GOSPEL TRUTH EVALUATION")
    print(f"{DIVIDER}")
    print(f"  Epic of Gilgamesh (English Version) — RAG Analysis")
    print(f"{DIVIDER}\n")

    print(f"FINAL RATING:   {verdict.final_rating}")
    print(f"SeekGood Score: {verdict.overall_seekgood_score:.2f} / 5.0  "
          f"(Philippians 4:8 criteria)")
    print(f"Truth Score:    {verdict.overall_truth_score:.1f} / 100  "
          f"(Biblical alignment)")

    print(f"\n{DIVIDER}")
    print("  FINAL RECOMMENDATION")
    print(f"{DIVIDER}")
    print(verdict.final_recommendation)

    print(f"\n{DIVIDER}")
    print("  STRONGEST TABLETS (highest Gospel alignment)")
    print(f"{DIVIDER}")
    for t in verdict.strongest_tablets:
        print(f"  + {t}")

    print(f"\n{DIVIDER}")
    print("  WEAKEST TABLETS (lowest Gospel alignment)")
    print(f"{DIVIDER}")
    for t in verdict.weakest_tablets:
        print(f"  - {t}")

    print(f"\n{DIVIDER}")
    print("  KEY POSITIVE ELEMENTS")
    print(f"{DIVIDER}")
    for p in verdict.key_positives:
        print(f"  ✅ {p}")

    print(f"\n{DIVIDER}")
    print("  KEY CONCERNING ELEMENTS")
    print(f"{DIVIDER}")
    for c in verdict.key_concerns:
        print(f"  ⚠️  {c}")

    if verdict.biblical_connections:
        print(f"\n{DIVIDER}")
        print("  BIBLICAL PARALLELS FOUND")
        print(f"{DIVIDER}")
        for b in verdict.biblical_connections:
            print(f"  📖 {b}")

    print(f"\n{DIVIDER}")
    print("  DISCUSSION QUESTIONS")
    print(f"{DIVIDER}")
    for i, q in enumerate(verdict.discussion_questions, 1):
        print(f"  {i}. {q}")

    if verbose:
        print(f"\n{DIVIDER}")
        print("  PER-TABLET BREAKDOWN")
        print(f"{DIVIDER}")
        for e in verdict.tablet_evaluations:
            print(f"\n  [{e.tablet_id}] {e.tablet_title}")
            print(f"    SeekGood: {e.seekgood_score:.2f}/5.0  ({e.seekgood_level})")
            print(f"    Truth:    {e.truth_score}/100  ({e.truth_alignment})")
            if e.positive_elements:
                print(f"    Positives: {', '.join(e.positive_elements[:3])}")
            if e.concerning_elements:
                print(f"    Concerns:  {', '.join(e.concerning_elements[:3])}")

    print(f"\n{DIVIDER}\n")


# ---------------------------------------------------------------------------
# Entry Point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Evaluate the Epic of Gilgamesh against Agape Core Gospel Truth standards"
    )
    parser.add_argument(
        "--file", "-f",
        type=str,
        default=None,
        help="Path to a plain-text file of Gilgamesh (optional). "
             "If omitted, the built-in tablet knowledge base is used."
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Show per-tablet breakdown in the report"
    )
    args = parser.parse_args()

    print("\n🏛️  AGAPE CORE — Epic of Gilgamesh RAG Evaluator")
    print("   Judging ancient literature against Gospel Truth standards")
    print("   Framework: SeekGood (Phil. 4:8) + MediaAnalyzer (Biblical Truth)")

    evaluator = GilgameshRAGEvaluator()
    verdict = evaluator.evaluate(file_path=args.file)
    print_verdict(verdict, verbose=args.verbose)


if __name__ == "__main__":
    main()
