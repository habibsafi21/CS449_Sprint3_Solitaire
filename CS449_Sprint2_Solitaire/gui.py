import tkinter as tk
from tkinter import messagebox
from board import Board
from game_logic import GameLogic


class SolitaireGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Peg Solitaire")

        # board size selector
        self.size_var = tk.IntVar(value=7)

        size_label = tk.Label(root, text="Board Size:")
        size_label.grid(row=0, column=8)

        size_menu = tk.OptionMenu(root, self.size_var, 5, 7, 9)
        size_menu.grid(row=1, column=8)

        new_game_btn = tk.Button(root, text="New Game", command=self.new_game)
        new_game_btn.grid(row=2, column=8)

        self.board = Board(size=7)
        self.game = GameLogic(self.board)

        self.buttons = []
        self.selected = None

        self.create_board()

    def create_board(self):
        for r in range(self.board.size):
            row_buttons = []
            for c in range(self.board.size):
                btn = tk.Button(
                    self.root,
                    width=4,
                    height=2,
                    command=lambda r=r, c=c: self.handle_click(r, c)
                )
                btn.grid(row=r, column=c)
                row_buttons.append(btn)

            self.buttons.append(row_buttons)

        self.update_board()

    def update_board(self):
        for r in range(self.board.size):
            for c in range(self.board.size):
                if self.board.grid[r][c] == 1:
                    self.buttons[r][c]["text"] = "●"
                else:
                    self.buttons[r][c]["text"] = ""

    def handle_click(self, r, c):
        if self.selected is None:
            if self.board.grid[r][c] == 1:
                self.selected = (r, c)
        else:
            start_r, start_c = self.selected

            if self.game.make_move(start_r, start_c, r, c):
                self.update_board()

                if self.game.is_game_over():
                    messagebox.showinfo("Game Over", "No more valid moves!")

            self.selected = None

    def new_game(self):
        size = self.size_var.get()

        self.board = Board(size=size)
        self.game = GameLogic(self.board)

        for row in self.buttons:
            for btn in row:
                btn.destroy()

        self.buttons = []

        self.create_board()

