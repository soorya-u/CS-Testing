import pytest
from q2 import combinations


def test_combinations_valid_input():
    assert combinations(5, 2) == 10


def test_combinations_edge_cases():
    assert combinations(0, 0) == 1
    assert combinations(5, 0) == 1


def test_combinations_same_n_and_r():
    assert combinations(5, 5) == 1


def test_combinations_r_greater_than_n():
    with pytest.raises(ValueError):
        combinations(2, 5)

# Coughed up by CODESOURCERER