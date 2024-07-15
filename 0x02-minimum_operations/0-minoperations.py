#!/usr/bin/python3
"""
This module provides a function to calculate the minimum number of operations
needed to achieve exactly n 'H' characters in a text file, starting with one
'H'. Operations allowed are copying all 'H' characters and pasting them.
"""


def minOperations(n):
    """
    Calculate the minimum number of operations needed to get n 'H' characters.

    Args:
        n (int): The target number of 'H' characters.

    Returns:
        int: The minimum number of operations required, or 0 if n is less than 2.
    """
    i = 2
    if n < 2:
        return 0
    while i < n + 1:
        if n % i == 0:
            return minOperations(n // i) + i
        i = i + 1
