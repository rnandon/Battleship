###        IMPORTS
### =================================
from cell import Cell

class Board:
    def __init__(self):
        self.matrix = self.build_board()

    def build_board(self):
        # Build a dictionary of rows for coordinate access
        board = {}
        for char in "ABCDEFGHIJ":
            # Each row is full of cells, which contain special formatting for display methods
            board[char] = [Cell() for i in range(10)]

        return board

    def check_for_hit(self, coordinates):
        # Get the appropriate cell and its hit status
        selected_cell = self.get_cell(coordinates)
        cell_hit_status = selected_cell.check_for_hit()

        # Return status message
        if cell_hit_status == 1:
            return "Hit"
        elif cell_hit_status == 0:
            return "Miss"
        else:
            # To let the game know something went wrong
            return -1

    def update_attack_results(self, coordinates, results):
        selected_cell = self.get_cell(coordinates)
        selected_cell.set_status(results)

    def get_cell(self, coordinates):
        row = coordinates[0]
        column = coordinates[1]

        selected_cell = self.matrix[row][column]

        return selected_cell

    def check_cell_clearance(self, coordinates):
        # Traverse each direction through the matrix until either the top of the matrix or another ship is found
        # Start row and column serve as point of reference to get counts from
        directions = {"up":0, "right":0, "down":0, "left":0,}
        row_names = "ABCDEFGHIJ"
        start_row_key = coordinates[0]
        start_column = coordinates[1]
        start_row_index = row_names.find(start_row_key)

        # Up
        up_cells = self.get_other_cells_in_column(start_column, start_row_key, -1, True)
        up_count = len(up_cells)
        directions["up"] = up_count

        # Down
        down_cells = self.get_other_cells_in_column(start_column, start_row_key, len(row_names), True)
        down_count = len(down_cells)
        directions["down"] = down_count

        # Left
        left_cells = self.get_other_cells_in_row(self.matrix[coordinates[0]], start_column, -1, True)
        left_count = len(left_cells)
        directions["left"] = left_count

        # Right
        right_cells = self.get_other_cells_in_row(self.matrix[coordinates[0]], start_column, len(self.matrix[coordinates[0]]), True)
        right_count = len(right_cells)
        directions["right"] = right_count

        return directions

    def get_possible_ship_placement_directions(self, ship, coordinates):
        ship_length = ship.length
        clearances = self.check_cell_clearance(coordinates)
        possible_directions = {}

        for key in clearances.keys():
            enough_clearance = (clearances[key] >= ship_length)
            possible_directions[key] = enough_clearance

        return possible_directions

    def place_ship(self, ship, start_coordinate, direction):
        ship_length = ship.get_length()
        start_row_name = start_coordinate[0]
        start_column_index = start_coordinate[1]
        start_row = self.matrix[start_coordinate[0]]
        
        ship_placement_cells = []
        ship_placement_cells.append(self.get_cell(start_coordinate))

        additional_cells = []

        if direction == "up":
            additional_cells = self.get_other_cells_in_column(start_column_index, start_row_name, -1)
        elif direction == "down":
            additional_cells = self.get_other_cells_in_column(start_column_index, start_row_name, 10)
        elif direction == "right":
            additional_cells = self.get_other_cells_in_row(start_row, start_column_index, len(start_row))
        else:
            additional_cells = self.get_other_cells_in_row(start_row, 0, start_column_index)

        for i in range(ship_length-1):
            ship_placement_cells.append(additional_cells[i])

        self.fill_cells(ship, ship_placement_cells)

    def fill_cells(self, ship, ship_placement_cells):
        for i in range(len(ship_placement_cells)):
            current_cell = ship_placement_cells[i]
            current_cell.set_ship(ship, i)

    def get_other_cells_in_column(self, column_index, start_row_key, stop_index=-1, get_empty=False):
        row_names = "ABCDEFGHIJ"
        start_index = row_names.find(start_row_key)

        traverse_upward = (0 > (stop_index - start_index))
        traversal_speed = 1
        if traverse_upward:
            traversal_speed = -1
            

        cells = []

        for i in range(start_index, stop_index, traversal_speed):
            current_row = self.matrix[row_names[i]]
            current_cell = current_row[column_index]
            if get_empty:
                if current_cell.has_ship():
                    break
                else:
                    cells.append(current_cell)
            else:
                cells.append(current_cell)

        return cells

    def get_other_cells_in_row(self, row, start_index, stop_index=-1, get_empty=False):
        traverse_left = (0 > (stop_index - start_index))
        traversal_speed = 1
        if traverse_left:
            traversal_speed = -1

        cells = []

        for i in range(start_index, stop_index, traversal_speed):
            current_cell = row[i]
            if get_empty:
                if current_cell.has_ship():
                    break
                else:
                    cells.append(current_cell)
            else:
                cells.append(current_cell)

        return cells

    def __repr__(self):
        output = ""

        row_names = "ABCDEFGHIJ"

        output += "+-------------------------------------------+\n"
        output += "|   | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |\n"
        output += "+-------------------------------------------+\n"
        for row_name in row_names:
            output += f'| {row_name} |'
            for cell in self.matrix[row_name]:
                output += f'{cell}|'
            output += '\n'
            output += "+-------------------------------------------+\n"
        
        return output