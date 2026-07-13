#!/usr/bin/env python3
"""
Challenge 1 — AI Agent Creation Platform for Autonomous Crypto Trading
=======================================================================
Downloads all required datasets and resources for Challenge 1.

Resources:
  1. Binance Vision     — Historical OHLCV (BTC, ETH, SOL, XRP)
  2. Fear & Greed Index — Daily market sentiment (365 days)
  3. Freqtrade Strategies — Sample trading strategy templates

Usage:
    python download.py

No login required. Internet connection needed.
"""

import os
import sys
import zipfile
import requests
import urllib.request
import subprocess
from pathlib import Path

BASE = Path(__file__).parent
DATA = BASE / "data"

def mkdir(p):
    Path(p).mkdir(parents=True, exist_ok=True)

def info(msg):  print(f"  [INFO]  {msg}")
def ok(msg):    print(f"  [OK]    {msg}")
def warn(msg):  print(f"  [WARN]  {msg}")
def err(msg):   print(f"  [ERROR] {msg}")

def download_file(url, dest, label=None):
    label = label or Path(dest).name
    if Path(dest).exists():
        ok(f"Already exists: {label}")
        return True
    info(f"Downloading {label}...")
    mkdir(Path(dest).parent)
    try:
        def progress(count, block, total):
            if total > 0:
                pct = min(count * block * 100 // total, 100)
                print(f"\r    {pct}%  ", end="", flush=True)
        urllib.request.urlretrieve(url, dest, reporthook=progress)
        print()
        ok(f"Saved: {dest}")
        return True
    except Exception as e:
        err(f"Failed: {e}")
        return False


# ─────────────────────────────────────────
# 1. Binance Vision — Historical OHLCV
# ─────────────────────────────────────────
def download_ohlcv():
    print("\n[1/3] Binance Vision — Historical OHLCV")
    print("      Source: https://data.binance.vision\n")

    pairs = ["BTCUSDT", "ETHUSDT", "SOLUSDT", "XRPUSDT"]
    intervals = ["1d"]   # daily candles — add "1h" for hourly
    months = ["2024-01", "2024-06", "2024-12"]  # sample months

    ohlcv_dir = DATA / "ohlcv"
    mkdir(ohlcv_dir)

    for pair in pairs:
        for interval in intervals:
            for month in months:
                filename = f"{pair}-{interval}-{month}.zip"
                url = f"https://data.binance.vision/data/spot/monthly/klines/{pair}/{interval}/{filename}"
                zip_dest = ohlcv_dir / filename
                csv_dest = ohlcv_dir / filename.replace(".zip", ".csv")

                if csv_dest.exists():
                    ok(f"Already extracted: {csv_dest.name}")
                    continue

                if download_file(url, str(zip_dest), f"{pair} {interval} {month}"):
                    try:
                        with zipfile.ZipFile(zip_dest, "r") as z:
                            z.extractall(ohlcv_dir)
                        zip_dest.unlink()
                        ok(f"Extracted: {csv_dest.name}")
                    except Exception as e:
                        warn(f"Extract failed: {e}")

    # Write column reference
    col_ref = ohlcv_dir / "COLUMNS.txt"
    col_ref.write_text(
        "Binance kline CSV columns:\n"
        "open_time, open, high, low, close, volume, close_time,\n"
        "quote_volume, count, taker_buy_volume, taker_buy_quote_volume, ignore\n"
    )
    ok("OHLCV download complete")


# ─────────────────────────────────────────
# 2. Fear & Greed Index
# ─────────────────────────────────────────
def download_fear_greed():
    print("\n[2/3] Fear & Greed Index — Market Sentiment")
    print("      Source: https://alternative.me/crypto/fear-and-greed-index/\n")

    dest = DATA / "sentiment" / "fear_greed_index.csv"
    if dest.exists():
        ok("Fear & Greed Index: already downloaded")
        return

    mkdir(dest.parent)
    try:
        info("Fetching 365 days of Fear & Greed data...")
        resp = requests.get(
            "https://api.alternative.me/fng/?limit=365&format=json",
            timeout=15
        )
        resp.raise_for_status()
        data = resp.json()["data"]

        import csv
        with open(str(dest), "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["timestamp", "value", "value_classification"])
            writer.writeheader()
            for row in reversed(data):  # chronological order
                writer.writerow({
                    "timestamp": row["timestamp"],
                    "value": row["value"],
                    "value_classification": row["value_classification"]
                })
        ok(f"Saved {len(data)} days → {dest.name}")
    except Exception as e:
        err(f"Fear & Greed download failed: {e}")
        warn("Manual download: https://api.alternative.me/fng/?limit=365&format=json")


# ─────────────────────────────────────────
# 3. Freqtrade Strategy Examples
# ─────────────────────────────────────────
def download_strategies():
    print("\n[3/3] Freqtrade — Sample Trading Strategy Templates")
    print("      Source: https://github.com/freqtrade/freqtrade-strategies\n")

    strat_dir = DATA / "strategies"
    if strat_dir.exists() and any(strat_dir.glob("*.py")):
        ok("Strategies: already downloaded")
        return

    mkdir(strat_dir)

    # Clone strategies repo (shallow)
    info("Cloning freqtrade-strategies repo...")
    result = subprocess.run(
        f'git clone --depth 1 https://github.com/freqtrade/freqtrade-strategies.git "{strat_dir}"',
        shell=True, capture_output=True, text=True
    )
    if result.returncode == 0:
        ok("Freqtrade strategies cloned")
    else:
        warn(f"Git clone failed: {result.stderr[:150]}")
        warn("Manual: git clone https://github.com/freqtrade/freqtrade-strategies.git data/strategies/")

    # Also download the official sample strategy template
    template_url = (
        "https://raw.githubusercontent.com/freqtrade/freqtrade/"
        "develop/freqtrade/templates/sample_strategy.py"
    )
    download_file(template_url, str(strat_dir / "sample_strategy.py"), "sample_strategy.py")


# ─────────────────────────────────────────
# 4. Write resource reference
# ─────────────────────────────────────────
def write_resource_guide():
    guide = DATA / "RESOURCES.md"
    guide.write_text("""# Challenge 1 — Resource Reference

## Libraries (install via pip)
| Library | Install | Purpose |
|---------|---------|---------|
| ccxt | pip install ccxt | Unified API for 100+ exchanges |
| pandas-ta-classic | pip install pandas-ta-classic | RSI, MACD, EMA, BBands, ATR, ADX, VWAP, OBV |
| backtesting | pip install backtesting | Strategy backtesting & simulation |
| requests | pip install requests | API calls (Fear & Greed, etc.) |

## Data Sources
| Dataset | Location | Source |
|---------|----------|--------|
| OHLCV klines | data/ohlcv/ | https://data.binance.vision |
| Fear & Greed | data/sentiment/fear_greed_index.csv | https://alternative.me/crypto/fear-and-greed-index/ |
| Strategy templates | data/strategies/ | https://github.com/freqtrade/freqtrade-strategies |

## Key Links
- CCXT Docs: https://docs.ccxt.com
- pandas-ta GitHub: https://github.com/xgboosted/pandas-ta-classic
- Backtesting.py GitHub: https://github.com/kernc/backtesting.py
- Freqtrade Strategy Guide: https://www.freqtrade.io/en/stable/strategy-customization/
""")
    ok("Resource guide written to data/RESOURCES.md")


# ─────────────────────────────────────────
# Main
# ─────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 60)
    print("  Challenge 1 — Crypto Trading Dataset Downloader")
    print("  Tech Mahindra CODE Hackathon")
    print("=" * 60)

    download_ohlcv()
    download_fear_greed()
    download_strategies()
    write_resource_guide()

    print("\n" + "=" * 60)
    print("  All done! Install libraries with:")
    print("  pip install ccxt backtesting pandas-ta-classic requests")
    print("=" * 60)
