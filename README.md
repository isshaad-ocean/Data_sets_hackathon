# Tech Mahindra CODE Hackathon — Dataset Repository

> **150 participants · 4 challenges · All datasets in one place**

This repository contains curated, open-source datasets for all 4 challenge problem statements.
Each challenge folder is self-contained with its own `README.md`, `download.py`, and data structure.

---

## Quick Start — 3 Steps

```bash
# 1. Clone
git clone https://github.com/isshaad-ocean/Data_sets_hackathon.git
cd Data_sets_hackathon

# 2. Install dependencies
pip install -r requirements.txt

# 3. Download your challenge datasets
python download_datasets.py --challenge <1|2|3|4>
```

> First time setup? → Read [**SETUP.md**](./SETUP.md) for Git LFS, Kaggle API, and virtual environment instructions.

---

## The 4 Challenges

| # | Challenge | Dataset Folder | Pre-built Zip | Size |
|---|-----------|---------------|---------------|------|
| **1** | [AI Agent Crypto Trading](#challenge-1--ai-agent-creation-platform-for-autonomous-crypto-trading) | `challenge-1-crypto-trading-agent/` | *(download script)* | ~416 MB |
| **2** | [Network Anomaly Root-Cause](#challenge-2--network-anomaly-root-cause-assistant) | `challenge-2-network-anomaly-rca/` | `zipped-datasets/challenge-2-network-anomaly-rca.zip` | ~24 MB zip |
| **3** | [Continuous KYC Auditor](#challenge-3--continuous-kyc-autonomous-auditor) | `challenge-3-kyc-autonomous-auditor/` | `zipped-datasets/challenge-3-kyc-autonomous-auditor.zip` | ~489 MB zip |
| **4** | [Contract & SOW Risk Analyzer](#challenge-4--contract--sow-risk-analyzer) | `challenge-4-contract-sow-risk-analyzer/` | `zipped-datasets/challenge-4-contract-sow-risk-analyzer.zip` | ~638 MB zip |

---

## Challenge 1 — AI Agent Creation Platform for Autonomous Crypto Trading

**Folder:** `challenge-1-crypto-trading-agent/`

Build an intelligent no-code/low-code platform to configure, deploy, and evaluate autonomous crypto trading agents.

| Dataset | Description | Size | License |
|---------|-------------|------|---------|
| **CryptoSentiment** | 14-coin FinBERT sentiment scores from news + social media | ~200 MB | CC0 |
| **Kraken OHLCV** | Historical BTC/ETH/altcoin OHLCV candlestick data | ~200 MB | Open |
| **Fear & Greed Index** | Daily market sentiment index (0-100) | <1 MB | Open |
| **Crypto News Labels** | Labeled crypto news headlines with sentiment | ~10 MB | Research |

```bash
# Download
python download_datasets.py --challenge 1
# OR
cd challenge-1-crypto-trading-agent && python download.py
```

---

## Challenge 2 — Network Anomaly Root-Cause Assistant

**Folder:** `challenge-2-network-anomaly-rca/`

Build an assistant that ingests telemetry, logs, alerts, and topology data to detect anomalies and generate explainable root-cause hypotheses.

| Dataset | Description | Size | License |
|---------|-------------|------|---------|
| **NSL-KDD** | 125K labeled network traffic records, 41 features, 5 attack types | 7 MB | Open |
| **UNSW-NB15** | Modern network intrusion dataset with 9 attack categories | 113 MB | CC-BY-NC-SA 4.0 |
| **LogHub (HDFS/BGL)** | Real system logs with Normal/Anomaly labels | ~170 MB | Open |

```bash
# Option A — Extract from pre-built zip (fastest)
Expand-Archive zipped-datasets\challenge-2-network-anomaly-rca.zip -DestinationPath challenge-2-network-anomaly-rca\

# Option B — Download fresh
python download_datasets.py --challenge 2   # Requires Kaggle API
```

> **Requires Kaggle API** for NSL-KDD and UNSW-NB15. See [SETUP.md](./SETUP.md#step-5--configure-kaggle-api).

---

## Challenge 3 — Continuous KYC Autonomous Auditor

**Folder:** `challenge-3-kyc-autonomous-auditor/`

Build an autonomous agent network that monitors high-risk corporate accounts using sanctions lists, adverse media, and entity resolution.

| Dataset | Description | Size | License |
|---------|-------------|------|---------|
| **OpenSanctions** | 100+ government sanctions + PEP lists in one dataset | ~500 MB | CC0 / ODbL |
| **OFAC SDN List** | US Treasury Specially Designated Nationals | ~5 MB | Public Domain |
| **EUR-Lex** | 65K EU legislative documents with EUROVOC labels | 600 MB | CC-BY 4.0 |
| **PrivacyQA** | 1,750 privacy policy Q&A pairs | 5 MB | CC-BY 4.0 |
| **GDPR Full Text** | Complete GDPR text, structured article-by-article | <1 MB | Public Domain |
| **OPP-115** | 115 annotated privacy policies, 10 practice categories | ~10 MB | CC-BY 4.0 |

```bash
# Option A — Extract from pre-built zip (no login needed)
Expand-Archive zipped-datasets\challenge-3-kyc-autonomous-auditor.zip -DestinationPath challenge-3-kyc-autonomous-auditor\

# Option B — Download fresh (no login needed)
python download_datasets.py --challenge 3
```

---

## Challenge 4 — Contract & SOW Risk Analyzer

**Folder:** `challenge-4-contract-sow-risk-analyzer/`

Build a contract review system that parses clauses, builds dependency graphs, detects contradictions, and generates redline suggestions.

| Dataset | Description | Size | License |
|---------|-------------|------|---------|
| **CUAD v1** | 510 expert-annotated commercial contracts, 41 clause types | 300 MB | CC-BY 4.0 |
| **ContractNLI** | NDA clause hypothesis-label pairs (Entailment / Contradiction / NotMentioned) | 5 MB | CC-BY-SA 4.0 |
| **LEDGAR** | 60K+ contract provisions with 83 category labels | 447 MB | CC-BY 4.0 |

```bash
# Option A — Extract from pre-built zip (no login needed)
Expand-Archive zipped-datasets\challenge-4-contract-sow-risk-analyzer.zip -DestinationPath challenge-4-contract-sow-risk-analyzer\

# Option B — Download fresh (no login needed)
python download_datasets.py --challenge 4
```

---

## Repository Structure

```
Data_sets_hackathon/
│
├── challenge-1-crypto-trading-agent/
│   ├── README.md                    ← Dataset guide
│   ├── download.py                  ← Standalone downloader
│   └── data/
│       ├── ohlcv/                   ← OHLCV market data
│       ├── sentiment/               ← News + social sentiment
│       └── indicators/              ← Pre-computed technical indicators
│
├── challenge-2-network-anomaly-rca/
│   ├── README.md
│   ├── download.py
│   └── data/
│       ├── nsl_kdd/                 ← NSL-KDD network traffic
│       ├── unsw_nb15/               ← UNSW-NB15 network flows
│       └── loghub/                  ← HDFS + BGL system logs
│
├── challenge-3-kyc-autonomous-auditor/
│   ├── README.md
│   ├── download.py
│   └── data/
│       ├── sanctions/               ← OpenSanctions + OFAC SDN
│       ├── eurlex/                  ← EU legislative documents
│       ├── privacy_qa/              ← PrivacyQA pairs
│       ├── gdpr_text/               ← GDPR structured JSON
│       └── opp115/                  ← Annotated privacy policies
│
├── challenge-4-contract-sow-risk-analyzer/
│   ├── README.md
│   ├── download.py
│   └── data/
│       ├── cuad/                    ← 510 annotated contracts
│       ├── contract_nli/            ← NDA clause entailment
│       └── ledgar/                  ← 60K+ contract provisions
│
├── zipped-datasets/
│   ├── challenge-2-network-anomaly-rca.zip         ← 24 MB
│   ├── challenge-3-kyc-autonomous-auditor.zip      ← 489 MB
│   └── challenge-4-contract-sow-risk-analyzer.zip  ← 638 MB
│
├── download_datasets.py             ← Master downloader (all challenges)
├── requirements.txt                 ← Python dependencies
├── SETUP.md                        ← Step-by-step environment setup
├── DATASET_CATALOG.md              ← Full dataset reference
├── PARTICIPANTS_GUIDE.md           ← Per-challenge download guide
├── DATASET_SIZES_AND_SOURCES.md    ← Sizes and original sources
│
└── ignore/                         ← Archived unrelated datasets
```

---

## Credential Requirements at a Glance

| Challenge | Kaggle API | Internet | Pre-built Zip |
|-----------|-----------|---------|---------------|
| C1 — Crypto Trading | Optional | ✅ | ❌ (use download script) |
| C2 — Network Anomaly | ✅ Required | ✅ | ✅ Available |
| C3 — KYC Auditor | ❌ Not needed | ✅ | ✅ Available |
| C4 — Contract Risk | ❌ Not needed | ✅ | ✅ Available |

---

## Documentation

| File | Description |
|------|-------------|
| [SETUP.md](./SETUP.md) | Environment setup: Python, Git LFS, Kaggle API |
| [PARTICIPANTS_GUIDE.md](./PARTICIPANTS_GUIDE.md) | Per-challenge download instructions |
| [DATASET_CATALOG.md](./DATASET_CATALOG.md) | Full reference: sizes, licenses, sources |
| [DATASET_SIZES_AND_SOURCES.md](./DATASET_SIZES_AND_SOURCES.md) | Download source URLs |

---

## Troubleshooting

```bash
# Verify all datasets are present
python download_datasets.py --verify

# Re-download a specific challenge
python download_datasets.py --challenge 2

# Fix missing large files after clone
git lfs pull
```

| Issue | Fix |
|-------|-----|
| `kaggle: command not found` | `pip install kaggle` |
| `401 Unauthorized` from Kaggle | Set up `~/.kaggle/kaggle.json` — see [SETUP.md](./SETUP.md) |
| Large files missing | `git lfs pull` |
| `ModuleNotFoundError` | `pip install -r requirements.txt` |

---

*Tech Mahindra CODE Hackathon — maintained for participants*
