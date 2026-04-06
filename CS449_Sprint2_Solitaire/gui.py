import tkinter as tk
from tkinter import messagebox
from board import Board
from game_logic import ManualGame, AutomatedGame


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

        # game mode selector
        self.mode_var = tk.StringVar(value="Manual")

        mode_label = tk.Label(root, text="Game Mode:")
        mode_label.grid(row=2, column=8)

        mode_menu = tk.OptionMenu(root, self.mode_var, "Manual", "Automated")
        mode_menu.grid(row=3, column=8)

        # new game button
        new_game_btn = tk.Button(root, text="New Game", command=self.new_game)
        new_game_btn.grid(row=4, column=8)

        # 🔥 NEW: randomize button
        random_btn = tk.Button(root, text="Randomize", command=self.randomize_board)
        random_btn.grid(row=5, column=8)

        self.board = Board(size=7)
        self.game = ManualGame(self.board)

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
        # only allow manual clicks
        if self.mode_var.get() != "Manual":
            return

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

        mode = self.mode_var.get()

        if mode == "Manual":
            self.game = ManualGame(self.board)
        else:
            self.game = AutomatedGame(self.board)

        # clear old buttons
        for row in self.buttons:
            for btn in row:
                btn.destroy()

        self.buttons = []

        self.create_board()

        # start automated mode
        if mode == "Automated":
            self.auto_play()

    def auto_play(self):
        auto_game = AutomatedGame(self.board)

        def step():
            moved = auto_game.automated_move()
            self.update_board()

            if moved:
                self.root.after(500, step)
            else:
                messagebox.showinfo("Game Over", "Automated game finished!")

        step()

    # 🔥 RANDOMIZE FUNCTION
    def randomize_board(self):
        auto_game = AutomatedGame(self.board)

        for _ in range(5):
            moved = auto_game.automated_move()
            if not moved:
                break

        self.update_board()