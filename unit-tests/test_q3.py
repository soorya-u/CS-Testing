import pytest
import q3

def test_q3_output_correctness(capsys):
    q3.result = 10
    expected_output = 'Combinations of 5 items taken 2 at a time: 10\n'
    q3.print(f'Combinations of {q3.n} items taken {q3.r} at a time: {q3.result}')
    captured = capsys.readouterr()
    assert captured.out == expected_output

# Coughed up by CODESOURCERER