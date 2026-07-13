#!/usr/bin/env python3
"""
Challenge 4 — Contract & SOW Risk Analyzer
Dataset downloader. Run from the repo root OR from this folder.
Usage: python download.py

No login required — all datasets available via HuggingFace.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from download_datasets import download_challenge_4
download_challenge_4()
