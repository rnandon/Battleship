###        IMPORTS
### =================================


class User_Interface:
    def __init__(self):
        pass

    # Sections
    # - Special strings
    # - - borders
    # - - spacing
    # - - layouts
    # - Displays

    # - - display_screen_welcome(self)
    def display_screen_welcome(self):
        print("Welcome to Battleship!")

    # - - display_screen_exit(self)
    def display_screen_exit(self):
        print("Thanks for playing Battleship!")

    # - - display_screen_game(self, player)
    def display_screen_game(self, player):
        print(player.player_board)
        print(player.tracker_board)

    # - - display_screen_outcome(self, outcome)
    def display_screen_outcome(self, outcome):
        print(outcome)

    # - - display_screen_winner(self, winner)
    def display_screen_winner(self, winner):
        print(f'{winner.name} wins!')

    # - - display_screen_restart(self)
    def display_screen_restart(self):
        print("Play again?")

    # - Prompts
    # - - prompt_options_player_names(self)
    def prompt_options_player_names(self):
        name1 = input("What is player one's name?")
        name2 = input("What is player two's name?")
        return [name1, name2]

    # - - prompt_options_ships(self)
    def prompt_options_ships(self):
        pass

    # - - prompt_options_rules(self)
    def prompt_options_rules(self):
        pass

    # - - prompt_restart(self)
    def prompt_restart(self):
        self.display_screen_restart()
        return input()

    def prompt_for_ship_start_position(self):
        return self.verify_coordinate_formatting("Select a start coordinate for ship ('A9')")

    def prompt_for_ship_direction(self, possible_directions):
        selections = []
        for key in possible_directions.keys():
            if possible_directions[key]:
                selections.append(key)
        message = "Which direction do you want to orient your ship?"
        for selection in selections:
            message += f' - {selection}'

        return self.verify_selection_in_list(message, selections)

    def prompt_for_attack_coordinates(self):
        return self.verify_coordinate_formatting("What coordinates do you want to attack?")

    # - Verification
    # - - verify_selection_in_list(self, input, selections)
    def verify_selection_in_list(self, message, selections):
        invalid_selection = True
        user_selection = ""
        while invalid_selection:
            user_selection = input(message)
            if user_selection in selections:
                invalid_selection = False

        return user_selection

    # - - verify_coordinate_formatting(self, input)
    def verify_coordinate_formatting(self, message):
        invalid_selection = True
        user_selection = ""
        while invalid_selection:
            user_selection = input(message)
            if len(user_selection) == 2 and user_selection[0] in "ABCDEFGHIJ" and user_selection[1] in "0123456789":
                invalid_selection = False

        return self.format_coordinates(user_selection)

    # - - verify_number -> might not be necessary
    # - - verify_string -> might not be necessary

    # - Formatting
    # - - format_coordinates(self, coordinates)
    def format_coordinates(self, coordinates):
        row = coordinates[0]
        column = int(coordinates[1])
        return (row, column)

    # - - format_options(self, options)
    def format_options(self, options):
        pass

    # - - format_display_screen_game(self, player)
    def format_display_screen_game(self, player):
        pass

    # - - format_display_screen_winner(self, winner)
    def format_display_screen_winner(self, winner):
        pass
