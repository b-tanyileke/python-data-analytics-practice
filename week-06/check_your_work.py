"""Optional self-checks for the Week 6 starter exercises.

Run from the repository root with:
python -m pytest week-06/check_your_work.py
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


def test_list_average():
    """Check the calculate_average function."""
    exercise = load_exercise("beginner/exercise_01_list_average.py", "student_list_average")
    assert exercise.calculate_average([6, 8, 10]) == 8.0
    assert exercise.calculate_average([2, 5, 9, 4]) == 5.0
    assert exercise.calculate_average([7]) == 7.0


def test_copy_and_add():
    """Check the copy_and_add function without accepting list mutation."""
    exercise = load_exercise("beginner/exercise_02_copy_and_add.py", "student_copy_and_add")
    items = ["pen", "paper"]
    assert exercise.copy_and_add(items, "folder") == ["pen", "paper", "folder"]
    assert items == ["pen", "paper"]
    assert exercise.copy_and_add(items, "pen") == ["pen", "paper"]


def test_word_counts():
    """Check the count_words function."""
    exercise = load_exercise("beginner/exercise_03_word_counts.py", "student_word_counts")
    assert exercise.count_words(["data", "python", "data", "code"]) == {
        "data": 2,
        "python": 1,
        "code": 1,
    }
    assert exercise.count_words([]) == {}


def test_format_coordinate():
    """Check the format_coordinate function."""
    exercise = load_exercise("beginner/exercise_04_format_coordinate.py", "student_coordinate")
    assert exercise.format_coordinate((3, 4)) == "x=3, y=4"
    assert exercise.format_coordinate((-2, 5.5)) == "x=-2, y=5.5"


def test_read_names(tmp_path):
    """Check the read_names function."""
    exercise = load_exercise("beginner/exercise_05_read_names.py", "student_names")
    filename = tmp_path / "names.txt"
    filename.write_text("Amara\n\nDiego\nLin\n")
    assert exercise.read_names(filename) == ["Amara", "Diego", "Lin"]


def test_score_summary():
    """Check the score_summary function."""
    exercise = load_exercise("intermediate/exercise_06_score_summary.py", "student_scores")
    assert exercise.score_summary({"Amina": 92, "Diego": 85, "Lin": 97}) == (
        "Lin",
        274 / 3,
    )
    assert exercise.score_summary({"Noah": 80}) == ("Noah", 80.0)


def test_update_inventory():
    """Check the update_inventory function without accepting dictionary mutation."""
    exercise = load_exercise("intermediate/exercise_07_update_inventory.py", "student_inventory")
    inventory = {"pens": 20, "notebooks": 12}
    sales = {"pens": 3, "notebooks": 5}
    assert exercise.update_inventory(inventory, sales) == {"pens": 17, "notebooks": 7}
    assert inventory == {"pens": 20, "notebooks": 12}


def test_row_totals():
    """Check the row_totals function."""
    exercise = load_exercise("intermediate/exercise_08_row_totals.py", "student_row_totals")
    assert exercise.row_totals([[1, 2, 3], [4, 5, 6]]) == [6, 15]
    assert exercise.row_totals([[10], [2, 3], [4, 1, 5]]) == [10, 5, 10]
    assert exercise.row_totals([]) == []
