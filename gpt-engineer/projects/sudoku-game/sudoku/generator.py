from sudoku.board import Board
import random

def generate_puzzle() -> Board:
    board = Board()
    # Fill the diagonal 3x3 subgrids
    for i in range(0, 9, 3):
        fill_subgrid(board, i, i)
    # Solve the board to ensure it's a valid puzzle
    solve(board)
    # Remove some numbers to create the puzzle
    remove_numbers(board)
    return board

def fill_subgrid(board: Board, row: int, col: int):
    nums = list(range(1, 10))
    random.shuffle(nums)
    for i in range(3):
        for j in range(3):
            board.grid[row + i][col + j] = nums.pop()

def remove_numbers(board: Board):
    attempts = 5
    while attempts > 0:
        row, col = random.randint(0, 8), random.randint(0, 8)
        while board.grid[row][col] == 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
        backup = board.grid[row][col]
        board.grid[row][col] = 0
        copy_board = Board([row[:] for row in board.grid])
        if not solve(copy_board):
            board.grid[row][col] = backup
            attempts -= 1