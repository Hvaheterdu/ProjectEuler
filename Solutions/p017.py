#!/usr/bin/env python3
from num2words import num2words


"""
Problem name: Number letter counts

Problem ID:   17
"""


def number_letter_counts(n) -> int:
    """Calculate sum of all letters when we convert
    all numbers from 1 to n written in words """
    res = 0
    for i in range(1, n + 1):
        res += len(num2words(i)) - num2words(i).count(' ') - \
            num2words(i).count('-')
    return res


if __name__ == "__main__":
    print(number_letter_counts(1000))
