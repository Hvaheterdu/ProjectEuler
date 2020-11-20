#!/usr/bin/env python3
import itertools
import timeit
import math
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


def divisor_function(n) -> int:
    """Divisor function. Return number of divisors
    for a given number 'n' """
    c = 2
    end = math.sqrt(n)
    for i in range(1, int(end)):
        if n % i == 0:
            c += 2
    if int(end) == n:
        c += 1
    return c


if __name__ == "__main__":
    start_time = timeit.default_timer()
    ans = triangle_number(N, 500)
    total_time = timeit.default_timer() - start_time
    print(f"Answer: {ans}\nExecution time: {total_time * 1000} ms")
