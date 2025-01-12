# /tests/test_b1.py
import pytest
from b1 import factorial


# Test case for factorial with a positive integer
def test_factorial_positive_integer():
    # Test factorial of 5
    assert factorial(5) == 120


# Test case for factorial with zero
def test_factorial_zero():
    # Test factorial of 0
    assert factorial(0) == 1


# Test case for factorial with one
def test_factorial_one():
    # Test factorial of 1
    assert factorial(1) == 1


# Test case for factorial with a larger integer
def test_factorial_large_integer():
    # Test factorial of 10
    assert factorial(10) == 3628800

# Coughed up by CODESOURCERER.