# Challenge 4 — Contract & SOW Risk Analyzer

## Problem Statement

Build a contract review system that analyzes complex legal agreements against a configurable legal playbook, maps legal dependencies mathematically, resolves cross-document contradictions, and generates precise redline suggestions.

---

## Datasets

| Dataset | Format | Size | License | Source |
|---------|--------|------|---------|--------|
| **CUAD v1** (510 contracts, 41 clause types) | JSON + PDF | 300 MB | CC-BY 4.0 | [HuggingFace](https://huggingface.co/datasets/theatticusproject/cuad) |
| **ContractNLI** | JSON | 5 MB | CC-BY-SA 4.0 | [HuggingFace](https://huggingface.co/datasets/stanfordnlp/contract_nli) |
| **LEDGAR** (60k+ provisions) | Parquet | 447 MB | CC-BY 4.0 | [HuggingFace](https://huggingface.co/datasets/coastalcph/lex_glue) |

## Key Fields
- CUAD: `contract_name`, `clause_type` (41 types: Governing Law, Indemnification, IP Rights, Termination...), `answer`, `context`
- ContractNLI: `hypothesis` (clause claim), `label` (Entailment/Contradiction/NotMentioned), `document`
- LEDGAR: `provision` (clause text), `label` (83 clause categories)

## Download
No login required. See [PARTICIPANTS_GUIDE.md](../PARTICIPANTS_GUIDE.md#challenge-4) for full instructions.

*Tech Mahindra CODE Hackathon — Challenge 4*
