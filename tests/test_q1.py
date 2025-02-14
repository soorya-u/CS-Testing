import pytest
from q1 import factorial


def test_factorial_positive_number():
  assert factorial(5) == 120


def test_factorial_zero():
  assert factorial(0) == 1


def test_factorial_one():
  assert factorial(1) == 1


def test_factorial_large_number():
    assert factorial(10) == 3628800

# Coughed up by CODESOURCERER