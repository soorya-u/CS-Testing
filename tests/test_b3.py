# /tests/test_b3.py
import pytest
from b3 import combinations


# Test case for testing the output of b3
def test_b3_output(capsys):
     # Test that the output is correct
    import b3
    captured = capsys.readouterr()
    assert "Combinations of 5 items taken 2 at a time: 10.0\n" == captured.out

# Coughed up by CODESOURCERER.