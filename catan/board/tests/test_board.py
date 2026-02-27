from catan.board.board import Board
from catan.board.board_layout import STANDARD_BOARD
from catan.board.hexes import Terrain, Hex
from catan.board.coordinates import CubeCoord
import pytest

terrains_expected = { 
    Terrain.FIELDS: 4, 
    Terrain.FOREST: 4, 
    Terrain.PASTURE: 4, 
    Terrain.HILLS: 3, 
    Terrain.MOUNTAINS: 3, 
    Terrain.DESERT: 1
    }

tokens_expected = {
    2: 1, 
    3: 2, 
    4: 2, 
    5: 2, 
    6: 2, 
    None: 1, 
    8: 2, 
    9: 2, 
    10: 2, 
    11: 2, 
    12: 1
    }

class TestBoard:
    def test_board_len(self):
        assert len(STANDARD_BOARD.tiles) == 19

    def test_terrain_counts(self):
        terrains = {
            Terrain.DESERT: 0, 
            Terrain.FIELDS: 0, 
            Terrain.FOREST: 0, 
            Terrain.PASTURE: 0, 
            Terrain.HILLS: 0, 
            Terrain.MOUNTAINS: 0
            }
        for coord, hex in STANDARD_BOARD.tiles.items():
            terrains[hex.terrainType] += 1
        assert terrains == terrains_expected

    def test_token_counts(self):
        tokens = {
            2: 0, 
            3: 0, 
            4: 0, 
            5: 0, 
            6: 0, 
            None: 0, 
            8: 0, 
            9: 0, 
            10: 0, 
            11: 0, 
            12: 0
            }
        for coord, hex in STANDARD_BOARD.tiles.items():
            tokens[hex.numberToken] += 1
        assert tokens == tokens_expected

    def test_get_hex_by_coord(self):
        coord = CubeCoord.hex_axial(0, 0)
        hex = STANDARD_BOARD.get_hex_by_coord(coord)
        assert hex == Hex(Terrain.HILLS, 12)

    def test_get_hex_by_token(self):
        sixes = STANDARD_BOARD.get_hex_by_token(6)
        assert len(sixes) == 2

    def test_get_desert_by_token(self):
        desert = STANDARD_BOARD.get_hex_by_token(None)
        assert STANDARD_BOARD.get_hex_by_coord(desert[0]).terrainType == Terrain.DESERT
