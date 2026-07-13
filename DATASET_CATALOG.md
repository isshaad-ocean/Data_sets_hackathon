# Dataset Catalog — Tech Mahindra CODE Hackathon

Complete reference for all 4 challenge datasets. Includes file sizes, licenses, and credential requirements.

---

## Challenge 1 — AI Agent Creation Platform for Autonomous Crypto Trading

**Folder:** `challenge-1-crypto-trading-agent/`

| Dataset | Format | Size | License | Credential | Source |
|---------|--------|------|---------|-----------|--------|
| **Kraken OHLCV Historical** | CSV | ~200 MB | Open | None | [CryptoDataDownload](https://cryptodatadownload.com/data/kraken/) |
| **CryptoSentiment (14 coins)** | JSON/CSV | ~200 MB | CC0 | None | [Zenodo](https://zenodo.org/records/7684409) |
| **Bitcoin Historical Data** | CSV | ~5 MB | Open | Kaggle (optional) | [Kaggle](https://www.kaggle.com/datasets/mczielinski/bitcoin-historical-data) |
| **Crypto News + Sentiment** | CSV | ~10 MB | Research | Kaggle (optional) | [Kaggle](https://www.kaggle.com/datasets/oliviervha/crypto-news) |
| **Fear & Greed Index** | CSV | <1 MB | Open | None | [Kaggle](https://www.kaggle.com/datasets/l3llff/bitcoin) |
| **Total** | | **~416 MB** | | | |

**Key Fields:**
- OHLCV: `timestamp`, `open`, `high`, `low`, `close`, `volume`, `pair`
- CryptoSentiment: `date`, `coin`, `sentiment_score`, `source`, `headline`
- Fear & Greed: `date`, `value` (0-100), `classification`

---

## Challenge 2 — Network Anomaly Root-Cause Assistant

**Folder:** `challenge-2-network-anomaly-rca/`

| Dataset | Format | Size | License | Credential | Source |
|---------|--------|------|---------|-----------|--------|
| **NSL-KDD** | TXT/CSV | 7 MB | Open | Kaggle | [Kaggle](https://www.kaggle.com/datasets/hassan06/nslkdd) |
| **UNSW-NB15** | CSV | 113 MB | CC-BY-NC-SA 4.0 | Kaggle | [Kaggle](https://www.kaggle.com/datasets/dhoogla/unswnb15) |
| **LogHub (HDFS + BGL)** | LOG | ~170 MB | Open | None | [HuggingFace](https://huggingface.co/datasets/aioha/loghub) |
| **Total** | | **~290 MB** | | | |

**Key Fields:**
- NSL-KDD: 41 network features, `attack_type` (DoS/Probe/R2L/U2R/Normal)
- UNSW-NB15: `srcip`, `dstip`, `proto`, `service`, `state`, `label`, `attack_cat`
- LogHub: `Timestamp`, `EventId`, `Component`, `Level`, `Content`, `Label`

---

## Challenge 3 — Continuous KYC Autonomous Auditor

**Folder:** `challenge-3-kyc-autonomous-auditor/`

| Dataset | Format | Size | License | Credential | Source |
|---------|--------|------|---------|-----------|--------|
| **OpenSanctions (100+ gov lists)** | JSON/CSV | ~500 MB | CC0/ODbL | None | [OpenSanctions](https://www.opensanctions.org/datasets/default/) |
| **OFAC SDN List** | CSV/XML | ~5 MB | Public Domain | None | [US Treasury](https://www.treasury.gov/ofac/downloads/sdn.csv) |
| **EU Consolidated Sanctions** | XML/JSON | ~3 MB | Public Domain | None | [EU](https://webgate.ec.europa.eu/fsd/fsf) |
| **EUR-Lex (LexGLUE)** | Parquet | 600 MB | CC-BY 4.0 | None | [HuggingFace](https://huggingface.co/datasets/coastalcph/lex_glue) |
| **PrivacyQA** | JSON | 5 MB | CC-BY 4.0 | None | [HuggingFace](https://huggingface.co/datasets/allenai/privacy_qa) |
| **GDPR Full Text** | JSON | <1 MB | Public Domain | None | [GitHub](https://github.com/nickmvincent/gdpr_text) |
| **OPP-115 Privacy Policies** | JSON/CSV | ~10 MB | CC-BY 4.0 | None | [GitHub](https://github.com/citp/privacy-policy-annotated) |
| **Total** | | **~1,124 MB** | | | |

**Key Fields:**
- OpenSanctions: `entity_id`, `name`, `aliases`, `dob`, `nationality`, `sanction_program`, `source_list`
- OFAC SDN: `uid`, `first_name`, `last_name`, `dob`, `nationality`, `program`, `remarks`
- OPP-115: `policy_text`, `practice_category` (10 types), `annotator_id`

---

## Challenge 4 — Contract & SOW Risk Analyzer

**Folder:** `challenge-4-contract-sow-risk-analyzer/`

| Dataset | Format | Size | License | Credential | Source |
|---------|--------|------|---------|-----------|--------|
| **CUAD v1** (510 contracts, 41 clause types) | JSON + PDF | 300 MB | CC-BY 4.0 | None | [HuggingFace](https://huggingface.co/datasets/theatticusproject/cuad) |
| **ContractNLI** | JSON | 5 MB | CC-BY-SA 4.0 | None | [HuggingFace](https://huggingface.co/datasets/stanfordnlp/contract_nli) |
| **LEDGAR (60k+ provisions)** | Parquet | 447 MB | CC-BY 4.0 | None | [HuggingFace](https://huggingface.co/datasets/coastalcph/lex_glue) |
| **Total** | | **~752 MB** | | | |

**Key Fields:**
- CUAD: `contract_name`, `clause_type` (41 types), `answer` (clause text), `context`
- ContractNLI: `hypothesis`, `label` (Entailment/Contradiction/NotMentioned), `document`
- LEDGAR: `provision` (clause text), `label` (83 clause categories), `source`

---

## Grand Summary

| Challenge | Folder | Total Size | Kaggle | Login |
|-----------|--------|------------|--------|-------|
| C1 — AI Agent Crypto Trading | `challenge-1-crypto-trading-agent/` | ~416 MB | Optional | None |
| C2 — Network Anomaly Root-Cause | `challenge-2-network-anomaly-rca/` | ~290 MB | Required | Kaggle |
| C3 — Continuous KYC Auditor | `challenge-3-kyc-autonomous-auditor/` | ~1,124 MB | Not needed | None |
| C4 — Contract & SOW Risk | `challenge-4-contract-sow-risk-analyzer/` | ~752 MB | Not needed | None |

---

## Kaggle API Setup (One-Time)

1. Go to **https://www.kaggle.com/settings**
2. Scroll to **API** section → click **"Create New API Token"**
3. Move `kaggle.json`:

**Windows PowerShell:**
```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.kaggle"
Move-Item "$env:USERPROFILE\Downloads\kaggle.json" "$env:USERPROFILE\.kaggle\kaggle.json"
```

4. Verify: `kaggle datasets list`

---

*Tech Mahindra CODE Hackathon — Dataset Catalog*
