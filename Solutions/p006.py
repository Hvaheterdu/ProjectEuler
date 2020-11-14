#!/usr/bin/env python3


"""
Problem name: Sum square difference

Problem ID:   06
"""


def sum_square_difference() -> int:
    """Return difference between sum of squares 
    and square of sums """
    sum_square = [i**2 for i in range(1, 101, 1)]
    square_sum = [i for i in range(1, 101, 1)]
    return sum(square_sum)**2 - sum(sum_square)


if __name__ == "__main__":
    print(sum_square_difference())
