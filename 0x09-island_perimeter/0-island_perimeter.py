def island_perimeter(grid):
    """
    Calculates the perimeter of the island described in the grid.
    
    Args:
        grid (List[List[int]]): The grid representing the island.
        
    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                # Check the left side
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                # Check the right side
                if j == len(grid[i]) - 1 or grid[i][j + 1] == 0:
                    perimeter += 1
                # Check the top side
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                # Check the bottom side
                if i == len(grid) - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
    
    return perimeter
