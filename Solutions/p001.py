#!/usr/bin/env python3

"""
Problem name:

Multiples of 3 and 5

Problem description:

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def multiples():
    """ Find sum of all multiples of 3 and 5
    below 1000. 

    Returns:
        int: sum of all multiples
    """
    return (i for i in range(1000) if i % 3 == 0 or i % 5 == 0)


if __name__ == "__main__":
    print(multiples())
