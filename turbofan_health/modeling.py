"""Transparent baseline models for Remaining Useful Life experiments."""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error


@dataclass(frozen=True)
class RulBaselineReport:
    mae: float
    train_engine_count: int
    test_engine_count: int


def train_and_evaluate_rul_baseline(
    cycles: pd.DataFrame,
    *,
    feature_columns: list[str],
    test_engine_ids: set[int],
) -> RulBaselineReport:
    """Fit a linear baseline and evaluate it on engines unseen during training."""
    train = cycles.loc[~cycles["engine_id"].isin(test_engine_ids)]
    test = cycles.loc[cycles["engine_id"].isin(test_engine_ids)]
    if train.empty or test.empty:
        raise ValueError("Both training and test engines are required.")

    model = LinearRegression().fit(train[feature_columns], train["rul"])
    predictions = model.predict(test[feature_columns])
    return RulBaselineReport(
        mae=float(mean_absolute_error(test["rul"], predictions)),
        train_engine_count=int(train["engine_id"].nunique()),
        test_engine_count=int(test["engine_id"].nunique()),
    )
