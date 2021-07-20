###        IMPORTS
### =================================
from player import Player


class Game:
    def __init__(self, player1_name, player2_name, ship_counts, ui):
        self.player1 = Player(player1_name, ship_counts)
        self.player2 = Player(player2_name, ship_counts)
        self.winner = None
