"""
Choose your own adventure game.

Basics:

1.  Enter username
2.  Have a list of options and paths to move through game
3.  Read user input to move down a path
4.  Add monsters and fight logic

"""


import prompt_toolkit
from prompt_toolkit import prompt
import random
from random import randint

class Player:
    _name = "no_name"
    _health_points = 100

    def __init__(self, name, health=100):
        """ This is the constructor, or initializer.
        We accept 2 arguments.
        Required argument of 'name', and an optional argument with health points.
        """
        self._name = name
        self._health_points = health

    def name(self):
        return self._name

    def change_name(self, name):
        self._name = name

    def lower_hp(self, points=1):
        self._health_points -= points

    def heal(self, points=1):
        self._health_points += points

    def __str__(self):
        return "{} has health of: {}".format(self.name(), self._health_points)

    def is_dead(self):
        return self._health_points <= 0

    def player_attack(slef, GodZilla):
        GodZilla.lower_hp_monster(self._damage)
        print("{} has damaged the monster".format(self.name))
        if GodZilla.monster_dead():
            print("{} has killed the monster"format(self.name))
            


class GodZilla:
    """
    A monster should have the following attributes:
        * a name
        * hit points
        * maximum damage they can inflict

    A single method:
        * an attack method, which acceptsthe player and deducts
          maximum damage from the player's hitpoints
    """
    def __init__(self, name, health=100):
        self._name = name
        self._health_points = health
        #self._damage = 20
        self._damage = (randint(10, 50))


    def attack(self, player):
        player.lower_hp(self._damage)
        print("you have lost {} of health".format(self._damage))
        if player.is_dead():
            print('you are dead')
        else:
            print('you are damaged')

    def lower_hp_monster(self, points=1):
        self._health_points -= points

    def monster_dead(self):
        return self._health_points <= 0





class Caves:
    """
    'name' is substituted after the phrase "You are"
    'story' is free text that is printed to the user for what they can do or see
    'exits' is just the list of cave state's that are available to move to
    """
    cave_state = {0: {'name': "at the start of cave", 
                      'story': "You are at the start of the cave.  You see two paths ahead.",
                      'monsters': [],
                      'exits': [1,2] },
                  1: {'name': "in a dark tunnel",
                      'story': "You are in a tunnel with two exits.",
                      'monsters': [GodZilla('bob')],
                      'exits': [0, 2]},
                  2: {'name': 'at the end of the cave',
                      'story': "You have exited the cave.",
                      'monsters': [],
                      'exits': None}}


    def __init__(self):
        self._state = 0

    def prompt_user(self, player):
        cur_state = self.cave_state[self._state]
        print("\n")
        print("=" * 40) 
        print("{} is {}".format(player.name(), cur_state['name']))
        print("Where do you want to go?")
        exit_points = cur_state['exits']

        for exit_option in exit_points:
            option_details = self.cave_state[exit_option]
            print("{}: Go {}".format(exit_option, option_details['name']))

        option = prompt("Pick an option: ")

        # TODO: validate that the option is actually one of our
        # available choices

        # Force string value in 'option' to an integer
        self._state = int(option)

        # Return the new state of the cave
        return self._state

    def is_exited(self):
        # 2 is our magic number for the end of the cave
        result = self._state == 2
        if result:
            print("You have exited the cave.")
        return result

    def monster_attack(self, player):
        cur_state = self.cave_state[self._state]
        for monster in cur_state['monsters']:
            monster.attack(player)

def get_username():
    # Prompt the user for their name
    text = prompt('What is your name? ')
    return text


# This is where the code 'starts'
if __name__ == '__main__':
    user_name = get_username()
    p = Player(user_name, 30)
    caves = Caves()

    while not (caves.is_exited() or p.is_dead()):
        cave_state = caves.prompt_user(p)
        caves.monster_attack(p)

    print("Your final stats are below:")
    print(str(p))

    