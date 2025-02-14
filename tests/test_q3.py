import pytest
import q3
from io import StringIO
import sys


def test_q3_output(monkeypatch):
    captured_output = StringIO()
    monkeypatch.setattr('sys.stdout', captured_output)
    q3  # Execute the script
    assert captured_output.getvalue() == 'Combinations of 5 items taken 2 at a time: 10.0\n'

# Coughed up by CODESOURCERER