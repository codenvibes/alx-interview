#!/usr/bin/python3

"""
This script defines a function to validate UTF-8 encoding.
"""


def validUTF8(data):
    """
    Checks if a given list of integers represents a valid UTF-8 encoding.

    Args:
        data (list): A list of integers, where each integer represents a byte
        of data.

    Returns:
        bool: True if the data is valid UTF-8 encoding, False otherwise.
    """
    i = 0
    while i < len(data):
        num_bytes = 0
        byte = data[i]
        while byte & (128 >> num_bytes):
            num_bytes += 1
        if num_bytes == 0:
            i += 1
        elif num_bytes == 1 or num_bytes > 4:
            return False
        else:
            for j in range(1, num_bytes):
                if (i + j >= len(data) or
                        (data[i+j] & 0b11000000) != 0b10000000):
                    return False
            i += num_bytes
    return True
