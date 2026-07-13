# Participants Dataset Guide — Hyderabad AI Hackathon 2026

This guide explains exactly how to download and access datasets for each of the 4 challenge problem statements.
Follow only the section for your assigned challenge.

---

## One-Time Setup (Everyone)

### Step 1 — Clone the Repository
```bash
git clone https://github.com/isshaad-ocean/Data_sets_hackathon.git
cd Data_sets_hackathon
```

### Step 2 — Install Git LFS
```bash
git lfs install
git lfs pull
```

### Step 3 — Install Python Dependencies
```bash
pip install datasets huggingface_hub kaggle requests pandas
```

---

## Challenge Folders

| Challenge | Folder |
|-----------|--------|
| C1 — AI Agent Crypto Trading | `challenge-1-crypto-trading-agent/` |
| C2 — Network Anomaly Root-Cause | `challenge-2-network-anomaly-rca/` |
| C3 — Continuous KYC Auditor | `challenge-3-kyc-autonomous-auditor/` |
| C4 — Contract & SOW Risk | `challenge-4-contract-sow-risk-analyzer/` |

---

---

## Challenge 1 — AI Agent Creation Platform for Autonomous Crypto Trading

**Datasets:** Kraken OHLCV, CryptoSentiment (14 coins), Crypto News, Fear & Greed Index

### Prerequisites
| Requirement | Details |
|-------------|---------|
| None | Zenodo and CryptoDataDownload are free — no login required |
| Kaggle API | Optional — for additional Kaggle crypto datasets |

### Download Steps

```bash
cd challenge-1-crypto-trading-agent

# Option A — Zenodo CryptoSentiment (no login needed)
python -c "
import urllib.request, os
os.makedirs('data/sentiment', exist_ok=True)
urllib.request.urlretrieve(
    'https://zenodo.org/records/7684409/files/crypto_sentiment_dataset.zip',
    'data/sentiment/crypto_sentiment.zip'
)
print('Downloaded CryptoSentiment')
"

# Option B — Kraken OHLCV CSVs (no login needed)
# Visit: https://cryptodatadownload.com/data/kraken/
# Download BTC/USD, ETH/USD daily/hourly CSVs and place in data/ohlcv/

# Option C — Kaggle datasets (requires kaggle.json)
kaggle datasets download -d mczielinski/bitcoin-historical-data -p data/ohlcv/ --unzip
kaggle datasets download -d oliviervha/crypto-news -p data/sentiment/ --unzip
```

### What You Get
```
challenge-1-crypto-trading-agent/data/
├── ohlcv/
│   └── Kraken_BTCUSD_d.csv     → Daily OHLCV (timestamp, open, high, low, close, volume)
├── sentiment/
│   └── crypto_sentiment.zip    → 14-coin sentiment scores (FinBERT, date, score, source)
└── indicators/
    └── (generate via pandas-ta — see Quick Start below)
```

### Quick Start
```python
import pandas as pd
import pandas_ta as ta

# Load OHLCV
df = pd.read_csv("data/ohlcv/Kraken_BTCUSD_d.csv", skiprows=1)
df.columns = df.columns.str.lower()

# Add technical indicators
df.ta.rsi(append=True)       # Relative Strength Index
df.ta.macd(append=True)      # MACD
df.ta.bbands(append=True)    # Bollinger Bands

print(df.tail())
```

---

---

## Challenge 2 — Network Anomaly Root-Cause Assistant

**Datasets:** NSL-KDD, UNSW-NB15, LogHub (HDFS/BGL system logs)

### Prerequisites
| Requirement | Details |
|-------------|---------|
| Kaggle API | Required for NSL-KDD and UNSW-NB15 |

### Download Steps
```bash
cd challenge-2-network-anomaly-rca

# NSL-KDD — Kaggle required
kaggle datasets download -d hassan06/nslkdd -p data/nsl_kdd --unzip

# UNSW-NB15 — Kaggle required
kaggle datasets download -d dhoogla/unswnb15 -p data/unsw_nb15 --unzip

# LogHub — free via HuggingFace (no login)
python -c "
from datasets import load_dataset
ds = load_dataset('aioha/loghub', 'HDFS')
ds.save_to_disk('data/loghub/HDFS')
"
```

### What You Get
```
challenge-2-network-anomaly-rca/data/
├── nsl_kdd/
│   ├── KDDTrain+.txt          → 125K labeled network traffic records (41 features)
│   └── KDDTest+.txt           → Test set with attack labels
├── unsw_nb15/
│   └── UNSW_NB15_*.csv        → Network flows + attack category labels
└── loghub/
    ├── HDFS/HDFS.log          → Hadoop Distributed File System logs
    └── BGL/BGL.log            → BlueGene supercomputer system logs
```

### Quick Start
```python
import pandas as pd

# NSL-KDD
cols = ['duration','protocol_type','service','flag','src_bytes','dst_bytes',
        'land','wrong_fragment','urgent','hot','num_failed_logins','logged_in',
        'num_compromised','root_shell','su_attempted','num_root','num_file_creations',
        'num_shells','num_access_files','num_outbound_cmds','is_host_login',
        'is_guest_login','count','srv_count','serror_rate','srv_serror_rate',
        'rerror_rate','srv_rerror_rate','same_srv_rate','diff_srv_rate',
        'srv_diff_host_rate','dst_host_count','dst_host_srv_count',
        'dst_host_same_srv_rate','dst_host_diff_srv_rate','dst_host_same_src_port_rate',
        'dst_host_srv_diff_host_rate','dst_host_serror_rate','dst_host_srv_serror_rate',
        'dst_host_rerror_rate','dst_host_srv_rerror_rate','label','difficulty']
df = pd.read_csv("data/nsl_kdd/KDDTrain+.txt", names=cols)
print(df['label'].value_counts())
```

---

---

## Challenge 3 — Continuous KYC Autonomous Auditor

**Datasets:** OpenSanctions, OFAC SDN, EU Sanctions, EUR-Lex, PrivacyQA, GDPR Text, OPP-115

### Prerequisites
| Requirement | Details |
|-------------|---------|
| None | All datasets are freely available — no login required |

### Download Steps
```bash
cd challenge-3-kyc-autonomous-auditor

# OpenSanctions — 100+ government sanction lists (no login)
python -c "
import urllib.request, os
os.makedirs('data/sanctions', exist_ok=True)
urllib.request.urlretrieve(
    'https://data.opensanctions.org/datasets/latest/default/targets.simple.csv',
    'data/sanctions/opensanctions_targets.csv'
)
print('Downloaded OpenSanctions')
"

# OFAC SDN List — US Treasury (no login)
python -c "
import urllib.request
urllib.request.urlretrieve(
    'https://www.treasury.gov/ofac/downloads/sdn.csv',
    'data/sanctions/ofac_sdn.csv'
)
print('Downloaded OFAC SDN')
"

# EUR-Lex — HuggingFace (no login)
python -c "
from datasets import load_dataset
ds = load_dataset('coastalcph/lex_glue', 'eurlex')
ds.save_to_disk('data/eurlex')
"

# PrivacyQA — HuggingFace (no login)
python -c "
from datasets import load_dataset
ds = load_dataset('allenai/privacy_qa')
ds.save_to_disk('data/privacy_qa')
"

# GDPR Full Text — GitHub (no login)
python -c "
import urllib.request
urllib.request.urlretrieve(
    'https://raw.githubusercontent.com/nickmvincent/gdpr_text/master/gdpr.json',
    'data/gdpr_text/gdpr.json'
)
print('Downloaded GDPR text')
"
```

### What You Get
```
challenge-3-kyc-autonomous-auditor/data/
├── sanctions/
│   ├── opensanctions_targets.csv  → Entities from 100+ sanction lists (name, dob, nationality, program)
│   └── ofac_sdn.csv               → US Treasury Specially Designated Nationals list
├── eurlex/
│   └── *.parquet                  → 65K EU laws with EUROVOC classification labels
├── privacy_qa/
│   ├── train.json                 → 1,750 privacy policy Q&A pairs
│   └── test.json
├── gdpr_text/
│   └── gdpr.json                  → Full GDPR text, article-by-article (structured JSON)
└── opp115/
    └── annotations/               → 115 annotated privacy policies (10 practice categories)
```

### Quick Start
```python
import pandas as pd

# Load OpenSanctions
df = pd.read_csv("data/sanctions/opensanctions_targets.csv")
print(f"Total sanctioned entities: {len(df):,}")
print(df.columns.tolist())

# Search by name
hits = df[df['name'].str.contains('Al-Qaeda', case=False, na=False)]
print(hits[['name','nationality','program','datasets']])
```

---

---

## Challenge 4 — Contract & SOW Risk Analyzer

**Datasets:** CUAD (510 expert-annotated contracts), ContractNLI, LEDGAR (60k+ provisions)

### Prerequisites
| Requirement | Details |
|-------------|---------|
| None | All datasets available via HuggingFace — no login required |

### Download Steps
```bash
cd challenge-4-contract-sow-risk-analyzer

# CUAD — 510 contracts, 41 clause types (no login)
python -c "
from datasets import load_dataset
ds = load_dataset('theatricusproject/cuad')
ds.save_to_disk('data/cuad')
"

# ContractNLI — NDA clause entailment (no login)
python -c "
from datasets import load_dataset
ds = load_dataset('stanfordnlp/contract_nli')
ds.save_to_disk('data/contract_nli')
"

# LEDGAR — 60K+ contract provisions classified (no login)
python -c "
from datasets import load_dataset
ds = load_dataset('coastalcph/lex_glue', 'ledgar')
ds.save_to_disk('data/ledgar')
"
```

### What You Get
```
challenge-4-contract-sow-risk-analyzer/data/
├── cuad/
│   ├── train-*.parquet    → 510 contracts with 41 clause-type annotations
│   └── test-*.parquet     → Test split
├── contract_nli/
│   ├── train.json         → NDA clause hypothesis-label pairs
│   └── dev.json           → Validation (Entailment/Contradiction/NotMentioned)
└── ledgar/
    └── *.parquet          → 60K+ contract provisions with 83 category labels
```

### Quick Start
```python
from datasets import load_from_disk

# Load CUAD
ds = load_from_disk("data/cuad")
sample = ds['train'][0]
print("Contract:", sample['title'])
print("Clause types with annotations:", [k for k,v in sample.items() if v and k != 'title'])

# Load ContractNLI
import json
with open("data/contract_nli/train.json") as f:
    nli = json.load(f)
doc = list(nli['documents'].values())[0]
print("Hypotheses:", list(doc['annotation_sets'][0]['annotations'].keys())[:3])
```

---

## Common Issues

| Problem | Solution |
|---------|----------|
| `kaggle: command not found` | Run `pip install kaggle` |
| `401 Unauthorized` from Kaggle | Check `~/.kaggle/kaggle.json` is present |
| Large files missing after clone | Run `git lfs pull` |
| `ModuleNotFoundError: datasets` | Run `pip install datasets huggingface_hub` |
| OpenSanctions CSV encoding issues | Add `encoding='utf-8'` to `pd.read_csv()` |

---

*Hyderabad AI Hackathon 2026 — Participants Dataset Guide*
