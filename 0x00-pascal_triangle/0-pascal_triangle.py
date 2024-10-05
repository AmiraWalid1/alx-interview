#!/usr/bin/python3
"""
This script contains a function that generates Pascal's triangle
up to a given number of rows `n`.
"""


def pascal_triangle(n):
    """
    Function to generate Pascal's triangle of `n` rows.

    Args:
        n (int): The number of rows in Pascal's triangle.

    Returns:
        List[List[int]]: A list of lists where each list represents
        a row of Pascal's triangle.

    Example:
        pascal_triangle(3) returns [[1], [1, 1], [1, 2, 1]]

    Notes:
        - If `n <= 0`, the function returns an empty list.
    """

    if (n <= 0):
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j] + triangle[i-1][j-1])
        row.append(1)
        triangle.append(row)

    return triangle
