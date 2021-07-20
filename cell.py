###        IMPORTS
### =================================


class Cell:
    def __init__(self, ship=None):
        self.ship = ship
        self.status = None

    def check_for_hit(self):
        # Check if already hit
        if self.status == "Hit":
            # If already hit, relay to checker
            return -1

        elif self.ship:
            hit_status = self.ship.hit()
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
