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
    check = [0] * len(boxes)
    check[0] = 1

    queue = []
    for key in boxes[0]:
        queue.append(key)

    while (len(queue) != 0):
        check[queue[0]] = 1
        if check.count(1) == len(boxes):
            return True

        for key in boxes[queue[0]]:
            if check[key] == 0:
                queue.append(key)
        queue.pop(0)

    return False
