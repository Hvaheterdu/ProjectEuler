#!/usr/bin/env python3
import math


"""
Problem name: Special Pythagorean triplet

Problem ID:   09
"""


def pythagorean_triplet(n) -> None:
    """Return the product of the pythagorean triplet that adds
    up to 1000. See https://en.wikipedia.org/wiki/Pythagorean_triple """
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            c = n - a - b
            if a * a + b * b == c * c:
                return a * b * c


if __name__ == "__main__":
    print(pythagorean_triplet(1000))
