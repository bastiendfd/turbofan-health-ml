import pandas as pd

from turbofan_health.features import add_remaining_useful_life
from turbofan_health.modeling import train_and_evaluate_rul_baseline


def test_rul_baseline_evaluates_on_unseen_engine() -> None:
    rows = []
    for engine_id in range(1, 5):
        for cycle in range(1, 6):
            rul = 5 - cycle
            rows.append(
                {
                    "engine_id": engine_id,
                    "cycle": cycle,
                    "sensor_degradation": 100 - rul * 3,
                }
            )
    cycles = add_remaining_useful_life(pd.DataFrame(rows))

    report = train_and_evaluate_rul_baseline(
        cycles,
        feature_columns=["sensor_degradation"],
        test_engine_ids={4},
    )

    assert report.train_engine_count == 3
    assert report.test_engine_count == 1
    assert report.mae == 0.0
