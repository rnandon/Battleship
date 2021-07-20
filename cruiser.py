###        IMPORTS
### =================================
from ship import Ship

class Cruiser(Ship):
    def __init__(self):
        super().__init__()
        self.length = 3
        self.hit_locations = self.create_hit_locations()
        self.name = "Cruiser"
