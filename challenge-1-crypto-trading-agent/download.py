#!/usr/bin/env python3
"""
Challenge 1 — AI Agent Creation Platform for Autonomous Crypto Trading
Dataset downloader. Run from the repo root OR from this folder.
Usage: python download.py
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from download_datasets import download_challenge_1
download_challenge_1()
