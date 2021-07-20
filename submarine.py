###        IMPORTS
### =================================
from ship import Ship

class Submarine(Ship):
    def __init__(self):
        super().__init__()
        self.length = 3
        self.create_hit_locations()
        self.name = "Submarine"