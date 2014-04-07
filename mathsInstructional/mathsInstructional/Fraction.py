from fractions import Fraction

"""
A MyFraction consists of a python fraction, which is its
lowest form representation, and a multiple, which
allows us to represent the fraction in a non-reduced form
"""


class MyFraction:
    def __init__(self, *args, **kwargs):
        d = 1
        n = args[0]
        if len(args) > 1:
            d = args[1]
        m = 1
        if len(args) > 2:
            m = args[2]
        self.reducedForm = Fraction(n, d)
        self.multiple = m

    def setMultiple(self, multiple):
        self.multiple = multiple

    def getMultiple(self):
        return self.multiple

    def __str__(self):
        return "(%s,%s)" % (self.multiple*self.reducedForm.numerator,
                            self.multiple*self.reducedForm.denominator)

