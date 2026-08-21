from pathlib import Path

from turbofan_health.cmapss import load_cmapss_text


def test_load_cmapss_text_assigns_engine_cycle_settings_and_sensors(tmp_path: Path) -> None:
    source = tmp_path / "train_FD001.txt"
    first_row = " ".join(str(value) for value in range(1, 27))
    second_row = " ".join(str(value) for value in range(27, 53))
    source.write_text(f"{first_row}\n{second_row}\n", encoding="utf-8")

    cycles = load_cmapss_text(source)

    assert cycles.shape == (2, 26)
    assert cycles.loc[0, "engine_id"] == 1
    assert cycles.loc[0, "cycle"] == 2
    assert cycles.loc[0, "setting_1"] == 3
    assert cycles.loc[0, "sensor_21"] == 26
