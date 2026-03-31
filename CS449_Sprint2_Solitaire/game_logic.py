from board import Board
import random

# Base class
class Game:
    def __init__(self, board):
        self.board = board

    def is_game_over(self):
        grid = self.board.grid
        size = self.board.size

        for r in range(size):
            for c in range(size):
                if grid[r][c] == 1:
                    # check right move
                    if c + 2 < size and grid[r][c+1] == 1 and grid[r][c+2] == 0:
                        return False

                    # check down move
                    if r + 2 < size and grid[r+1][c] == 1 and grid[r+2][c] == 0:
                        return False

        return True


# Manual Game (Sprint 2)
class ManualGame(Game):
    def make_move(self, start_row, start_col, end_row, end_col):
        grid = self.board.grid

        # Check start
        if grid[start_row][start_col] != 1:
            return False

        # Check end
        if grid[end_row][end_col] != 0:
            return False

        # Middle
        mid_row = (start_row + end_row) // 2
        mid_col = (start_col + end_col) // 2

        if grid[mid_row][mid_col] != 1:
            return False

        # Move
        grid[start_row][start_col] = 0
        grid[mid_row][mid_col] = 0
        grid[end_row][end_col] = 1

        return True


# Automated Game (Sprint 3)
class AutomatedGame(Game):

    def get_all_valid_moves(self):
        moves = []
        grid = self.board.grid
        size = self.board.size

        for r in range(size):
            for c in range(size):
                if grid[r][c] == 1:
                    # right
                    if c + 2 < size and grid[r][c+1] == 1 and grid[r][c+2] == 0:
                        moves.append((r, c, r, c+2))

                    # down
                    if r + 2 < size and grid[r+1][c] == 1 and grid[r+2][c] == 0:
                        moves.append((r, c, r+2, c))

        return moves

    def automated_move(self):
        moves = self.get_all_valid_moves()

        if not moves:
            return False

        move = random.choice(moves)

        # reuse manual move logic
        manual = ManualGame(self.board)
        return manual.make_move(*move)