"""Feature engineering for cycle-based turbofan health data."""

from __future__ import annotations

import pandas as pd


def add_remaining_useful_life(cycles: pd.DataFrame) -> pd.DataFrame:
    """Add per-engine Remaining Useful Life based on the final observed cycle."""
    result = cycles.copy()
    final_cycles = result.groupby("engine_id")["cycle"].transform("max")
    result["rul"] = final_cycles - result["cycle"]
    return result
