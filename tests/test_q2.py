import pytest
from q2 import combinations


def test_combinations_valid_input():
    assert combinations(5, 2) == 10.0


def test_combinations_edge_cases():
    assert combinations(0, 0) == 1.0
    assert combinations(5, 0) == 1.0
    assert combinations(5, 5) == 1.0



# Coughed up by CODESOURCERER