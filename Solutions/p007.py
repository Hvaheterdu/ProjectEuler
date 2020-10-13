#!/usr/bin/env python3
import math

"""
Problem name:

10001st prime

Problem description:

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""


def find_prime_num(n):
    """Find the Nth prime number. This function uses the
    square root method to find the nth prime number.
    See https://en.wikipedia.org/wiki/Prime_number#Trial_division

    Args:
        n (int): nth prime number

    Returns:
        int: prime number
    """
    start = 2
    count = 0
    while True:
        if all(start % i for i in range(2, int(math.sqrt(start)) + 1)) != 0:
            count += 1
            if count == n:
                return start
        start += 1


if __name__ == "__main__":
    print(find_prime_num(10001))
