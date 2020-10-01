#!/usr/bin/env python3

"""
Problem name:

Even Fibonacci numbers

Problem description:

Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""


def fibonacci(n):
    if n <= 0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    res = 0
    i = 1
    fib_num = 0
    while fib_num < 4000000:
        fib_num = fibonacci(i)
        if fib_num % 2 == 0:
            res += fib_num
        i += 1
    print(res)
