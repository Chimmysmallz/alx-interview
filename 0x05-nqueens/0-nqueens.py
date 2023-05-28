#!/usr/bin/python3
"""
Module nqueens
"""

import sys


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at position (row, col) on the board.

    Args:
        board (list): The chessboard with queens placed.
        row (int): The current row to check.
        col (int): The current column to check.

    Returns:
        bool: True if it's safe to place a queen, False otherwise.
    """
    for i in range(col):
        if board[i] == row or board[i] == row - (col - i) or board[i] == row + (col - i):
            return False
    return True


def solve_nqueens(n):
    """
    Solve the N Queens problem and print all possible solutions.

    Args:
        n (int): The number of queens and the size of the board.
    """
    board = [-1] * n  # Initialize the board as an empty list

    def place_queen(col):
        """
        Place a queen in the current column (col) recursively.

        Args:
            col (int): The current column to place a queen.
        """
        if col == n:
            # If all queens are placed, print the solution
            print([[i, board[i]] for i in range(n)])
        else:
            for row in range(n):
                if is_safe(board, row, col):
                    board[col] = row
                    place_queen(col + 1)

    place_queen(0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(n)
