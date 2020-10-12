#!/usr/bin/env python3

"""
Problem name:

Sum square difference

Problem description:

The sum of the squares of the first ten natural numbers is,

                                                        1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,

                                                        (1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
3025 - 385 = 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


def sum_square_difference():
    """ Find difference between sum of squares and square of sums """
    sum_square = 0
    square_sum = 0
    diff = 0
    for i in range(1, 101, 1):
        sum_square += i**2
        square_sum += i
    square_sum = square_sum**2
    diff = square_sum - sum_square
    return diff


if __name__ == "__main__":
    print(sum_square_difference())
