from dataclasses import dataclass, field
from typing import List

@dataclass
class Board:
    grid: List[List[int]] = field(default_factory=lambda: [[0]*9 for _ in range(9)])

    def is_valid_move(self, row: int, col: int, value: int) -> bool:
        # Check if the value is not already in the row, column, or 3x3 subgrid
        if value in self.grid[row]:
            return False
        if value in [self.grid[i][col] for i in range(9)]:
            return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.grid[start_row + i][start_col + j] == value:
                    return False
        return True