#!/usr/bin/env python3
from math import gcd


"""
Problem name: Smallest multiple

Problem ID:   05
"""


def smallest_multiple():
    """Find smallest multiple of 1 - 20 with 
    numpy GCD and formula from LCM Wikipedia page

    Returns:
        int: smallest multiple
    """
    total = 1
    for i in range(1, 21, 1):
        total *= i // gcd(i, total)
    return total


if __name__ == "__main__":
    print(smallest_multiple())
