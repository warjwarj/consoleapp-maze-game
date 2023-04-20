import pygame

from modules.Structure import Structure
from modules.Config import Config
from modules.Game import Game
from modules.Player import Player

pygame.init()

CLOCK = pygame.time.Clock()

STRUCT_CFG = Config.read("Structure")
ITEM_CFG = Config.read("Item")

SCREEN_HEIGHT = STRUCT_CFG["height"] * STRUCT_CFG["cell_size"]
SCREEN_WIDTH = STRUCT_CFG["width"] * STRUCT_CFG["cell_size"]
SCREEN = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
DRAWSPEED = STRUCT_CFG["draw_speed"]

# SCREEN = False
# CLOCK = False

# maze
struct = Structure(SCREEN, STRUCT_CFG, ITEM_CFG, CLOCK, drawspeed=1000)

# player
player = Player(struct, SCREEN)

# game instance
game = Game(SCREEN, struct, player)

# seperate thread, main game - have to run in seperate thread
game.consoleloop.start()

# main thread, pygame window
game.pygloop()