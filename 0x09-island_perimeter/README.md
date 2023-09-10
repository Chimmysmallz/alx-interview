# Island Perimeter


This project implements a function to calculate the perimeter of an island described in a grid.

The `island_perimeter` function takes a grid as input and returns the perimeter of the island. The grid is represented as a list of lists of integers, where 0 represents water and 1 represents land. The cells in the grid are connected horizontally and vertically, and the grid is completely surrounded by water. The function assumes there is only one island (or nothing) in the grid, and the island doesn't have any "lakes" (water inside that isn't connected to the water surrounding the island).

## Requirements

- Ubuntu 14.04 LTS
- Python 3.4.3

## Usage

To use the `island_perimeter` function, follow these steps:

1. Clone the repository: `git clone <repository-url>`
2. Navigate to the project directory: `cd island-perimeter`
3. Run the Python script: `python3 island_perimeter.py`

The script will execute and display the perimeter of the island described in the provided grid.

## Documentation

The `island_perimeter` function is documented as follows:

```python
def island_perimeter(grid):
    """
    Calculates the perimeter of the island described in the grid.
    
    Args:
        grid (List[List[int]]): The grid representing the island.
        
    Returns:
        int: The perimeter of the island.
    """
    # Function implementation
```

The function takes a grid as input, which is a list of lists of integers. It returns an integer representing the perimeter of the island.

## Testing

Unit tests for the `island_perimeter` function can be found in the `test_island_perimeter.py` file. To run the tests, execute the following command:

```bash
python3 -m unittest test_island_perimeter.py
```

The tests ensure that the function calculates the perimeter correctly for different grid configurations.

## Contributing

Contributions to this project are welcome. If you find any issues or want to suggest improvements, please open an issue or submit a pull request.
