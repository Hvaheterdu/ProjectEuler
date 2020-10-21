#!/usr/bin/env python3
import math

"""
Problem name:

Special Pythagorean triplet

Problem description:

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

                                                        a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


def pythagorean_triplet(n):
    """Find the product of the pythagorean triplet that adds
    up to 1000. See Wikipedia page for Pythagorean Triple
    for forumla

    Args:
        n (int): a + b + c

    Returns:
        int: product of a, b and c
    """
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            # Count c down from 1000
            c = n - a - b
            if a * a + b * b == c * c:
                return a*b*c


if __name__ == "__main__":
    print(pythagorean_triplet(1000))
