#!/usr/bin/env python3
import functools


"""
Problem name: Longest Collatz sequence

Problem ID:   14
"""


@functools.lru_cache(maxsize=None)
def collatz_sequence(n) -> int:
    """Return longest collatz sequence
    up to a number 'n' """
    if n == 1:
        return 1
    if n % 2 == 0:
        i = n // 2
    else:
        i = (3 * n) + 1
    return collatz_sequence(i) + 1


if __name__ == "__main__":
    # Use range and max() 'key' parameter
    # to find biggest sequence
    print(max(range(1, 1000000), key=collatz_sequence))
