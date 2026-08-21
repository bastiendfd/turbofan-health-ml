# Turbofan Health ML

> A reproducible, **synthetic-first** baseline for Remaining Useful Life (RUL) experiments on C-MAPSS-style turbofan cycle data.

![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white)
![scikit--learn](https://img.shields.io/badge/scikit--learn-baseline-F7931E?logo=scikitlearn&logoColor=white)
![Tests](https://img.shields.io/badge/tests-pytest-0A9EDC)
![Data](https://img.shields.io/badge/data-synthetic_first-2E8B57)

## Purpose

This project demonstrates a disciplined predictive-maintenance workflow without claiming to predict real engine health:

```text
cycle data
→ per-engine RUL labels
→ engine-level train/test split
→ transparent linear-regression baseline
→ MAE on engines unseen during training
```

The key design choice is the split: an engine never appears in both train and test sets. Randomly splitting individual cycles would leak engine trajectories and produce misleadingly optimistic scores.

## Current experiment

The included synthetic demonstration generates fictional cycle data and evaluates a baseline on five unseen engines:

```text
train engines: 15
held-out engines: 5
MAE: 2.182 cycles
```

This result is **only for the synthetic generator bundled here**. It is not a claim about aircraft, turbines, maintenance intervals or real-world Remaining Useful Life.

## Run locally

```bash
git clone https://github.com/bastiendfd/turbofan-health-ml.git
cd turbofan-health-ml

python -m venv .venv
# Windows Git Bash
.venv/Scripts/python.exe -m pip install -r requirements.txt
.venv/Scripts/python.exe -m pytest -q
.venv/Scripts/python.exe scripts/run_synthetic_experiment.py
```

The script prints a JSON report with the dataset label, MAE and engine split.

## C-MAPSS-compatible input

`turbofan_health.cmapss.load_cmapss_text()` reads the common whitespace-delimited C-MAPSS layout:

- engine ID;
- cycle;
- three operating settings;
- 21 sensor columns.

No external dataset is distributed, downloaded or committed by this repository. If you supply a public C-MAPSS-style file yourself, keep it outside Git under `data/raw/` and verify its source, licence and terms first.

## Scientific limits

- RUL labels in the training split use the last observed cycle of each engine; real test-set evaluation requires true RUL labels supplied separately.
- The baseline is linear and intentionally interpretable, not a production model.
- A synthetic sensor trajectory is not a physical turbine model.
- This project is for learning and portfolio demonstration, not flight safety, maintenance planning, certification or engineering decision-making.

## Repository structure

```text
turbofan_health/
  cmapss.py       C-MAPSS-compatible parser
  features.py     RUL-label feature engineering
  modeling.py     engine-level baseline evaluation
  synthetic.py    fictional demo cycle generator
scripts/
  run_synthetic_experiment.py
 tests/
  behavioural tests for parsing, features, model split and experiment script
```

## Safety and data policy

- Do not use employer, customer, supplier or confidential maintenance data.
- Do not commit raw datasets, model artifacts, `.env` files, credentials or keys.
- Keep all experiments local until the data source and intended use are explicitly reviewed.

See [SECURITY.md](SECURITY.md) and [data/README.md](data/README.md).

## License

No license has been selected yet. All rights reserved unless and until a license is added.
