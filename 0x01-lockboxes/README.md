# 0x01. Lockboxes

# # This project is part of my interview preparation curriculum, focusing on the topic of Lockboxes. It involves solving a specific algorithmic problem related to unlocking boxes containing keys.

Task
Lockboxes
You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1, and each box may contain keys to other boxes.

Write a method canUnlockAll(boxes) that determines if all the boxes can be opened.

Prototype:

python
Copy code
def canUnlockAll(boxes)
Requirements:

boxes is a list of lists.
A key with the same number as a box opens that box.
You can assume all keys will be positive integers.
There can be keys that do not have boxes.
The first box boxes[0] is initially unlocked.
Return True if all boxes can be opened; otherwise, return False.
Example
python
Copy code
boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # False
Repository Information
GitHub Repository: alx-interview
Directory: 0x01-lockboxes
File: 0-lockboxes.py
Author
This project was provided by Carrie Ybay, a Software Engineer at Holberton School.
