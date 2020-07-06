"""Tests for Calc class."""
from calculator.calc import Calc


def main():
    """Test Calc class."""

    # Initialise calculator instance
    calculator = Calc()

    # Define variables
    x = 5
    y = 10

    # Method Tests
    multiply_ans = calculator.multiply_nums(x, y)
    assert multiply_ans == 50

    divide_ans = calculator.divide_nums(y, x)
    assert divide_ans == 2

    add_ans = calculator.add_nums(x, y)
    assert add_ans == 15

    subtract_ans = calculator.subtract_nums(y, x)
    assert subtract_ans == 5


if __name__ == '__main__':
    main()
