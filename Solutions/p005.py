#!/usr/bin/env python3
import numpy as np

"""
Problem name:

Smallest multiple

Problem description:

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


def smallest_multiple():
    """Find smallest multiple of 1 - 20 with 
    numpy GCD and formula from LCM Wikipedia page

    Returns:
        [int]: smallest multiple
    """
    total = 1
    for i in range(1, 21, 1):
        total *= i // np.gcd(i, total)
    return total


if __name__ == "__main__":
    print(smallest_multiple())
