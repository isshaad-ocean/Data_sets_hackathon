# 🚀 Participants Dataset Guide — Hyderabad AI Hackathon 2026

This guide explains **exactly how to download and access datasets** for each problem statement.
Follow only the section for your assigned problem.

---

## ⚙️ One-Time Setup (Do This First — Everyone)

### Step 1 — Clone the Repository
```bash
# Clone with submodules (required for Problem 1 SROIE dataset)
git clone --recurse-submodules https://github.com/isshaad-ocean/Data_sets_hackathon.git
cd Data_sets_hackathon
```

### Step 2 — Install Git LFS (required for large binary files)
```bash
# Install Git LFS
git lfs install
git lfs pull    # Download large files tracked by LFS
```

### Step 3 — Install Python dependencies
```bash
pip install datasets huggingface_hub kaggle
```

---

## 📁 Problem Folders

| Problem | Folder Name |
|---------|-------------|
| 1 | `problem-1-intelligent-document-processor/` |
| 2 | `problem-2-conversational-analytics/` |
| 3 | `problem-3-network-anomaly-detection/` |
| 4 | `problem-4-contract-risk-analyzer/` |
| 5 | `problem-5-synthetic-data-generator/` |
| 6 | `problem-6-visual-inspection/` |
| 7 | `problem-7-misinformation-detector/` |
| 8 | `problem-8-compliance-checker/` |

---

---

## 🔖 Problem 1 — Intelligent Document Processor

**Datasets:** SROIE 2019, CORD v2, FUNSD, Invoice NER

### Prerequisites
| Requirement | Details |
|-------------|---------|
| Git LFS | Required for CORD v2 (2.2 GB) |
| Kaggle API | Required for Invoice NER |

### Download Steps

**Option A — Windows PowerShell**
```powershell
cd problem-1-intelligent-document-processor
.\download.ps1
```

**Option B — Linux / Mac / WSL**
```bash
cd problem-1-intelligent-document-processor
bash download.sh
```

**Option C — Manual (dataset by dataset)**
```bash
# SROIE 2019 (already in repo as submodule)
git submodule update --init --recursive

# CORD v2 (Git LFS — auto-downloaded on clone)
git lfs pull

# FUNSD (already in repo)
ls data/funsd/dataset/

# Invoice NER (Kaggle required)
kaggle datasets download -d nikitpatel/invoice-ner-dataset \
  -p data/invoice_ner --unzip
```

### What You Get
```
data/
├── sroie/          → 1,000 receipt images + OCR .txt annotations
├── cord/           → 11K receipts as .arrow parquet files
├── funsd/dataset/
│   ├── training_data/annotations/*.json
│   └── training_data/images/*.png
└── invoice_ner/
    └── converted_invoice_dataset.xlsx
```

### Kaggle Setup
1. Go to https://www.kaggle.com/settings → API → **Create New Token**
2. Move downloaded file: `mv ~/Downloads/kaggle.json ~/.kaggle/kaggle.json`
3. On Windows: `Move-Item "$env:USERPROFILE\Downloads\kaggle.json" "$env:USERPROFILE\.kaggle\kaggle.json"`

---

---

## 🔖 Problem 2 — Conversational Analytics

**Datasets:** Spider 1.0 (Text-to-SQL), WikiTableQuestions, Chinook SQLite DB

### Prerequisites
| Requirement | Details |
|-------------|---------|
| None | All datasets are freely accessible — no login required |

### Download Steps
```bash
cd problem-2-conversational-analytics

# All datasets are already in the repo — just use them directly!
ls data/spider/             # Spider text-to-SQL benchmark
ls data/wikitablequestions/ # NL questions over tables
ls data/chinook/            # Chinook business SQLite database
```

### What You Get
```
data/
├── spider/
│   ├── train_spider.json   → Training NL-SQL pairs
│   ├── dev.json            → Validation set
│   └── tables.json         → DB schema definitions
├── wikitablequestions/
│   └── *.tsv               → Questions + table data
└── chinook/
    └── Chinook_Sqlite.sqlite → Ready-to-query SQLite business DB
```

### Quick Start — Query the Chinook DB
```python
import sqlite3
conn = sqlite3.connect("data/chinook/Chinook_Sqlite.sqlite")
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
print("Tables:", cursor.fetchall())
```

---

---

## 🔖 Problem 3 — Network Anomaly Detection

**Datasets:** NSL-KDD, UNSW-NB15, LogHub (HDFS/BGL system logs)

### Prerequisites
| Requirement | Details |
|-------------|---------|
| Kaggle API | Required for NSL-KDD and UNSW-NB15 |

### Download Steps
```bash
cd problem-3-network-anomaly-detection

# Kaggle datasets — run after setting up kaggle.json
kaggle datasets download -d hassan06/nslkdd -p data/nsl_kdd --unzip
kaggle datasets download -d dhoogla/unswnb15 -p data/unsw_nb15 --unzip

# LogHub logs — already in repo
ls data/loghub/
```

### What You Get
```
data/
├── nsl_kdd/
│   ├── KDDTrain+.txt       → Training network traffic (labeled)
│   └── KDDTest+.txt        → Test set
├── unsw_nb15/
│   └── UNSW_NB15_*.csv     → Network flow features + attack labels
└── loghub/
    ├── HDFS/HDFS.log       → Hadoop system logs
    └── BGL/BGL.log         → BlueGene supercomputer logs
```

### Quick Start
```python
import pandas as pd
df = pd.read_csv("data/nsl_kdd/KDDTrain+.txt", header=None)
print(df.shape)  # (125,973, 43) — 43 network features
```

---

---

## 🔖 Problem 4 — Contract & SOW Risk Analyzer

**Datasets:** CUAD (510 expert-annotated contracts), ContractNLI, LEDGAR

### Prerequisites
| Requirement | Details |
|-------------|---------|
| None | All datasets already in repo — no login required |

### Download Steps
```bash
cd problem-4-contract-risk-analyzer

# All datasets already downloaded — use directly
ls data/cuad/            # 510 contracts, 41 clause types
ls data/contract_nli/    # NDA entailment dataset
ls data/ledgar/          # Clause classification (SEC filings)
```

### What You Get
```
data/
├── cuad/
│   ├── train-*.parquet     → Contract text + clause annotations
│   └── test-*.parquet
├── contract_nli/
│   ├── train.json          → Hypothesis-premise NLI pairs
│   └── dev.json
└── ledgar/
    └── *.parquet           → Contract clauses + labels
```

### Quick Start
```python
import pandas as pd
df = pd.read_parquet("data/cuad/", engine="pyarrow")
print(df.columns.tolist())   # Shows all 41 clause-type columns
print(f"Contracts: {df['id'].nunique()}")
```

---

---

## 🔖 Problem 5 — Privacy-Safe Synthetic Data Generator

**Datasets:** Adult Census Income, Credit Card Fraud, Diabetes (PIMA)

### Prerequisites
| Requirement | Details |
|-------------|---------|
| Kaggle API | Required for Credit Card Fraud and Diabetes datasets |

### Download Steps
```bash
cd problem-5-synthetic-data-generator

# Adult Census — already in repo (UCI direct download)
ls data/adult_census/

# Credit Card Fraud — Kaggle required
kaggle datasets download -d mlg-ulb/creditcardfraud \
  -p data/credit_card_fraud --unzip

# Diabetes PIMA — Kaggle required
kaggle datasets download -d uciml/pima-indians-diabetes-database \
  -p data/diabetes --unzip
```

### What You Get
```
data/
├── adult_census/
│   ├── adult.data          → 32,561 training records (14 features)
│   ├── adult.test          → 16,281 test records
│   └── adult.names         → Column descriptions
├── credit_card_fraud/
│   └── creditcard.csv      → 284,807 transactions (31 features, 0.17% fraud)
└── diabetes/
    └── diabetes.csv        → 768 patient records (8 features)
```

### Quick Start
```python
import pandas as pd

# Load Adult Census
cols = ['age','workclass','fnlwgt','education','education-num',
        'marital-status','occupation','relationship','race','sex',
        'capital-gain','capital-loss','hours-per-week','native-country','income']
df = pd.read_csv("data/adult_census/adult.data", names=cols, na_values=' ?')
print(df.head())
```

---

---

## 🔖 Problem 6 — Explainable Visual Inspection

**Datasets:** MVTec AD, NEU Surface Defect Database, DAGM 2007

### Prerequisites
| Requirement | Details |
|-------------|---------|
| Kaggle API | Required for NEU Defect and DAGM datasets |
| HuggingFace | MVTec AD can be downloaded via HuggingFace (free, no login for public version) |

### Download Steps
```bash
cd problem-6-visual-inspection

# NEU Surface Defect — Kaggle required
kaggle datasets download \
  -d kaustubhdikshit/neu-surface-defect-database \
  -p data/neu_defect --unzip

# DAGM 2007 — Kaggle required
kaggle datasets download -d mhkhan27/dagm2007 \
  -p data/dagm --unzip

# MVTec AD — Large (~5GB), HuggingFace
python -c "
from huggingface_hub import snapshot_download
snapshot_download(
    repo_id='Bingsu/mvtec_anomaly_detection',
    repo_type='dataset',
    local_dir='data/mvtec'
)
"
```

### What You Get
```
data/
├── neu_defect/
│   ├── train/              → 6 defect types (crazing, inclusion, patches, etc.)
│   └── test/
├── dagm/
│   └── Class*/             → Textured surface images + weak labels
└── mvtec/                  → 15 categories (bottle, cable, carpet...)
    ├── bottle/
    │   ├── train/good/     → Defect-free training images
    │   └── test/           → Test images (good + defective)
    └── ...
```

---

---

## 🔖 Problem 7 — Misinformation Detector

**Datasets:** LIAR, FEVER, FakeNewsNet

### Prerequisites
| Requirement | Details |
|-------------|---------|
| None | All datasets already in repo — no login required |

### Download Steps
```bash
cd problem-7-misinformation-detector

# All datasets already in the repo — use directly!
ls data/liar/           # LIAR labeled statements
ls data/fever/          # FEVER claim verification
ls data/fakenewsnet/    # FakeNewsNet metadata
ls data/fake_news_kaggle/  # Additional fake news dataset
```

### What You Get
```
data/
├── liar/
│   ├── train.tsv       → 10,269 political statements (6 labels)
│   ├── valid.tsv       → 1,284 validation statements
│   └── test.tsv        → 1,267 test statements
├── fever/
│   ├── train.jsonl     → 145,449 claims + evidence (SUPPORTS/REFUTES/NEI)
│   ├── dev.jsonl       → 19,998 dev claims
│   └── test.jsonl      → 19,998 test claims
└── fakenewsnet/
    ├── politifact/     → Real/fake political news metadata
    └── gossipcop/      → Real/fake celebrity news metadata
```

### LIAR Label Key
| Label | Meaning |
|-------|---------|
| true | Completely true |
| mostly-true | Mostly accurate |
| half-true | Partially true |
| barely-true | Mostly inaccurate |
| false | Completely false |
| pants-fire | Blatantly false |

### Quick Start
```python
import pandas as pd
cols = ['id','label','statement','subject','speaker','job',
        'state','party','barely_true','false','half_true',
        'mostly_true','pants_fire','context']
df = pd.read_csv("data/liar/train.tsv", sep="\t", names=cols)
print(df['label'].value_counts())
```

---

---

## 🔖 Problem 8 — Compliance & Policy Conformance Checker

**Datasets:** EUR-Lex (EU Legislation), PrivacyQA, GDPR Text, OPP-115 Privacy Policies

### Prerequisites
| Requirement | Details |
|-------------|---------|
| None | All datasets already in repo — no login required |

### Download Steps
```bash
cd problem-8-compliance-checker

# All datasets already in the repo — use directly!
ls data/eurlex/         # EU legislative documents
ls data/privacy_qa/    # Privacy policy Q&A
ls data/gdpr_text/     # GDPR full text (structured JSON)
ls data/opp115/        # 115 annotated privacy policies
```

### What You Get
```
data/
├── eurlex/
│   └── *.parquet       → 65K EU laws with EUROVOC classification labels
├── privacy_qa/
│   ├── train.json      → 1,750 privacy policy Q&A pairs
│   └── test.json
├── gdpr_text/
│   └── gdpr.json       → Full GDPR text, article-by-article (structured)
└── opp115/
    └── annotations/    → 115 privacy policies with 10 practice categories
```

### Quick Start
```python
import json

# Load GDPR structured text
with open("data/gdpr_text/gdpr.json") as f:
    gdpr = json.load(f)

# Access a specific article
article_5 = gdpr['articles']['5']
print(article_5['title'])
print(article_5['text'][:500])
```

---

## ❓ Common Issues

| Problem | Solution |
|---------|---------|
| `kaggle: command not found` | Run `pip install kaggle` |
| `401 Unauthorized` from Kaggle | Check `~/.kaggle/kaggle.json` is present |
| Large files missing after clone | Run `git lfs pull` |
| Submodule empty (SROIE) | Run `git submodule update --init --recursive` |
| `ModuleNotFoundError: datasets` | Run `pip install datasets huggingface_hub` |

---

*Hyderabad AI Hackathon 2026 — Dataset Guide*
