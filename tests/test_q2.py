import pytest
from q2 import combinations


def test_combinations_valid_input():
    assert combinations(5, 2) == 10


def test_combinations_n_equals_r():
    assert combinations(5, 5) == 1


def test_combinations_r_equals_zero():
    assert combinations(5, 0) == 1


def test_combinations_r_greater_than_n():
    with pytest.raises(Exception):
        combinations(2, 5)

# Coughed up by CODESOURCERER