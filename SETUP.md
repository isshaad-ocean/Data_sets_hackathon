# Environment Setup Guide — Hyderabad AI Hackathon 2026

Follow this guide **once** before downloading datasets. Estimated time: 10 minutes.

---

## Prerequisites Checklist

- [ ] Python 3.9 or later installed
- [ ] Git installed
- [ ] Internet connection (for dataset downloads)

---

## Step 1 — Clone the Repository

```bash
git clone https://github.com/isshaad-ocean/Data_sets_hackathon.git
cd Data_sets_hackathon
```

---

## Step 2 — Install Git LFS

Git LFS (Large File Storage) is required to download large binary files from the repo.

**Windows:**
```powershell
# Download installer from https://git-lfs.com/ OR use winget:
winget install GitHub.GitLFS

# Then in the repo folder:
git lfs install
git lfs pull
```

**macOS:**
```bash
brew install git-lfs
git lfs install
git lfs pull
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install git-lfs
git lfs install
git lfs pull
```

---

## Step 3 — Create a Python Virtual Environment (Recommended)

```bash
# Create environment
python -m venv .venv

# Activate — Windows PowerShell
.\.venv\Scripts\Activate.ps1

# Activate — macOS / Linux
source .venv/bin/activate
```

---

## Step 4 — Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 5 — Configure Kaggle API (Required for Challenge 2 only)

Challenge 2 datasets (NSL-KDD, UNSW-NB15) require a free Kaggle account.

1. Create a free account at **https://www.kaggle.com**
2. Go to **Settings → API → Create New Token**
3. A file `kaggle.json` will download — place it here:

**Windows PowerShell:**
```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.kaggle"
Move-Item "$env:USERPROFILE\Downloads\kaggle.json" "$env:USERPROFILE\.kaggle\kaggle.json"
```

**macOS / Linux:**
```bash
mkdir -p ~/.kaggle
mv ~/Downloads/kaggle.json ~/.kaggle/kaggle.json
chmod 600 ~/.kaggle/kaggle.json
```

4. Verify it works:
```bash
kaggle datasets list
```

---

## Step 6 — Download Your Challenge Datasets

### Option A — Quickest: Extract from Zipped Archive

Pre-downloaded zips are in `zipped-datasets/`:

| Challenge | Zip File | Size |
|-----------|----------|------|
| C2 — Network Anomaly RCA | `challenge-2-network-anomaly-rca.zip` | ~24 MB |
| C3 — KYC Autonomous Auditor | `challenge-3-kyc-autonomous-auditor.zip` | ~489 MB |
| C4 — Contract & SOW Risk | `challenge-4-contract-sow-risk-analyzer.zip` | ~638 MB |

```bash
# Windows PowerShell — extract Challenge 2 example
Expand-Archive zipped-datasets\challenge-2-network-anomaly-rca.zip `
  -DestinationPath challenge-2-network-anomaly-rca\

# macOS / Linux
unzip zipped-datasets/challenge-2-network-anomaly-rca.zip \
  -d challenge-2-network-anomaly-rca/
```

### Option B — Master Downloader Script

Downloads fresh copies from original sources:

```bash
# Download all 4 challenges
python download_datasets.py

# Download only your challenge (replace N with 1, 2, 3, or 4)
python download_datasets.py --challenge 2
```

### Option C — Per-Challenge Script

Run the standalone script inside your challenge folder:

```bash
cd challenge-2-network-anomaly-rca
python download.py
```

---

## Verify Your Setup

```bash
python download_datasets.py --verify
```

Expected output:
```
[OK] challenge-1-crypto-trading-agent — data folder present
[OK] challenge-2-network-anomaly-rca  — data folder present
[OK] challenge-3-kyc-autonomous-auditor — data folder present
[OK] challenge-4-contract-sow-risk-analyzer — data folder present
```

---

## Troubleshooting

| Error | Fix |
|-------|-----|
| `git lfs: command not found` | Install Git LFS (Step 2 above) |
| `kaggle: command not found` | Run `pip install kaggle` |
| `401 Unauthorized` from Kaggle | Check `~/.kaggle/kaggle.json` exists |
| `ModuleNotFoundError: datasets` | Run `pip install -r requirements.txt` |
| Zip file corrupt on extract | Re-download with `git lfs pull` |
| `SSL: CERTIFICATE_VERIFY_FAILED` (macOS) | Run `Install Certificates.command` from your Python installation |
| Large files missing after clone | Run `git lfs pull` |

---

## What Each Challenge Needs

| Challenge | Git LFS | Kaggle API | Internet |
|-----------|---------|-----------|---------|
| C1 — Crypto Trading Agent | ❌ | Optional | ✅ (Zenodo/CryptoDataDownload) |
| C2 — Network Anomaly RCA | ❌ | ✅ Required | ✅ |
| C3 — KYC Auditor | ✅ (zip) | ❌ | ✅ or use zip |
| C4 — Contract & SOW Risk | ✅ (zip) | ❌ | ✅ or use zip |

---

*Hyderabad AI Hackathon 2026 — Setup Guide*
