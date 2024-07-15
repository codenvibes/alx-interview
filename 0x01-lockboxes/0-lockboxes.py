#!/usr/bin/python3

"""
This module provides a function to determine if all boxes can be unlocked.
Each box may contain keys to other boxes, and the function checks if it's
possible to unlock all the boxes starting from the first one.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.

    Args:
        boxes (list of list of int): A list of lists where each sublist
        represents a box and contains keys to other boxes.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    n = len(boxes)
    seen_boxes = set([0])
    unseen_boxes = set(boxes[0]).difference(set([0]))

    while len(unseen_boxes) > 0:
        index = unseen_boxes.pop()

        if not index or index >= n or index < 0:
            continue
        if index not in seen_boxes:
            unseen_boxes = unseen_boxes.union(boxes[index])
            seen_boxes.add(index)
    return n == len(seen_boxes)
