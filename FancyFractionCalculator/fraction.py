from FancyFractionCalculator.exceptions import NumberNeedsToBeIntError, DoNotDivideByZeroDude

#C'mon guys, I'm not implementing a GCD on my own!
from fractions import gcd

# This is a faith jump, as there's nothing in the specification saying that fractions should be integer only, but for me
# it makes sense to represent them as integer. But converting float to numbers is OVERKILLING this
# (see http://stackoverflow.com/questions/95727/how-to-convert-floats-to-human-readable-fractions)
# So I'll just keep it int only. Way more beautiful

class Fraction:
    def __init__(self, numerator, denominator=None):
        if not isinstance(numerator, int):
            raise NumberNeedsToBeIntError("I am expecting a integer numerator, instead of {}".format(numerator))
        if denominator and not isinstance(denominator, int):
            raise NumberNeedsToBeIntError("I am expecting a integer denominator, instead of {}".format(denominator))
        if denominator == 0:
            raise DoNotDivideByZeroDude("Ok, let's go back to school... What happen when you divide someting by 0?")
        self.numerator = numerator
        if not denominator:
            denominator = 1
        self.denominator = denominator

    def __str__(self):
        return "{} / {}".format(self.numerator, self.denominator)

    def canonize(self):
        divisor = gcd(self.numerator, self.denominator)
        self.numerator = self.numerator / divisor
        self.denominator = self.denominator / divisor