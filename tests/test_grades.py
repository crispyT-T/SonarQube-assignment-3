
import pytest

from src.grades import (
    calculate_average,
    get_letter_grade,
    generate_report,
    find_highest_grade,
    find_lowest_grade
)


def test_calculate_average():
    assert calculate_average([80, 90, 100]) == 90


def test_empty_grades():
    assert calculate_average([]) == 0


def test_letter_grade():
    assert get_letter_grade(95) == "A"
    assert get_letter_grade(85) == "B"
    assert get_letter_grade(75) == "C"
    assert get_letter_grade(65) == "D"
    assert get_letter_grade(45) == "F"


def test_generate_report():
    report = generate_report("Amna", [80, 90, 100])
    assert report["average"] == 90
    assert report["letter"] == "A"
    assert report["status"] == "Pass"


def test_highest_grade():
    assert find_highest_grade([70, 85, 95]) == 95


def test_lowest_grade():
    assert find_lowest_grade([70, 85, 95]) == 70


def test_lowest_grade_empty_list():
    assert find_lowest_grade([]) is None


def test_invalid_grade_above_100():
    with pytest.raises(ValueError):
        calculate_average([80, 120])

def test_negative_grade():
    with pytest.raises(ValueError):
        calculate_average([80, -10])


def test_non_numeric_grade():
    with pytest.raises(ValueError):
        calculate_average([80, "invalid"])


def test_boolean_grade():
    with pytest.raises(ValueError):
        calculate_average([80, True])


def test_valid_grade_boundaries():
    assert calculate_average([0, 100]) == 50
