#!/usr/bin/python3
"""Function that returns a list of integers representing the
    Pascal's triangle.
"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing the Pascal's
        triangle.
    """
    if n <= 0:
        return []

    # Initialize the triangle with the first row
    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            value = triangle[i - 1][j - 1] + triangle[i - 1][j]
            row.append(value)

        row.append(1)
        triangle.append(row)

    return triangle
