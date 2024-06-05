#!/usr/bin/python3
"""
AUTH: bugsnvibes
TASK: Create a function def pascal_triangle(n): that returns a list of
      lists of integers representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize the first row

    for _ in range(1, n):
        row = [1]  # Start each row with a 1
        for j in range(1, _):
            # Each number in the row is the sum of the two
            # numbers directly above it
            row.append(triangle[_-1][j-1] + triangle[_-1][j])
        row.append(1)  # End each row with a 1
        triangle.append(row)

    return triangle
