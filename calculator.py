"""
Calculator Module - Application Code
Contains core mathematical operations and input validation.
"""


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b 


def subtract(a: float, b: float) -> float:
    """Return the difference of two numbers."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return the division of a by b.
    
    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
