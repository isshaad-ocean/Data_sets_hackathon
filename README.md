# Hackathon Datasets — Hyderabad AI Hackathon 2026

Datasets for all problem statements, organized by challenge.

---

## 📖 Start Here

| Document | Purpose |
|----------|---------|
| 📘 [PARTICIPANTS_GUIDE.md](./PARTICIPANTS_GUIDE.md) | **How to download & use datasets** — read this first |
| 📊 [DATASET_CATALOG.md](./DATASET_CATALOG.md) | All dataset sizes, licenses & credential requirements |

---

## Problem Folders

| Problem | Folder | Datasets Included |
|---------|--------|------------------|
| **1** | `problem-1-intelligent-document-processor/` | SROIE 2019, CORD v2, FUNSD, Invoice NER |
| **2** | `problem-2-conversational-analytics/` | Spider, WikiTableQuestions, Chinook DB |
| **3** | `problem-3-network-anomaly-detection/` | NSL-KDD, UNSW-NB15, LogHub |
| **4** | `problem-4-contract-risk-analyzer/` | CUAD, ContractNLI, LEDGAR |
| **5** | `problem-5-synthetic-data-generator/` | Adult Census, Credit Card Fraud, Diabetes |
| **6** | `problem-6-visual-inspection/` | MVTec AD, NEU Surface Defect, DAGM |
| **7** | `problem-7-misinformation-detector/` | LIAR, FEVER, FakeNewsNet |
| **8** | `problem-8-compliance-checker/` | EUR-Lex, PrivacyQA, GDPR Text, OPP-115 |

---

## Quick Start

```bash
# Clone (with submodules for Problem 1)
git clone --recurse-submodules https://github.com/isshaad-ocean/Data_sets_hackathon.git
cd Data_sets_hackathon

# Pull large files (Git LFS)
git lfs install
git lfs pull

# Install Python tools
pip install datasets huggingface_hub kaggle
```

Then read [PARTICIPANTS_GUIDE.md](./PARTICIPANTS_GUIDE.md) for your specific problem.

---

## Credential Requirements Summary

| Problem | Kaggle API | Git LFS | Other |
|---------|-----------|---------|-------|
| P1 — Intelligent Document Processor | ✅ Required | ✅ Required | Git submodule |
| P2 — Conversational Analytics | ❌ Not needed | ❌ Not needed | — |
| P3 — Network Anomaly Detection | ✅ Required | ❌ Not needed | — |
| P4 — Contract Risk Analyzer | ❌ Not needed | ❌ Not needed | — |
| P5 — Synthetic Data Generator | ✅ Required | ❌ Not needed | — |
| P6 — Visual Inspection | ✅ Required | ❌ Not needed | — |
| P7 — Misinformation Detector | ❌ Not needed | ❌ Not needed | — |
| P8 — Compliance Checker | ❌ Not needed | ❌ Not needed | — |

---

*Maintained for Hyderabad AI Hackathon 2026*
