#!/usr/bin/env python3
from math import gcd
import timeit


"""
Problem name: Smallest multiple

Problem ID:   05
"""


def smallest_multiple() -> int:
    """Return smallest multiple of 1 to 20 with numpy GCD.
    See https://en.wikipedia.org/wiki/Least_common_multiple """
    total = 1
    for i in range(1, 21, 1):
        total *= i // gcd(i, total)
    return total


if __name__ == "__main__":
    start_time = timeit.default_timer()
    ans = smallest_multiple()
    total_time = timeit.default_timer() - start_time
    print(f"Answer: {ans}\nExecution time: {total_time * 1000} ms")
