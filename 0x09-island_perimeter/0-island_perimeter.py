#!/usr/bin/python3
'''  Island Perimeter '''


def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the grid.

    Args:
        grid (list of list of int): 2D grid representing water (0)
        and land (1).

    Returns:
        int: The perimeter of the island.
    """
    if not grid or not grid[0]:
        return 0

    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if (grid[i][j] == 1):
                # Add 4 for the current land cell
                perimeter += 4

                # Subtract 2 for a shared edge to the right
                if j+1 < cols and grid[i][j+1] == 1:
                    perimeter -= 2

                # Subtract 2 for a shared edge below
                if i+1 < rows and grid[i+1][j] == 1:
                    perimeter -= 2
    return perimeter
