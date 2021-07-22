###        IMPORTS
### =================================
from board import Board
from fleet import Fleet

class Player:
    def __init__(self, name, ship_counts):
        self.name = name
        self.player_board = Board()
        self.tracker_board = Board()
        self.fleet = Fleet(ship_counts)

    def place_ship(self, ship, start_coordinate, direction):
        self.player_board.place_ship(ship, start_coordinate, direction)

    def check_for_defeat(self):
        self.fleet.update_living_ships_count()
        if self.fleet.living_ships_count == 0:
            return True
        else:
            return False

    def update_attack_results(self, coordinates, results):
        self.tracker_board.update_attack_results(coordinates, results)