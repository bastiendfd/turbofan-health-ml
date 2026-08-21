import pandas as pd

from turbofan_health.features import add_remaining_useful_life


def test_add_remaining_useful_life_uses_last_cycle_per_engine() -> None:
    cycles = pd.DataFrame(
        {
            "engine_id": [1, 1, 1, 2, 2],
            "cycle": [1, 2, 3, 1, 2],
            "sensor_1": [0.1, 0.2, 0.3, 0.4, 0.5],
        }
    )

    result = add_remaining_useful_life(cycles)

    assert result["rul"].tolist() == [2, 1, 0, 1, 0]
