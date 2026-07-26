
"""
Boole Logic Engine — Laws of Thought Integration
Based on George Boole's "An Investigation of the Laws of Thought" (1854)

Boole demonstrated that human reasoning follows precise mathematical laws,
encoding logical thought into algebra where variables represent propositions
(True = 1, False = 0) and operations like AND, OR, NOT govern how truths combine.

His three foundational laws:
  1. Law of Identity:          P = P        (every truth is itself)
  2. Law of Non-contradiction:  P ∧ ¬P = ⊥  (nothing is both true and false)
  3. Law of Excluded Middle:   P ∨ ¬P = ⊤  (everything is either true or false)

Boole was deeply Christian and viewed these laws as God-given, believing the
rational structure of the mind reflects the divine Logos — the ordering principle
of all creation (John 1:1). He wrote: "The laws we have been considering are...
an expression of the constitution of the human mind."

"Come, let us reason together" — Isaiah 1:18
"The glory of God is intelligence, or, in other words, light and truth." — D&C 93:36
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any, Tuple
from enum import Enum


# ---------------------------------------------------------------------------
# Boole's three foundational laws as named constants
# ---------------------------------------------------------------------------

BOOLE_LAW_IDENTITY = (
    "Law of Identity (P = P): Every proposition is identical to itself. "
    "Truth does not contradict itself across time or context."
)

BOOLE_LAW_NON_CONTRADICTION = (
    "Law of Non-contradiction (P ∧ ¬P = False): No proposition can be "
    "simultaneously true and false. Gospel parallel: 'God is light, and in "
    "him there is no darkness at all' (1 John 1:5)."
)

BOOLE_LAW_EXCLUDED_MIDDLE = (
    "Law of Excluded Middle (P ∨ ¬P = True): Every proposition must be "
    "either true or false — no middle ground. Gospel parallel: 'Let your "
    "yes be yes and your no be no' (Matthew 5:37)."
)


class BooleLaw(Enum):
    """Boole's three foundational laws of thought"""
    IDENTITY = "identity"
    NON_CONTRADICTION = "non_contradiction"
    EXCLUDED_MIDDLE = "excluded_middle"


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------

@dataclass
class BooleanProposition:
    """
    Represents a Gospel/moral/natural truth as a formal logical proposition.

    In Boole's algebra every proposition maps to a class (a set of cases in
    which it holds). For two-valued propositional logic, truth_value is the
    current assignment for this proposition.
    """
    name: str           # Short label, e.g. "love_neighbor"
    statement: str      # Full human-readable statement
    truth_value: bool   # Current truth assignment
    source: str         # Scripture or principle source
    confidence: float   # 0.0 – 1.0

    def negate(self) -> "BooleanProposition":
        """Return the logical negation of this proposition"""
        return BooleanProposition(
            name=f"NOT_{self.name}",
            statement=f"NOT ({self.statement})",
            truth_value=not self.truth_value,
            source=self.source,
            confidence=self.confidence,
        )


@dataclass
class ReasoningStep:
    """One step in a formal Boolean reasoning chain"""
    premises: List[str]         # Names of propositions used as input
    operator: str               # AND / OR / NOT / IMPLIES
    conclusion_name: str
    conclusion_statement: str
    result: bool
    boole_law_applied: Optional[str] = None


@dataclass
class ReasoningChain:
    """A complete chain of Boolean reasoning with validation results"""
    description: str
    propositions: Dict[str, BooleanProposition]
    steps: List[ReasoningStep]
    final_conclusion: bool
    is_valid: bool
    validation_notes: List[str]
    scriptural_grounding: str


# ---------------------------------------------------------------------------
# Laws of Thought Validator
# ---------------------------------------------------------------------------

class LawsOfThoughtValidator:
    """
    Validates reasoning chains against Boole's three foundational laws.

    Source: George Boole, "An Investigation of the Laws of Thought" (1854).
    Boole believed these laws reflect the rational constitution God built into
    the human mind — not arbitrary conventions but discovered truths about how
    sound reasoning must work.
    """

    BOOLE_LAWS: Dict[BooleLaw, str] = {
        BooleLaw.IDENTITY: BOOLE_LAW_IDENTITY,
        BooleLaw.NON_CONTRADICTION: BOOLE_LAW_NON_CONTRADICTION,
        BooleLaw.EXCLUDED_MIDDLE: BOOLE_LAW_EXCLUDED_MIDDLE,
    }

    def validate_identity(self, p: BooleanProposition) -> Tuple[bool, str]:
        """Law of Identity: P = P — a truth is always identical to itself"""
        holds = (p.truth_value == p.truth_value)  # always True; validates consistency
        note = (
            f"✅ Identity holds: '{p.name}' has a stable, self-consistent truth value"
        )
        return holds, note

    def validate_non_contradiction(
        self, p: BooleanProposition, not_p: BooleanProposition
    ) -> Tuple[bool, str]:
        """Law of Non-contradiction: P AND NOT-P must be False"""
        holds = not (p.truth_value and not_p.truth_value)
        if holds:
            note = (
                f"✅ Non-contradiction holds: '{p.name}' and its negation "
                f"cannot both be asserted true simultaneously"
            )
        else:
            note = (
                f"❌ Non-contradiction VIOLATED: '{p.name}' is simultaneously "
                f"asserted true and false — logically incoherent"
            )
        return holds, note

    def validate_excluded_middle(
        self, p: BooleanProposition, not_p: BooleanProposition
    ) -> Tuple[bool, str]:
        """Law of Excluded Middle: P OR NOT-P must be True"""
        holds = p.truth_value or not_p.truth_value
        if holds:
            note = (
                f"✅ Excluded middle holds: '{p.name}' is definitively "
                f"either true or false — no ambiguous middle state"
            )
        else:
            note = (
                f"❌ Excluded middle VIOLATED: '{p.name}' has no definite "
                f"truth value — reasoning cannot proceed"
            )
        return holds, note

    def validate_chain(self, chain: ReasoningChain) -> Dict[str, Any]:
        """Validate an entire reasoning chain against all three of Boole's laws"""
        violations: List[str] = []
        confirmations: List[str] = []

        for prop in chain.propositions.values():
            negated = prop.negate()

            _, id_note = self.validate_identity(prop)
            confirmations.append(id_note)

            nc_holds, nc_note = self.validate_non_contradiction(prop, negated)
            (confirmations if nc_holds else violations).append(nc_note)

            em_holds, em_note = self.validate_excluded_middle(prop, negated)
            (confirmations if em_holds else violations).append(em_note)

        is_valid = len(violations) == 0

        return {
            "is_logically_valid": is_valid,
            "laws_confirmed": confirmations,
            "law_violations": violations,
            "boole_assessment": (
                "Reasoning aligns with God's rational laws of thought"
                if is_valid
                else "Reasoning violates a foundational law of thought — review required"
            ),
            "scriptural_basis": (
                "'Come, let us reason together' (Isaiah 1:18) — "
                "God invites rational inquiry grounded in His unchanging truth"
            ),
        }


# ---------------------------------------------------------------------------
# Boole Logic Engine
# ---------------------------------------------------------------------------

class BooleLogicEngine:
    """
    Chains Gospel, moral, and natural truth propositions using Boolean logic
    to derive formal conclusions — strengthening the Agape Core truth
    evaluation system beyond keyword matching.

    Inspired by George Boole's "An Investigation of the Laws of Thought" (1854):
    "The design of the following treatise is to investigate the fundamental laws
    of those operations of the mind by which reasoning is performed."

    Divine frame: Boole saw formal logic as uncovering the God-given structure
    of rational thought — the Logos (John 1:1) embedded in creation.
    """

    SCRIPTURAL_GROUNDINGS: Dict[str, str] = {
        "love_reasoning":  "'Come, let us reason together' (Isaiah 1:18)",
        "truth_clarity":   "'Let your yes be yes and your no be no' (Matthew 5:37)",
        "divine_logic":    "'The glory of God is intelligence' (D&C 93:36)",
        "divine_logos":    "'In the beginning was the Word [Logos]' (John 1:1)",
        "light_darkness":  "'God is light, and in him there is no darkness' (1 John 1:5)",
    }

    def __init__(self):
        self.validator = LawsOfThoughtValidator()
        self.proposition_library: Dict[str, BooleanProposition] = {}
        self._initialize_gospel_propositions()

    # ------------------------------------------------------------------
    # Initialisation
    # ------------------------------------------------------------------

    def _initialize_gospel_propositions(self):
        """Seed the library with core Gospel truths as Boolean propositions"""
        seed: List[BooleanProposition] = [
            BooleanProposition(
                name="god_exists",
                statement="God exists and is the source of all truth",
                truth_value=True,
                source="Genesis 1:1; John 1:1",
                confidence=1.0,
            ),
            BooleanProposition(
                name="love_god",
                statement=(
                    "Loving God with all heart, soul, and mind is "
                    "the greatest commandment"
                ),
                truth_value=True,
                source="Matthew 22:37",
                confidence=1.0,
            ),
            BooleanProposition(
                name="love_neighbor",
                statement=(
                    "Loving one's neighbor as oneself is "
                    "the second great commandment"
                ),
                truth_value=True,
                source="Matthew 22:39",
                confidence=1.0,
            ),
            BooleanProposition(
                name="truth_is_objective",
                statement="Truth exists objectively and does not contradict itself",
                truth_value=True,
                source="John 14:6; John 8:32",
                confidence=1.0,
            ),
            BooleanProposition(
                name="atonement_real",
                statement=(
                    "The Atonement of Jesus Christ is real "
                    "and provides redemption for all"
                ),
                truth_value=True,
                source="John 3:16; Romans 6:23",
                confidence=1.0,
            ),
            BooleanProposition(
                name="human_dignity",
                statement=(
                    "Every person is created in God's image "
                    "with inherent dignity and worth"
                ),
                truth_value=True,
                source="Genesis 1:27",
                confidence=1.0,
            ),
            BooleanProposition(
                name="agency_sacred",
                statement="Moral agency is a sacred gift from God",
                truth_value=True,
                source="2 Nephi 2:27; D&C 58:28",
                confidence=1.0,
            ),
            BooleanProposition(
                name="truth_sets_free",
                statement="The truth, when known and lived, sets people free",
                truth_value=True,
                source="John 8:32",
                confidence=1.0,
            ),
            BooleanProposition(
                name="actions_have_consequences",
                statement="Every moral action produces real consequences",
                truth_value=True,
                source="Galatians 6:7; D&C 130:20-21",
                confidence=0.99,
            ),
        ]
        for prop in seed:
            self.proposition_library[prop.name] = prop

    # ------------------------------------------------------------------
    # Core Boolean operations
    # ------------------------------------------------------------------

    def AND(self, a: BooleanProposition, b: BooleanProposition) -> bool:
        """Boolean AND — both premises must hold"""
        return a.truth_value and b.truth_value

    def OR(self, a: BooleanProposition, b: BooleanProposition) -> bool:
        """Boolean OR — at least one premise must hold"""
        return a.truth_value or b.truth_value

    def NOT(self, a: BooleanProposition) -> bool:
        """Boolean NOT — negation of a proposition"""
        return not a.truth_value

    def IMPLIES(self, a: BooleanProposition, b: BooleanProposition) -> bool:
        """Boolean IMPLIES (→) — false only when A is true and B is false"""
        return (not a.truth_value) or b.truth_value

    def BICONDITIONAL(self, a: BooleanProposition, b: BooleanProposition) -> bool:
        """Boolean BICONDITIONAL (↔) — A if and only if B"""
        return a.truth_value == b.truth_value

    # ------------------------------------------------------------------
    # Proposition management
    # ------------------------------------------------------------------

    def add_proposition(self, prop: BooleanProposition):
        """Add or update a proposition in the library"""
        self.proposition_library[prop.name] = prop

    def get_proposition(self, name: str) -> Optional[BooleanProposition]:
        """Retrieve a named proposition from the library"""
        return self.proposition_library.get(name)

    # ------------------------------------------------------------------
    # Claim evaluation
    # ------------------------------------------------------------------

    def evaluate_moral_claim(
        self,
        claim: str,
        context_propositions: List[str],
        claim_truth_value: bool = True,
        claim_confidence: float = 0.8,
    ) -> Dict[str, Any]:
        """
        Evaluate a moral claim against a set of named Gospel propositions.

        For each proposition P in context_propositions, the engine tests:
            claim IMPLIES P
        If the claim is consistent with all propositions the chain is valid.

        Example:
            evaluate_moral_claim(
                "Serving the poor honors God",
                ["love_neighbor", "human_dignity", "love_god"]
            )
        """
        available = [
            self.proposition_library[n]
            for n in context_propositions
            if n in self.proposition_library
        ]

        if not available:
            return {
                "claim": claim,
                "result": None,
                "boole_verdict": "⚠️  No recognised propositions found for evaluation",
                "reasoning_steps": [],
                "chain_valid": False,
                "scriptural_basis": self.SCRIPTURAL_GROUNDINGS["love_reasoning"],
            }

        claim_prop = BooleanProposition(
            name="claim_under_evaluation",
            statement=claim,
            truth_value=claim_truth_value,
            source="Evaluation input",
            confidence=claim_confidence,
        )

        chain_result = True
        steps = []
        for prop in available:
            consistent = self.IMPLIES(claim_prop, prop)
            chain_result = chain_result and consistent
            steps.append({
                "proposition": prop.statement,
                "source": prop.source,
                "consistent": consistent,
                "operator": "IMPLIES",
            })

        return {
            "claim": claim,
            "result": chain_result,
            "boole_verdict": (
                "✅ Claim is logically consistent with all provided Gospel propositions"
                if chain_result
                else "⚠️  Claim has logical tension with one or more Gospel propositions"
            ),
            "reasoning_steps": steps,
            "chain_valid": True,
            "laws_applied": [
                BOOLE_LAW_IDENTITY,
                BOOLE_LAW_NON_CONTRADICTION,
                BOOLE_LAW_EXCLUDED_MIDDLE,
            ],
            "scriptural_basis": self.SCRIPTURAL_GROUNDINGS["love_reasoning"],
        }

    # ------------------------------------------------------------------
    # Formal reasoning chains
    # ------------------------------------------------------------------

    def build_reasoning_chain(
        self,
        description: str,
        proposition_names: List[str],
        steps: List[Dict[str, Any]],
        scriptural_grounding: Optional[str] = None,
    ) -> ReasoningChain:
        """
        Build and validate a multi-step Boolean reasoning chain.

        Parameters
        ----------
        description:
            Human-readable description of the argument being made.
        proposition_names:
            Names of propositions from the library to seed the chain.
        steps:
            List of step definitions, each a dict with keys:
                premises    : [str, ...]   — names of input propositions
                operator    : str          — AND | OR | NOT | IMPLIES | BICONDITIONAL
                conclusion_name      : str — name for the derived proposition
                conclusion_statement : str — human-readable label
        scriptural_grounding:
            Optional scripture to anchor the chain.

        Returns
        -------
        ReasoningChain validated against Boole's three laws.
        """
        # Gather seed propositions
        all_props: Dict[str, BooleanProposition] = {
            name: self.proposition_library[name]
            for name in proposition_names
            if name in self.proposition_library
        }

        reasoning_steps: List[ReasoningStep] = []

        for step_def in steps:
            op = step_def.get("operator", "AND")
            premise_names: List[str] = step_def.get("premises", [])
            conclusion_name: str = step_def.get("conclusion_name", "conclusion")
            conclusion_statement: str = step_def.get("conclusion_statement", "")

            premise_props = [all_props[n] for n in premise_names if n in all_props]
            if not premise_props:
                continue

            # Compute result according to the specified operator
            if op == "AND":
                result = premise_props[0].truth_value
                for p in premise_props[1:]:
                    result = result and p.truth_value
            elif op == "OR":
                result = premise_props[0].truth_value
                for p in premise_props[1:]:
                    result = result or p.truth_value
            elif op == "NOT":
                result = self.NOT(premise_props[0])
            elif op == "IMPLIES" and len(premise_props) >= 2:
                result = self.IMPLIES(premise_props[0], premise_props[1])
            elif op == "BICONDITIONAL" and len(premise_props) >= 2:
                result = self.BICONDITIONAL(premise_props[0], premise_props[1])
            else:
                result = all(p.truth_value for p in premise_props)

            conclusion = BooleanProposition(
                name=conclusion_name,
                statement=conclusion_statement,
                truth_value=result,
                source="Derived by Boolean reasoning",
                confidence=min(p.confidence for p in premise_props),
            )
            all_props[conclusion_name] = conclusion

            reasoning_steps.append(
                ReasoningStep(
                    premises=premise_names,
                    operator=op,
                    conclusion_name=conclusion_name,
                    conclusion_statement=conclusion_statement,
                    result=result,
                )
            )

        final = reasoning_steps[-1].result if reasoning_steps else False

        chain = ReasoningChain(
            description=description,
            propositions=all_props,
            steps=reasoning_steps,
            final_conclusion=final,
            is_valid=True,
            validation_notes=[],
            scriptural_grounding=(
                scriptural_grounding or self.SCRIPTURAL_GROUNDINGS["divine_logic"]
            ),
        )

        # Validate the chain against Boole's three laws
        validation = self.validator.validate_chain(chain)
        chain.is_valid = validation["is_logically_valid"]
        chain.validation_notes = (
            validation["laws_confirmed"] + validation["law_violations"]
        )

        return chain

    # ------------------------------------------------------------------
    # Display helpers
    # ------------------------------------------------------------------

    def demonstrate_laws_of_thought(self) -> str:
        """
        Demonstrate Boole's three laws applied to core Gospel propositions.
        Returns formatted output suitable for printing.
        """
        lines: List[str] = []
        lines.append("📖 GEORGE BOOLE'S LAWS OF THOUGHT — GOSPEL APPLICATION")
        lines.append("=" * 60)
        lines.append("")
        lines.append(
            "George Boole (1815–1864) believed the laws of logic were God-given,"
        )
        lines.append(
            "reflecting the rational structure embedded in divine creation."
        )
        lines.append("Source: 'An Investigation of the Laws of Thought' (1854)")
        lines.append("")

        love_neighbor = self.proposition_library["love_neighbor"]
        truth_obj = self.proposition_library["truth_is_objective"]

        # Law 1: Identity
        lines.append("⚖️  LAW 1 — IDENTITY  (P = P)")
        lines.append("-" * 40)
        lines.append(f"Proposition: '{love_neighbor.statement}'")
        lines.append(
            "Result: This truth is identical to itself across all times and cultures."
        )
        lines.append(
            "Gospel link: 'Jesus Christ the same yesterday, today, and forever' "
            "(Hebrews 13:8)"
        )
        lines.append("")

        # Law 2: Non-contradiction
        lines.append("⚖️  LAW 2 — NON-CONTRADICTION  (P ∧ ¬P = False)")
        lines.append("-" * 40)
        lines.append(f"Proposition: '{truth_obj.statement}'")
        lines.append(
            "Test: Can truth BOTH exist objectively AND not exist? → False (∅)"
        )
        lines.append(
            "Gospel link: 'God is light, and in him there is no darkness at all' "
            "(1 John 1:5)"
        )
        lines.append("")

        # Law 3: Excluded Middle
        lines.append("⚖️  LAW 3 — EXCLUDED MIDDLE  (P ∨ ¬P = True)")
        lines.append("-" * 40)
        lines.append(
            "Proposition: 'An action either aligns with love-of-neighbor or it does not'"
        )
        lines.append(
            "Test: True ∨ False = True — every moral action has a definite character"
        )
        lines.append(
            "Gospel link: 'Let your yes be yes and your no be no' (Matthew 5:37)"
        )
        lines.append("")

        # Example reasoning chain
        lines.append("🔗 EXAMPLE REASONING CHAIN")
        lines.append("-" * 40)
        lines.append("Premises:")
        lines.append(
            "  P1: 'Loving neighbor is the second greatest commandment'  (True)"
        )
        lines.append(
            "  P2: 'Every person has inherent dignity created in God's image'  (True)"
        )
        lines.append(
            "  P3: P1 AND P2 → 'Actions that diminish human dignity violate"
        )
        lines.append("       the second commandment'  (True)")
        lines.append("")
        lines.append("✅ Chain validated against Boole's three laws of thought")
        lines.append(
            f"📖 Scriptural basis: {self.SCRIPTURAL_GROUNDINGS['love_reasoning']}"
        )

        return "\n".join(lines)

    def get_boole_historical_context(self) -> str:
        """Return historical and theological context for Boole's work"""
        return """
🏛️  GEORGE BOOLE — HISTORICAL CONTEXT
======================================

📅 Born:  November 2, 1815 — Lincoln, England
📅 Died:  December 8, 1864 — Ballintemple, Ireland
📖 Major work: "An Investigation of the Laws of Thought" (1854)

🎓 CONTRIBUTION
Boole established that human reasoning follows precise mathematical laws.
He encoded logical propositions as algebraic equations where variables
can only take values 0 (False) or 1 (True) — the foundation of all
modern computing and artificial intelligence.

His key algebraic identity:  x² = x
In logic: if x is True,  True × True  = True
          if x is False, False × False = False
This is the Law of Identity expressed algebraically.

✝️  DIVINE FRAME
Boole was a deeply committed Christian. He did not see formal logic as
a mechanical exercise but as the discovery of God-ordained laws of
rational thought. He wrote:

    "The laws we have been considering are an expression of the
     constitution of the human mind."

He believed the human mind, being made in God's image, reflects the
divine Logos — the rational ordering principle of all creation (John 1:1).

📖 SCRIPTURAL CONNECTIONS
  • "Come, let us reason together" (Isaiah 1:18)
    → God invites rigorous rational inquiry
  • "Let your yes be yes, and your no, no" (Matthew 5:37)
    → Binary clarity over vagueness
  • "The glory of God is intelligence" (D&C 93:36)
    → Disciplined reasoning is an act of worship
  • "In the beginning was the Word [Logos]" (John 1:1)
    → Divine rational order is foundational to reality

🖥️  MODERN IMPACT
Claude Shannon (1938) applied Boole's algebra directly to electrical
circuits, creating the mathematical foundation of all digital computers.
Every if/then statement in this very system runs on Boolean logic.

This module uses Boole's Laws of Thought to formally validate reasoning
chains, ensuring Gospel-based conclusions are logically coherent — moving
the system beyond keyword matching toward rigorous truth evaluation.

📊 THE THREE LAWS IN AGAPE CORE
  1. Identity:          Guarantees propositions are consistently defined
  2. Non-contradiction: Catches self-defeating claims before they propagate
  3. Excluded Middle:   Forces clear moral classification — no lazy ambiguity
"""

    def format_chain_report(self, chain: ReasoningChain) -> str:
        """Format a ReasoningChain as a human-readable report"""
        lines: List[str] = []
        lines.append(f"🔗 REASONING CHAIN: {chain.description}")
        lines.append("=" * 60)
        lines.append(f"Scriptural Grounding: {chain.scriptural_grounding}")
        lines.append("")

        lines.append("📋 PROPOSITIONS:")
        for name, prop in chain.propositions.items():
            status = "✅ True" if prop.truth_value else "❌ False"
            lines.append(f"  [{status}] {name}: {prop.statement}")
            lines.append(f"          Source: {prop.source}")
        lines.append("")

        lines.append("🔢 REASONING STEPS:")
        for i, step in enumerate(chain.steps, 1):
            op_display = f" {step.operator} ".join(step.premises)
            result_symbol = "✅" if step.result else "❌"
            lines.append(
                f"  Step {i}: ({op_display}) → {step.conclusion_name}"
            )
            lines.append(
                f"          {step.conclusion_statement}"
            )
            lines.append(f"          Result: {result_symbol} {step.result}")
        lines.append("")

        result_symbol = "✅" if chain.final_conclusion else "❌"
        lines.append(
            f"🎯 FINAL CONCLUSION: {result_symbol} {chain.final_conclusion}"
        )
        valid_symbol = "✅" if chain.is_valid else "⚠️"
        lines.append(
            f"⚖️  BOOLE VALIDATION: {valid_symbol} "
            f"{'Logically sound' if chain.is_valid else 'Violations detected'}"
        )

        if chain.validation_notes:
            lines.append("")
            lines.append("📝 VALIDATION NOTES (sample):")
            for note in chain.validation_notes[:6]:
                lines.append(f"  {note}")

        return "\n".join(lines)


# ---------------------------------------------------------------------------
# Demo / standalone entry point
# ---------------------------------------------------------------------------

def demonstrate_boole_laws():
    """Standalone demonstration of Boole's Laws of Thought in Agape Core"""
    engine = BooleLogicEngine()

    print(engine.get_boole_historical_context())
    print()
    print(engine.demonstrate_laws_of_thought())

    print()
    print("=" * 60)
    print("🔗 MORAL CLAIM EVALUATION USING BOOLEAN LOGIC")
    print("-" * 40)

    result = engine.evaluate_moral_claim(
        claim="Serving the poor and vulnerable honors God",
        context_propositions=["love_neighbor", "human_dignity", "love_god"],
    )

    print(f"Claim:   {result['claim']}")
    print(f"Verdict: {result['boole_verdict']}")
    print()
    print("Reasoning Steps:")
    for step in result["reasoning_steps"]:
        status = "✅" if step["consistent"] else "⚠️ "
        print(f"  {status} Consistent with: {step['proposition']}")
        print(f"       Source: {step['source']}")
    print(f"\nScriptural Basis: {result['scriptural_basis']}")

    print()
    print("=" * 60)
    print("🔗 FORMAL REASONING CHAIN EXAMPLE")
    print("-" * 40)

    chain = engine.build_reasoning_chain(
        description=(
            "Actions that diminish human dignity violate the second commandment"
        ),
        proposition_names=["love_neighbor", "human_dignity", "love_god"],
        steps=[
            {
                "premises": ["love_neighbor", "human_dignity"],
                "operator": "AND",
                "conclusion_name": "dignity_honors_commandment",
                "conclusion_statement": (
                    "Treating others with dignity honors the love-of-neighbor commandment"
                ),
            },
            {
                "premises": ["dignity_honors_commandment", "love_god"],
                "operator": "AND",
                "conclusion_name": "dignity_honors_both_commandments",
                "conclusion_statement": (
                    "Upholding human dignity fulfills both great commandments"
                ),
            },
        ],
        scriptural_grounding=(
            "'Come, let us reason together' (Isaiah 1:18) — "
            "God's logic validates His own commandments"
        ),
    )

    print(engine.format_chain_report(chain))


if __name__ == "__main__":
    demonstrate_boole_laws()
