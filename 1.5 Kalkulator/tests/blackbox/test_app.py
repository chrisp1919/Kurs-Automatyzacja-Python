import subprocess


def test_addition():
    result = subprocess.run(['python', 'main.py', '2', '+', '3'], stdout=subprocess.PIPE)
    assert result.stdout.decode('utf-8') == '5\r\n'


def test_subtract():
    result = subprocess.run(['python', 'main.py', '2', '-', '3'], stdout=subprocess.PIPE)
    assert result.stdout.decode('utf-8') == '-1\r\n'


def test_multiply():
    result = subprocess.run(['python', 'main.py', '3', 'x', '2'], stdout=subprocess.PIPE)
    assert result.stdout.decode('utf-8') == '6\r\n'


def test_multiply_by_zero():
    result = subprocess.run(['python', 'main.py', '3', 'x', '0'], stdout=subprocess.PIPE)
    assert result.stdout.decode('utf-8') == '0\r\n'


def test_multiply_float():
    result = subprocess.run(['python', 'main.py', '3.5', 'x', '5.2'], stdout=subprocess.PIPE)
    assert result.stdout.decode('utf-8') == '0\r\n'


def test_divide():
    result = subprocess.run(['python', 'main.py', '3', '/', '2'], stdout=subprocess.PIPE)
    assert result.stdout.decode('utf-8') == '1.5\r\n'


def test_divide_by_zero():
    result = subprocess.run(['python', 'main.py', '3', '/', '0'], stdout=subprocess.PIPE)
    assert result.stdout.decode('utf-8') == '?'


def test_invalid_literal_for_int():
    result = subprocess.run(['python', 'main.py', 'ala', '+', '3'], stdout=subprocess.PIPE)
    assert result.stdout.decode('utf-8') == '?'


def test_not_enough_values():
    result = subprocess.run(['python', 'main.py', '2', '5'], stdout=subprocess.PIPE)
    assert result.stdout.decode('utf-8') == '?'


def test_to_many_values():
    result = subprocess.run(['python', 'main.py', '2', '+', '3', '5'], stdout=subprocess.PIPE)
    assert result.stdout.decode('utf-8') == '?'



