from sudoku.board import Board

def solve(board: Board) -> Board:
    empty = find_empty(board)
    if not empty:
        return board
    row, col = empty
    for num in range(1, 10):
        if board.is_valid_move(row, col, num):
            board.grid[row][col] = num
            if solve(board):
                return board
            board.grid[row][col] = 0
    return None

def find_empty(board: Board):
    for i in range(9):
        for j in range(9):
            if board.grid[i][j] == 0:
                return (i, j)
    return None