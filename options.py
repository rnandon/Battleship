###        IMPORTS
### =================================


# TODO - add default options for now

class Options:
    def __init__(self):
        self.player_names = None
        self.rules = None
        self.ship_counts = None

        self.default_player_names()
        self.default_ship_counts()

    def set_player_names(self, player_names):
        self.player_names = player_names

    def set_rules(self, rules):
        self.rules = rules

    def set_ship_counts(self, ship_counts):
        self.ship_counts = ship_counts

    def default_player_names(self):
        self.player_names = ['Player 1', 'Player 2']

    def default_rules(self):
        pass

    def default_ship_counts(self):
        ships = {}
        ships["Carrier"] = 1
        ships["Battleship"] = 2
        ships["Cruiser"] = 0
        ships["Submarine"] = 1
        ships["Destroyer"] = 1

        self.ship_counts = ships