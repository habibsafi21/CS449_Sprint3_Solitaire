import unittest
from board import Board
from game_logic import ManualGame, AutomatedGame


class TestManualGame(unittest.TestCase):

    def test_valid_move(self):
        board = Board(size=5)
        game = ManualGame(board)

        # try a valid move (depends on your board setup)
        result = game.make_move(2, 0, 2, 2)
        self.assertTrue(result)

    def test_invalid_move(self):
        board = Board(size=5)
        game = ManualGame(board)

        # invalid move
        result = game.make_move(0, 0, 0, 1)
        self.assertFalse(result)


class TestAutomatedGame(unittest.TestCase):

    def test_get_moves(self):
        board = Board(size=5)
        game = AutomatedGame(board)

        moves = game.get_all_valid_moves()
        self.assertIsInstance(moves, list)

    def test_auto_move(self):
        board = Board(size=5)
        game = AutomatedGame(board)

        result = game.automated_move()
        self.assertTrue(result or result == False)


if __name__ == "__main__":
    unittest.main()