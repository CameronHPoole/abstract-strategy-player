from dataclasses import dataclass

@dataclass(frozen=True)
class ResourceMap:
    brick: int = 0
    wood: int = 0
    wool: int = 0
    grain: int = 0
    ore: int = 0

    def __post_init__(self):
        if not (
            self.grain >= 0 and
            self.wood >= 0 and
            self.wool >= 0 and
            self.brick >= 0 and
            self.ore >= 0
        ):
            raise ValueError('Invalid to have a negative resource')

    
    def can_afford(self, price: 'ResourceMap') -> bool:
        return (
            self.grain >= price.grain and 
            self.wood >= price.wood and 
            self.wool >= price.wool and 
            self.brick >= price.brick and 
            self.ore >= price.ore
            )
    
    def add(self, gain: 'ResourceMap') -> 'ResourceMap':
        return ResourceMap(
            grain = self.grain + gain.grain, 
            wood = self.wood + gain.wood,
            wool = self.wool + gain.wool, 
            brick = self.brick + gain.brick,
            ore = self.ore + gain.ore
            )
    
    def subtract(self, cost: 'ResourceMap') -> 'ResourceMap':
        return ResourceMap(
            grain = self.grain - cost.grain, 
            wood = self.wood - cost.wood,
            wool = self.wool - cost.wool,
            brick = self.brick - cost.brick,
            ore = self.ore - cost.ore
        )