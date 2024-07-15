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

if len(sys.argv) != 2:
    print('Usage: nqueens N')
    exit(1)

try:
    n_q = int(sys.argv[1])
except ValueError:
    print('N must ba a number')
    exit(1)

if n_q < 4:
    print('N must ba at least 4')
    exit(1)


def solve_nqueens(n):
    '''
    Solve the N-Queens problem.

    Args:
        n (int): The number of queens and the size of the chessboard (NxN).

    Returns:
        List[List[Tuple[int, int]]]: A list of solutions, where each solution
        is a list of tuples representing the positions of queens on the
        chessboard.
    '''
    if n == 0:
        return [[]]
    inner_solution = solve_nqueens(n - 1)
    return [solution + [(n, i + 1)]
            for i in range(n_q)
            for solution in inner_solution
            if safe_queen((n, i + 1), solution)]


def attack_queen(square, queen):
    '''
    Determine if a queen can attack another queen.

    Args:
        square (Tuple[int, int]): The position of the first queen (row, column)
        queen (Tuple[int, int]): The position of the second queen (row, column)

    Returns:
        bool: True if the queens can attack each other, False otherwise.
    '''
    (row1, col1) = square
    (row2, col2) = queen
    return (row1 == row2) or (col1 == col2) or\
        abs(row1 - row2) == abs(col1 - col2)


def safe_queen(sqr, queens):
    '''
    Check if a queen can be placed on the board without being attacked.

    Args:
        sqr (Tuple[int, int]): The position to check (row, column).
        queens (List[Tuple[int, int]]): The positions of the existing queens.

    Returns:
        bool: True if the position is safe, False otherwise.
    '''
    for queen in queens:
        if attack_queen(sqr, queen):
            return False
    return True


for answer in reversed(solve_nqueens(n_q)):
    result = []
    for p in [list(p) for p in answer]:
        result.append([i - 1 for i in p])
    print(result)
