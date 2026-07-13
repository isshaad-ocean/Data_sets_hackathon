# Challenge 2 — Network Anomaly Root-Cause Assistant

## Problem Statement

Build a Network Anomaly Root-Cause Assistant that ingests telemetry, logs, alerts, topology data, and configuration changes to detect anomalies and generate explainable root-cause hypotheses.

---

## Datasets

| Dataset | Format | Size | License | Source |
|---------|--------|------|---------|--------|
| **NSL-KDD** | TXT/CSV | 7 MB | Open | [Kaggle](https://www.kaggle.com/datasets/hassan06/nslkdd) |
| **UNSW-NB15** | CSV | 113 MB | CC-BY-NC-SA 4.0 | [Kaggle](https://www.kaggle.com/datasets/dhoogla/unswnb15) |
| **LogHub (HDFS + BGL)** | LOG | ~170 MB | Open | [HuggingFace](https://huggingface.co/datasets/aioha/loghub) |

## Key Fields
- NSL-KDD: 41 network features, `attack_type` (DoS/Probe/R2L/U2R/Normal)
- UNSW-NB15: `srcip`, `dstip`, `proto`, `service`, `state`, `label`, `attack_cat`
- LogHub: `Timestamp`, `EventId`, `Component`, `Level`, `Content`, `Label` (Normal/Anomaly)

## Download
See [PARTICIPANTS_GUIDE.md](../PARTICIPANTS_GUIDE.md#challenge-2) for full download instructions.

*Tech Mahindra CODE Hackathon — Challenge 2*
