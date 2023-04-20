import pygame
import sys

from modules.Structure import Structure
from modules.Config import Config
from modules.Game import Game
from modules.Player import Player

# pygame.init()

CLOCK = pygame.time.Clock()

STRUCT_CFG = Config.read("Structure")
ITEM_CFG = Config.read("Item")

SCREEN_HEIGHT = STRUCT_CFG["height"] * STRUCT_CFG["cell_size"]
SCREEN_WIDTH = STRUCT_CFG["width"] * STRUCT_CFG["cell_size"]
SCREEN = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))

# SCREEN = False
# CLOCK = False

# create maze
struct = Structure(SCREEN, STRUCT_CFG, ITEM_CFG, CLOCK)
struct.assemble()

# player
player = Player(struct, SCREEN)

# game instance
game = Game(SCREEN, struct, player)
game.loop()
