"""Synthetic turbofan-like cycles for reproducible local demonstrations."""

from __future__ import annotations

import numpy as np
import pandas as pd


def generate_synthetic_turbofan_cycles(
    *, engine_count: int = 20, cycles_per_engine: int = 50, seed: int = 42
) -> pd.DataFrame:
    """Create fictional cycle data with a monotonic degradation signal and small noise."""
    if engine_count < 2 or cycles_per_engine < 2:
        raise ValueError("At least two engines and two cycles per engine are required.")

    random = np.random.default_rng(seed)
    rows: list[dict[str, float | int]] = []
    for engine_id in range(1, engine_count + 1):
        baseline = random.normal(100.0, 1.0)
        for cycle in range(1, cycles_per_engine + 1):
            degradation = baseline - cycle * 0.35 + random.normal(0.0, 0.08)
            rows.append(
                {
                    "engine_id": engine_id,
                    "cycle": cycle,
                    "sensor_degradation": degradation,
                }
            )
    return pd.DataFrame(rows)
