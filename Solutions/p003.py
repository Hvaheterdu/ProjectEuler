#!/usr/bin/env python3

"""
Problem name: Largest prime factor

Problem ID:   03
"""


def largest_prime_factor(number) -> int:
    """ Return largest prime factor of 'number' """
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
