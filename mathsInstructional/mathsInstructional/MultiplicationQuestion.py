from Question import Question
from Fraction import MyFraction

"""
A multiplication question asks for the product of first and second
"""


class MultiplicationQuestion(Question):
    def __init__(self, first, second):
        self.first = first
        self.second = second
        self.reversed = False
        self.answer = MyFraction(first.reducedForm*second.reducedForm)

    def reverse(self):
        if self.reversed:
            self.reversed = False
        else:
            self.reversed = True

    def __str__(self):
        first, second = self.first, self.second
        if self.reversed:
            second, first = first, second
        return "%s%s%s" % (first, chr(158), second)

    def __repr__(self):
        first, second = self.first, self.second
        if self.reversed:
            second, first = first, second
            return r'%s\times%s' % (first, second)