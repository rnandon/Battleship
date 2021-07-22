###        IMPORTS
### =================================
from user_interface import User_Interface
from game import Game
from player import Player
from options import Options

class Game_Setup:
    def __init__(self, testing=False):
        self.ui = User_Interface()
        self.options = Options()
        # Currently leaving out set options, will navigate around it until MVP is implemented
        # After MVP, implement different options such as game modes, rules, etc.
        # self.set_options()

        if not testing:
            # Refactor this section out later
            self.ui.display_screen_welcome()
            self.select_player_names()
            # End section

            # Note: options has a field for custom rules, but it isn't currently implemented
            self.game = Game(self.options, self.ui)
            self.restart()

        if testing:
            self.options.player_names = ['Player1', 'Player2']
            self.game = Game(self.options, self.ui, testing)

    def set_options(self):
        self.ui.display_welcome()
        self.select_player_names()
        self.select_ship_count()
        self.select_rules()

    def select_player_names(self):
        self.options.player_names = self.ui.prompt_options_player_names()

    def select_ship_count(self):
        self.options.ship_counts =  self.ui.prompt_options_ships()

    def select_rules(self):
        self.options.rules = self.ui.prompt_options_rules()

    def restart(self):
        user_selection = self.ui.prompt_restart()
        if user_selection == "y":
            self.set_options()
            self.game = Game(self.player_names, self.ship_count, self.rules)
        else:
            self.ui.display_screen_exit()

    