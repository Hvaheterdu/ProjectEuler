#!/usr/bin/env python3
import sympy
import timeit


"""
Problem name: Summation of primes

Problem ID:   10
"""


def sum_of_primes(n) -> str:
    """ Return sum of all prime numbers below 'n' """
    ans = str(sum(sympy.primerange(0, n)))
    return ans


if __name__ == "__main__":
    start_time = timeit.default_timer()
    ans = sum_of_primes(2000000)
    total_time = timeit.default_timer() - start_time
    print(f"Answer: {ans}\nExecution time: {total_time * 1000} ms")
