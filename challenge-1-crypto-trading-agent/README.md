# Challenge 1 — AI Agent Creation Platform for Autonomous Crypto Trading

## Problem Statement

Develop an intelligent platform that enables users to create, configure, deploy, and evaluate autonomous AI-powered crypto trading agents with minimal coding.

---

## Datasets

### 1. Historical OHLCV Market Data

| Dataset | Format | Size | License | Source |
|---------|--------|------|---------|--------|
| Kraken Historical OHLCV | CSV | ~200 MB | Open | https://cryptodatadownload.com/data/kraken/ |
| Bitcoin Historical Data | CSV | ~5 MB | Open | https://www.kaggle.com/datasets/mczielinski/bitcoin-historical-data |
| BTC/ETH Multi-Exchange OHLCV | CSV | ~30 MB | Open | https://www.kaggle.com/datasets/tencars/392-crypto-currency-pairs-at-minute-resolution |

Key Fields: timestamp, open, high, low, close, volume, pair

### 2. Sentiment & News Data

| Dataset | Format | Size | License | Source |
|---------|--------|------|---------|--------|
| CryptoSentiment (14 coins, FinBERT) | JSON/CSV | ~200 MB | CC0 | https://zenodo.org/records/7684409 |
| Crypto News + Sentiment Labels | CSV | ~10 MB | Research | https://www.kaggle.com/datasets/oliviervha/crypto-news |
| Bitcoin Tweets Sentiment | CSV | ~50 MB | Open | https://www.kaggle.com/datasets/kaushiksuresh147/bitcoin-tweets |
| Fear and Greed Index (BTC) | CSV | <1 MB | Open | https://www.kaggle.com/datasets/l3llff/bitcoin |

Key Fields: date, coin, sentiment_score (-1 to 1), source (news/twitter), headline

### 3. Quick Start

# CryptoSentiment via Zenodo (no login needed)
# wget https://zenodo.org/records/7684409/files/crypto_sentiment_dataset.zip

# Kaggle (free account + API token)
# kaggle datasets download -d mczielinski/bitcoin-historical-data -p data/ohlcv/
# kaggle datasets download -d oliviervha/crypto-news -p data/sentiment/

## Credential Requirements
- CryptoDataDownload: No login
- Zenodo (CryptoSentiment): No login
- Kaggle: Free account + API token
- HuggingFace: No login

Hyderabad AI Hackathon 2026 - Challenge 1 Dataset
