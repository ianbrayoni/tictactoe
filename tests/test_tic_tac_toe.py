from unittest import TestCase
from unittest.mock import patch

from tic_tac_toe import (
    create_board,
    select_any,
    winning_move,
    move_handler,
    play_corners,
    play_center,
    play_edges,
    play,
    is_safe_to_play,
)


class TestTicTacToeUtils(TestCase):
    def setUp(self):
        self.str_board = " xxo  o x"
        self.board = [" ", " ", "x", "x", "o", " ", " ", "o", " ", "x"]
        self.corners_positions = [1, 3, 7, 9]
        self.edge_positions = [2, 4, 6, 8]

    def tearDown(self):
        pass

    def test_create_board(self):
        self.assertEqual(self.board, create_board(self.str_board))

    def test_winning_move(self):
        board = [" ", "o", "x", "x", "o", " ", " ", "o", " ", "x"]
        self.assertTrue(winning_move(board))

    @patch("tic_tac_toe.random.randrange", return_value=0)
    def test_select_any(self, mock):
        self.assertEqual(select_any([1, 3, 5]), 1)

    def test_move_handler(self):
        self.assertEqual(move_handler(self.board), 1)

    def test_play_corners(self):
        response = play_corners([1, 4, 7, 8])
        assert response in self.corners_positions

    def test_play_center(self):
        response = play_center([5, 8])
        self.assertEqual(response, 5)

    def test_play_edges(self):
        response = play_edges([1, 2, 5])
        assert response in self.edge_positions

    def test_play(self):
        response = play(self.board)
        self.assertEqual(response, "oxxo  o x")
        self.assertEqual(len(response), 9)

    def test_is_safe_to_play(self):
        # valid board string
        self.assertTrue(is_safe_to_play(self.str_board))
        # unexpected characters received
        self.assertFalse(is_safe_to_play("aaa  ddf"))
        # there is a winner already
        self.assertFalse(is_safe_to_play("oxxo  o x"))
        # all inputs must be 9 characters long
        self.assertFalse(is_safe_to_play(self.str_board[:4]))
        # board is full
        self.assertFalse(is_safe_to_play("oxoxooxox"))
        # a player can only be one move ahead
        self.assertFalse(is_safe_to_play("oxxox  x "))
        self.assertFalse(is_safe_to_play("xooxo  o "))
