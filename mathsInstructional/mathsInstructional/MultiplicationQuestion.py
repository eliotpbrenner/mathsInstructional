from Question import Question
from Fraction import MyFraction

"""
A multiplication question asks for the product of first and second
"""


class MultiplicationQuestion(Question):
    def __init__(self, first, second):
        self.super()
        self.first = first
        self.second = second
        self.reversed = False
        self.answer = MyFraction(first*second)

    def reverse(self):
        if self.reversed:
            self.reversed = False
        else:
            self.reversed = True

    def __str__(self):
        first, second = self.first, self.second
        if self.reversed:
            second, first = first, second
            return "%schr(158)%s" % (first, second)

    def __repr__(self):
        first, second = self.first, self.second
        if self.reversed:
            second, first = first, second
            return r'%s\times%s' % (first, second)