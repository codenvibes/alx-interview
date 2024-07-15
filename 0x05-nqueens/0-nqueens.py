#!/usr/bin/python3
"""
N-Queens Problem Solver

This script solves the N-Queens problem for a given board size N.
The N-Queens problem involves placing N chess queens on an NxN chessboard
so that no two queens threaten each other.

Usage:
  nqueens N

Arguments:
  N - The size of the chessboard (must be a number greater than or equal to4)
"""
import sys


def is_valid_position(board, row, col):
    """
    Check if a queen can be placed at board[row][col] without being attacked.

    Args:
        board (list): The current state of the chessboard.
        row (int): The row index.
        col (int): The column index.

    Returns:
        bool: True if the position is valid, False otherwise.
    """
    b_size = len(board)
    if sum(board[row]) or sum([board[i][col] for i in range(b_size)]) != 0:
        return False

    for i, j in [(1, 1), (-1, -1), (1, -1), (-1, 1)]:
        r, c = row, col
        while 0 <= r + i < b_size and 0 <= c + j < b_size:
            r, c = r + i, c + j
            if board[r][c]:
                return False
    return True


def place_next_queen(board, row):
    """
    Attempt to place a queen on the chessboard in the given row.

    Args:
        board (list): The current state of the chessboard.
        row (int): The row index where the queen is to be placed.

    Returns:
        bool: True if a queen was placed, False otherwise.
    """
    st, end = 0, len(board)
    if sum(board[row]) == 1:
        st = board[row].index(1) + 1
        board[row] = [0 for col in range(end)]

    for col in range(st, end):
        if is_valid_position(board, row, col):
            board[row][col] = 1
            return True
    return False


def solve_nqueens(board, solutions=[]):
    """
    Solve the N-Queens problem by placing queens on the board.

    Args:
        board (list): The current state of the chessboard.
        solutions (list): A list to store the solutions found.

    Returns:
        None
    """
    n = len(board)
    row = 0
    while row < n:
        if place_next_queen(board, row):
            row += 1
        else:
            if row - 1 < 0:
                break
            row -= 1
        if row == n:
            solutions.append([[row, board[row].index(1)] for row in range(n)])
            row -= 1

    if row == 0:
        return

    solutions.append([[row, board[row].index(1)] for row in range(n)])
    idx = board[0].index(1)
    if idx > -1:
        board = [[0 for _ in range(n)] for row in range(n)]
        board[0][idx] = 1
        solve_nqueens(board, solutions)


def find_solutions(n):
    """
    Find and print all solutions to the N-Queens problem for a board of size n.

    Args:
        n (int): The size of the chessboard.

    Returns:
        None
    """
    board = [[0 for col in range(n)] for row in range(n)]
    solutions = []
    solve_nqueens(board, solutions)
    for row in solutions:
        print(row)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n < 4:
            print('N must be at least 4')
            sys.exit(1)
        find_solutions(n)

    except ValueError:
        print('N must be a number')
        sys.exit(1)
