from catan.board.board import Board, Setup
from catan.board.hex_layout import STANDARD_TILES

STANDARD_BOARD = Board(
    tiles = STANDARD_TILES,
    coordByNumber = {}, # created in __post_init__
    boardType = Setup.STANDARD
)