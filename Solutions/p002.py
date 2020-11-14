#!/usr/bin/env python3


"""
Problem name: Even Fibonacci numbers

Problem ID:   02
"""


def fibonacci(n):
    """Fibonacci sequence

    Args:
        n (int): the n'th fibonacci number

    Returns:
        int: the n'th fibonacci number
    """
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def even_summation(n):
    """Finds the sum of even fibonacci numbers

    Args:
        n (int): numbers to consider

    Returns:
        int: sum of even-valued fibonacci terms
    """
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
