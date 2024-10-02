import random
from typing import List

def generate_puzzle() -> List[List[int]]:
    # Generate a new Sudoku puzzle
    puzzle = [[0 for _ in range(9)] for _ in range(9)]
    # Fill the puzzle with a valid Sudoku solution
    fill_puzzle(puzzle)
    # Remove some numbers to create the puzzle
    remove_numbers(puzzle)
    return puzzle

def fill_puzzle(puzzle: List[List[int]]) -> bool:
    # Fill the puzzle with a valid Sudoku solution
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                random.shuffle(numbers)
                for number in numbers:
                    if is_valid(puzzle, i, j, number):
                        puzzle[i][j] = number
                        if fill_puzzle(puzzle):
                            return True
                        puzzle[i][j] = 0
                return False
    return True

def remove_numbers(puzzle: List[List[int]]):
    # Remove some numbers to create the puzzle
    attempts = 5
    while attempts > 0:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        while puzzle[row][col] == 0:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
        backup = puzzle[row][col]
        puzzle[row][col] = 0
        copy = [row[:] for row in puzzle]
        if not solve_puzzle(copy):
            puzzle[row][col] = backup
            attempts -= 1

def is_valid(puzzle: List[List[int]], row: int, col: int, num: int) -> bool:
    # Check if a number can be placed in a cell
    for i in range(9):
        if puzzle[row][i] == num or puzzle[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if puzzle[i][j] == num:
                return False
    return True

def validate_move(puzzle: List[List[int]], row: int, col: int, value: int) -> bool:
    # Validate a move made by the user
    return is_valid(puzzle, row, col, value)

def solve_puzzle(puzzle: List[List[int]]) -> List[List[int]]:
    # Solve the Sudoku puzzle
    if fill_puzzle(puzzle):
        return puzzle
    return []

numbers = list(range(1, 10))