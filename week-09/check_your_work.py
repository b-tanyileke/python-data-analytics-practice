"""Optional self-checks: python -m pytest week-09/check_your_work.py."""

import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("week09_checks", Path(__file__).parent / "checks.py")
checks = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checks)


def test_series():
    checks.check_series("exercises")


def test_missing():
    checks.check_missing("exercises")


def test_scores():
    checks.check_scores("exercises")


def test_categories():
    checks.check_categories("exercises")
