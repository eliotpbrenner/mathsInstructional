from MultiplicationQuestion import MultiplicationQuestion
from Fraction import MyFraction


def main():
    nums = [1, 4, 6, 3, 27, 7, 3, 5, 3, 6]
    denoms = [6, 3, 6, 7, 2, 1, 8, 9, 2, 3]
    multiples = [1, 1, 1, 1, 2, 2, 3, 50, 300, 6]
    integers = [3, 21, 10, 19, 21, 52, 33, 550, 3, 0]
    for i in range(len(denoms)):
        print MultiplicationQuestion(MyFraction(nums[i], denoms[i], multiples[i]), MyFraction(integers[i]))


if __name__ == "__main__":
    main()