import unittest

from FancyFractionCalculator.exceptions import NumberNeedsToBeIntError, DoNotDivideByZeroDude
from FancyFractionCalculator.fraction import Fraction


# Assertions are going to be slightly different depending on the amount of logging vs simplicity required.
# Showing both examples, but the ideal scenario is adapting it to each team needs / wants.
class LinkedListTest(unittest.TestCase):
    def test_fraction_init_with_numerator_and_denominator(self):
        fraction = Fraction(1, 2)

        assert fraction.numerator == 1
        assert fraction.denominator == 2
        assert str(fraction) == "1 / 2"

    def test_fraction_init_only_with_numerator(self):
        fraction = Fraction(3)

        assert fraction.numerator == 3
        assert fraction.denominator == 1
        assert str(fraction) == "3 / 1"

    def test_init_denominator_zero(self):
        with self.assertRaises(DoNotDivideByZeroDude):
            Fraction(2,0)

    def test_fraction_init_with_string(self):
        with self.assertRaises(NumberNeedsToBeIntError):
            Fraction("I'm not a number")

    def test_fraction_init_with_real(self):
        with self.assertRaises(NumberNeedsToBeIntError):
            Fraction(2.3)

    # This is extra!
    def test_fraction_canonize_when_needed(self):
        fraction = Fraction (20, 30)
        fraction.canonize()

        assert fraction.numerator == 2
        assert fraction.denominator == 3
        assert str(fraction) == "2 / 3"

    def test_fraction_canonize_when_not_needed(self):
        fraction = Fraction (20, 7)
        fraction.canonize()

        assert fraction.numerator == 20
        assert fraction.denominator == 7
        assert str(fraction) == "20 / 7"


if __name__ == '__main__':
    unittest.main()
