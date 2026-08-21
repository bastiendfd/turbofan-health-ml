"""Run a deterministic, synthetic-only turbofan RUL baseline experiment."""

import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from turbofan_health.features import add_remaining_useful_life
from turbofan_health.modeling import train_and_evaluate_rul_baseline
from turbofan_health.synthetic import generate_synthetic_turbofan_cycles


if __name__ == "__main__":
    cycles = generate_synthetic_turbofan_cycles(
        engine_count=20,
        cycles_per_engine=50,
        seed=42,
    )
    labeled_cycles = add_remaining_useful_life(cycles)
    report = train_and_evaluate_rul_baseline(
        labeled_cycles,
        feature_columns=["sensor_degradation"],
        test_engine_ids={16, 17, 18, 19, 20},
    )
    print(
        json.dumps(
            {
                "dataset": "synthetic demonstration data",
                "mae_cycles": round(report.mae, 3),
                "test_engine_count": report.test_engine_count,
                "train_engine_count": report.train_engine_count,
            },
            sort_keys=True,
        )
    )
