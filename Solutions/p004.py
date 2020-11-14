#!/usr/bin/env python3


"""
Problem name: Largest palindrome product

Problem ID:   04
"""


def palindrome_num():
    """Find palindrome number from product of two 3-digit numbers

    Returns:
        str: largest palindrome
    """
    return max(i * j for i in range(100, 1000)
               for j in range(100, 1000) if str(i * j) == str(i * j)[:: -1])


if __name__ == "__main__":
    print(palindrome_num())
