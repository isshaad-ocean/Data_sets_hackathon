# Problem 1 — Intelligent Document Processor (Human-in-the-Loop)

> **Core deliverable**: A pipeline that extracts key fields from business documents (invoices, POs, claims forms),
> auto-processes high-confidence extractions, and routes anything below a confidence threshold to a human review queue.

---

## Datasets Overview

| # | Dataset | Source | Size | License | Purpose |
|---|---------|--------|------|---------|---------|
| 1 | **SROIE 2019** | [GitHub (ICDAR)](https://github.com/zzzDavid/ICDAR-2019-SROIE) | ~200 MB | Research use | Receipt OCR + key-value extraction |
| 2 | **CORD v2** | [HuggingFace](https://huggingface.co/datasets/naver-clova-ix/cord-v2) | ~1–2 GB | CC BY 4.0 | Structured receipt parsing (JSON) |
| 3 | **FUNSD** | [Official Site](https://guillaumejaume.github.io/FUNSD/) | ~50 MB | Research use | Scanned form understanding + NER |
| 4 | **Invoice NER** | [Kaggle](https://www.kaggle.com/datasets/nikitpatel/invoice-ner-dataset) | ~5 MB | Open | Invoice text → structured JSON |

---

## Dataset Details

### 1. SROIE 2019 (`data/sroie/`)
- **Full name**: Scanned Receipts OCR and Information Extraction (ICDAR 2019)
- **Size**: ~1,000 receipt images (200 MB)
- **Fields**: `company`, `date`, `address`, `total` + bounding box annotations + OCR text
- **Tasks**: Text localization, OCR, key information extraction
- **Format**: `.jpg` images + `.txt` annotation files
- **License**: Research / academic use only

### 2. CORD v2 (`data/cord/`)
- **Full name**: Consolidated Receipt Dataset v2 (NAVER CLOVA)
- **Size**: ~11,000 Indonesian receipt images
- **Fields**: `menu.name`, `menu.price`, `menu.count`, `sub_total`, `total`, `tax`, `void_menu`
- **Labels**: 5 superclasses, 42 subclass semantic labels
- **Format**: HuggingFace `datasets` format (Parquet + JSON metadata)
- **License**: Creative Commons BY 4.0

### 3. FUNSD (`data/funsd/`)
- **Full name**: Form Understanding in Noisy Scanned Documents
- **Size**: 199 annotated scanned forms (~50 MB)
- **Fields**: Entity labels (`header`, `question`, `answer`, `other`), key-value linking
- **Format**: `.png` images + `.json` annotations per form
- **License**: Research use (subset of RVL-CDIP)

### 4. Invoice NER (`data/invoice_ner/`)
- **Full name**: Invoice NER Dataset
- **Size**: ~5 MB (CSV/JSON)
- **Fields**: `vendor_name`, `invoice_date`, `invoice_number`, `line_items`, `total_amount`, `tax`
- **Format**: CSV or JSON with NER-tagged invoice text
- **License**: Open (Kaggle community)

---

## Folder Structure

```
problem-1-intelligent-document-processor/
├── data/
│   ├── sroie/
│   │   ├── 0325671932/         ← sample receipt folder
│   │   │   ├── 0325671932.jpg
│   │   │   ├── 0325671932.txt  ← OCR ground truth
│   │   │   └── ...
│   │   └── ...
│   ├── cord/
│   │   ├── dataset_dict.json
│   │   ├── train/
│   │   ├── validation/
│   │   └── test/
│   ├── funsd/
│   │   ├── training_data/
│   │   │   ├── annotated_jsons/
│   │   │   └── images/
│   │   └── testing_data/
│   │       ├── annotated_jsons/
│   │       └── images/
│   └── invoice_ner/
│       └── invoice_ner.csv    ← or .json
├── download.sh
├── download.ps1
└── README.md                  ← This file
```

---

## How to Download

### Prerequisites
```bash
pip install datasets kaggle huggingface_hub
```
For Kaggle: place your `kaggle.json` at `~/.kaggle/kaggle.json`

### Linux / Mac / WSL
```bash
bash download.sh
```

### Windows PowerShell
```powershell
.\download.ps1
```
