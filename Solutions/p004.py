#!/usr/bin/env python3

"""
Problem name:

Largest palindrome product

Problem description:

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def palindrome_num():
    """Find palindrome number from product of two 3-digit numbers

    Returns:
        [str]: largest palindrome
    """
    palindrome = []
    for i in range(100, 1000):
        for j in range(100, 1000):
            if str(i * j) == str(i * j)[:: -1]:
                palindrome.append(i*j)
    return max(palindrome)


if __name__ == "__main__":
    print(palindrome_num())
