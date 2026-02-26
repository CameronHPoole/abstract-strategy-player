from dataclasses import dataclass
from enum import Enum, auto
from collections import defaultdict
from catan.board.coordinates import CubeCoord
from catan.board.hexes import Hex, Terrain
from catan.board.hex_layout import STANDARD_BOARD_COORDS

class Setup(Enum):
    STANDARD = auto()   # Default layout of hexes and number tokens
    VARIABLE = auto()   # Variable/Random setup

@dataclass(frozen = True)
class Board:
    tiles: dict[CubeCoord, Hex]
    coordByNumber: dict[int | None, list[CubeCoord]]
    boardType: Setup
        
    def __post_init__(self):
        coordByNumber = defaultdict(list)
        for coord, hex in self.tiles.items():
            coordByNumber[hex.numberToken].append(coord)
        
        # set using setattr because board is frozen
        object.__setattr__(self, "coordByNumber", dict(coordByNumber))

        # validate board
        if self.boardType == Setup.STANDARD:
            for coord, hex in self.tiles.items():
                assert coord in STANDARD_BOARD_COORDS

    def get_hex_by_coord(self, coord: CubeCoord) -> Hex:
        return self.tiles[coord]

    def get_hex_by_token(self, token: int | None) -> list[CubeCoord]:
        return self.coordByNumber[token]