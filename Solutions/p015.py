#!/usr/bin/env python3
import math


"""
Problem name: Lattice paths

Problem ID:   15
"""


def lattice_paths(n, k) -> int:
    """Find how many lattice paths there are from
    (0, 0) to (n, k). Using formula from Wikipedia.
    See https://en.wikipedia.org/wiki/Lattice_path

    Args:
        n (int): x-cord for end
        k (int): y-cord for end

    Returns:
        int: number of lattice paths
    """
    # This is the binomial coefficient (n + k)
    #                                  (  n  )
    return math.comb(n, k)


if __name__ == "__main__":
    print(lattice_paths(40, 20))
