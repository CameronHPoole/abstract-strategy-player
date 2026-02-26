from catan.board.board import Board
from catan.board.board_layout import STANDARD_BOARD
import pytest

class TestBoard:
    def test_board_len(self):
        assert len(STANDARD_BOARD) == 19

    def test_valid_numberTokens(self):
        tokens = {'2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0}
        tokens_expected = {'2': 1, '3': 2, '4': 2, '5': 2, '6': 2, '8': 2, '9': 2, '10': 2, '11': 2, '12': 1}
        for coord, hex in STANDARD_BOARD.tiles.items():
            tokens[hex.numberToken] += 1
        assert tokens == tokens_expected