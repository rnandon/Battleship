###        IMPORTS
### =================================
from player import Player
from random import randint


class Game:
    def __init__(self, options, ui, testing=False):
        self.player1 = Player(options.player_names[0], options.ship_counts)
        self.player2 = Player(options.player_names[1], options.ship_counts)
        self.winner = None
        self.ui = ui
        if not testing:
            self.player_setup()
            self.run_game()
        if testing:
            self.test_setup()
            self.test_run_game()

    def player_setup(self):
        self.place_ships(self.player1)
        self.place_ships(self.player2)

    # Game flow
    # - Prompts & setup
    # - Initialize with prompt & setup results
    def place_ships(self, player):
        self.ui.display_screen_turn_start(player)
        automatic_placement = self.ui.prompt_for_placement_option(player)
        ships_to_place = []
        for key in player.fleet.ships.keys():
            current_ships = player.fleet.ships[key]
            for ship in current_ships:
                ships_to_place.append(ship)
        for ship in ships_to_place:
            if automatic_placement:
                self.automatically_place_ships(ship, player)
            else:
                self.get_input_and_place_ship(ship, player)
    
    def get_input_and_place_ship(self, ship, player):
        self.ui.display_screen_player_board(player)
        selected_coordinates = self.ui.prompt_for_ship_start_position()
        possible_directions = player.player_board.get_possible_ship_placement_directions(ship, selected_coordinates)
        # Check to make sure this is a valid cell and that there are possible directions to choose from 
        has_possible_directions = False
        for direction in possible_directions:
            if possible_directions[direction]:
                has_possible_directions = True
                break

        if has_possible_directions:
            selected_direction = self.ui.prompt_for_ship_direction(possible_directions)
            player.place_ship(ship, selected_coordinates, selected_direction)
        else:
            print("Invalid selection, please try again")
            self.get_input_and_place_ship(ship, player)

    def automatically_place_ships(self, ship, player):
        rows = "ABCDEFGHIJ"
        columns = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        row_selection = rows[randint(0, 9)]
        column_selection = columns[randint(0, 9)]
        selected_coordinates = (row_selection, column_selection)

        possible_directions = player.player_board.get_possible_ship_placement_directions(ship, selected_coordinates)
        possible_directions_filtered = [key for key in possible_directions.keys() if possible_directions[key]]

        if len(possible_directions_filtered) == 0:
            self.automatically_place_ships(ship, player)
        else:
            selected_direction = possible_directions_filtered[randint(0, len(possible_directions_filtered)-1)]
            player.place_ship(ship, selected_coordinates, selected_direction)

    def run_game(self):
        while not self.winner:
            self.player_turn(self.player1, self.player2)
            if self.winner:
                break
            else:
                self.player_turn(self.player2, self.player1)
            
        self.end_game()

    def player_turn(self, player, opponent, repeated=False):
        if not repeated:
            self.ui.display_screen_turn_start(player)
            self.ui.display_screen_game(player)

        attack_coordinates = self.ui.prompt_for_attack_coordinates()
        result = opponent.player_board.check_for_hit(attack_coordinates)

        if result == -1:
            print("Something went wrong, try again")
            self.player_turn(player, opponent, True)
        else:
            player.update_attack_results(attack_coordinates, result)
            self.ui.display_screen_outcome(result)

        self.check_for_winner()

    def check_for_winner(self):
        player1_lost = self.player1.check_for_defeat()
        player2_lost = self.player2.check_for_defeat()

        if player1_lost:
            self.winner = self.player2
        elif player2_lost:
            self.winner = self.player1
        

    def end_game(self):
        self.ui.display_screen_winner(self.winner)

    # - enter while loop
    # - - Player one turn
    # - - - Check for winner
    # - - Player two turn 
    # - - - Check for winner
    # - exit while loop when winner
    # - display exit
    # - prompt restart

    def test_setup(self):
        self.test_place_ships(self.player1)
        self.test_place_ships(self.player2)

    def test_run_game(self):
        self.test_player_turns() 
        self.end_game()

    def test_player_turns(self):
        for letter in "ABCDE":
            for number in [0, 1, 2, 3, 4]:
                attack_coordinates = (letter, number)
                result = self.player2.player_board.check_for_hit(attack_coordinates)
                self.player1.update_attack_results(attack_coordinates, result)
                print(self.player1.tracker_board)
                print(self.player2.player_board)
                self.check_for_winner()
                if self.winner:
                    return


    def test_place_ships(self, player):
        row_names = "ABCDE"
        row_index = 0
        i = 0
        ships_to_place = []
        for key in player.fleet.ships.keys():
            current_ships = player.fleet.ships[key]
            for ship in current_ships:
                ships_to_place.append(ship)
        for ship in ships_to_place:
            player.place_ship(ship, (row_names[i], row_index), "right")
            i += 1
