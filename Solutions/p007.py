#!/usr/bin/env python3
import math
import timeit


"""
Problem name: 10001st prime

Problem ID:   07
"""


def find_prime_num(n) -> int:
    """Return the N'th prime number. This function
    uses the square root method to find the n'th prime number.
    See https://en.wikipedia.org/wiki/Prime_number#Trial_division """
    start = 2
    count = 0
    while True:
        if all(start % i for i in range(2, int(math.sqrt(start)) + 1)) != 0:
            count += 1
            if count == n:
                return start
        start += 1


if __name__ == "__main__":
    start_time = timeit.default_timer()
    ans = find_prime_num(10001)
    total_time = timeit.default_timer() - start_time
    print(f"Answer: {ans}\nExecution time: {total_time * 1000} ms")
