"""Reader for C-MAPSS-style whitespace-delimited text files."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

CMAPSS_COLUMNS = [
    "engine_id",
    "cycle",
    "setting_1",
    "setting_2",
    "setting_3",
    *[f"sensor_{index}" for index in range(1, 22)],
]


def load_cmapss_text(path: Path) -> pd.DataFrame:
    """Load a C-MAPSS-format text file and assign explicit column names."""
    cycles = pd.read_csv(path, sep=r"\s+", header=None, names=CMAPSS_COLUMNS)
    if cycles.shape[1] != len(CMAPSS_COLUMNS):
        raise ValueError("C-MAPSS input must contain exactly 26 columns.")
    return cycles
