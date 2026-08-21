import json
import subprocess
import sys
from pathlib import Path


def test_synthetic_experiment_script_outputs_honest_metrics() -> None:
    repository_root = Path(__file__).resolve().parents[1]
    completed = subprocess.run(
        [sys.executable, "scripts/run_synthetic_experiment.py"],
        cwd=repository_root,
        capture_output=True,
        text=True,
        check=False,
    )

    assert completed.returncode == 0, completed.stderr
    report = json.loads(completed.stdout)
    assert report["dataset"] == "synthetic demonstration data"
    assert report["train_engine_count"] > 0
    assert report["test_engine_count"] > 0
    assert report["mae_cycles"] >= 0
