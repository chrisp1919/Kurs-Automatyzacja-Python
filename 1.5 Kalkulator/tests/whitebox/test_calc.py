from src.calc import Calculator


def test_addition():
    calc = Calculator()
    assert calc.add(2, 3) == 5


def test_subtract():
    calc = Calculator()
    assert calc.sub(2, 3) == -1


def test_multiply():
    calc = Calculator()
    assert calc.mul(2, 3) == 6


def test_divide():
    calc = Calculator()
    assert calc.div(2, 4) == 0.5


def test_multiply_by_zero():
    calc = Calculator()
    assert calc.mul(2, 0) == 0


def test_divide_by_zero():
        calc = Calculator()
        assert calc.div(10, 0) == 0


def test_addition_float():
    calc = Calculator()
    assert calc.add(2.5, 5.55) == 8.05


def test_subtract_float():
    calc = Calculator()
    assert calc.sub(2.5, 5.55) == -3.05


def test_multiply_float():
    calc = Calculator()
    assert calc.mul(2.5, 5.55) == 13.875


def test_divide_flaot():
    calc = Calculator()
    assert calc.div(2.5, 5.5) == 0.45


def test_divide_by_unsupported_value():
    calc = Calculator()
    assert calc.div(2, "aaa") == 2


def test_divid_not_enough_values():
    calc = Calculator()
    assert calc.div(2) == 2


def test_divid_to_many_values():
    calc = Calculator()
    assert calc.div(2, 2, 2) == 0.5