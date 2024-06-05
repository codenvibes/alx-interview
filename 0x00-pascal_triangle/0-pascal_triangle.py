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

    for i in range(1, n):
        row = [1]  # Start each row with a 1
        for j in range(1, i):
            # Each number in the row is the sum of the two
            # numbers directly above it
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # End each row with a 1
        triangle.append(row)

    return triangle


# Test the function
if __name__ == "__main__":
    def print_triangle(triangle):
        for row in triangle:
            print("[{}]".format(",".join([str(x) for x in row])))

    print_triangle(pascal_triangle(5))
