#!/usr/bin/python3
'''
canUnlockAll.py

This module contains a function `canUnlockAll` that determines
whether all boxes in a sequence can be opened.
Each box contains keys to other boxes, and the first box is always unlocked.
The function returns True if all boxes can be opened,
otherwise it returns False.

Boxes are numbered from 0 to n-1, and each box may contain keys to other boxes.
The keys are represented as positive integers.
'''


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened, starting from the first box.

    Args:
        boxes: list
    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    unlocked = [False] * len(boxes)
    unlocked[0] = True

    keys = boxes[0]

    for key in keys:
        if 0 <= key < len(boxes) and not unlocked[key]:
            unlocked[key] = True
            keys.extend(boxes[key])
        

    return all(unlocked)
