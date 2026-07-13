# =============================================================================
# download.ps1 — Dataset downloader for Problem 1: Intelligent Document Processor
# Usage: .\download.ps1
# Requirements: git, Python + pip (datasets, kaggle), kaggle.json at ~\.kaggle\kaggle.json
# =============================================================================

$ErrorActionPreference = "Stop"

$BaseDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$DataDir = Join-Path $BaseDir "data"

Write-Host "==================================================" -ForegroundColor Cyan
Write-Host " Hackathon Dataset Downloader -- Problem 1" -ForegroundColor Cyan
Write-Host " Intelligent Document Processor (Human-in-the-Loop)" -ForegroundColor Cyan
Write-Host "==================================================" -ForegroundColor Cyan
Write-Host ""

# ------------------------------------------------------------------
# 1. SROIE 2019
# ------------------------------------------------------------------
Write-Host "[1/4] Downloading SROIE 2019..." -ForegroundColor Yellow
$SroieDir = Join-Path $DataDir "sroie"
if (Test-Path (Join-Path $SroieDir ".git")) {
    Write-Host "  SROIE already cloned. Pulling latest..."
    git -C $SroieDir pull
} else {
    git clone https://github.com/zzzDavid/ICDAR-2019-SROIE $SroieDir
}
Write-Host "  OK SROIE 2019 ready" -ForegroundColor Green
Write-Host ""

# ------------------------------------------------------------------
# 2. CORD v2 (HuggingFace)
# ------------------------------------------------------------------
Write-Host "[2/4] Downloading CORD v2 (HuggingFace)..." -ForegroundColor Yellow
pip install -q datasets huggingface_hub
$CordDir = Join-Path $DataDir "cord"
python -c @"
from datasets import load_dataset
ds = load_dataset('naver-clova-ix/cord-v2')
ds.save_to_disk(r'$CordDir')
print('  OK CORD v2 ready')
"@
Write-Host ""

# ------------------------------------------------------------------
# 3. FUNSD
# ------------------------------------------------------------------
Write-Host "[3/4] Downloading FUNSD..." -ForegroundColor Yellow
$FunsdDir = Join-Path $DataDir "funsd"
New-Item -ItemType Directory -Force -Path $FunsdDir | Out-Null
$FunsdFiles = Get-ChildItem $FunsdDir -ErrorAction SilentlyContinue
if ($FunsdFiles.Count -eq 0) {
    $ZipPath = Join-Path $FunsdDir "dataset.zip"
    Invoke-WebRequest `
        -Uri "https://guillaumejaume.github.io/FUNSD/dataset.zip" `
        -OutFile $ZipPath
    Expand-Archive -Path $ZipPath -DestinationPath $FunsdDir -Force
    Remove-Item $ZipPath
} else {
    Write-Host "  FUNSD already downloaded. Skipping."
}
Write-Host "  OK FUNSD ready" -ForegroundColor Green
Write-Host ""

# ------------------------------------------------------------------
# 4. Invoice NER (Kaggle)
# ------------------------------------------------------------------
Write-Host "[4/4] Downloading Invoice NER (Kaggle)..." -ForegroundColor Yellow
$KaggleJson = Join-Path $env:USERPROFILE ".kaggle\kaggle.json"
if (!(Test-Path $KaggleJson)) {
    Write-Host "  WARNING: ~/.kaggle/kaggle.json not found." -ForegroundColor Red
    Write-Host "  1. Go to https://www.kaggle.com/settings"
    Write-Host "  2. API section -> Create New Token"
    Write-Host "  3. Move downloaded kaggle.json to: $KaggleJson"
    Write-Host "  Skipping Invoice NER download."
} else {
    pip install -q kaggle
    $InvoiceDir = Join-Path $DataDir "invoice_ner"
    kaggle datasets download `
        -d nikitpatel/invoice-ner-dataset `
        -p $InvoiceDir `
        --unzip
    Write-Host "  OK Invoice NER ready" -ForegroundColor Green
}
Write-Host ""

# ------------------------------------------------------------------
# Summary — Tree View
# ------------------------------------------------------------------
Write-Host "==================================================" -ForegroundColor Cyan
Write-Host " Download Complete! Directory tree:" -ForegroundColor Cyan
Write-Host "==================================================" -ForegroundColor Cyan
Get-ChildItem -Recurse -Depth 3 $DataDir | Select-Object FullName
