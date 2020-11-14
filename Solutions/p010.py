#!/usr/bin/env python3
import sympy


"""
Problem name: Summation of primes

Problem ID:   10
"""


def sum_of_primes(n):
    """Find sum of all prime numbers below n

    Returns:
        int: sum of all primes below n
    """
    return sum(sympy.primerange(0, n))


if __name__ == "__main__":
    print(sum_of_primes(2000000))
