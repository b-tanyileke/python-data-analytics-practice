"""Optional self-checks for the Week 4 starter exercises.

Run from the repository root with:
python -m pytest week-04/check_your_work.py
"""

import importlib.util
import sys
from pathlib import Path


EXERCISE_ROOT = Path(__file__).parent / "exercises"


def load_exercise(relative_path, module_name):
    """Load a student exercise file so its functions can be checked."""
    module_path = EXERCISE_ROOT / relative_path
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
    """Check the number_category function."""
    exercise = load_exercise("beginner/exercise_01_number_category.py", "student_number_category")
    assert exercise.number_category(8) == "positive"
    assert exercise.number_category(-8) == "negative"
    assert exercise.number_category(0) == "zero"


def test_admission_message():
    """Check the admission_message function."""
    exercise = load_exercise("beginner/exercise_02_admission_check.py", "student_admission")
    assert exercise.admission_message(18, "yes") == "Admitted"
    assert exercise.admission_message(17, "yes") == "Not admitted"
    assert exercise.admission_message(21, "no") == "Not admitted"


def test_grade_label():
    """Check the grade_label function."""
    exercise = load_exercise("beginner/exercise_03_grade_label.py", "student_grade")
    assert exercise.grade_label(93) == "A"
    assert exercise.grade_label(84) == "B"
    assert exercise.grade_label(70) == "C"
    assert exercise.grade_label(69) == "Needs improvement"


def test_safe_division():
    """Check the divide_numbers function."""
    exercise = load_exercise("beginner/exercise_04_safe_division.py", "student_division")
    assert exercise.divide_numbers(12, 3) == 4
    assert exercise.divide_numbers(12, 0) == "Cannot divide by zero."


def test_distance_to_origin():
    """Check the distance_to_origin function."""
    exercise = load_exercise("beginner/exercise_05_distance_to_origin.py", "student_distance")
    assert exercise.distance_to_origin(3, 4) == 5


def test_order_total():
    """Check the order_total function."""
    exercise = load_exercise("intermediate/exercise_06_order_total.py", "student_order")
    assert exercise.order_total(25.0, 5, "yes") == 112.5
    assert exercise.order_total(25.0, 5, "no") == 125.0
    assert exercise.order_total(20.0, 4, "yes") == 80.0


def test_package_status():
    """Check the package_status function."""
    exercise = load_exercise("intermediate/exercise_07_package_status.py", "student_package")
    assert exercise.package_status("local", 5) == "Local standard"
    assert exercise.package_status("local", 5.1) == "Local heavy"
    assert exercise.package_status("international", 2) == "International standard"
    assert exercise.package_status("international", 2.1) == "International heavy"


def test_temperature_converter_module():
    """Check the temperature converter module."""
    tools = load_exercise("intermediate/conversion_tools.py", "conversion_tools")
    converter = load_exercise("intermediate/exercise_08_temperature_converter.py", "student_converter")
    assert tools.celsius_to_fahrenheit(20) == 68
    assert converter.convert_temperature(68, "F") == 20
    assert converter.convert_temperature(20, "C") == 68
    assert converter.convert_temperature(20, "K") == "Invalid scale"
