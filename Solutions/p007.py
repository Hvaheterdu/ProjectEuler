#!/usr/bin/env python3
import math


"""
Problem name: 10001st prime

Problem ID:   07
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
