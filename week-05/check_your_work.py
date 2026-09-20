"""Optional self-checks for the Week 5 starter exercises.

Run from the repository root with:
python -m pytest week-05/check_your_work.py
"""

import importlib.util
import sys
from pathlib import Path


EXERCISE_ROOT = Path(__file__).parent / "exercises"


def load_exercise(relative_path, module_name):
    """Load a student exercise file so its functions can be checked."""
    module_path = EXERCISE_ROOT / relative_path
    specification = importlib.util.spec_from_file_location(module_name, module_path)
    if specification is None or specification.loader is None:
        raise ImportError(f"Unable to load exercise module from {module_path}")
    module = importlib.util.module_from_spec(specification)
    sys.modules[module_name] = module
    specification.loader.exec_module(module)
    return module


def test_running_total():
    """Check the sum_to_number function."""
    exercise = load_exercise("beginner/exercise_01_running_total.py", "student_running_total")
    assert exercise.sum_to_number(1) == 1
    assert exercise.sum_to_number(4) == 10
    assert exercise.sum_to_number(10) == 55


def test_sentinel_counter():
    """Check the count_before_stop function."""
    exercise = load_exercise("beginner/exercise_02_sentinel_counter.py", "student_sentinel")
    assert exercise.count_before_stop("data*analysis") == 4
    assert exercise.count_before_stop("Python") == 6
    assert exercise.count_before_stop("*start") == 0


def test_count_vowels():
    """Check the count_vowels function."""
    exercise = load_exercise("beginner/exercise_03_count_vowels.py", "student_vowels")
    assert exercise.count_vowels("Data Analytics") == 5
    assert exercise.count_vowels("PYTHON") == 1
    assert exercise.count_vowels("rhythms") == 0


def test_first_digit():
    """Check the first_digit function."""
    exercise = load_exercise("beginner/exercise_04_first_digit.py", "student_first_digit")
    assert exercise.first_digit("Room B204") == "2"
    assert exercise.first_digit("Version 3.11") == "3"
    assert exercise.first_digit("No digits here") == ""


def test_write_message(tmp_path):
    """Check the write_message function."""
    exercise = load_exercise("beginner/exercise_05_write_message.py", "student_message")
    filename = tmp_path / "message.txt"
    assert exercise.write_message("Welcome", filename) == 7
    assert filename.read_text() == "Welcome\n"


def test_number_file_summary(tmp_path):
    """Check the write_number_summary function."""
    exercise = load_exercise("intermediate/exercise_06_number_file_summary.py", "student_summary")
    input_filename = tmp_path / "numbers.txt"
    output_filename = tmp_path / "summary.txt"
    input_filename.write_text("8\n3\n12\n7\n")

    assert exercise.write_number_summary(input_filename, output_filename) == 7.5
    assert output_filename.read_text() == (
        "Count: 4\nTotal: 30\nSmallest: 3\nLargest: 12\nAverage: 7.50\n"
    )


def test_mailbox_analysis(tmp_path):
    """Check the count_sender_lines function."""
    exercise = load_exercise("intermediate/exercise_07_mailbox_analysis.py", "student_mailbox")
    filename = tmp_path / "mailbox.txt"
    filename.write_text(
        "From alex@example.com Tue Sep 1\n"
        "From: alex@example.com\n"
        "Hello class\n"
        "From sam@example.com Wed Sep 2\n"
    )

    assert exercise.count_sender_lines(filename) == 2


def test_multiplication_table(tmp_path):
    """Check the write_multiplication_table function."""
    exercise = load_exercise("intermediate/exercise_08_multiplication_table.py", "student_table")
    filename = tmp_path / "table.txt"

    assert exercise.write_multiplication_table(3, filename) == 9
    assert filename.read_text() == "1 2 3 \n2 4 6 \n3 6 9 \n"
