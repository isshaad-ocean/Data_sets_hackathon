#!/usr/bin/env python3
"""
Challenge 3 — Continuous KYC Autonomous Auditor
Dataset downloader. Run from the repo root OR from this folder.
Usage: python download.py

No login required — all datasets are freely available.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from download_datasets import download_challenge_3
download_challenge_3()
