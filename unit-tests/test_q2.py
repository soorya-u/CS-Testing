import pytest
from q2 import combinations


def test_combinations_valid():
    assert combinations(5, 2) == 10


def test_combinations_same():
    assert combinations(5, 5) == 1


def test_combinations_zero_r():
    assert combinations(5, 0) == 1


def test_combinations_zero_n():
    assert combinations(0, 0) == 1


def test_combinations_invalid():
    with pytest.raises(Exception):
        combinations(2, 5)

# Coughed up by CODESOURCERER