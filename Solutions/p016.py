#!/usr/bin/env python3

"""
Problem name: Power digit sum

Problem ID:   16
"""


def power_digit_sum(base, exp):
    """Get the sum of base^exp. Calculate the
    sum from the digits that makes the sum
    for the exponent

    Args:
        base (int): base number
        exp (int): exponent

    Returns:
        int: sum of the digits
    """
    return sum([int(i) for i in str(base**exp)])


if __name__ == "__main__":
    print(power_digit_sum(2, 1000))
