# Instead of havingthe operations inside the fraction for a fancy fraction1.add(fraction2), fraction1.multiply(fraction2)
# I create a fraction calculator where the operations are going to be add(fraction1, fraction2)
from copy import copy
from fractions import gcd

from FancyFractionCalculator.exceptions import ElementNotAFraction
from FancyFractionCalculator.fraction import Fraction


def fraction_addition(fraction1, fraction2):
    if not isinstance(fraction1, Fraction):
        raise ElementNotAFraction("Element {} expected to be a fraction", fraction1)

    if not isinstance(fraction2, Fraction):
        raise ElementNotAFraction("Element {} expected to be a fraction", fraction2)

    result_denominator = lcm(fraction1.denominator, fraction2.denominator)
    result_numerator = ((fraction1.numerator * (result_denominator / fraction1.denominator)) +
                        (fraction2.numerator * (result_denominator / fraction2.denominator)))
    result_fraction = Fraction(result_numerator, result_denominator)
    result_fraction.canonize()
    return result_fraction


# DRY!!
def fraction_substraction(fraction1, fraction2):
    fraction2_negated = Fraction(-1 * fraction2.numerator, fraction2.denominator)
    return fraction_addition(fraction1, fraction2_negated)


def fraction_multiplication(fraction1, fraction2):
    if not isinstance(fraction1, Fraction):
        raise ElementNotAFraction("Element {} expected to be a fraction", fraction1)

    if not isinstance(fraction2, Fraction):
        raise ElementNotAFraction("Element {} expected to be a fraction", fraction2)

    result_numerator = fraction1.numerator * fraction2.numerator
    result_denominator = fraction1.denominator * fraction2.denominator

    result_fraction = Fraction(result_numerator, result_denominator)
    result_fraction.canonize()

    return result_fraction


# Don't have to deal with division by 0 because Reciprocal raises exception when needed
def fraction_division(fraction1, fraction2):
    fraction2_reciprocal = copy(fraction2)
    fraction2_reciprocal.reciprocal()

    return fraction_multiplication(fraction1, fraction2_reciprocal)


# Some extra
def add_int(fraction, int):
    return fraction_addition(fraction, Fraction(int))


def substract_int(fraction, int):
    return fraction_substraction(fraction, Fraction(int))


# So Lazy to extract this to Utils
# Least common multiple is not in standard libraries? It's in gmpy, but this is simple enough:
# props to https://gist.github.com/endolith/114336

def lcm(*numbers):
    """Return lowest common multiple."""

    def lcm(a, b):
        return (a * b) // gcd(a, b)

    return reduce(lcm, numbers, 1)
