import core
import pyglet
from pyglet.window import key
from core import GameElement
import sys

class Rock(GameElement):
    IMAGE = "Rock"
    SOLID = True
 
class Character(GameElement):
    IMAGE = "Princess"

    def __init__(self):
        GameElement.__init__(self)
        self.inventory = []

    def next_pos(self, direction):
        if direction == "up":
            return (self.x, self.y-1)
        elif direction == "down":
            return (self.x, self.y+1)
        elif direction == "left":
            return (self.x-1, self.y)
        elif direction == "right":
            return (self.x+1, self.y)
        return None


class Gem(GameElement):
    IMAGE = "BlueGem"
    SOLID = False

    def interact(self, player):
        player.inventory.append(self)
        GAME_BOARD.draw_msg("You just acquired a gem! You have %d items!" %(len(player.inventory)))

#### DO NOT TOUCH ####
GAME_BOARD = None
DEBUG = False
KEYBOARD = None
PLAYER = None
######################

GAME_WIDTH = 5
GAME_HEIGHT = 5

#### Put class definitions here ####
pass
####   End class definitions    ####

def initialize():
    """Put game initialization code here"""
    # rock = Rock()
    # GAME_BOARD.register(rock)
    # GAME_BOARD.set_el(3, 3, rock)
    # print "The rock is at", (rock.x, rock.y)

    # #Initialize and register rock 1
    # rock1 = Rock()
    # GAME_BOARD.register(rock1)
    # GAME_BOARD.set_el(1, 1, rock1)

    # # initialize and register rock 2
    # rock2 = Rock()
    # GAME_BOARD.register(rock2)
    # GAME_BOARD.set_el(2, 2, rock2)

    # print "The first rock is at", (rock1.x, rock1.y)
    # print "The second rock is at", (rock2.x, rock2.y)
    # print "Rock 1 image", rock1.IMAGE
    # print "Rock 2 image", rock2.IMAGE

    rock_positions = [
        (2,1),
        (1,2),
        (3,2),
        (2,3)
    ]

    rocks = []

    for pos in rock_positions:
        rock = Rock()
        GAME_BOARD.register(rock)
        GAME_BOARD.set_el(pos[0], pos[1], rock)
        rocks.append(rock)

    rocks[-1].SOLID = False

    for rock in rocks:
        print rock


    #intitalize global player

    global PLAYER
    PLAYER = Character()
    GAME_BOARD.register(PLAYER)
    GAME_BOARD.set_el(2, 2, PLAYER)
    print PLAYER


    GAME_BOARD.draw_msg("This game is wicked awesome.")

    gem = Gem()
    GAME_BOARD.register(gem)
    GAME_BOARD.set_el(3,1,gem)

    gem2 = Gem()
    GAME_BOARD.register(gem2)
    GAME_BOARD.set_el(0,3,gem2)

def keyboard_handler():
    # if KEYBOARD[key.UP]:
    #     GAME_BOARD.draw_msg("You pressed up")
    #     next_y = PLAYER.y - 1
    #     GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
    #     GAME_BOARD.set_el(PLAYER.x, next_y, PLAYER)
    # elif KEYBOARD[key.DOWN]:
    #     GAME_BOARD.draw_msg("You pressed down")
    #     next_y = PLAYER.y + 1
    #     GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
    #     GAME_BOARD.set_el(PLAYER.x, next_y, PLAYER)
    # elif KEYBOARD[key.RIGHT]:
    #     GAME_BOARD.draw_msg("You pressed right")
    #     next_x = PLAYER.x + 1
    #     GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
    #     GAME_BOARD.set_el(next_x, PLAYER.y, PLAYER)
    # elif KEYBOARD[key.LEFT]:
    #     GAME_BOARD.draw_msg("You pressed left")
    #     next_x = PLAYER.x - 1
    #     GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
    #     GAME_BOARD.set_el(next_x, PLAYER.y, PLAYER)
    # else:
    #     KEYBOARD[key.SPACE]
    #     GAME_BOARD.erase_msg()
    direction = None

    if KEYBOARD[key.UP]:
        direction = "up"
    if KEYBOARD[key.DOWN]:
        direction = "down"
    if KEYBOARD[key.LEFT]:
        direction = "left"
    if KEYBOARD[key.RIGHT]:
        direction = "right"

    if direction:
        next_location = PLAYER.next_pos(direction)
        next_x = next_location[0]
        next_y = next_location[1]

        existing_el = GAME_BOARD.get_el(next_x, next_y)

        if existing_el:
            existing_el.interact(PLAYER)

        if existing_el is None or not existing_el.SOLID:
            GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
            GAME_BOARD.set_el(next_x, next_y, PLAYER)

        
        

