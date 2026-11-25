"""Optional self-checks: python -m pytest week-10/check_your_work.py."""

import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("week10_checks", Path(__file__).parent / "checks.py")
checks = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checks)


def test_clean():
    checks.check_clean("exercises")


def test_transform():
    checks.check_transform("exercises")


def test_bands():
    checks.check_bands("exercises")


def test_sample():
    checks.check_sample("exercises")
