###        IMPORTS
### =================================
from ship import Ship
from carrier import Carrier
from battleship import Battleship
from cruiser import Cruiser
from submarine import Submarine
from destroyer import Destroyer


class Fleet:
    def __init__(self, ship_counts):
        self.ships = self.build_fleet(ship_counts)
        self.living_ships_count = self.update_living_ships_count()

    def build_fleet(self, ship_counts):
        ships = {}

        ships["Carrier"] = [Carrier() for i in range(ship_counts["Carrier"])]
        ships["Battleship"] = [Battleship() for i in range(ship_counts["Battleship"])]
        ships["Cruiser"] = [Cruiser() for i in range(ship_counts["Cruiser"])]
        ships["Submarine"] = [Submarine() for i in range(ship_counts["Submarine"])]
        ships["Destroyer"] = [Destroyer() for i in range(ship_counts["Destroyer"])]

        return ships

    def update_living_ships_count(self):
        living_ships_count = 0
        for key in self.ships.keys():
            current_ships = self.ships[key]
            for ship in current_ships:
                if ship.status != "Destroyed":
                    living_ships_count += 1

        return living_ships_count

    def get_living_ships_count(self):
        return self.living_ships_count