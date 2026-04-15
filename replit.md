# Agape Core AI

A Christ-centered AI framework built on the two greatest commandments: Love God and Love thy neighbor.

## Overview

Agape Core evaluates information, media, and ideas against Gospel truth using a hierarchical truth system (Gospel > Moral > Natural > Practical > Opinion). It includes tools for media discernment, spiritual self-evaluation, and ethical reasoning.

## Architecture

### Core Modules

- **`main.py`** — CLI entry point with a numbered menu for all subsystems
- **`truth_foundation/`** — Heart of the system; Gospel truth engine, SeekGood evaluator, core truth hierarchy
- **`truth_discerner/`** — Media analysis engine; evaluates books, movies, and content against biblical standards
- **`agape_core_seed/`** — Modular AI ethics evaluator that can be embedded in other AI systems
- **`arcos/`** — ArcOs: Advanced Revelation and Covenant Operating System
- **`human_potential/`** — Human potential equation framework
- **`chat_interface/`** — Conversational wrapper for Agape Core
- **`gilgamesh_evaluator/`** — RAG-based evaluator for the Epic of Gilgamesh

### Gilgamesh RAG Evaluator (NEW)

Located in `gilgamesh_evaluator/gilgamesh_rag_evaluator.py`.

Applies a Retrieval-Augmented Generation (RAG) pipeline to evaluate the Epic of Gilgamesh (English version) against Gospel truth:

1. **Load** — built-in 12-tablet knowledge base, or a user-supplied text file
2. **Chunk** — split by tablet/section
3. **Evaluate** — each chunk through `SeekGoodEvaluator` (Philippians 4:8 criteria) + `MediaAnalyzer` (biblical truth alignment)
4. **Aggregate** — per-chunk scores combined into a final verdict with rating, recommendation, biblical parallels, and discussion questions

Run standalone:
```
python3 gilgamesh_evaluator/gilgamesh_rag_evaluator.py
python3 gilgamesh_evaluator/gilgamesh_rag_evaluator.py --verbose
python3 gilgamesh_evaluator/gilgamesh_rag_evaluator.py --file /path/to/gilgamesh.txt
```

Or access via the main menu: **Option 10**.

## Running the App

The main workflow runs `python main.py` which launches the interactive CLI menu.

## Key Truth Framework

- **SeekGood (Philippians 4:8)**: 8 criteria — true, honest, just, pure, lovely, good report, virtuous, praiseworthy
- **MediaAnalyzer**: Detects worldviews (secular humanism, relativism, hedonism, etc.) and biblical theme alignment
- **TruthAlignment**: PURE_TRUTH / MIXED_TRUTH / DECEPTIVE / ACTIVELY_HARMFUL
- **GoodnessLevel**: EXCELLENT / GOOD / MIXED / QUESTIONABLE / AVOID

## Runtime

Python 3.11 (installed via Replit module system)
