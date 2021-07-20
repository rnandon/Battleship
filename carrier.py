###        IMPORTS
### =================================
from ship import Ship

class Carrier(Ship):
    def __init__(self):
        super().__init__()
        self.length = 5
        self.create_hit_locations()
        self.name = "Carrier"
