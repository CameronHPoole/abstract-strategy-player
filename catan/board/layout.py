from catan.board.coordinates import CubeCoord

STANDARD_BOARD_RADIUS = 2

def generate_board(radius: int) -> frozenset[CubeCoord]:
    board = []
    for r in range(-radius, radius + 1):
        for q in range(-radius, radius + 1):
            # have to make sure coords are valid
            if abs(q + r) <= radius:
                board.append(CubeCoord.hex_axial(q, r))
    return frozenset(board)

STANDARD_BOARD = generate_board(STANDARD_BOARD_RADIUS)
