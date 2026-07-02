# 🗃️ Dataset Sources & Size Summary

This document provides a comprehensive overview of all datasets used across the 8 hackathon problem statements, including their original sources, the extracted file sizes, and the compressed zip sizes.

---

## 📊 Size Overview by Problem

| Problem | Extracted Data Size | Zip File Size | Zip File Name |
|---------|---------------------|---------------|---------------|
| **Problem 1** (Intelligent Document Processor) | ~2,865 MB | *N/A (Too large for GitHub LFS)* | Handled via `git clone` & download scripts |
| **Problem 2** (Conversational Analytics) | ~2 MB | ~1 MB | `p2-conversational-analytics-datasets.zip` |
| **Problem 3** (Network Anomaly Detection) | ~120 MB | ~24 MB | `p3-network-anomaly-detection-datasets.zip` |
| **Problem 4** (Contract Risk Analyzer) | ~752 MB | ~638 MB | `p4-contract-risk-analyzer-datasets.zip` |
| **Problem 5** (Synthetic Data Generator) | ~150 MB | ~66 MB | `p5-synthetic-data-generator-datasets.zip` |
| **Problem 6** (Explainable Visual Inspection) | ~27 MB* | ~26 MB* | `p6-visual-inspection-datasets.zip` |
| **Problem 7** (Misinformation Detector) | ~101 MB | ~29 MB | `p7-misinformation-detector-datasets.zip` |
| **Problem 8** (Compliance Checker) | ~630 MB | ~489 MB | `p8-compliance-checker-datasets.zip` |

*\*Note: Problem 6 excludes the optional 5GB MVTec AD dataset which participants can download dynamically via the HuggingFace script provided in the participant guide.*

---

## 🌐 Dataset Download Sources

Below are the exact original sources where all the data was downloaded from. 

### Problem 1 — Intelligent Document Processor
- **SROIE 2019**: GitHub repository (`https://github.com/zzzDavid/ICDAR-2019-SROIE`)
- **CORD v2**: Hugging Face Datasets (`naver-clova-ix/cord-v2`)
- **FUNSD**: Official Direct Download (`https://guillaumejaume.github.io/FUNSD/dataset.zip`)
- **Invoice NER**: Kaggle (`nikitpatel/invoice-ner-dataset`)

### Problem 2 — Conversational Analytics
- **Spider 1.0**: Hugging Face Datasets (`xlangai/spider`)
- **WikiTableQuestions**: Hugging Face Datasets (`wikitablequestions`)
- **Chinook SQLite DB**: GitHub repository (`https://github.com/lerocha/chinook-database/raw/master/ChinookDatabase/DataSources/Chinook_Sqlite.sqlite`)

### Problem 3 — Network Anomaly Detection
- **NSL-KDD**: Kaggle (`hassan06/nslkdd`)
- **UNSW-NB15**: Kaggle (`dhoogla/unswnb15`)
- **LogHub (HDFS/BGL)**: Hugging Face Datasets (`aioha/loghub`)

### Problem 4 — Contract & SOW Risk Analyzer
- **CUAD**: Hugging Face Datasets (`theatticusproject/cuad`)
- **ContractNLI**: Hugging Face Datasets (`stanfordnlp/contract_nli`)
- **LEDGAR (LexGLUE)**: Hugging Face Datasets (`coastalcph/lex_glue`)

### Problem 5 — Privacy-Safe Synthetic Data Generator
- **Adult Census Income**: UCI Machine Learning Repository (`https://archive.ics.uci.edu/ml/machine-learning-databases/adult/`)
- **Credit Card Fraud**: Kaggle (`mlg-ulb/creditcardfraud`)
- **Diabetes (PIMA)**: Kaggle (`uciml/pima-indians-diabetes-database`)

### Problem 6 — Explainable Visual Inspection
- **MVTec AD**: Hugging Face Datasets (`Bingsu/mvtec_anomaly_detection`)
- **NEU Surface Defect**: Kaggle (`kaustubhdikshit/neu-surface-defect-database`)
- **DAGM 2007**: Kaggle (`mhkhan27/dagm2007`)

### Problem 7 — Misinformation Detector
- **LIAR**: UCSB Direct Download (`https://www.cs.ucsb.edu/~william/data/liar_dataset.zip`)
- **FEVER**: Official AWS S3 bucket (`https://s3-eu-west-1.amazonaws.com/fever.public/`)
- **FakeNewsNet**: GitHub repository (`https://github.com/KaiDMML/FakeNewsNet`)
- **Fake News (Kaggle)**: Kaggle (`therealsampat/fake-news-detection`)

### Problem 8 — Compliance & Policy Conformance Checker
- **EUR-Lex (LexGLUE)**: Hugging Face Datasets (`coastalcph/lex_glue`)
- **PrivacyQA**: Hugging Face Datasets (`allenai/privacy_qa`)
- **GDPR Text**: GitHub repository (`https://raw.githubusercontent.com/nickmvincent/gdpr_text/master/gdpr.json`)
- **OPP-115**: GitHub repository (`https://github.com/citp/privacy-policy-annotated`)
