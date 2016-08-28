
import random

character_stats = ['Strength', 'Dexterity', 'Consitution', 'Intelligence',
'Wisdom', 'Charisma']

classes = ['fighter', 'mage', 'cleric', 'thief']

races = ['dwarf', 'human', 'elf', 'hobbit']

equipment_available = ['dagger', 'axe', 'hammer', 'club', 'crossbow', 'padded', 'leather', 'Chainmail',
'shield', 'Food and Drink', 'clothes', 'compass']


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


def create_random_name():

    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
    'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
    syllable_count = random.randint(2, 3)
    i = 0
    syllable_list = []
    while i <= syllable_count:
        syllable = random.choice(vowels) + random.choice(consonants)
        syllable_list.append(syllable)
        i += 1
    name = "".join([str(x) for x in syllable_list])

    return name


def roll_for_stats(num_rolls, dice):

    total_roll = 0

    for i in range(0, num_rolls):
        rolled = random.randint(0, dice)
        total_roll += rolled

    return total_roll


def roll_for_HP(num_rolls, dice):

    total_roll = 0
    i = 0
    while i < num_rolls:
        rolled = random.randint(1, dice)
        if rolled > 2:
            total_roll += rolled
            i += 1
        else:
            continue

    return total_roll


def create_random_character():

    global character

    character = Dnd_character(None, None, None, None, None, None, None, None, None, None, [])

    character.Name = create_random_name()

    print "Name :", character.Name

    character.Race = random.choice(races)

    print "Race :", character.Race

    character.Class = random.choice(classes)

    print "Class :", character.Class

    for character_stat in character_stats:
        character.character_stat = roll_for_stats(3, 6)
        print character_stat, ":", character.character_stat

    if character.Class is "fighter":
        character.HP = roll_for_HP(1, 10)
        print "HP :", character.HP

    elif character.Class is "thief" or character.Class is "cleric":
        character.HP = roll_for_HP(1, 6)
        print "HP :", character.HP

    else:
        character.HP = roll_for_HP(1, 4)
        print "HP :", character.HP

    number_of_items = random.randint(1, len(equipment_available))

    i = 0
    while i <= number_of_items:
        equipment_item = random.choice(equipment_available)
        character.Equipment.append(equipment_item)
        i += 1

    for i in range(len(character.Equipment)):
        print "Equipment :", character.Equipment[i]


create_random_character()
