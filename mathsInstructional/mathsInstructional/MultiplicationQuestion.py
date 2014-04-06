from Question import Question

"""
A multiplication question asks for the product of first and second
"""


class MultiplicationQuestion(Question):
    def __init__(self, first, second):
        self.super()
        self.first = first
        self.second = second