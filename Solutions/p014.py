#!/usr/bin/env python3
import functools
import timeit


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
    start_time = timeit.default_timer()
    # Use range and max() 'key' parameter to find biggest sequence
    ans = max(range(1, 1000000), key=collatz_sequence)
    total_time = timeit.default_timer() - start_time
    print(f"Answer: {ans}\nExecution time: {total_time * 1000} ms")
