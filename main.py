###        IMPORTS
### =================================
from battleship import Battleship
from game_setup import Game_Setup
from board import Board

def main():
    #game = Game_Setup()
    board = Board()
    board.place_ship(Battleship(), ('A', 0), "right")
    current_cell = board.get_cell(('A', 0))
    current_cell.check_for_hit()
    print(board)
main()