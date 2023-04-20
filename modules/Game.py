import os
import sys
import pygame
import threading

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
        self.consoleloop = threading.Thread(target=self.consoleloop)

    def pygloop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.flip()

    def consoleloop(self):

        os.system("cls")

        if self.error_advice:
            print(self.error_advice)

        print(""" 
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                                MAZE-GAME

                                Jon Ward
            
                github.com/warjwarj/consoleapp-maze-game

            The goal is to reach the exit, whilst picking up 
            items. Be careful! each item has the chance to add 
            to, or detract from your wealth.

            Each room will be described to you, along with the
            item inside that room. You can choose between
            picking up the item or not, making the descision
            based on whether or not you believe that item
            to be dangerous.

            Edit the 'config.json' file to customise the game.

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
        
        self.error_advice = self.player.move(direction)

        self.loop()