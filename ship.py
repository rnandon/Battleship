###        IMPORTS
### =================================


class Ship:
    def __init__(self):
        self.name = ""
        self.length = 0
        self.status = "Intact"
        self.hit_locations = []

    def create_hit_locations(self):
        self.hit_locations = [0 for i in range(self.length)]

    def hit(self, hit_location):
        if self.hit_locations[hit_location] == 0:
            self.hit_locations[hit_location] = 1
            if self.is_destroyed():
                self.status = "Destroyed"
            else:
                self.status = "Damaged"
            # Successful hit
            return 1
        else:
            # Ship was already hit at this location
            return None

    def is_destroyed(self):
        is_destroyed = True
        for hit_location in self.hit_locations:
            if hit_location == 0:
                is_destroyed = False

        return is_destroyed

    def get_name(self):
        return self.name

    def get_status(self):
        return self.status