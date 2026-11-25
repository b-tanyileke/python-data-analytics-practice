"""Maintenance checks for the Week 10 sample solutions."""

import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("week10_checks", Path(__file__).parents[1] / "checks.py")
checks = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checks)


def test_clean():
    checks.check_clean("solutions")


def test_transform():
    checks.check_transform("solutions")


def test_bands():
    checks.check_bands("solutions")


def test_sample():
    checks.check_sample("solutions")
