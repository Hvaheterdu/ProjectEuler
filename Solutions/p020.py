# !/usr/bin/env python3
import math


"""
Problem name: Factorial digit sum

Problem ID:   20
"""


def factorial_digit_sum(n):
    """ Return sum of all digits in 'n!' """
    num = math.factorial(n)
    return sum(int(i) for i in str(num))


if __name__ == "__main__":
    print(factorial_digit_sum(100))
