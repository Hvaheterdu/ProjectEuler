#!/usr/bin/env python3
import eulerlib

"""
Problem name:

Summation of primes

Problem description:

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


def sum_of_primes(n):
    """Find sum of all prime numbers below n

    Returns:
        int: sum of all primes below n
    """
    return sum(eulerlib.primes(n))


if __name__ == "__main__":
    print(sum_of_primes(2000000))
