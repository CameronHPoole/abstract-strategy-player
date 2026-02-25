from dataclasses import dataclass

@dataclass(frozen = True)
class CubeCoord:
    q: int
    r: int
    s: int
    VertexID = frozenset  # frozenset of 3 CubeCoords
    EdgeID = frozenset    # frozenset of 2 CubeCoords

    def __post_init__(self):
        if self.q + self.r + self.s != 0:
            raise ValueError(f"Invalid coordniates: q: {self.q}, r: {self.r}, s: {self.s}")

    @classmethod
    def hex(cls, q, r, s):
        return cls(q=q, r=r, s=s)

    @classmethod
    def hex_axial(cls, q, r):
        return cls(q=q, r=r, s=-q-r)
    
    @classmethod
    def origin(cls):
        return cls(0, 0, 0)
    
    def dist_from_origin(self):
        return max(abs(self.q), abs(self.r), abs(self.s))
    
    def dist_to(self, other: 'CubeCoord'):
        return max(abs(self.q - other.q), abs(self.r - other.r), abs(self.s - other.s))
    
    def neighbors(self) -> list['CubeCoord']:
        return [
            CubeCoord(self.q + d.q, self.r + d.r, self.s + d.s)
            for d in _CUBE_DIRECTIONS
        ]

    # vertices
    def vertices(self) -> set[VertexID]:
        neighbors = self.neighbors()
        vertex_set = set()
        for i in range(6):
            n1 = neighbors[i]
            n2 = neighbors[(i + 1) % 6] # wrap indicies above 5
            vertex_set.add(frozenset([self, n1, n2]))
        return vertex_set
    
    # edges
    def edges(self) -> set[EdgeID]:
        edge_set = set()
        for neighbor in self.neighbors():
            edge_set.add(frozenset([self, neighbor]))
        return edge_set

# order these in clock-wise starting to the right
_CUBE_DIRECTIONS = [
    CubeCoord(1, -1, 0),
    CubeCoord(1, 0, -1),
    CubeCoord(0, 1, -1),
    CubeCoord(-1, 1, 0),
    CubeCoord(-1, 0, 1),
    CubeCoord(0, -1, 1)
]