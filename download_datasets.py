#!/usr/bin/env python3
"""
Tech Mahindra CODE Hackathon — Master Dataset Downloader
========================================================
Downloads datasets for all 4 challenge problem statements.

Usage:
    python download_datasets.py                  # Download all challenges
    python download_datasets.py --challenge 1    # Only Challenge 1
    python download_datasets.py --challenge 2    # Only Challenge 2
    python download_datasets.py --verify         # Verify existing downloads

Requirements:
    pip install -r requirements.txt
"""

import os
import sys
import argparse
import subprocess
import urllib.request
import zipfile
import shutil
from pathlib import Path

# ─────────────────────────────────────────────
# Utilities
# ─────────────────────────────────────────────

def header(title):
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")

def info(msg):   print(f"  [INFO]  {msg}")
def ok(msg):     print(f"  [OK]    {msg}")
def warn(msg):   print(f"  [WARN]  {msg}")
def error(msg):  print(f"  [ERROR] {msg}")

def mkdir(path):
    Path(path).mkdir(parents=True, exist_ok=True)

def already_exists(path, min_files=1):
    p = Path(path)
    if not p.exists():
        return False
    files = list(p.rglob("*"))
    non_gitkeep = [f for f in files if f.is_file() and f.name != ".gitkeep"]
    return len(non_gitkeep) >= min_files

def run(cmd, check=False):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.stdout.strip():
        print(f"    {result.stdout.strip()[:200]}")
    if result.returncode != 0 and result.stderr.strip():
        warn(result.stderr.strip()[:200])
    return result.returncode == 0

def direct_download(url, dest_path, label=None):
    label = label or Path(dest_path).name
    info(f"Downloading {label}...")
    mkdir(Path(dest_path).parent)
    try:
        def progress(count, block_size, total_size):
            if total_size > 0:
                pct = min(count * block_size * 100 // total_size, 100)
                print(f"\r    {pct}% ", end="", flush=True)
        urllib.request.urlretrieve(url, dest_path, reporthook=progress)
        print()
        ok(f"Saved: {dest_path}")
        return True
    except Exception as e:
        error(f"Failed to download {label}: {e}")
        return False

def hf_download(repo_id, local_dir, config=None):
    if already_exists(local_dir):
        ok(f"Already downloaded: {local_dir}")
        return True
    info(f"Downloading from HuggingFace: {repo_id}")
    mkdir(local_dir)
    try:
        from huggingface_hub import snapshot_download
        kwargs = dict(
            repo_id=repo_id,
            repo_type="dataset",
            local_dir=local_dir,
            ignore_patterns=["*.md", ".gitattributes"],
        )
        if config:
            kwargs["repo_id"] = repo_id  # config handled via load_dataset
            from datasets import load_dataset
            ds = load_dataset(repo_id, config)
            ds.save_to_disk(local_dir)
        else:
            snapshot_download(**kwargs)
        ok(f"Downloaded: {repo_id}")
        return True
    except Exception as e:
        error(f"HuggingFace download failed for {repo_id}: {e}")
        return False

def kaggle_download(dataset_id, dest_dir):
    if already_exists(dest_dir):
        ok(f"Already downloaded: {dest_dir}")
        return True
    info(f"Downloading from Kaggle: {dataset_id}")
    mkdir(dest_dir)
    if not run(f'kaggle datasets download -d {dataset_id} -p "{dest_dir}" --unzip'):
        error(f"Kaggle download failed. Make sure kaggle.json is configured. See SETUP.md.")
        return False
    ok(f"Downloaded: {dataset_id}")
    return True

def unzip_file(src, dest_dir):
    info(f"Extracting {Path(src).name}...")
    mkdir(dest_dir)
    with zipfile.ZipFile(src, "r") as z:
        z.extractall(dest_dir)
    ok(f"Extracted to {dest_dir}")

# ─────────────────────────────────────────────
# Challenge 1 — AI Agent Crypto Trading
# ─────────────────────────────────────────────

def download_challenge_1():
    header("Challenge 1 — AI Agent Creation Platform for Autonomous Crypto Trading")
    base = Path("challenge-1-crypto-trading-agent/data")

    # CryptoSentiment via Zenodo (no login needed)
    sentiment_zip = base / "sentiment" / "crypto_sentiment.zip"
    if not already_exists(base / "sentiment"):
        direct_download(
            "https://zenodo.org/records/7684409/files/crypto_sentiment_dataset.zip",
            str(sentiment_zip),
            "CryptoSentiment Dataset (Zenodo)"
        )
        if sentiment_zip.exists():
            unzip_file(str(sentiment_zip), str(base / "sentiment"))
            sentiment_zip.unlink()
    else:
        ok("CryptoSentiment: already downloaded")

    # OFAC SDN - (proxy for financial sanctions/risk data useful for trading context)
    gdpr_dest = base / "ohlcv" / "README_download_instructions.txt"
    if not gdpr_dest.exists():
        mkdir(base / "ohlcv")
        instructions = """OHLCV Data Download Instructions
=================================
Download free historical crypto OHLCV CSVs from:

1. CryptoDataDownload (no login required):
   https://cryptodatadownload.com/data/kraken/
   - Download: Kraken_BTCUSD_d.csv (BTC daily)
   - Download: Kraken_ETHUSD_d.csv (ETH daily)
   - Save to: challenge-1-crypto-trading-agent/data/ohlcv/

2. Fear & Greed Index (no login required):
   https://www.kaggle.com/datasets/l3llff/bitcoin
   kaggle datasets download -d l3llff/bitcoin -p data/ohlcv/ --unzip

3. Kaggle BTC historical:
   kaggle datasets download -d mczielinski/bitcoin-historical-data -p data/ohlcv/ --unzip
"""
        with open(str(gdpr_dest), "w") as f:
            f.write(instructions)
        ok("Created OHLCV download instructions")

    print(f"\n  Challenge 1 datasets ready.")
    print(f"  Note: For OHLCV data, see: challenge-1-crypto-trading-agent/data/ohlcv/README_download_instructions.txt")

# ─────────────────────────────────────────────
# Challenge 2 — Network Anomaly Root-Cause
# ─────────────────────────────────────────────

def download_challenge_2():
    header("Challenge 2 — Network Anomaly Root-Cause Assistant")
    base = Path("challenge-2-network-anomaly-rca/data")

    # NSL-KDD
    kaggle_download("hassan06/nslkdd", str(base / "nsl_kdd"))

    # UNSW-NB15
    kaggle_download("dhoogla/unswnb15", str(base / "unsw_nb15"))

    # LogHub via HuggingFace (HDFS logs — no login)
    hf_download("aioha/loghub", str(base / "loghub"), config="HDFS")

    ok("Challenge 2 complete.")

# ─────────────────────────────────────────────
# Challenge 3 — Continuous KYC Autonomous Auditor
# ─────────────────────────────────────────────

def download_challenge_3():
    header("Challenge 3 — Continuous KYC Autonomous Auditor")
    base = Path("challenge-3-kyc-autonomous-auditor/data")

    # OpenSanctions consolidated targets (no login)
    sanctions_csv = base / "sanctions" / "opensanctions_targets.csv"
    if not sanctions_csv.exists():
        direct_download(
            "https://data.opensanctions.org/datasets/latest/default/targets.simple.csv",
            str(sanctions_csv),
            "OpenSanctions targets.csv (~40MB)"
        )
    else:
        ok("OpenSanctions: already downloaded")

    # OFAC SDN List (US Treasury, public domain)
    ofac_csv = base / "sanctions" / "ofac_sdn.csv"
    if not ofac_csv.exists():
        direct_download(
            "https://www.treasury.gov/ofac/downloads/sdn.csv",
            str(ofac_csv),
            "OFAC SDN List"
        )
    else:
        ok("OFAC SDN: already downloaded")

    # PrivacyQA (HuggingFace, no login)
    hf_download("allenai/privacy_qa", str(base / "privacy_qa"))

    # GDPR full text (GitHub)
    gdpr_json = base / "gdpr_text" / "gdpr.json"
    if not gdpr_json.exists():
        direct_download(
            "https://raw.githubusercontent.com/nickmvincent/gdpr_text/master/gdpr.json",
            str(gdpr_json),
            "GDPR Full Text JSON"
        )
    else:
        ok("GDPR text: already downloaded")

    # EUR-Lex via LexGLUE (HuggingFace, no login)
    hf_download("coastalcph/lex_glue", str(base / "eurlex"), config="eurlex")

    ok("Challenge 3 complete.")

# ─────────────────────────────────────────────
# Challenge 4 — Contract & SOW Risk Analyzer
# ─────────────────────────────────────────────

def download_challenge_4():
    header("Challenge 4 — Contract & SOW Risk Analyzer")
    base = Path("challenge-4-contract-sow-risk-analyzer/data")

    # CUAD — 510 expert-annotated contracts (HuggingFace, no login)
    hf_download("theatticusproject/cuad", str(base / "cuad"))

    # ContractNLI (HuggingFace, no login)
    hf_download("stanfordnlp/contract_nli", str(base / "contract_nli"))

    # LEDGAR via LexGLUE (HuggingFace, no login)
    hf_download("coastalcph/lex_glue", str(base / "ledgar"), config="ledgar")

    ok("Challenge 4 complete.")

# ─────────────────────────────────────────────
# Verify
# ─────────────────────────────────────────────

def verify_downloads():
    header("Verifying Downloads")
    checks = {
        "Challenge 1 — Crypto Trading": "challenge-1-crypto-trading-agent/data",
        "Challenge 2 — Network Anomaly": "challenge-2-network-anomaly-rca/data",
        "Challenge 3 — KYC Auditor":     "challenge-3-kyc-autonomous-auditor/data",
        "Challenge 4 — Contract Risk":   "challenge-4-contract-sow-risk-analyzer/data",
    }
    all_ok = True
    for name, path in checks.items():
        p = Path(path)
        if p.exists():
            non_gitkeep = [f for f in p.rglob("*") if f.is_file() and f.name != ".gitkeep"]
            count = len(non_gitkeep)
            size_mb = sum(f.stat().st_size for f in non_gitkeep) / (1024*1024)
            if count > 0:
                ok(f"{name}: {count} files, {size_mb:.1f} MB")
            else:
                warn(f"{name}: folder exists but no data downloaded yet")
                all_ok = False
        else:
            error(f"{name}: data folder missing — run download first")
            all_ok = False
    print()
    if all_ok:
        ok("All challenge datasets are present!")
    else:
        warn("Some datasets missing. Run: python download_datasets.py")

# ─────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Tech Mahindra CODE Hackathon — Dataset Downloader"
    )
    parser.add_argument(
        "--challenge", type=int, choices=[1, 2, 3, 4],
        help="Download only a specific challenge (1-4). Omit to download all."
    )
    parser.add_argument(
        "--verify", action="store_true",
        help="Verify that datasets are present without downloading."
    )
    args = parser.parse_args()

    print("\n" + "="*60)
    print("  Tech Mahindra CODE Hackathon — Dataset Downloader")
    print("="*60)
    print("  Run with --help for usage options.")

    if args.verify:
        verify_downloads()
        return

    dispatch = {1: download_challenge_1, 2: download_challenge_2,
                3: download_challenge_3, 4: download_challenge_4}

    if args.challenge:
        dispatch[args.challenge]()
    else:
        for fn in dispatch.values():
            fn()

    print()
    header("All Done!")
    verify_downloads()

if __name__ == "__main__":
    main()
