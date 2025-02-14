import pytest
import q3
from io import StringIO
import sys


def test_q3_output_correctness(capsys):
    captured = capsys.readouterr()
    sys.stdout = StringIO()
    q3.result = 10.0
    q3.print = lambda s: sys.stdout.write(str(s) + '\n')
    try:
        q3.print(f"Combinations of {q3.n} items taken {q3.r} at a time: {q3.result}")
        output = sys.stdout.getvalue().strip()
    finally:
        sys.stdout = sys.__stdout__

    assert "Combinations of 5 items taken 2 at a time: 10.0" in output

# Coughed up by CODESOURCERER