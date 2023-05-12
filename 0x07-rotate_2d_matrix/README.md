# Rotate 2D Matrix

This Python script provides a function `rotate_2d_matrix(matrix)` that rotates an n x n 2D matrix 90 degrees clockwise. It modifies the matrix in place, rather than creating a new one.

First of all, what is a 2D matrix? You can think of a 2D matrix as a table or grid of numbers. Each number in the matrix is identified by two indices, which tell you its position in the matrix. The first index tells you the row number, and the second index tells you the column number.


## Usage

To use the `rotate_2d_matrix` function, follow these steps:

1. Import the `rotate_2d_matrix` function from the module:
   ```python
   from rotate_2d_matrix import rotate_2d_matrix
   ```

2. Create an n x n 2D matrix, for example:
   ```python
   matrix = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
   ```

3. Call the `rotate_2d_matrix` function, passing in the matrix as an argument:
   ```python
   rotate_2d_matrix(matrix)
   ```

4. The original matrix will be modified to rotate it 90 degrees clockwise:
   ```python
   print(matrix)
   # Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
   ```

## Examples

Here are some examples of using the `rotate_2d_matrix` function:

```python
from rotate_2d_matrix import rotate_2d_matrix

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
rotate_2d_matrix(matrix)
print(matrix)
# Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
```

```python
from rotate_2d_matrix import rotate_2d_matrix

matrix = [[1, 2],
          [3, 4]]
rotate_2d_matrix(matrix)
print(matrix)
# Output: [[3, 1], [4, 2]]
```

```python
from rotate_2d_matrix import rotate_2d_matrix

matrix = [[1]]
rotate_2d_matrix(matrix)
print(matrix)
# Output: [[1]]
```

## How It Works

The `rotate_2d_matrix` function works by first transposing the matrix, swapping elements along its diagonal, and then reversing the order of the rows.

For example, given the matrix:
```
1 2 3
4 5 6
7 8 9
```

The transposed matrix is:
```
1 4 7
2 5 8
3 6 9
```

After swapping elements along the diagonal, the matrix becomes:
```
1 4 7
5 2 8
9 6 3
```

Finally, the order of the rows is reversed to produce the final result:
```
7 4 1
8 5 2
9 6 3
```
