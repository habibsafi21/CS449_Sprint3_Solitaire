class Board:
    def __init__(self, size=7, board_type="English"):
        self.size = size
        self.board_type = board_type
        self.grid = self.create_board()

    def create_board(self):
        board = []

        for row in range(self.size):
            board.append([1] * self.size)

        # center hole empty
        center = self.size // 2
        board[center][center] = 0

        return board

    def reset(self):
        self.grid = self.create_board()

    def display(self):
        for row in self.grid:
            print(row)
