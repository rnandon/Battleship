###        IMPORTS
### =================================
from player import Player


class Game:
    def __init__(self, options, ui):
        self.player1 = Player(options.player_names[0], options.ship_counts)
        self.player2 = Player(options.player_names[1], options.ship_counts)
        self.winner = None
        self.ui = ui
        self.player_setup()
        self.run_game()

    def player_setup(self):
        self.place_ships(self.player1)
        self.place_ships(self.player2)

    # Game flow
    # - Prompts & setup
    # - Initialize with prompt & setup results
    def place_ships(self, player):
        player_board = player.player_board
        ships_to_place = []
        for key in player.fleet.ships.keys():
            current_ships = player.fleet.ships[key]
            for ship in current_ships:
                ships_to_place.append(ship)
        for ship in ships_to_place:
            selected_coordinates = self.ui.prompt_for_ship_start_position()
            possible_directions = player_board.get_possible_ship_placement_directions(ship, selected_coordinates)
            selected_direction = self.ui.prompt_for_ship_direction(possible_directions)
            player.place_ship(ship, selected_coordinates, selected_direction)

    # - Player one place ships
    # - Player two place ships

    def run_game(self):
        while not self.winner:
            self.player_turn(self.player1, self.player2)
            if self.winner:
                break
            else:
                self.player_turn(self.player2, self.player1)
            
        self.end_game()

    def player_turn(self, player, opponent):
        attack_coordinates = self.ui.prompt_for_attack_coordinates()
        result = opponent.player_board.check_for_hit(attack_coordinates)

        if result == -1:
            print("Something went wrong, try again")
            self.player_turn(player, opponent)
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
        pass
    # - enter while loop
    # - - Player one turn
    # - - - Check for winner
    # - - Player two turn 
    # - - - Check for winner
    # - exit while loop when winner
    # - display exit
    # - prompt restart
