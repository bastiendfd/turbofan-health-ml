from turbofan_health.synthetic import generate_synthetic_turbofan_cycles


def test_synthetic_generator_creates_deterministic_engine_cycles() -> None:
    cycles = generate_synthetic_turbofan_cycles(engine_count=3, cycles_per_engine=4, seed=7)

    assert len(cycles) == 12
    assert set(cycles.columns) == {"engine_id", "cycle", "sensor_degradation"}
    assert cycles.groupby("engine_id")["cycle"].max().tolist() == [4, 4, 4]
