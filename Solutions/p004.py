#!/usr/bin/env python3
import timeit


"""
Problem name: Largest palindrome product

Problem ID:   04
"""


def palindrome_num():
    """Return largest palindrome number from product of 
    two 3-digit numbers """
    return max(i * j for i in range(100, 1000)
               for j in range(100, 1000) if str(i * j) == str(i * j)[:: -1])


if __name__ == "__main__":
    start_time = timeit.default_timer()
    ans = palindrome_num()
    total_time = timeit.default_timer() - start_time
    print(f"Answer: {ans}\nExecution time: {total_time * 1000} ms")
