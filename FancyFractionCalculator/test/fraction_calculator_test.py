import unittest

from FancyFractionCalculator.exceptions import DoNotDivideByZeroDude, ElementNotAFraction
from FancyFractionCalculator.fraction import Fraction
from FancyFractionCalculator.fraction_calculator import fraction_addition, fraction_substraction, add_int, \
    fraction_multiplication, fraction_division


# Assertions are going to be slightly different depending on the amount of logging vs simplicity required.
# Showing both examples, but the ideal scenario is adapting it to each team needs / wants.
class LinkedListTest(unittest.TestCase):
    def test_add_fractions_with_string(self):
        fraction1 = Fraction(2, 3)

        with self.assertRaises(ElementNotAFraction):
            fraction_addition(fraction1, "1 / 3")

    def test_add_fractions_with_int(self):
        fraction1 = Fraction(2, 3)

        with self.assertRaises(ElementNotAFraction):
            fraction_addition(fraction1, -3)

    def test_add_same_denominator(self):
        fraction1 = Fraction(2, 3)
        fraction2 = Fraction(3, 3)

        result = fraction_addition(fraction1, fraction2)
        assert str(result) == "5 / 3"

    def test_add_different_denominator(self):
        fraction1 = Fraction(2, 3)
        fraction2 = Fraction(3, 2)

        result = fraction_addition(fraction1, fraction2)
        assert str(result) == "13 / 6"

    def test_add_returns_canon(self):
        fraction1 = Fraction(10, 5)
        fraction2 = Fraction(2, 3)

        result = fraction_addition(fraction1, fraction2)
        assert str(result) == "8 / 3"

    def test_add_negative_fraction(self):
        fraction1 = Fraction(1, 2)
        fraction2 = Fraction(-1, 4)

        result = fraction_addition(fraction1, fraction2)
        assert str(result) == "1 / 4"

    def test_add_negative_result(self):
        fraction1 = Fraction(-1, 2)
        fraction2 = Fraction(1, 4)

        result = fraction_addition(fraction1, fraction2)
        assert str(result) == "-1 / 4"

    # This require less tests because I know the implementation. Use the same as add!
    def test_substract_positive(self):
        fraction1 = Fraction(1, 4)
        fraction2 = Fraction(1, 2)

        result = fraction_substraction(fraction1, fraction2)
        assert str(result) == "-1 / 4"

    def test_substract_negative(self):
        fraction1 = Fraction(1, 4)
        fraction2 = Fraction(-1, 2)

        result = fraction_substraction(fraction1, fraction2)
        assert str(result) == "3 / 4"

    def test_multiply_fractions_with_string(self):
        fraction1 = Fraction(2, 3)

        with self.assertRaises(ElementNotAFraction):
            fraction_multiplication(fraction1, "1 / 3")

    def test_multiply_fractions_with_int(self):
        fraction1 = Fraction(2, 3)

        with self.assertRaises(ElementNotAFraction):
            fraction_multiplication(-3, fraction1)

    def test_multiply_unity(self):
        fraction1 = Fraction(1, 4)
        fraction2 = Fraction(2, 2)

        result = fraction_multiplication(fraction1, fraction2)
        assert str(result) == "1 / 4"

    def test_multiply_positive(self):
        fraction1 = Fraction(1, 4)
        fraction2 = Fraction(3, 2)

        result = fraction_multiplication(fraction1, fraction2)
        assert str(result) == "3 / 8"

    def test_multiply_negative(self):
        fraction1 = Fraction(1, 4)
        fraction2 = Fraction(-9, 2)

        result = fraction_multiplication(fraction1, fraction2)
        assert str(result) == "-9 / 8"

    def test_divide_unity(self):
        fraction1 = Fraction(1, 4)
        fraction2 = Fraction(2, 2)

        result = fraction_division(fraction1, fraction2)
        assert str(result) == "1 / 4"

    def test_divide_positive(self):
        fraction1 = Fraction(1, 4)
        fraction2 = Fraction(3, 2)

        result = fraction_division(fraction1, fraction2)
        assert str(result) == "1 / 6"

    def test_divide_negative(self):
        fraction1 = Fraction(1, 4)
        fraction2 = Fraction(-9, 2)

        result = fraction_multiplication(fraction1, fraction2)
        assert str(result) == "-9 / 8"

    def test_divide_by_0(self):
        fraction1 = Fraction(1, 4)
        fraction2 = Fraction(0, 2)

        with self.assertRaises(DoNotDivideByZeroDude):
            fraction_division(fraction1, fraction2)

    # Extra
    def test_add_int(self):
        fraction1 = Fraction(1, 2)

        result = add_int(fraction1, 3)
        assert str(result) == "7 / 2"


if __name__ == '__main__':
    unittest.main()
