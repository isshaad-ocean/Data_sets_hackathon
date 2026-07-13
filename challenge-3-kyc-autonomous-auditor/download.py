#!/usr/bin/env python3
"""
Challenge 3 — Continuous KYC Autonomous Auditor
================================================
Downloads all datasets for Challenge 3.

Datasets:
  1. Synthetic KYC & Transaction Risk Dataset  (Kaggle - Apache 2.0)
  2. SAML-D AML Transaction Data               (Kaggle - CDLA-Sharing-1.0)
  3. OpenSanctions targets.csv                 (Free - CC0)
  4. OFAC SDN List                             (Free - Public Domain)
  5. PrivacyQA                                 (HuggingFace - CC-BY 4.0)
  6. GDPR Full Text                            (Free - Public Domain)

Usage:
    python download.py

Requirements:
    pip install kaggle datasets requests
    Kaggle API configured for datasets 1 & 2 (see SETUP.md)
"""

import os
import sys
import subprocess
import urllib.request
import requests
from pathlib import Path

BASE = Path(__file__).parent
DATA = BASE / "data"

def mkdir(p):   Path(p).mkdir(parents=True, exist_ok=True)
def info(msg):  print(f"  [INFO]  {msg}")
def ok(msg):    print(f"  [OK]    {msg}")
def warn(msg):  print(f"  [WARN]  {msg}")
def err(msg):   print(f"  [ERROR] {msg}")

def already_has_data(path, min_files=1):
    p = Path(path)
    if not p.exists(): return False
    files = [f for f in p.rglob("*") if f.is_file() and f.name != ".gitkeep"]
    return len(files) >= min_files

def kaggle_download(dataset_id, dest_dir, label):
    if already_has_data(dest_dir):
        ok(f"Already downloaded: {label}")
        return True
    info(f"Downloading {label} from Kaggle...")
    mkdir(dest_dir)
    result = subprocess.run(
        f'kaggle datasets download -d {dataset_id} -p "{dest_dir}" --unzip',
        shell=True, capture_output=True, text=True
    )
    if result.returncode == 0:
        ok(f"Downloaded: {label}")
        return True
    else:
        err(f"Kaggle download failed for {label}")
        err(result.stderr[:300])
        warn("Make sure kaggle.json is configured — see SETUP.md")
        return False

def direct_download(url, dest_path, label):
    if Path(dest_path).exists():
        ok(f"Already exists: {label}")
        return True
    info(f"Downloading {label}...")
    mkdir(Path(dest_path).parent)
    try:
        def progress(count, block, total):
            if total > 0:
                pct = min(count * block * 100 // total, 100)
                print(f"\r    {pct}%  ", end="", flush=True)
        urllib.request.urlretrieve(url, dest_path, reporthook=progress)
        print()
        ok(f"Saved: {Path(dest_path).name}")
        return True
    except Exception as e:
        err(f"Failed: {e}")
        return False

def hf_download(repo_id, local_dir, label, config=None):
    if already_has_data(local_dir):
        ok(f"Already downloaded: {label}")
        return True
    info(f"Downloading {label} from HuggingFace...")
    mkdir(local_dir)
    try:
        from datasets import load_dataset
        ds = load_dataset(repo_id) if not config else load_dataset(repo_id, config)
        ds.save_to_disk(local_dir)
        ok(f"Downloaded: {label}")
        return True
    except Exception as e:
        err(f"HuggingFace download failed for {label}: {e}")
        return False


print("=" * 60)
print("  Challenge 3 — Continuous KYC Autonomous Auditor")
print("  Tech Mahindra CODE Hackathon")
print("=" * 60)

# ── 1. Synthetic KYC Dataset ──────────────────────────────
print("\n[1/6] Synthetic KYC & Transaction Risk Dataset (Kaggle)")
kaggle_download(
    "berkanoztas/synthetic-kyc-transaction-risk-dataset",
    str(DATA / "kyc_profiles"),
    "Synthetic KYC Dataset (~5-10 MB)"
)

# ── 2. SAML-D AML Transaction Data ───────────────────────
print("\n[2/6] SAML-D — Anti Money Laundering Transaction Data (Kaggle)")
print("      WARNING: This dataset is ~500MB-1GB. Download may take several minutes.")
kaggle_download(
    "berkanoztas/synthetic-transaction-monitoring-dataset-aml",
    str(DATA / "aml_transactions"),
    "SAML-D AML Transactions (~9.5M rows)"
)

# ── 3. OpenSanctions ─────────────────────────────────────
print("\n[3/6] OpenSanctions — 100+ Government Sanction Lists (Free)")
direct_download(
    "https://data.opensanctions.org/datasets/latest/default/targets.simple.csv",
    str(DATA / "sanctions" / "opensanctions_targets.csv"),
    "OpenSanctions targets (~40MB)"
)

# ── 4. OFAC SDN List ─────────────────────────────────────
print("\n[4/6] OFAC SDN List — US Treasury (Free)")
direct_download(
    "https://www.treasury.gov/ofac/downloads/sdn.csv",
    str(DATA / "sanctions" / "ofac_sdn.csv"),
    "OFAC SDN List"
)

# ── 5. PrivacyQA ─────────────────────────────────────────
print("\n[5/6] PrivacyQA — Regulatory Q&A (HuggingFace, Free)")
hf_download("allenai/privacy_qa", str(DATA / "privacy_qa"), "PrivacyQA")

# ── 6. GDPR Full Text ────────────────────────────────────
print("\n[6/6] GDPR Full Text — Structured JSON (Free)")
direct_download(
    "https://raw.githubusercontent.com/nickmvincent/gdpr_text/master/gdpr.json",
    str(DATA / "gdpr_text" / "gdpr.json"),
    "GDPR Full Text JSON"
)

print("\n" + "=" * 60)
print("  Challenge 3 download complete!")
print("  Install dependencies: pip install pandas numpy scikit-learn")
print("=" * 60)
