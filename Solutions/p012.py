#!/usr/bin/env python3
import math
import itertools
import sys


"""
Problem name: Highly divisible triangular number

Problem ID:   12
"""

N = sys.maxsize


def triangle_number(n, div_num):
    """Computes smallest triangle number with
    div_num divisors

    Args:
        n (int): maximum int size
        div_num (int): number of divisors

    Returns:
        int: triangle number with div_num divisors
    """
    tri_num = itertools.accumulate(range(1, n))
    for i in tri_num:
        if divisor_function(i) > div_num:
            return i


def divisor_function(n):
    """Divisor function

    Args:
        n (int): maximum int size

    Returns:
        int: number of divisors for a given number
    """
    c = 2
    end = math.sqrt(n)
    for i in range(1, int(end)):
        if n % i == 0:
            c += 2
    if int(end) == n:
        c += 1
    return c


if __name__ == "__main__":
    print(triangle_number(N, 500))
