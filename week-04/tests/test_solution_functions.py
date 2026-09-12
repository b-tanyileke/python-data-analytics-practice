"""Maintenance tests for the Week 4 sample solutions."""

import importlib.util
import sys
from pathlib import Path


SOLUTION_ROOT = Path(__file__).parents[1] / "solutions"


def load_solution(relative_path, module_name):
    """Loads a solution module from the specified relative path."""
    module_path = SOLUTION_ROOT / relative_path
    sys.path.insert(0, str(module_path.parent))
    try:
        specification = importlib.util.spec_from_file_location(module_name, module_path)
        module = importlib.util.module_from_spec(specification)
        sys.modules[module_name] = module
        specification.loader.exec_module(module)
        return module
    finally:
        sys.path.pop(0)


def test_number_category():
    """Tests the number_category function from exercise_01_number_category.py."""

    solution = load_solution("beginner/exercise_01_number_category.py", "number_category_solution")
    assert solution.number_category(8) == "positive"
    assert solution.number_category(-8) == "negative"
    assert solution.number_category(0) == "zero"


def test_admission_message():
    """Tests the admission_message function from exercise_02_admission_check.py."""

    solution = load_solution("beginner/exercise_02_admission_check.py", "admission_solution")
    assert solution.admission_message(18, "yes") == "Admitted"
    assert solution.admission_message(17, "yes") == "Not admitted"
    assert solution.admission_message(21, "no") == "Not admitted"


def test_grade_label():
    """Tests the grade_label function from exercise_03_grade_label.py."""

    solution = load_solution("beginner/exercise_03_grade_label.py", "grade_solution")
    assert solution.grade_label(93) == "A"
    assert solution.grade_label(84) == "B"
    assert solution.grade_label(70) == "C"
    assert solution.grade_label(69) == "Needs improvement"


def test_safe_division():
    """Tests the divide_numbers function from exercise_04_safe_division.py."""

    solution = load_solution("beginner/exercise_04_safe_division.py", "division_solution")
    assert solution.divide_numbers(12, 3) == 4
    assert solution.divide_numbers(12, 0) == "Cannot divide by zero."


def test_distance_to_origin():
    """Tests the distance_to_origin function from exercise_05_distance_to_origin.py."""

    solution = load_solution("beginner/exercise_05_distance_to_origin.py", "distance_solution")
    assert solution.distance_to_origin(3, 4) == 5


def test_order_total():
    """Tests the order_total function from exercise_06_order_total.py."""

    solution = load_solution("intermediate/exercise_06_order_total.py", "order_solution")
    assert solution.order_total(25.0, 5, "yes") == 112.5
    assert solution.order_total(25.0, 5, "no") == 125.0
    assert solution.order_total(20.0, 4, "yes") == 80.0


def test_package_status():
    """Tests the package_status function from exercise_07_package_status.py."""

    solution = load_solution("intermediate/exercise_07_package_status.py", "package_solution")
    assert solution.package_status("local", 5) == "Local standard"
    assert solution.package_status("local", 5.1) == "Local heavy"
    assert solution.package_status("international", 2) == "International standard"
    assert solution.package_status("international", 2.1) == "International heavy"


def test_temperature_converter_module():
    """Tests the conversion functions from exercise_08_temperature_converter.py."""

    tools = load_solution("intermediate/conversion_tools.py", "conversion_tools")
    converter = load_solution("intermediate/exercise_08_temperature_converter.py", "converter_solution")
    assert tools.celsius_to_fahrenheit(20) == 68
    assert converter.convert_temperature(68, "F") == 20
    assert converter.convert_temperature(20, "C") == 68
    assert converter.convert_temperature(20, "K") == "Invalid scale"
