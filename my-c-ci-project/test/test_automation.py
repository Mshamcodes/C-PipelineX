import subprocess
import pytest

def run_calculator(expression):
    proc = subprocess.Popen(['../calculator'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, cwd='../src')
    out, err = proc.communicate(expression + '\n')
    return out, err, proc.returncode

def test_add():
    out, err, code = run_calculator('2 + 2')
    assert 'Result: 4.00' in out
    assert code == 0

def test_subtract():
    out, err, code = run_calculator('5 - 3')
    assert 'Result: 2.00' in out
    assert code == 0

def test_multiply():
    out, err, code = run_calculator('3 * 4')
    assert 'Result: 12.00' in out
    assert code == 0

def test_divide():
    out, err, code = run_calculator('10 / 2')
    assert 'Result: 5.00' in out
    assert code == 0

def test_divide_by_zero():
    out, err, code = run_calculator('10 / 0')
    assert 'Error: Division by zero!' in out
    assert code == 1
