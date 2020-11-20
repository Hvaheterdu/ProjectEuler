# !/usr/bin/env python3
import timeit


"""
Problem name: Maximum path sum I

Problem ID:   18
"""


TRIANGLE = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 65],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
]


"""
    Reverse the 2D array and calculate each element on last row with
    adjacent elements on the row above (row + 1). This will create a
    new row that replaces the second to last row, were the elements
    are the sum of the element from the last row and the largest adjacent
    element from the row above. Last row is not discarded and the row above
    is the new last row with the new elements. In the end we will only have
    one number remaining which is the sum of the largest numbers and the
    largest adjacent number to it. Approach is also explained well on the web.
    See https://stackoverflow.com/questions/8002252/euler-project-18-approach
"""


def maximum_path_sum() -> int:
    """Return the maximum sum of adjacent numbers in the row below """
    for i in reversed(range(len(TRIANGLE) - 1)):
        for j in range(len(TRIANGLE[i])):
            TRIANGLE[i][j] += max(TRIANGLE[i + 1][j], TRIANGLE[i + 1][j + 1])
    return TRIANGLE[0][0]


if __name__ == "__main__":
    start_time = timeit.default_timer()
    ans = maximum_path_sum()
    total_time = timeit.default_timer() - start_time
    print(f"Answer: {ans}\nExecution time: {total_time * 1000} ms")
