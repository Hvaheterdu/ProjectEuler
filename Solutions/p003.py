#!/usr/bin/env python3

"""
Problem name:

Largest prime factor

Problem description:

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


def largest_prime_factor(number):
    """Find largest prime factor of parameter number

    Args:
        number (int): number to find largest factor from

    Returns:
        int: lagerst factor
    """
    factors = []
    i = 2
    while number != 1:
        if number % i == 0:
            number = number / i
            factors.append(i)
        else:
            i += 1
    return max(factors)


if __name__ == "__main__":
    print(largest_prime_factor(600851475143))
