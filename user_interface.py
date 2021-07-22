###        IMPORTS
### =================================
import os
from time import sleep

class User_Interface:
    def __init__(self):
        self.left_pad_small = '\t'
        self.left_pad_large = '\t\t\t\t'
        self.end = '\n'

    # Sections
    # - Special strings
    # - - borders
    # - - spacing
    # - - layouts
    # - Displays

    # - - display_screen_welcome(self)
    def display_screen_welcome(self):
        screen_welcome = self.format_display_screen_welcome()
        print(screen_welcome)

    # - - display_screen_exit(self)
    def display_screen_exit(self):
        screen_exit = self.format_display_screen_exit()
        print(screen_exit)

    def display_screen_turn_start(self, player):
        screen_turn_start = self.format_display_screen_turn_start(player)
        input(screen_turn_start)

    # - - display_screen_game(self, player)
    def display_screen_game(self, player):
        screen_game = self.format_display_screen_game(player)
        print(screen_game)

    def display_screen_player_board(self, player):
        self.clear_console()
        screen_player_board = self.format_display_screen_player_board(player)
        print(screen_player_board)

    # - - display_screen_outcome(self, outcome)
    def display_screen_outcome(self, outcome):
        print(f"{self.left_pad_large}{outcome}")
        sleep(1)

    # - - display_screen_winner(self, winner)
    def display_screen_winner(self, winner):
        print(f'{winner.name} wins!')

    # - - display_screen_restart(self)
    def display_screen_restart(self):
        print(f"{self.left_pad_large}Play again? (Y/N):   ")


    # - Prompts
    # - - prompt_options_player_names(self)
    def prompt_options_player_names(self):
        name1 = input(f"{self.left_pad_large}What is player one's name?  ")
        name2 = input(f"{self.left_pad_large}What is player two's name?  ")
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
        return input(f"{self.left_pad_large}")

    def prompt_for_ship_start_position(self):
        return self.verify_coordinate_formatting(f"{self.left_pad_large}Select a start coordinate for ship ('A9')")

    def prompt_for_ship_direction(self, possible_directions):
        selections = []
        options = []
        i = 1
        for key in possible_directions.keys():
            if possible_directions[key]:
                selections.append(f'{i}')
                options.append(key)
                i += 1
        message = f"{self.left_pad_large}Which direction do you want to orient your ship?\n"
        for i in range(len(selections)):
            message += f'{self.left_pad_large}{self.left_pad_small} -{selections[i]}- {options[i]}\n'
        message += f"{self.left_pad_large}"

        return self.verify_selection_in_list(message, selections, options)

    def prompt_for_attack_coordinates(self):
        return self.verify_coordinate_formatting(f"{self.left_pad_large}What coordinates do you want to attack?")

    # - Verification
    # - - verify_selection_in_list(self, input, selections)
    def verify_selection_in_list(self, message, selections, options):
        invalid_selection = True
        user_selection = ""
        while invalid_selection:
            user_selection = input(message)
            if user_selection in selections:
                invalid_selection = False

        return options[int(user_selection)-1]

    # - - verify_coordinate_formatting(self, input)
    def verify_coordinate_formatting(self, message):
        invalid_selection = True
        user_selection = ""
        while invalid_selection:
            user_selection = input(message)
            if len(user_selection) == 2 and user_selection[0].upper() in "ABCDEFGHIJ" and user_selection[1] in "0123456789":
                invalid_selection = False

        return self.format_coordinates(user_selection)

    # - - verify_number -> might not be necessary
    # - - verify_string -> might not be necessary

    # - Formatting
    # - - format_coordinates(self, coordinates)
    def format_coordinates(self, coordinates):
        row = coordinates[0].upper()
        column = int(coordinates[1])
        return (row, column)

    # - - format_options(self, options)
    def format_options(self, options):
        pass

    # - - format_display_screen_game(self, player)
    def format_display_screen_game(self, player):
        player_board = player.player_board.printable
        tracker_board = player.tracker_board.printable

        split_player_board = player_board.split("\n")
        split_tracker_board = tracker_board.split("\n")

        output = ""
        output += f'{"*" * 106}\n'
        output += f'*{self.center_value_in_space(player.name, 104)}*\n'
        output += f'{"*" * 106}\n'
        output += f'*{self.center_value_in_space("YOUR SHIPS", 51)}||{self.center_value_in_space("TRACKER BOARD", 51)}*\n'
        output += f'{"*" * 106}\n'
        output += f'*{self.center_value_in_space("||", 104)}*\n'
        for i in range(len(split_player_board)):
            output += f'*{self.center_value_in_space(split_player_board[i], 51)}||{self.center_value_in_space(split_tracker_board[i], 51)}*\n'
        output += f'{"*" * 106}\n'

        return output


    # - - format_display_screen_winner(self, winner)
    def format_display_screen_winner(self, winner):
        self.clear_console()
        output = "\n\n"

        output += f'{self.left_pad_large}*******************************************\n'
        output += f'{self.left_pad_large}***                                     ***\n'
        output += f'{self.left_pad_large}***               WINNER:               ***\n'
        output += f'{self.left_pad_large}***{self.center_value_in_space(winner.name, 37)}***\n'
        output += f'{self.left_pad_large}***                                     ***\n'
        output += f'{self.left_pad_large}*******************************************\n\n'

        return output

    def center_value_in_space(self, value, total_columns):
        value_length = len(value)
        left_pad = (total_columns - value_length) // 2
        right_pad = total_columns - left_pad - value_length

        output = f"{' ' * left_pad}{value}{' ' * right_pad}"
        return output

    def format_display_screen_player_board(self, player):
        player_board = player.player_board.printable
        split_player_board = player_board.split("\n")

        output = ""
        output += f'{self.left_pad_large}{"*" * 53}{self.end}'
        output += f'{self.left_pad_large}*{self.center_value_in_space(player.name, 51)}*{self.end}'
        output += f'{self.left_pad_large}{"*" * 53}{self.end}'
        output += f'{self.left_pad_large}*{self.center_value_in_space("PLACE YOUR SHIPS", 51)}*{self.end}'
        output += f'{self.left_pad_large}{"*" * 53}{self.end}'
        output += f'{self.left_pad_large}*{" " * 51}*{self.end}'
        for i in range(len(split_player_board)):
            output += f'{self.left_pad_large}*{self.center_value_in_space(split_player_board[i], 51)}*{self.end}'
        output += f'{self.left_pad_large}{"*" * 53}{self.end}'

        return output

    def format_display_screen_welcome(self):
        output = "\n\n"

        output += f'{self.left_pad_large}*******************************************\n'
        output += f'{self.left_pad_large}***                                     ***\n'
        output += f'{self.left_pad_large}***        WELCOME TO BATTLESHIP        ***\n'
        output += f'{self.left_pad_large}***                                     ***\n'
        output += f'{self.left_pad_large}*******************************************\n\n'

        return output

    def format_display_screen_turn_start(self, player):
        self.clear_console()
        output = "\n\n\n\n"

        output += f'{self.left_pad_large}*******************************************\n'
        output += f'{self.left_pad_large}***                                     ***\n'
        output += f'{self.left_pad_large}***{self.center_value_in_space(player.name, 37)}***\n'
        output += f"{self.left_pad_large}***            IT'S YOUR TURN           ***\n"
        output += f'{self.left_pad_large}***                                     ***\n'
        output += f'{self.left_pad_large}*******************************************\n\n'

        return output

    def format_display_screen_exit(self):
        output = "\n\n"

        output += f'{self.left_pad_large}*******************************************\n'
        output += f'{self.left_pad_large}***                                     ***\n'
        output += f'{self.left_pad_large}***        THANK YOU FOR PLAYING        ***\n'
        output += f'{self.left_pad_large}***                                     ***\n'
        output += f'{self.left_pad_large}*******************************************\n\n'

        return output


    def clear_console(self):
        os.system('cls' if os.name == 'nt' else "clear")