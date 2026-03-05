from calculator import Calculator

calc = Calculator()

def test_add():
    assert calc.add(5,3) == 8

def test_subtract():
    assert calc.subtract(10,4) == 6

def test_multiply():
    assert calc.multiply(6,7) == 42

def test_divide():
    assert calc.divide(8,2) == 4

def test_divide_by_zero():
    assert calc.divide(5,0) == "Error: Division by zero"

def test_negative_numbers():
    assert calc.add(-5,-3) == -8

def test_decimal_numbers():
    assert calc.multiply(2.5,2) == 5

def test_large_numbers():
    assert calc.add(1000000,2000000) == 3000000