from catan.board.board import Board
from catan.board.board_layout import STANDARD_BOARD
from catan.board.hexes import Terrain
import pytest

class TestBoard:
    def test_board_len(self):
        assert len(STANDARD_BOARD.tiles) == 19

    def test_valid_numbers(self):
        tokens = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, None: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
        tokens_expected = {2: 1, 3: 2, 4: 2, 5: 2, 6: 2, None: 1, 8: 2, 9: 2, 10: 2, 11: 2, 12: 1}

        terrains = {Terrain.DESERT: 0, Terrain.FIELDS: 0, Terrain.FOREST: 0, Terrain.HILLS: 0, Terrain.MOUNTAINS: 0, Terrain.PASTURE: 0}
        terrains_expected = {Terrain.DESERT: 1, Terrain.FIELDS: 4, Terrain.FOREST: 4, Terrain.HILLS: 3, Terrain.MOUNTAINS: 3, Terrain.PASTURE: 4}
        for coord, hex in STANDARD_BOARD.tiles.items():
            tokens[hex.numberToken] += 1
            terrains[hex.terrainType] += 1
            print(tokens, terrains)

        assert terrains == terrains_expected
        assert tokens == tokens_expected