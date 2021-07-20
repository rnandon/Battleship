###        IMPORTS
### =================================


class Cell:
    def __init__(self):
        self.ship = None
        self.status = None
        self.hit_location = None

    def set_ship(self, ship, hit_location):
        self.ship = ship
        self.hit_location = hit_location

    def check_for_hit(self):
        # Check if already hit
        if self.status == "Hit":
            # If already hit, relay to checker
            return -1

        elif self.ship:
            hit_status = self.ship.hit(self.hit_location)
            # If the cell points to a ship, check for hit. If good, then change status
            if hit_status == 1:
                self.status = "Hit"
                return 1
            else:
                # Relay error to checker
                return -1
        else:
            # No ship, no hit.
            self.status = "Miss"
            return 0

    def has_ship(self):
        return self.ship != None

    def __repr__(self):
        if self.status == "Miss":
            return "   "
        elif self.status == "Hit":
            return " H "
        else:
            return "   "