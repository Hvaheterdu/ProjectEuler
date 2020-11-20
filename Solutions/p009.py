#!/usr/bin/env python3
import timeit


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
    start_time = timeit.default_timer()
    ans = pythagorean_triplet(1000)
    total_time = timeit.default_timer() - start_time
    print(f"Answer: {ans}\nExecution time: {total_time * 1000} ms")
