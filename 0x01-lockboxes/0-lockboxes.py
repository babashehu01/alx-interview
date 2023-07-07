#!/usr/bin/python3
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
    unlocked_boxes = set(keys)

    for key in keys:
        for box in boxes[key]:
            if box not in unlocked_boxes:
                unlocked_boxes.add(box)
                keys.append(box)

    return len(unlocked_boxes) == len(boxes)
