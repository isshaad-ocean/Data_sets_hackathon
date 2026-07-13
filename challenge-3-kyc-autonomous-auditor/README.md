# Challenge 3 — Continuous KYC Autonomous Auditor

## Problem Statement

Build an autonomous Continuous KYC agent network that monitors high-risk corporate accounts in near real time, checking adverse media, sanctions lists, and risk signals to generate explainable risk assessments and draft SAR reports.

---

## Datasets

| Dataset | Format | Size | License | Source |
|---------|--------|------|---------|--------|
| **OpenSanctions** (100+ lists) | CSV/JSON | ~500 MB | CC0/ODbL | [OpenSanctions](https://www.opensanctions.org/datasets/default/) |
| **OFAC SDN List** | CSV | ~5 MB | Public Domain | [US Treasury](https://www.treasury.gov/ofac/downloads/sdn.csv) |
| **EU Consolidated Sanctions** | XML/JSON | ~3 MB | Public Domain | [EU Portal](https://webgate.ec.europa.eu/fsd/fsf) |
| **EUR-Lex (LexGLUE)** | Parquet | 600 MB | CC-BY 4.0 | [HuggingFace](https://huggingface.co/datasets/coastalcph/lex_glue) |
| **PrivacyQA** | JSON | 5 MB | CC-BY 4.0 | [HuggingFace](https://huggingface.co/datasets/allenai/privacy_qa) |
| **GDPR Full Text** | JSON | <1 MB | Public Domain | [GitHub](https://github.com/nickmvincent/gdpr_text) |
| **OPP-115** | JSON/CSV | ~10 MB | CC-BY 4.0 | [GitHub](https://github.com/citp/privacy-policy-annotated) |

## Key Fields
- OpenSanctions: `entity_id`, `name`, `aliases`, `dob`, `nationality`, `sanction_program`, `source_list`
- OFAC SDN: `uid`, `first_name`, `last_name`, `dob`, `nationality`, `program`
- OPP-115: `policy_text`, `practice_category` (10 types)

## Download
No login required. See [PARTICIPANTS_GUIDE.md](../PARTICIPANTS_GUIDE.md#challenge-3) for full instructions.

*Hyderabad AI Hackathon 2026 — Challenge 3*
