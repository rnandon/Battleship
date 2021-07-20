###        IMPORTS
### =================================
from ship import Ship

class Destroyer(Ship):
    def __init__(self):
        super().__init__()
        self.length = 2
        self.hit_locations = self.create_hit_locations()
        self.name = "Destroyer"
