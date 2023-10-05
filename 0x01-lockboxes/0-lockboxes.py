#!/usr/bin/python3
""" Unlocking LockBoxes"""


def canUnlockAll(boxes):
    """Method that determines if all boxes can be opened"""
    opened = [False] * len(boxes)
    opened[0] = True
    stack = [0]

    while stack:
        """Pops box so we can iterate through it's keys, marks the unopened
            boxes as opened and adds them to the stack.
        """
        current_box = stack.pop()
        for key in boxes[current_box]:
            if not opened[key]:
                opened[key] = True
                stack.append(key)

    return all(opened)
