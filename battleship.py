###        IMPORTS
### =================================
from ship import Ship

class Battleship(Ship):
    def __init__(self):
        super().__init__()
        self.length = 4
        self.hit_locations = self.create_hit_locations()
        self.name = "Battleship"
