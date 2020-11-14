#!/usr/bin/env python3


"""
Problem name: Even Fibonacci numbers

Problem ID:   02
"""


def fibonacci(n) -> int:
    """ Fibonacci sequence of 'n' numbers """
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def even_summation(n) -> int:
    """Return the sum of even fibonacci numbers up to 'n' """
    fib_num = 0
    res = 0
    i = 1
    while fib_num < n:
        fib_num = fibonacci(i)
        if fib_num % 2 == 0:
            res += fib_num
        i += 1
    return res


if __name__ == "__main__":
    print(even_summation(4000000))
