#!/usr/bin/python3
"""Minimum Operations challenge"""


def minOperations(n):
    """calculates the fewest number of operations needed to
        result in exactly n H characters in the file.
    """
    pasted = 1
    copied = 0
    count = 0

    while pasted < n:
        '''If it did not copy anything'''
        if copied == 0:
            '''Copy all'''
            copied = pasted
            count += 1

        '''If it has not pasted anything'''
        if pasted == 1:
            '''paste'''
            pasted += copied
            count += 1
            continue

        remaining = n - pasted
        if remaining < copied:
            return 0

        if remaining % pasted != 0:
            pasted += copied
            count += 1
        else:
            copied = pasted
            pasted += copied
            count += 2

    if pasted == n:
        return count
    else:
        return 0
