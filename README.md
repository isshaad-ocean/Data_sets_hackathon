# Hackathon Datasets — Hyderabad AI Hackathon 2026

Datasets for all 4 challenge problem statements, organized by challenge.

---

## Challenge Folders

| Challenge | Folder | Datasets Included |
|-----------|--------|------------------|
| **Challenge 1** — AI Agent Crypto Trading | `challenge-1-crypto-trading-agent/` | CryptoSentiment, Kraken OHLCV, Fear & Greed Index, Crypto News |
| **Challenge 2** — Network Anomaly Root-Cause | `challenge-2-network-anomaly-rca/` | NSL-KDD, UNSW-NB15, LogHub (HDFS/BGL) |
| **Challenge 3** — Continuous KYC Autonomous Auditor | `challenge-3-kyc-autonomous-auditor/` | OpenSanctions, OFAC SDN, EUR-Lex, PrivacyQA, GDPR Text, OPP-115 |
| **Challenge 4** — Contract & SOW Risk Analyzer | `challenge-4-contract-sow-risk-analyzer/` | CUAD, ContractNLI, LEDGAR |

> **Note:** Unrelated problem datasets are archived in the `ignore/` folder and are not part of this hackathon.

---

## Quick Start

```bash
# Clone the repository
git clone https://github.com/isshaad-ocean/Data_sets_hackathon.git
cd Data_sets_hackathon

# Pull large files (Git LFS)
git lfs install
git lfs pull

# Install Python tools
pip install datasets huggingface_hub kaggle
```

Then read [PARTICIPANTS_GUIDE.md](./PARTICIPANTS_GUIDE.md) for your specific challenge.

---

## Credential Requirements Summary

| Challenge | Kaggle API | Login Required |
|-----------|-----------|----------------|
| C1 — AI Agent Crypto Trading | Optional | ❌ None (Zenodo/CryptoDataDownload are free) |
| C2 — Network Anomaly Root-Cause | ✅ Required | Kaggle (NSL-KDD, UNSW-NB15) |
| C3 — Continuous KYC Auditor | ❌ Not needed | ❌ None |
| C4 — Contract & SOW Risk Analyzer | ❌ Not needed | ❌ None |

---

*Maintained for Hyderabad AI Hackathon 2026*
