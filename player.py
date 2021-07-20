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
