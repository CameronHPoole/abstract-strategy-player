# Your first test should assert that any hex has exactly 
# 6 neighbors, 6 vertices, and 6 edges, and 
# that neighbor relationships are symmetric (if A neighbors B, B neighbors A). 
# These two tests will catch 90% of coordinate bugs before they ever infect the rest of the codebase.

import pytest
from catan.board.coordinates import CubeCoord

class TestCubeCoord:
    def test_constuction(self):
        cc = CubeCoord(1, 0, -1)
        assert cc.q == 1 and cc.r == 0 and cc.s == -1
    
    def test_axial_construction(self):
        cc = CubeCoord.hex_axial(1, 0)
        assert cc.s == -1

    def test_origin(self):
        cc = CubeCoord.origin()
        assert cc.q == 0 and cc.r == 0 and cc.s == 0

    def test_invalid_hex(self):
        with pytest.raises(ValueError):
            CubeCoord(1, 2, 3)

    def test_frozen(self):
        cc = CubeCoord.origin()
        with pytest.raises(Exception):
            cc.q = 7 # type: ignore

    def test_equality(self):
        cc_1 = CubeCoord.hex_axial(0, 1)
        cc_2 = CubeCoord.hex_axial(0, 1)
        assert cc_1 == cc_2

class TestCubeCoordDist:
    def test_origin_dist_is_zero(self):
        assert CubeCoord.origin().dist_from_origin() == 0

    def test_immediate_neighbor_distance_is_one(self):
        cc = CubeCoord.hex_axial(2, 0)
        assert cc.dist_from_origin() == 2

    def test_dist_to_self_is_zero(self):
        cc = CubeCoord.hex_axial(1, -1)
        assert cc.dist_to(cc) == 0

    def test_dist_is_symmetric(self):
        a = CubeCoord.hex_axial(1, 0)
        b = CubeCoord.hex_axial(2, -1)
        assert a.dist_to(b) == b.dist_to(a)

    def test_known_dist(self):
        origin = CubeCoord.origin()
        other = CubeCoord.hex_axial(3, -3)
        assert origin.dist_to(other) == 3

class TestCubeCoordNeighbors:
    def test_origin_has_six_neighbors(self):
        assert len(CubeCoord.origin().neighbors()) == 6

    def test_all_coords_have_six_neighbors(self):
        # Every hex has exactly 6 neighbors
        test_coords = [
            CubeCoord.hex_axial(0, 0),
            CubeCoord.hex_axial(6, -1),
            CubeCoord.hex_axial(-9, 1),
        ]
        for coord in test_coords:
            assert len(coord.neighbors()) == 6

    def test_neighbors_are_dist_one(self):
        origin = CubeCoord.origin()
        for neighbor in origin.neighbors():
            assert origin.dist_to(neighbor) == 1

    def test_neighbor_relationship_is_symmetric(self):
        # if A neighbors B, B must neighbor A
        origin = CubeCoord.origin()
        for neighbor in origin.neighbors():
            assert origin in neighbor.neighbors()

    def test_neighbors_are_unique(self):
        neighbors = CubeCoord.origin().neighbors()
        assert 6 == len(set(neighbors))

    def test_neighbors_are_valid_cube_coords(self):
        # All neighbors must satisfy q+r+s=0
        for neighbor in CubeCoord.origin().neighbors():
            assert neighbor.q + neighbor.r + neighbor.s == 0

class TestVertexAndEdge:
    def test_hex_has_six_vertices(self):
        assert len(CubeCoord.origin().vertices()) == 6

    def test_hex_has_six_edges(self):
        assert len(CubeCoord.origin().edges()) == 6

    def test_shared_vertex_between_neighbors(self):
        a = CubeCoord.hex_axial(0, 2)
        b = CubeCoord.hex_axial(1, 2)
        shared = a.vertices() & b.vertices() # intersection of sets
        assert len(shared) == 2 # adjacent hexes share 2 vertices

    def test_shared_edge_between_neighbors(self):
        a = CubeCoord.hex_axial(0, 2)
        b = CubeCoord.hex_axial(1, 2)
        shared = a.edges() & b.edges() # intersection of sets
        assert len(shared) == 1 # adjacent hexes share 1 edge

    def test_non_adjacent_hexes_share_no_vertex(self):
        a = CubeCoord.hex_axial(0, 0)
        b = CubeCoord.hex_axial(2, 0)
        shared = a.vertices() & b.vertices() # intersection of sets
        assert len(shared) == 0 # non-adjacent hexes have no shared vreticies

    def test_non_adjacent_hexes_share_no_edges(self):
        a = CubeCoord.hex_axial(0, 0)
        b = CubeCoord.hex_axial(7, 0)
        shared = a.edges() & b.edges() # intersection of sets
        assert len(shared) == 0 # non-adjacent hexes have no shared edges