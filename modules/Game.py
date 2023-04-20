import enum
import time
import os
import sys
import pygame

from modules.Structure import Passage, Room


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (222, 90, 67)
DARK_BLUE = (15, 99, 255)
GREY = (92, 92, 92)
LIGHTER_GRAY = (145, 145, 145)
GREEN = (28, 252, 3)
BROWN = (150, 75, 0)

class Game:

    def __init__(self, screen, structure, player):
        self.screen = screen
        self.structure = structure
        self.player = player
        self.error_advice = ""

    def loop(self):

        os.system("cls")

        if self.error_advice:
            print(self.error_advice)

        print(""" 
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                                MAZE-GAME

            The goal is to reach the exit, whilst picking up 
            items. Be careful! each item has the chance to add 
            to, or detract from your wealth.

            Each room will be described to you, along with the
            item inside that room. You can choose between
            picking up the item or not, making the descision
            based on whether or not you believe that item
            to be dangerous.

            Use Ctrl + C to exit the game at any time.

        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        """)

        if self.player.room.isExit == True:
            print(f"""

            CONGRATULATIONS!

            You Won!

            With a wealth of: { self.player.wealth }

            """)

            sys.exit()

        # describe current situation
        print(self.player.room.describe())

        # interact?
        interaction = input("do you want to interact with the item? (y/n) \n")
        if interaction == "yes" or interaction == "y" or interaction == "Y" or interaction == "YES":
            self.player.wealth += self.player.room.item.pickup(self.player.wealth) 

        # input
        direction = input("choose a direction to move to: (e = East, w = West, s = South, n = North) \n")
        
        # choice
        if direction == "e" or direction == "east":
            try:
                #print(self.structure.grid_array[x - 1][y])
                if not type(self.player.room.east_passage) == str:
                    self.player.room = self.player.room.east_passage.east_room
                    self.loop()
                else:
                    self.error_advice = "you cannot go in that direction"
                    self.loop()
            except IndexError:
                print("at edge of grid")
                pass
        elif direction == "w" or direction == "west":
            try:
                #print(self.structure.grid_array[x + 1][y])
                if not type(self.player.room.west_passage) == str:
                    self.player.room = self.player.room.west_passage.west_room
                    self.loop()
                else:
                    self.error_advice = "you cannot go in that direction"
                    self.loop()
            except IndexError:
                print("at edge of grid")
                pass
        elif direction == "s" or direction == "south":
            try:
                #print(self.structure.grid_array[x][y + 1])
                if not type(self.player.room.south_passage) == str:
                    self.player.room = self.player.room.south_passage.south_room
                    self.loop()
                else:
                    self.error_advice = "you cannot go in that direction"
                    self.loop()
            except IndexError:
                print("at edge of grid")
                pass
        elif direction == "n" or direction == "north":
            try:
                #print(self.structure.grid_array[x][y - 1])
                if not type(self.player.room.north_passage) == str:
                    self.player.room = self.player.room.north_passage.north_room
                    self.loop()
                else:
                    self.error_advice = "you cannot go in that direction"
                    self.loop()
            except IndexError:
                print("at edge of grid")
                pass
        else:
            self.error_advice = "invalid input, make sure your input is e, w, s, or n."
            self.loop()