#!/usr/bin/env python3


"""
Problem name: Multiples of 3 and 5

Problem ID:   01
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
