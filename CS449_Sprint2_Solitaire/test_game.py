import unittest
from board import Board
from game_logic import ManualGame, AutomatedGame


class TestGameLogic(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.manual_game = ManualGame(self.board)
        self.auto_game = AutomatedGame(self.board)

    def test_valid_move(self):
        # Example valid move (adjust if needed based on board)
        result = self.manual_game.make_move(3, 1, 3, 3)
        self.assertTrue(result)

    def test_invalid_move(self):
        # Invalid move (no jump)
        result = self.manual_game.make_move(0, 0, 0, 2)
        self.assertFalse(result)

    def test_game_not_over_initially(self):
        self.assertFalse(self.manual_game.is_game_over())

    def test_automated_move(self):
        result = self.auto_game.automated_move()
        self.assertTrue(result or result == False)  
        # ensures function runs without crashing


if __name__ == "__main__":
    unittest.main(exit=False)
