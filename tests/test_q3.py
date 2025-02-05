import pytest
import subprocess

def test_q3_output():
    result = subprocess.run(['python', 'q3.py'], capture_output=True, text=True, check=True)
    assert "Combinations of 5 items taken 2 at a time: 10.0" in result.stdout

# Coughed up by CODESOURCERER