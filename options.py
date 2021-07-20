###        IMPORTS
### =================================

class Options:
    def __init__(self):
        self.player_names = None
        self.rules = None
        self.ship_counts = None

    def set_player_names(self, player_names):
        self.player_names = player_names

    def set_rules(self, rules):
        self.rules = rules

    def set_ship_counts(self, ship_counts):
        self.ship_counts = ship_counts