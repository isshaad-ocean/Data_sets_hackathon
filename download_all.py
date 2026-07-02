"""
Master dataset downloader — Hackathon Problems 2-8 (Robust Version)
"""
import os, urllib.request, zipfile, gzip, subprocess, sys

def run(cmd, check=True):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.stdout: print(result.stdout.strip())
    if result.returncode != 0 and check:
        print(f"  WARNING: command failed: {cmd[:80]}")
        print(f"  {result.stderr[:300]}")
    return result.returncode == 0

def mkdir(p): os.makedirs(p, exist_ok=True)

def hf_download(repo_id, local_dir, fallback_fn=None):
    from huggingface_hub import snapshot_download
    print(f"  HF download: {repo_id}")
    mkdir(local_dir)
    try:
        snapshot_download(
            repo_id=repo_id,
            repo_type="dataset",
            local_dir=local_dir,
            ignore_patterns=["*.md", ".gitattributes", "*.lock"]
        )
        print(f"  OK {repo_id}")
        return True
    except Exception as e:
        print(f"  FAILED {repo_id}: {str(e)[:150]}")
        if fallback_fn:
            print("  Trying fallback...")
            fallback_fn(local_dir)
        return False

def direct_download(url, dest_path):
    print(f"  Downloading {url.split('/')[-1]}...")
    mkdir(os.path.dirname(dest_path))
    try:
        urllib.request.urlretrieve(url, dest_path)
        print(f"  OK saved to {dest_path}")
        return True
    except Exception as e:
        print(f"  FAILED: {e}")
        return False

def git_clone(url, dest, depth=1):
    if os.path.exists(dest) and os.listdir(dest):
        print(f"  Already exists: {dest}")
        return True
    ok = run(f'git clone --depth {depth} {url} "{dest}"')
    if ok: print(f"  OK cloned {dest}")
    return ok

def kaggle_dl(dataset_id, dest):
    mkdir(dest)
    ok = run(f'kaggle datasets download -d {dataset_id} -p "{dest}" --unzip')
    if ok: print(f"  OK Kaggle: {dataset_id}")
    return ok

def unzip(src, dst):
    if not os.path.exists(src): return
    with zipfile.ZipFile(src, 'r') as z: z.extractall(dst)
    os.remove(src)

# ============================================================
print("\n" + "="*60)
print("PROBLEM 7 — Misinformation Detection")
print("="*60)

# LIAR — check already downloaded
if os.path.exists("problem-7/data/liar/train.tsv"):
    print("  LIAR: already downloaded")
else:
    mkdir("problem-7/data/liar")
    direct_download("https://www.cs.ucsb.edu/~william/data/liar_dataset.zip",
                    "problem-7/data/liar/liar.zip")
    unzip("problem-7/data/liar/liar.zip", "problem-7/data/liar")

# FEVER — check already downloaded
if os.path.exists("problem-7/data/fever/train.jsonl"):
    print("  FEVER: already downloaded")
else:
    mkdir("problem-7/data/fever")
    for fname, url in [
        ("train.jsonl", "https://fever.ai/download/fever/train.jsonl"),
        ("dev.jsonl",   "https://fever.ai/download/fever/shared_task_dev.jsonl"),
        ("test.jsonl",  "https://fever.ai/download/fever/shared_task_test.jsonl"),
    ]:
        direct_download(url, f"problem-7/data/fever/{fname}")

# FakeNewsNet metadata — GitHub (replaces AVeriTeC)
git_clone("https://github.com/KaiDMML/FakeNewsNet", "problem-7/data/fakenewsnet")

# GossipCop small sample — Kaggle
kaggle_dl("therealsampat/fake-news-detection", "problem-7/data/fake_news_kaggle")

print("PROBLEM 7 COMPLETE")

# ============================================================
print("\n" + "="*60)
print("PROBLEM 8 — Compliance & Policy")
print("="*60)

# PrivacyQA
hf_download("allenai/privacy_qa", "problem-8/data/privacy_qa",
    fallback_fn=lambda d: git_clone("https://github.com/AbhilashaRavichander/PrivacyQA_EMNLP", d))

# EUR-Lex via LexGLUE
hf_download("coastalcph/lex_glue", "problem-8/data/eurlex")

# GDPR full text (structured JSON)
git_clone("https://github.com/nickmvincent/gdpr_text", "problem-8/data/gdpr_text")

# OPP-115 Privacy Policy annotations
git_clone("https://github.com/citp/privacy-policy-annotated", "problem-8/data/opp115")

print("PROBLEM 8 COMPLETE")

# ============================================================
print("\n" + "="*60)
print("PROBLEM 4 — Contract Risk Analysis")
print("="*60)

# CUAD — 510 expert-annotated contracts, 41 clause types
hf_download("theatticusproject/cuad", "problem-4/data/cuad")

# ContractNLI
hf_download("stanfordnlp/contract_nli", "problem-4/data/contract_nli",
    fallback_fn=lambda d: direct_download(
        "https://stanfordnlp.github.io/contract-nli/resources/contract-nli.zip",
        f"{d}/contract_nli.zip"
    ))

# LEDGAR via LexGLUE (same repo as eurlex, skip if done)
if not os.path.exists("problem-4/data/ledgar"):
    hf_download("coastalcph/lex_glue", "problem-4/data/ledgar")

print("PROBLEM 4 COMPLETE")

# ============================================================
print("\n" + "="*60)
print("PROBLEM 5 — Synthetic Data Generation")
print("="*60)

# Adult Census via UCI (direct)
mkdir("problem-5/data/adult_census")
direct_download("https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data",
                "problem-5/data/adult_census/adult.data")
direct_download("https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.test",
                "problem-5/data/adult_census/adult.test")
direct_download("https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.names",
                "problem-5/data/adult_census/adult.names")

# Credit Card Fraud — Kaggle
kaggle_dl("mlg-ulb/creditcardfraud", "problem-5/data/credit_card_fraud")

# Diabetes PIMA — Kaggle
kaggle_dl("uciml/pima-indians-diabetes-database", "problem-5/data/diabetes")

print("PROBLEM 5 COMPLETE")

# ============================================================
print("\n" + "="*60)
print("PROBLEM 2 — Conversational Analytics")
print("="*60)

# Spider 1.0
hf_download("xlangai/spider", "problem-2/data/spider",
    fallback_fn=lambda d: git_clone("https://github.com/taoyds/spider", d))

# WikiTableQuestions
hf_download("wikitablequestions", "problem-2/data/wikitablequestions")

# Chinook SQLite DB
mkdir("problem-2/data/chinook")
if not os.path.exists("problem-2/data/chinook/ChinookDatabase1.4.5_CompleteVersion.zip"):
    direct_download(
        "https://github.com/lerocha/chinook-database/releases/download/ChinookVersion1.4.5/ChinookDatabase1.4.5_CompleteVersion.zip",
        "problem-2/data/chinook/ChinookDatabase1.4.5_CompleteVersion.zip"
    )
    unzip("problem-2/data/chinook/ChinookDatabase1.4.5_CompleteVersion.zip", "problem-2/data/chinook")

print("PROBLEM 2 COMPLETE")

# ============================================================
print("\n" + "="*60)
print("PROBLEM 3 — Network Anomaly Detection")
print("="*60)

# NSL-KDD via Kaggle
kaggle_dl("hassan06/nslkdd", "problem-3/data/nsl_kdd")

# HDFS + BGL via LogHub HuggingFace
hf_download("aioha/loghub", "problem-3/data/loghub")

# UNSW-NB15 via Kaggle (smaller, good network anomaly dataset)
kaggle_dl("dhoogla/unswnb15", "problem-3/data/unsw_nb15")

print("PROBLEM 3 COMPLETE")

# ============================================================
print("\n" + "="*60)
print("PROBLEM 6 — Visual Inspection (Large ~5GB)")
print("="*60)

# NEU Surface Defect — Kaggle (~50MB)
kaggle_dl("kaustubhdikshit/neu-surface-defect-database", "problem-6/data/neu_defect")

# DAGM 2007 — Kaggle (~130MB)
kaggle_dl("mhkhan27/dagm2007", "problem-6/data/dagm")

# MVTec AD — HuggingFace (~5GB)
hf_download("Bingsu/mvtec_anomaly_detection", "problem-6/data/mvtec")

print("PROBLEM 6 COMPLETE")

# ============================================================
print("\n" + "="*60)
print("ALL DOWNLOADS COMPLETE! Verifying...")
print("="*60)

for prob in ["problem-2","problem-3","problem-4","problem-5","problem-6","problem-7","problem-8"]:
    data_dir = f"{prob}/data"
    if os.path.exists(data_dir):
        items = os.listdir(data_dir)
        total_size = sum(
            os.path.getsize(os.path.join(root, f))
            for dirpath, _, files in os.walk(data_dir)
            for root, _, _ in [os.walk(data_dir).__next__()]
            for f in files
        ) if items else 0
        print(f"  {prob}: {items}")
    else:
        print(f"  {prob}: MISSING")
