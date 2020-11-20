#!/usr/bin/env python3
import timeit


"""
Problem name: Multiples of 3 and 5

Problem ID:   01
"""


def multiples() -> int:
    """Return sum of all multiples of 3 and 5 below 1000 """
    ans = sum(i for i in range(1000) if i % 3 == 0 or i % 5 == 0)
    return ans


if __name__ == "__main__":
    start_time = timeit.default_timer()
    ans = multiples()
    total_time = timeit.default_timer() - start_time
    print(f"Answer: {ans}\nExecution time: {total_time * 1000} ms")
