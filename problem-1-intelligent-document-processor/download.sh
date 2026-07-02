#!/usr/bin/env bash
# =============================================================================
# download.sh — Dataset downloader for Problem 1: Intelligent Document Processor
# Usage: bash download.sh
# Requirements: git, pip (datasets, kaggle), kaggle.json at ~/.kaggle/kaggle.json
# =============================================================================

set -e

BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DATA_DIR="$BASE_DIR/data"

echo "=================================================="
echo " Hackathon Dataset Downloader — Problem 1"
echo " Intelligent Document Processor (Human-in-the-Loop)"
echo "=================================================="
echo ""

# ------------------------------------------------------------------
# 1. SROIE 2019
# ------------------------------------------------------------------
echo "[1/4] Downloading SROIE 2019..."
if [ -d "$DATA_DIR/sroie/.git" ]; then
  echo "  SROIE already cloned. Pulling latest..."
  git -C "$DATA_DIR/sroie" pull
else
  git clone https://github.com/zzzDavid/ICDAR-2019-SROIE "$DATA_DIR/sroie"
fi
echo "  ✓ SROIE 2019 ready"
echo ""

# ------------------------------------------------------------------
# 2. CORD v2 (HuggingFace)
# ------------------------------------------------------------------
echo "[2/4] Downloading CORD v2 (HuggingFace)..."
pip install -q datasets huggingface_hub
python3 - <<'EOF'
from datasets import load_dataset
import os
save_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "cord")
print(f"  Saving to {save_path}...")
ds = load_dataset("naver-clova-ix/cord-v2")
ds.save_to_disk(save_path)
print("  ✓ CORD v2 ready")
EOF
echo ""

# ------------------------------------------------------------------
# 3. FUNSD
# ------------------------------------------------------------------
echo "[3/4] Downloading FUNSD..."
mkdir -p "$DATA_DIR/funsd"
if [ "$(ls -A $DATA_DIR/funsd)" ]; then
  echo "  FUNSD already downloaded. Skipping."
else
  wget -q "https://guillaumejaume.github.io/FUNSD/dataset.zip" \
       -O "$DATA_DIR/funsd/dataset.zip"
  unzip -q "$DATA_DIR/funsd/dataset.zip" -d "$DATA_DIR/funsd"
  rm "$DATA_DIR/funsd/dataset.zip"
fi
echo "  ✓ FUNSD ready"
echo ""

# ------------------------------------------------------------------
# 4. Invoice NER (Kaggle)
# ------------------------------------------------------------------
echo "[4/4] Downloading Invoice NER (Kaggle)..."
if [ ! -f "$HOME/.kaggle/kaggle.json" ]; then
  echo "  ⚠ WARNING: ~/.kaggle/kaggle.json not found."
  echo "  Get your API token from https://www.kaggle.com/settings"
  echo "  Skipping Invoice NER download."
else
  pip install -q kaggle
  kaggle datasets download \
    -d nikitpatel/invoice-ner-dataset \
    -p "$DATA_DIR/invoice_ner" \
    --unzip
  echo "  ✓ Invoice NER ready"
fi
echo ""

# ------------------------------------------------------------------
# Summary
# ------------------------------------------------------------------
echo "=================================================="
echo " Download Complete! Directory tree:"
echo "=================================================="
find "$DATA_DIR" -maxdepth 3 -print | sort
