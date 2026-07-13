#!/usr/bin/env python3
"""
Challenge 2 — Network Anomaly Root-Cause Assistant
Dataset downloader. Run from the repo root OR from this folder.
Usage: python download.py

Requirements: Kaggle API configured (~/.kaggle/kaggle.json)
See SETUP.md for instructions.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from download_datasets import download_challenge_2
download_challenge_2()
