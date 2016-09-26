
class Position(object):

    def __init__(self, row, col):
        Position.row = row
        Position.col = col


class Dungeon:

    def __init__(self, max_size):
        self.max_size = max_size
        self.entrance = Position(0, max_size)
        self.boss = Position(max_size, 2)
        self.current = Position(2, 2)

    def south(self):
        self.current.col -= 1

    def north(self):
        self.current.col += 1

    def east(self):
        self.current.row += 1

    def west(self):
        self.current.row -= 1

    def get_directions(self, current):

        options = ['north', 'south', 'west', 'east']

        if self.current.col == 0:
            options.remove('west')
        if self.current.col == self.max_size:
            options.remove('east')
        if self.current.row == 0:
            options.remove('north')
        if self.current.row == self.max_size:
            options.remove('south')
        return options
