"""Calculator class."""


class Calc:
    """Calculator class to complete basic equations."""

    def __init__(self):
        """Initialise calculator instance."""
        self.result = 0

    def __str__(self):
        """Return last calculation result."""
        return str(self.result)

    def multiply_nums(self, number_1, number_2):
        """Multiply number 1 by number 2."""
        self.result = number_1 * number_2
        return self.result

    def add_nums(self, number_1, number_2):
        """Add number 1 and number 2."""
        self.result = number_1 + number_2
        return self.result

    def subtract_nums(self, number_1, number_2):
        """Minus number 2 from number 1."""
        self.result = number_1 - number_2
        return self.result

    def divide_nums(self, number_1, number_2):
        """Divide number 1 by number 2."""
        if not number_2 == 0:
            self.result = number_1 / number_2
            return self.result
        else:
            return "Cannot Divide by zero!"
