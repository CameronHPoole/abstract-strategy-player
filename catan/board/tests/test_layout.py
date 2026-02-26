from catan.board.coord_layout import generate_board, STANDARD_BOARD_COORDS, STANDARD_BOARD_RADIUS
from catan.board.coordinates import CubeCoord

class TestLayout:
    def test_standard_board_has_19_hexes(self):
        assert len(STANDARD_BOARD_COORDS) == 19

    def test_all_hexes_within_radius(self):
        for hex in STANDARD_BOARD_COORDS:
            assert hex.dist_from_origin() <= STANDARD_BOARD_RADIUS

    def test_center_hex_exists(self):
        assert CubeCoord.origin() in STANDARD_BOARD_COORDS

    def test_custom_radius_0_has_1_hex(self):
        assert len(generate_board(0)) == 1

    def test_custom_radius_1_has_7_hexes(self):
        assert len(generate_board(1)) == 7

    def test_custom_radius_5_has_91_hexes(self):
        assert len(generate_board(5)) == 91

    def test_custom_radius_7_has_169_hexes(self):
        assert len(generate_board(7)) == 169
