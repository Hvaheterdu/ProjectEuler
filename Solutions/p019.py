# !/usr/bin/env python3
import datetime
from datetime import date


"""
Problem name: Counting sundays

Problem ID:   19
"""


def counting_sundays() -> int:
    """Return sum of all sundays that are the first 
    day in the month from 1901 to (and inclusive) 2000-12-31"""
    res = 0
    for i in range(1901, 2001):
        for j in range(1, 13):
            res += (1 if datetime.date(i, j, 1).weekday() == 6 else 0)
    return res


if __name__ == "__main__":
    print(counting_sundays())
