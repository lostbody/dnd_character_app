class Position(object):

    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __str__(self):
        return str(self.row) + " , " + str(self.col)

    def south(self):
        return Position(self.row+1, self.col)

    def go_south(self):
        self.row += 1
        return self

    def north(self):
        return Position(self.row-1, self.col)

    def go_north(self):
        self.row -= 1
        return self

    def east(self):
        return Position(self.row, self.col+1)

    def go_east(self):
        self.col += 1
        return self

    def west(self):
        return Position(self.row, self.col-1)

    def go_west(self):
        self.col -= 1
        return self

class Player(object):

    def __init__(self, position):
        self.position = Position(position.row, position.col)


class Dungeon(object):

    def __init__(self, max_size):
        self.max_size = max_size
        self.entrance = Position(0, 0)
        self.boss = Position(max_size, 2)

    def get_directions(self, position):

        global options

        options = ['north', 'south', 'west', 'east']

        if position.col == 0:
            options.remove('west')
        if position.col == self.max_size:
            options.remove('east')
        if position.row == 0:
            options.remove('north')
        if position.row == self.max_size:
            options.remove('south')
        return options


def enter_dungeon():
    print "You enter the dungeon!"
    global dungeon, position, player
    dungeon = Dungeon(4)
    position = dungeon.entrance
    player = Player(position)
    while True:
        print "\nWhere do you want to go? Choose direction or press exit to leave the dungeon\n"
        print dungeon.get_directions(player.position)

        print "you are at position: ", player.position

        chosen_move = raw_input(">")

        if chosen_move in options:
            if chosen_move == "west":
                player.position.go_west()
            elif chosen_move == "east":
                player.position.go_east()
            elif chosen_move == "north":
                player.position.go_north()
            elif chosen_move == "south":
                player.position.go_south()

        elif chosen_move == "exit":
            return

        else:
            print "Sorry you can't go that way"
            continue

        # print player.position


enter_dungeon()
# print player.position
# position1.go_east()
# print position1
