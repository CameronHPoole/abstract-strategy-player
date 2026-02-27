from catan.game.resources import ResourceMap
import pytest

class TestResources:
    def test_invalid_init(self):
        with pytest.raises(ValueError):
            rm = ResourceMap(-1, 0, 0, 0, 0)

    def test_invlalid_sub(self):
        with pytest.raises(ValueError):
            rm = ResourceMap(0, 0, 0, 0, 0).subtract(ResourceMap(1, 0, 0, 0, 0))

    def test_can_afford(self):
        rm = ResourceMap(1, 1, 0, 0, 0)
        road_cost = ResourceMap(1, 1, 0, 0, 0)
        assert rm.can_afford(road_cost)

    def test_cannot_afford(self):
        rm = ResourceMap(0, 0, 0, 0, 0)
        road_cost = ResourceMap(1, 1, 0, 0, 0)
        assert not rm.can_afford(road_cost)

    def test_add(self):
        rm = ResourceMap(1, 2, 3, 4, 5)
        gain = ResourceMap(10, 9, 8, 7, 6)
        assert rm.add(gain) == ResourceMap(11, 11, 11, 11, 11)

    def test_sub(self):
        rm = ResourceMap(10, 9, 8, 7, 6)
        cost = ResourceMap(5, 4, 3, 2, 1)
        assert rm.subtract(cost) == ResourceMap(5, 5, 5, 5, 5)