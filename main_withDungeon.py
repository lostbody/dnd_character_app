import sys
import os

from collections import OrderedDict


traits_names = ['Name', 'Race', 'Class',
                'Strength', 'Dexterity', 'Constitution',
                'Intelligence', 'Wisdom', 'Charisma',
                'HP', 'Equipment']


class Dnd_character(object):

    def __init__(self, Name, Race, Class, Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma, HP, Equipment):
        self.Name = Name
        self.Race = Race
        self.Class = Class
        self.Strength = Strength
        self.Dexterity = Dexterity
        self.Constitution = Constitution
        self.Intelligence = Intelligence
        self.Wisdom = Wisdom
        self.Charisma = Charisma
        self.HP = HP
        self.Equipment = Equipment


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

    def get_roomInfo(self, position):

        if player.position.row == dungeon.entrance.row and player.position.col == dungeon.entrance.col:
            return "This is the Entrance"

        elif player.position.row == dungeon.boss.row and player.position.col == dungeon.boss.col:
            return "This is the Boss room"

        else:
            return ""    


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
        if position.row == self.entrance.row and position.col == self.entrance.col:
            options.append('exit')
        return options



def create_character():

    global character

    character = Dnd_character(None, None, None, None, None, None, None, None, None, None, [])

    Name = raw_input("Name" + ": ")
    character.Name = Name

    Race = raw_input("Race" + ": ")
    character.Race = Race

    Class = raw_input("Class" + ": ")
    character.Class = Class

    Strength = raw_input("Strength" + ": ")
    character.Strength = Strength

    Dexterity = raw_input("Dexterity" + ": ")
    character.Dexterity = Dexterity

    Constitution = raw_input("Constitution" + ": ")
    character.Constitution = Constitution

    Intelligence = raw_input("Intelligence" + ": ")
    character.Intelligence = Intelligence

    Wisdom = raw_input("Wisdom" + ": ")
    character.Wisdom = Wisdom

    Charisma = raw_input("Charisma" + ": ")
    character.Charisma = Charisma

    HP = raw_input("HP" + ": ")
    character.HP = HP

    print "Enter equipment item and press 'Enter'.When you are done press 'Control+C'\n"
    while True:
        try:
            equipment_item = raw_input("Equipment" + ": ")
            character.Equipment.append(equipment_item)

        except KeyboardInterrupt:
            break

    write_dnd_character('characters/' + character.Name + ".dnd")


def write_dnd_character(character_file):

    with open(character_file, 'w+') as f:
        f.writelines(character.Name + "\n")
        f.writelines(character.Race + "\n")
        f.writelines(character.Class + "\n")
        f.writelines(character.Strength + "\n")
        f.writelines(character.Dexterity + "\n")
        f.writelines(character.Constitution + "\n")
        f.writelines(character.Intelligence + "\n")
        f.writelines(character.Wisdom + "\n")
        f.writelines(character.Charisma + "\n")
        f.writelines(character.HP + "\n")
        for equipment_item in character.Equipment:
            f.writelines(equipment_item + "\n")


def update_list_for_chosing():

    files = os.listdir("characters")

    global file_dict
    file_dict = dict()
    list_for_chosing = []

    for character_file in files:
        with open("characters/" + character_file) as f:
            char_name = f.readline().rstrip()
            file_dict.update(dict.fromkeys([character_file, char_name], "characters/" + character_file))
            pair = (char_name, character_file)
            list_for_chosing.append(pair)
    for i in list_for_chosing:
        print i

char_instances = []

def read_dnd_character(character_file):

    global character

    character = Dnd_character(None, None, None, None, None, None, None, None, None, None, [])

    with open(character_file) as f:

        content = f.readlines()

        lines = [line.strip() for line in content]
        character.Name = lines[0]
        character.Race =lines[1]
        character.Class = lines[2]
        character.Strength = lines[3]
        character.Dexterity = lines[4]
        character.Constitution = lines[5]
        character.Intelligence = lines[6]
        character.Wisdom = lines[7]
        character.Charisma = lines[8]
        character.HP = lines[9]
    # line 10 onwards there is one equip.item in each line

        character.Equipment = lines[10:]

    print "reading character file '%s'" % character_file

    with open(character_file) as f:

        content = f.readlines()

        lines = [line.strip() for line in content]

        char_instance = Dnd_character(lines[0], lines[1], lines[2], lines[3], lines[4], lines[5], lines[6], lines[7],
         lines[8], lines[9], lines[10:])

    char_instances.append(char_instance)

    return char_instance

    # print "reading character file '%s'" % character_file



def show_character(character_file):

    print "Name" + ": " + character.Name
    print "Race" + ":" + character.Race
    print "Class" + ":" + character.Class
    print "Strength" + ":" + character.Strength
    print "Dexterity" + ": " + character.Dexterity
    print "Constitution" + ":" + character.Constitution
    print "Intelligence" + ":" + character.Intelligence
    print "Wisdom" + ":" + character.Wisdom
    print "Charisma" + ":" + character.Charisma
    print "HP" + ":" + character.HP
    if len(character.Equipment) == 0:
        print "Equipment" + ":"
    else:
        for i in range(len(character.Equipment)):
            print "Equipment" + ":" + character.Equipment[i]

def edit_character_menu():
    global traits_dict
    traits_dict = OrderedDict()
    for index in range(0, len(traits_names)-1):
        traits_dict[str(index)] = traits_names[index]
    for i, j in traits_dict.items():
        print i, "--> ", j, "\n"


def modify_character(character_file):

    print "\nChoose a trait to modify or write 'back' to go back to main_menu:\n"
    edit_character_menu()
    choice = raw_input(">")

    if choice in traits_dict.keys():
        print choice, '-->', traits_names[int(choice)], "\n"
        newtrait_value = raw_input("Enter new value for trait: \n%s : " % traits_names[int(choice)])
        setattr(character, traits_names[int(choice)], newtrait_value)

        print "trait updated\n"
        write_dnd_character(character_file)

    elif choice == "back":
        print "Back to Main menu"

    else:
        print "not an option. Back to Main menu"


def exit(character_file):

    sys.exit(0)


def main_menu_options():
    global main_menu_dict
    main_menu_dict = OrderedDict()
    main_menu_options = [show_character, modify_character, edit_equipment, enter_dungeon, exit]
    for index in range(0, len(main_menu_options)):
        main_menu_dict[str(index)] = main_menu_options[index]
        print index, "--> ", main_menu_dict[str(index)].__name__, "\n"


def choose_character():

    try:

        while True:

            print "Choose a character writing the file name or character name OR write 'new' to create a new character\n"

            update_list_for_chosing()
            char_input = raw_input(">")

            if char_input in file_dict.keys():
                global character_file
                character_file = file_dict[char_input]
                main_menu()
            elif char_input == 'new':
                create_character()

            else:
                print "\nThere is no character file with this name.\n"
    except KeyboardInterrupt:

        print "got KeyboardInterrupt, exiting"
        sys.exit(0)


def main_menu():
    try:
        while True:
            print "\nMAIN MENU\n"

            read_dnd_character(character_file)

            print "What do you want to do with this DnD character?\n"
            main_menu_options()
            print "OR write 'back' to choose another character"
            choice = raw_input(">")

            if choice in main_menu_dict.keys():
                print "\nyou chose to:%s\n" % main_menu_dict[choice].__name__

                main_menu_dict[choice](character_file)
            elif choice == 'back':
                return
            else:
                print "Not an option. Please choose one of the options or exit"
    except KeyboardInterrupt:
        print "got KeyboardInterrupt, exiting"
        exit(character_file)


def edit_equipment_menu():
    global edit_equipment_dict
    edit_equipment_dict = OrderedDict()
    edit_equipment_options = ['add new item', 'remove item']
    for index in range(0, len(edit_equipment_options)):
        edit_equipment_dict[str(index)] = edit_equipment_options[index]
        print index, "--> ", edit_equipment_dict[str(index)], "\n"

    print "Equipment = %s" % character.Equipment


def edit_equipment(character_file):
    print "How do you want to modify your equipment list?\n"

    edit_equipment_menu()

    choice = raw_input(">")

    if choice == "0":
        print "\nyou chose to:%s\n" % edit_equipment_dict[str(choice)]

        new_item = (raw_input("Enter new item: "))

        character.Equipment.append(new_item)

        # setattr(character, "Equipment", Equipment)

        print "equipment updated\n%s\nBack to Main menu\n" % character.Equipment

        write_dnd_character(character_file)

    elif choice == "1":
        print "\nyou chose to:%s\n" % edit_equipment_dict[str(choice)]

        print "Which one of these items you want to remove?\n"

        for i in range(0, len(character.Equipment)):

            print i, ": ", character.Equipment[i]

        chosen_item = raw_input(">")

        if int(chosen_item) in range(0, len(character.Equipment)):
            print "you chose to remove: %s" % character.Equipment[int(chosen_item)]
            character.Equipment.pop(int(chosen_item))

        print "equipment updated\n%s\nBack to Main menu\n" % character.Equipment
        write_dnd_character(character_file)

    else:
        print "not an option. Back to Main menu"


def enter_dungeon(character_file):
    print "\nYou enter the dungeon!\n"
    global dungeon, position, player
    dungeon = Dungeon(4)
    position = dungeon.entrance
    player = Player(position)
    while True:
       
        print "\nyou are now at position: ", player.position
        
        print "\n", player.get_roomInfo(player.position)

        print "Choose direction! Below are your options. You have the option to exit when you are in the Entrance room\n"

        print dungeon.get_directions(player.position)

        chosen_move = raw_input(">\n")

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
            print "\nSorry you can't go that way\n"
            continue


files = os.listdir("characters")
class_dict = dict()
i = 0

for character_file in files:
    read_dnd_character("characters/" + character_file)
    class_dict[character_file] = char_instances[i]
    i += 1

choose_character()