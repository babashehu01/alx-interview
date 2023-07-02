#!/usr/bin/python3
'''Defines the pascal's triangle function
'''


def pascal_triangle(n):
    '''Args:
        n: number of the rows
       Return:
         returns a list of lists of integers(n)
    '''
    if n <= 0:
        return []
    pascals = []

    for i in range(n):
        temp = []
        for j in range(i+1):
            if j == 0 or j == i:
                temp.append(1)
            else:
                temp.append(pascals[i-1][j-1] + pascals[i-1][j])
        pascals.append(temp)

    return pascals
