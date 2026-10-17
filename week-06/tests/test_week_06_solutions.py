"""Maintenance tests for the Week 6 sample solutions."""

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


def test_list_average():
    """Test the calculate_average function."""
    solution = load_solution("beginner/exercise_01_list_average.py", "list_average_solution")
    assert solution.calculate_average([6, 8, 10]) == 8.0
    assert solution.calculate_average([2, 5, 9, 4]) == 5.0
    assert solution.calculate_average([7]) == 7.0


def test_copy_and_add():
    """Test the copy_and_add function without accepting list mutation."""
    solution = load_solution("beginner/exercise_02_copy_and_add.py", "copy_and_add_solution")
    items = ["pen", "paper"]
    assert solution.copy_and_add(items, "folder") == ["pen", "paper", "folder"]
    assert items == ["pen", "paper"]
    assert solution.copy_and_add(items, "pen") == ["pen", "paper"]


def test_word_counts():
    """Test the count_words function."""
    solution = load_solution("beginner/exercise_03_word_counts.py", "word_counts_solution")
    assert solution.count_words(["data", "python", "data", "code"]) == {
        "data": 2,
        "python": 1,
        "code": 1,
    }
    assert solution.count_words([]) == {}


def test_format_coordinate():
    """Test the format_coordinate function."""
    solution = load_solution("beginner/exercise_04_format_coordinate.py", "coordinate_solution")
    assert solution.format_coordinate((3, 4)) == "x=3, y=4"
    assert solution.format_coordinate((-2, 5.5)) == "x=-2, y=5.5"


def test_read_names(tmp_path):
    """Test the read_names function."""
    solution = load_solution("beginner/exercise_05_read_names.py", "names_solution")
    filename = tmp_path / "names.txt"
    filename.write_text("Amara\n\nDiego\nLin\n")
    assert solution.read_names(filename) == ["Amara", "Diego", "Lin"]


def test_score_summary():
    """Test the score_summary function."""
    solution = load_solution("intermediate/exercise_06_score_summary.py", "score_summary_solution")
    assert solution.score_summary({"Amina": 92, "Diego": 85, "Lin": 97}) == (
        "Lin",
        274 / 3,
    )
    assert solution.score_summary({"Noah": 80}) == ("Noah", 80.0)


def test_update_inventory():
    """Test the update_inventory function without accepting dictionary mutation."""
    solution = load_solution("intermediate/exercise_07_update_inventory.py", "inventory_solution")
    inventory = {"pens": 20, "notebooks": 12}
    sales = {"pens": 3, "notebooks": 5}
    assert solution.update_inventory(inventory, sales) == {"pens": 17, "notebooks": 7}
    assert inventory == {"pens": 20, "notebooks": 12}


def test_row_totals():
    """Test the row_totals function."""
    solution = load_solution("intermediate/exercise_08_row_totals.py", "row_totals_solution")
    assert solution.row_totals([[1, 2, 3], [4, 5, 6]]) == [6, 15]
    assert solution.row_totals([[10], [2, 3], [4, 1, 5]]) == [10, 5, 10]
    assert solution.row_totals([]) == []
