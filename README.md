# Hackathon Datasets — Hyderabad AI Hackathon 2026

This repository contains curated datasets organized by **problem statement** for the Hyderabad AI Hackathon.  
Each folder is self-contained with its own `README.md` and download scripts.

---

## Problem Statements

| # | Folder | Problem | Status |
|---|--------|---------|--------|
| 1 | [`problem-1-intelligent-document-processor/`](./problem-1-intelligent-document-processor/) | Intelligent Document Processor (Human-in-the-Loop) | ✅ Ready |

> More problem statements will be added here as they are finalized.

---

## How to Use

### Clone the repo
```bash
git clone https://github.com/isshaad-ocean/Data_sets_hackathon.git
cd Data_sets_hackathon
git lfs pull   # Download large files tracked by Git LFS
```

### Download datasets for a specific problem
```bash
# Linux / Mac / WSL
cd problem-1-intelligent-document-processor
bash download.sh

# Windows PowerShell
cd problem-1-intelligent-document-processor
.\download.ps1
```

---

## Repository Structure

```
hackathon-datasets/
├── problem-1-intelligent-document-processor/
│   ├── data/
│   │   ├── sroie/           ← ICDAR 2019 SROIE (invoices/receipts)
│   │   ├── cord/            ← CORD v2 (structured receipt JSON)
│   │   ├── funsd/           ← FUNSD (scanned forms)
│   │   └── invoice_ner/     ← Invoice NER (text → JSON)
│   ├── download.sh
│   ├── download.ps1
│   └── README.md
├── .gitattributes           ← Git LFS rules
├── .gitignore
└── README.md                ← This file
```

---

## Notes
- Large binary files (images, parquets) are tracked via **Git LFS**.
- Raw dataset archives (`.zip`, `.tar.gz`) are excluded from git — use the download scripts.
- Kaggle datasets require a `~/.kaggle/kaggle.json` API token.

---

*Maintained by Team — Hyderabad Hackathon 2026*
