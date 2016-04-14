# Instead of havingthe operations inside the fraction for a fancy fraction1.add(fraction2), fraction1.multiply(fraction2)
# I create a fraction calculator where the operations are going to be add(fraction1, fraction2)
from FancyFractionCalculator.fraction import Fraction
from fraction import gcd


def addition(fraction1, fraction2):
    result_denominator = lcm(fraction1.denominator, fraction2.denominator)
    result_numerator = ((fraction1.numerator * (fraction1.denominator / result_denominator)) +
                        (fraction2.numerator * (fraction2.denominator / result_denominator)))
    return Fraction(result_numerator, result_denominator)


# Least common multiple is not in standard libraries? It's in gmpy, but this is simple enough:
# props to https://gist.github.com/endolith/114336

def lcm(*numbers):
    """Return lowest common multiple."""

    def lcm(a, b):
        return (a * b) // gcd(a, b)

    return reduce(lcm, numbers, 1)
