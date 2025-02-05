import pytest
import q3
from io import StringIO
import sys


def test_q3_output(capsys):
    # Capture stdout
    sys.stdout = captured_output = StringIO()
    q3.result # calling this calculates result so the captured output has access
    sys.stdout = sys.__stdout__ # Reset stdout

    assert captured_output.getvalue().strip() == 'Combinations of 5 items taken 2 at a time: 10.0'

# Coughed up by CODESOURCERER