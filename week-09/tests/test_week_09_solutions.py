"""Maintenance checks for the Week 9 sample solutions."""

import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("week09_checks", Path(__file__).parents[1] / "checks.py")
checks = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checks)


def test_series():
    checks.check_series("solutions")


def test_missing():
    checks.check_missing("solutions")


def test_scores():
    checks.check_scores("solutions")


def test_categories():
    checks.check_categories("solutions")
