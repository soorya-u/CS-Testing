import pytest
import q3
from io import StringIO
import sys

def test_q3_output_correctness(capsys):
    # Redirect stdout to capture the print output
    # Call the script
    q3.result = 10
    old_stdout = sys.stdout
    sys.stdout = captured_output = StringIO()
    q3.print(f"Combinations of {q3.n} items taken {q3.r} at a time: {q3.result}")
    sys.stdout = old_stdout
    assert captured_output.getvalue().strip() == 'Combinations of 5 items taken 2 at a time: 10'




# Coughed up by CODESOURCERER