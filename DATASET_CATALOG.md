# 📊 Dataset Catalog — Hyderabad AI Hackathon 2026

Complete reference for all datasets across all problem statements.
Includes file sizes, licenses, and what credentials are required.

---

## 🔑 Credentials Required — At a Glance

| Credential | Problems Affected | How to Get |
|-----------|------------------|-----------|
| **Kaggle API Key** | P1, P3, P5, P6 | https://www.kaggle.com/settings → API → Create New Token |
| **Git LFS** | P1 (CORD v2) | `git lfs install` then `git lfs pull` |
| **Git submodule** | P1 (SROIE) | `git submodule update --init --recursive` |
| ❌ No credential | P2, P4, P7, P8 | Just clone and use! |

---

## Problem 1 — Intelligent Document Processor

| Dataset | Format | Size | License | Credential | Source |
|---------|--------|------|---------|-----------|--------|
| **SROIE 2019** | JPG + TXT | 349 MB | Research only | Git submodule | [GitHub](https://github.com/zzzDavid/ICDAR-2019-SROIE) |
| **CORD v2** | Parquet (.arrow) | 2,211 MB | CC-BY 4.0 | Git LFS | [HuggingFace](https://huggingface.co/datasets/naver-clova-ix/cord-v2) |
| **FUNSD** | PNG + JSON | 27 MB | Research only | None | [Official Site](https://guillaumejaume.github.io/FUNSD/) |
| **Invoice NER** | XLSX | 0.02 MB | CC-BY-NC-SA-4.0 | ✅ Kaggle | [Kaggle](https://www.kaggle.com/datasets/nikitpatel/invoice-ner-dataset) |
| **Total** | | **~2,587 MB** | | | |

**Key Fields:**
- SROIE: `company`, `date`, `address`, `total` + bounding boxes
- CORD: `menu.name`, `menu.price`, `sub_total`, `total`, `tax` (42 labels)
- FUNSD: `entity_type` (header/question/answer/other), `linking` (key→value pairs)
- Invoice NER: `vendor_name`, `invoice_date`, `invoice_number`, `line_items`, `total_amount`

---

## Problem 2 — Conversational Analytics

| Dataset | Format | Size | License | Credential | Source |
|---------|--------|------|---------|-----------|--------|
| **Spider 1.0** | JSON | ~70 MB | CC-BY-SA 4.0 | ❌ None | [HuggingFace](https://huggingface.co/datasets/xlangai/spider) |
| **WikiTableQuestions** | TSV | ~50 MB | CC-BY-SA 4.0 | ❌ None | [HuggingFace](https://huggingface.co/datasets/wikitablequestions) |
| **Chinook SQLite DB** | SQLite | 1 MB | Open | ❌ None | [GitHub](https://github.com/lerocha/chinook-database) |
| **Total** | | **~121 MB** | | | |

**Key Fields:**
- Spider: `question` (NL), `query` (SQL), `db_id`, `db_schema`
- WikiTableQuestions: `question`, `answers`, `table` (Wikipedia HTML table)
- Chinook: 11 tables — `Artist`, `Album`, `Track`, `Invoice`, `Customer`, `Employee`

> 💡 **No credentials needed — best for beginners!**

---

## Problem 3 — Network Anomaly Detection

| Dataset | Format | Size | License | Credential | Source |
|---------|--------|------|---------|-----------|--------|
| **NSL-KDD** | TXT/CSV | 7 MB | Open | ✅ Kaggle | [Kaggle](https://www.kaggle.com/datasets/hassan06/nslkdd) |
| **UNSW-NB15** | CSV | 113 MB | CC-BY-NC-SA 4.0 | ✅ Kaggle | [Kaggle](https://www.kaggle.com/datasets/dhoogla/unswnb15) |
| **LogHub (HDFS+BGL)** | LOG | ~170 MB | Open | ❌ None | [HuggingFace](https://huggingface.co/datasets/aioha/loghub) |
| **Total** | | **~290 MB** | | | |

**Key Fields:**
- NSL-KDD: 41 network features, `attack_type` label (DoS/Probe/R2L/U2R/Normal)
- UNSW-NB15: `srcip`, `dstip`, `proto`, `service`, `state`, `label`, `attack_cat`
- LogHub: Raw log lines with `Timestamp`, `EventId`, `Label` (Normal/Anomaly)

---

## Problem 4 — Contract & SOW Risk Analyzer

| Dataset | Format | Size | License | Credential | Source |
|---------|--------|------|---------|-----------|--------|
| **CUAD** | Parquet + JSON | 300 MB | CC-BY 4.0 | ❌ None | [HuggingFace](https://huggingface.co/datasets/theatticusproject/cuad) |
| **ContractNLI** | JSON | 5 MB | CC-BY-SA 4.0 | ❌ None | [HuggingFace](https://huggingface.co/datasets/stanfordnlp/contract_nli) |
| **LEDGAR (LexGLUE)** | Parquet | 447 MB | CC-BY 4.0 | ❌ None | [HuggingFace](https://huggingface.co/datasets/coastalcph/lex_glue) |
| **Total** | | **~752 MB** | | | |

**Key Fields:**
- CUAD: 41 clause categories (Governing Law, Indemnification, IP Rights, Termination, etc.)
- ContractNLI: `hypothesis` (clause claim), `label` (Entailment/Contradiction/NotMentioned)
- LEDGAR: `provision` (clause text), `label` (83 clause type categories)

> 💡 **No credentials needed — best for legal AI work!**

---

## Problem 5 — Privacy-Safe Synthetic Data Generator

| Dataset | Format | Size | License | Credential | Source |
|---------|--------|------|---------|-----------|--------|
| **Adult Census Income** | CSV | 4 MB | Public Domain | ❌ None | [UCI ML Repo](https://archive.ics.uci.edu/ml/datasets/adult) |
| **Credit Card Fraud** | CSV | 144 MB | DbCL-1.0 | ✅ Kaggle | [Kaggle](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud) |
| **Diabetes (PIMA)** | CSV | 0.02 MB | CC0 1.0 | ✅ Kaggle | [Kaggle](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database) |
| **Total** | | **~148 MB** | | | |

**Key Fields:**
- Adult Census: 14 features — `age`, `education`, `occupation`, `income` (>50K or ≤50K)
- Credit Card: `Time`, `V1-V28` (PCA anonymized), `Amount`, `Class` (0=normal, 1=fraud)
- Diabetes: `Pregnancies`, `Glucose`, `BloodPressure`, `BMI`, `Outcome` (0/1)

---

## Problem 6 — Explainable Visual Inspection

| Dataset | Format | Size | License | Credential | Source |
|---------|--------|------|---------|-----------|--------|
| **MVTec AD** | PNG (high-res) | ~5,000 MB | CC-BY-NC-SA 4.0 | ❌ None (HF) | [HuggingFace](https://huggingface.co/datasets/Bingsu/mvtec_anomaly_detection) |
| **NEU Surface Defect** | BMP | ~50 MB | Research only | ✅ Kaggle | [Kaggle](https://www.kaggle.com/datasets/kaustubhdikshit/neu-surface-defect-database) |
| **DAGM 2007** | PNG | ~130 MB | Research only | ✅ Kaggle | [Kaggle](https://www.kaggle.com/datasets/mhkhan27/dagm2007) |
| **Total** | | **~5,180 MB** | | | |

**Key Fields:**
- MVTec AD: 15 categories × `train/good/` + `test/{defect_type}/` + pixel masks
- NEU: 6 defect types — `crazing`, `inclusion`, `patches`, `pitted_surface`, `rolled-in_scale`, `scratches`
- DAGM: 10 texture classes, each with Normal + Defective images + weak labels

> ⚠️ **MVTec AD is ~5 GB** — download only what you need (select specific categories)

---

## Problem 7 — Misinformation Detector

| Dataset | Format | Size | License | Credential | Source |
|---------|--------|------|---------|-----------|--------|
| **LIAR** | TSV | 3 MB | Research only | ❌ None | [UCSB](https://www.cs.ucsb.edu/~william/data/liar_dataset.zip) |
| **FEVER** | JSONL | 60 MB | CC-BY-SA 4.0 | ❌ None | [fever.ai](https://fever.ai/dataset/fever.html) |
| **FakeNewsNet** | JSON + metadata | ~20 MB | Research only | ❌ None | [GitHub](https://github.com/KaiDMML/FakeNewsNet) |
| **Fake News (Kaggle)** | CSV | ~1 MB | Open | ✅ Kaggle | [Kaggle](https://www.kaggle.com/datasets/therealsampat/fake-news-detection) |
| **Total** | | **~84 MB** | | | |

**Key Fields:**
- LIAR: `label` (6 veracity levels), `statement`, `speaker`, `subject`, `party`, `context`
- FEVER: `claim`, `label` (SUPPORTS/REFUTES/NOT ENOUGH INFO), `evidence` (Wikipedia sentences)
- FakeNewsNet: `title`, `content_url`, `label` (real/fake), social engagement counts

> 💡 **Mostly no credentials needed — great starting point!**

---

## Problem 8 — Compliance & Policy Conformance Checker

| Dataset | Format | Size | License | Credential | Source |
|---------|--------|------|---------|-----------|--------|
| **EUR-Lex (LexGLUE)** | Parquet | 600 MB | CC-BY 4.0 | ❌ None | [HuggingFace](https://huggingface.co/datasets/coastalcph/lex_glue) |
| **PrivacyQA** | JSON | 5 MB | CC-BY 4.0 | ❌ None | [HuggingFace](https://huggingface.co/datasets/allenai/privacy_qa) |
| **GDPR Text** | JSON | <1 MB | Public Domain | ❌ None | [GitHub](https://github.com/nickmvincent/gdpr_text) |
| **OPP-115** | JSON/CSV | ~10 MB | CC-BY 4.0 | ❌ None | [GitHub](https://github.com/citp/privacy-policy-annotated) |
| **Total** | | **~616 MB** | | | |

**Key Fields:**
- EUR-Lex: `text` (EU legal document), `labels` (EUROVOC concepts, multi-label)
- PrivacyQA: `question`, `segment` (policy text), `label` (Relevant/Irrelevant)
- GDPR: Article number, title, full text — structured by chapter/section
- OPP-115: `policy_text`, `practice_category` (10 types: Data Collection, Data Retention, etc.)

> 💡 **No credentials needed — all free!**

---

## 🗂️ Grand Summary

| Problem | Total Size | Kaggle Needed | HF Login | Git LFS | Submodule |
|---------|-----------|--------------|---------|---------|----------|
| P1 — Intelligent Document Processor | ~2,587 MB | ✅ Yes | ❌ No | ✅ Yes | ✅ Yes |
| P2 — Conversational Analytics | ~121 MB | ❌ No | ❌ No | ❌ No | ❌ No |
| P3 — Network Anomaly Detection | ~290 MB | ✅ Yes | ❌ No | ❌ No | ❌ No |
| P4 — Contract Risk Analyzer | ~752 MB | ❌ No | ❌ No | ❌ No | ❌ No |
| P5 — Synthetic Data Generator | ~148 MB | ✅ Yes | ❌ No | ❌ No | ❌ No |
| P6 — Visual Inspection | ~5,180 MB | ✅ Yes | ❌ No | ❌ No | ❌ No |
| P7 — Misinformation Detector | ~84 MB | ❌ No | ❌ No | ❌ No | ❌ No |
| P8 — Compliance Checker | ~616 MB | ❌ No | ❌ No | ❌ No | ❌ No |

---

## 🔑 Kaggle API Setup (One-Time)

1. Go to **https://www.kaggle.com/settings**
2. Scroll to **API** section → click **"Create New API Token"**
3. A file `kaggle.json` downloads to your computer
4. Move it to the right place:

**Linux / Mac / WSL:**
```bash
mkdir -p ~/.kaggle
mv ~/Downloads/kaggle.json ~/.kaggle/kaggle.json
chmod 600 ~/.kaggle/kaggle.json
```

**Windows PowerShell:**
```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.kaggle"
Move-Item "$env:USERPROFILE\Downloads\kaggle.json" "$env:USERPROFILE\.kaggle\kaggle.json"
```

5. Verify: `kaggle datasets list`

---

*Hyderabad AI Hackathon 2026 — Dataset Catalog*
