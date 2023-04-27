#!/usr/bin/env python3

import sys

def print_board(board):
    """
    Prints the board
    """
    for row in board:
        print(" ".join(row))
    print("\n")

def is_valid(board, row, col, n):
    """
    Returns True if the queen can be placed at board[row][col]
    """
    # Check this row on left side
    for i in range(col):
        if board[row][i] == "Q":
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == "Q":
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == "Q":
            return False

    return True

def solve_n_queens(board, col, n):
    """
    Solves the N Queens problem
    """
    if col == n:
        print_board(board)
        return True

    # Try to place the queen in each row of the current column
    for i in range(n):
        if is_valid(board, i, col, n):
            board[i][col] = "Q"

            # Recur to place the rest of the queens
            solve_n_queens(board, col+1, n)

            # If placing the queen in board[i][col] doesn't lead to a solution, remove the queen
            board[i][col] = "."

    return False

def main():
    """
    Main function
    """
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

    board = [["." for _ in range(n)] for _ in range(n)]
    solve_n_queens(board, 0, n)

if __name__ == "__main__":
    main()
