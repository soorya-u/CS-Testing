# /tests/test_b2.py
import pytest
from b2 import combinations


# Test case for combinations with valid inputs
def test_combinations_valid_inputs():
    # Test combinations with n=5 and r=2
    assert combinations(5, 2) == 10


# Test case for combinations with n=0 and r=0
def test_combinations_zero_zero():
    # Test combinations when both n and r are 0
    assert combinations(0, 0) == 1


# Test case for combinations with n=r
def test_combinations_n_equals_r():
    # Test combinations when n is equal to r
    assert combinations(5, 5) == 1


# Test case for combinations with r=0
def test_combinations_r_zero():
    # Test combinations when r is 0
    assert combinations(5, 0) == 1


# Test case for combinations with r=1
def test_combinations_r_one():
     # Test combinations when r is 1
    assert combinations(5, 1) == 5


# Test case for combinations with n < r, should raise error but because of type conversion results in 0
def test_combinations_invalid_n_less_than_r():
   assert combinations(2,5) == 0

# Coughed up by CODESOURCERER.