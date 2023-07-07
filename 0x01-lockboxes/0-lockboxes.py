#!/usr/bin/bash
'''Defines canUnlockAll function
'''


def canUnlockAll(boxes):
    '''determines if all the boxes can be opened
    args:
        @boxes: is a list of lists
    Returns:
        True if all boxes can be opened
        else return False
    '''
    keys = [0]
    n = len(boxes)

    for i in keys:
        for key in boxes[i]:
            if key not in keys:
                keys.append(key)

        if len(keys) == n:
            return True
        else:
            return False
