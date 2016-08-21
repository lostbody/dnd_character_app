import cPickle, pickle
import sys
import os

from collections import OrderedDict



traits_names = ['Name', 'Race', 'Class',
                'Strength', 'Dexterity', 'Constitution',
                'Intelligence', 'Wisdom', 'Charisma',
                'HP', 'Equipment']

traits_dict = OrderedDict()

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


def create_character2():
    global dndfileName
    dndfileName = raw_input(traits_names[0]+": ")
    global character


    character = Dnd_character(str(dndfileName), None, None, None, None, None, None,
        None, None, None, None)


    for traits_name in traits_names[1:]:
        setattr(character, traits_name, raw_input(traits_name + ": "))
    print character.Name, character.Class
    global character_traits



def write_dnd_character(dnd_file, character):
    with open(dndfileName + '.dnd', 'w+') as f:
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
        f.writelines(character.Equipment + "\n")

def show_character(dnd_file):

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
        print "Equipment" + ":" + character.Equipment

list1 = []
print len(list1)
# character.save()

# values = {
#      'title': 'This is edit title',
#      ...
#  }
#  for k, v in values.items():
#       setattr(ticket, k, v)

# # for i in range(0, len(traits_names)-1):
# #   olniki.__dict__[traits_names[i]] = raw_input(traits_names[i]+": ")

# # print 
# >>> x = SomeObject()
# >>> attr = 'myAttr'
# >>> # magic goes here
# >>> x.myAttr
# 'magic'

# setattr(x, attr, 'magic')
