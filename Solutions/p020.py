# !/usr/bin/env python3
import timeit
import math


"""
Problem name: Factorial digit sum

Problem ID:   20
"""


def factorial_digit_sum(n) -> int:
    """ Return sum of all digits in 'n!' """
    num = math.factorial(n)
    res = sum(int(i) for i in str(num))
    return res


if __name__ == "__main__":
    start_time = timeit.default_timer()
    ans = factorial_digit_sum(100)
    total_time = timeit.default_timer() - start_time
    print(f"Answer: {ans}\nExecution time: {total_time * 1000} ms")
