"""
Automated Test Suite for Calculator Module
Uses pytest to verify normal and boundary operations.
"""

import pytest
from calculator import add, subtract, multiply, divide


# --- Tests for Addition ---
def test_add_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-1, -1) == -2


def test_add_with_zero():
    assert add(5, 0) == 5


def test_add_floating_point():
    assert add(1.5, 2.5) == 4.0


# --- Tests for Subtraction ---
def test_subtract_positive_numbers():
    assert subtract(10, 4) == 6


def test_subtract_negative_numbers():
    assert subtract(-5, -5) == 0


def test_subtract_resulting_in_negative():
    assert subtract(3, 7) == -4


# --- Tests for Multiplication ---
def test_multiply_positive_numbers():
    assert multiply(3, 4) == 12


def test_multiply_by_zero():
    assert multiply(10, 0) == 0


def test_multiply_negative_numbers():
    assert multiply(-2, 3) == -6
    assert multiply(-2, -3) == 6


# --- Tests for Division ---
def test_divide_valid_numbers():
    assert divide(10, 2) == 5.0
    assert divide(9, 2) == 4.5


def test_divide_negative_numbers():
    assert divide(-10, 2) == -5.0


def test_divide_by_zero_raises_exception():
    """Verify that dividing by zero raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        divide(10, 0)
