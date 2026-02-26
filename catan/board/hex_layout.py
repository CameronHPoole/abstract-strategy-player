from catan.board.coordinates import CubeCoord
from catan.board.hexes import Hex, Terrain

STANDARD_BOARD_RADIUS = 2

def generate_board(radius: int) -> frozenset[CubeCoord]:
    board = []
    for r in range(-radius, radius + 1):
        for q in range(-radius, radius + 1):
            # have to make sure coords are valid
            if abs(q + r) <= radius:
                board.append(CubeCoord.hex_axial(q, r))
    return frozenset(board)

STANDARD_BOARD_COORDS = generate_board(STANDARD_BOARD_RADIUS)

STANDARD_TILES = {
    CubeCoord.hex_axial(+2,-2): Hex(Terrain.PASTURE, 11),
    CubeCoord.hex_axial(+1,-2): Hex(Terrain.FIELDS, 8),
    CubeCoord.hex_axial(+0,-2): Hex(Terrain.DESERT, None),
    CubeCoord.hex_axial(-1,-1): Hex(Terrain.HILLS, 6),
    CubeCoord.hex_axial(-2, 0): Hex(Terrain.FOREST, 10),
    CubeCoord.hex_axial(-2,+1): Hex(Terrain.FIELDS, 2),
    CubeCoord.hex_axial(-2,+2): Hex(Terrain.MOUNTAINS, 6),
    CubeCoord.hex_axial(-1,+2): Hex(Terrain.FIELDS, 3),
    CubeCoord.hex_axial( 0,+2): Hex(Terrain.PASTURE, 10),
    CubeCoord.hex_axial(+1,+1): Hex(Terrain.FOREST, 8),
    CubeCoord.hex_axial(+2, 0): Hex(Terrain.PASTURE, 5),
    CubeCoord.hex_axial(+2,-1): Hex(Terrain.MOUNTAINS, 9),
    CubeCoord.hex_axial(+1,-1): Hex(Terrain.FOREST, 4),
    CubeCoord.hex_axial( 0,-1): Hex(Terrain.PASTURE, 3),
    CubeCoord.hex_axial(-1, 0): Hex(Terrain.FIELDS, 5),
    CubeCoord.hex_axial(-1,+1): Hex(Terrain.HILLS, 9),
    CubeCoord.hex_axial( 0,+1): Hex(Terrain.MOUNTAINS, 4),
    CubeCoord.hex_axial(+1, 0): Hex(Terrain.FOREST, 11),
    CubeCoord.hex_axial( 0, 0): Hex(Terrain.HILLS, 12),
    }