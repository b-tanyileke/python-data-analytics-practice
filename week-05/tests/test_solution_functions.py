"""Maintenance tests for the Week 5 sample solutions."""

import importlib.util
import sys
from pathlib import Path


SOLUTION_ROOT = Path(__file__).parents[1] / "solutions"


def load_solution(relative_path, module_name):
    """Load a sample solution module from the specified relative path."""
    module_path = SOLUTION_ROOT / relative_path
    specification = importlib.util.spec_from_file_location(module_name, module_path)
    if specification is None or specification.loader is None:
        raise ImportError(f"Unable to load solution module from {module_path}")
    module = importlib.util.module_from_spec(specification)
    sys.modules[module_name] = module
    specification.loader.exec_module(module)
    return module


def test_running_total():
    """Test the sum_to_number function."""
    solution = load_solution("beginner/exercise_01_running_total.py", "running_total_solution")
    assert solution.sum_to_number(1) == 1
    assert solution.sum_to_number(4) == 10
    assert solution.sum_to_number(10) == 55


def test_sentinel_counter():
    """Test the count_before_stop function."""
    solution = load_solution("beginner/exercise_02_sentinel_counter.py", "sentinel_solution")
    assert solution.count_before_stop("data*analysis") == 4
    assert solution.count_before_stop("Python") == 6
    assert solution.count_before_stop("*start") == 0


def test_count_vowels():
    """Test the count_vowels function."""
    solution = load_solution("beginner/exercise_03_count_vowels.py", "vowels_solution")
    assert solution.count_vowels("Data Analytics") == 5
    assert solution.count_vowels("PYTHON") == 1
    assert solution.count_vowels("rhythms") == 0


def test_first_digit():
    """Test the first_digit function."""
    solution = load_solution("beginner/exercise_04_first_digit.py", "first_digit_solution")
    assert solution.first_digit("Room B204") == "2"
    assert solution.first_digit("Version 3.11") == "3"
    assert solution.first_digit("No digits here") == ""


def test_write_message(tmp_path):
    """Test the write_message function."""
    solution = load_solution("beginner/exercise_05_write_message.py", "message_solution")
    filename = tmp_path / "message.txt"
    assert solution.write_message("Welcome", filename) == 7
    assert filename.read_text() == "Welcome\n"


def test_number_file_summary(tmp_path):
    """Test the write_number_summary function."""
    solution = load_solution("intermediate/exercise_06_number_file_summary.py", "summary_solution")
    input_filename = tmp_path / "numbers.txt"
    output_filename = tmp_path / "summary.txt"
    input_filename.write_text("8\n3\n12\n7\n")

    assert solution.write_number_summary(input_filename, output_filename) == 7.5
    assert output_filename.read_text() == (
        "Count: 4\nTotal: 30\nSmallest: 3\nLargest: 12\nAverage: 7.50\n"
    )


def test_mailbox_analysis(tmp_path):
    """Test the count_sender_lines function."""
    solution = load_solution("intermediate/exercise_07_mailbox_analysis.py", "mailbox_solution")
    filename = tmp_path / "mailbox.txt"
    filename.write_text(
        "From alex@example.com Tue Sep 1\n"
        "From: alex@example.com\n"
        "Hello class\n"
        "From sam@example.com Wed Sep 2\n"
    )

    assert solution.count_sender_lines(filename) == 2


def test_multiplication_table(tmp_path):
    """Test the write_multiplication_table function."""
    solution = load_solution("intermediate/exercise_08_multiplication_table.py", "table_solution")
    filename = tmp_path / "table.txt"

    assert solution.write_multiplication_table(3, filename) == 9
    assert filename.read_text() == "1 2 3 \n2 4 6 \n3 6 9 \n"
