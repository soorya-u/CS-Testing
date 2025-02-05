import pytest
from q2 import combinations


def test_combinations_valid_input():
  assert combinations(5, 2) == 10


def test_combinations_same_numbers():
  assert combinations(5, 5) == 1


def test_combinations_r_zero():
  assert combinations(5, 0) == 1


def test_combinations_n_zero():
  assert combinations(0, 0) == 1


# Coughed up by CODESOURCERER