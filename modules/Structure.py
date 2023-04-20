# create the main structure of the maze
# each room is blind to others, each passage knows about the rooms it is connected to

from dataclasses import dataclass
import random
import pygame

from modules.Item import Item

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (222, 90, 67)
DARK_BLUE = (15, 99, 255)   
GREY = (92, 92, 92)
LIGHTER_GRAY = (145, 145, 145)
GREEN = (28, 252, 3)

@dataclass
class Cell():

    x: int
    y: int

    def draw(self, surface, cell_size, colour):
        self.rect = pygame.Rect(
            self.x * cell_size,
            self.y * cell_size,
            cell_size,
            cell_size
        )
        pygame.draw.rect(surface, colour, self.rect)

@dataclass
class Room(Cell):

    ''' room class '''

    dead: bool = False
    
    isExit: bool = False

    visited: bool = False

    item = Item()

    north_passage = "blocked."
    south_passage = "blocked."
    east_passage = "blocked."
    west_passage = "blocked."

    def describe(self):

        def describePassage(passage):
            if isinstance(passage, str):
                return passage
            elif isinstance(passage, Passage):
                return passage.x, passage.y
        
        return f"""
        ROOM: { self.x, self.y }

        north_passage: { describePassage(self.north_passage) }
        south_passage: { describePassage(self.south_passage) }
        east_passage: { describePassage(self.east_passage) }
        west_passage: { describePassage(self.west_passage) }

        ITEM:
            { self.item.describe() }

            """

@dataclass
class Passage(Cell):

    ''' passage class '''

    usable: bool = False

    north_room: Room = "n/a"
    south_room: Room = "n/a"
    east_room: Room = "n/a"
    west_room: Room = "n/a"

    def describe(self):  
        coordinates = self.x, self.y
        return f"""
        PASSAGE: { coordinates }:
            usable: { self.usable } \n """
    
class Structure():

    ''' the structure is the object that holds the information
    that describes the framework of the maze.'''

    reachable_rooms: list = []

    def assemble(self):

        ''' in order to create a random maze we need to
        create a grid and then draw the maze out of that grid.'''

        def grid(cols, rows, draw=False):

            ''' create a grid, starter for the maze. '''

            # populate grid
            grid_array = []
            dead_row = False
            room = True
            for y in range(rows):
                grid_array.append([])
                for x in range(cols):
                    if draw:
                        self.clock.tick()
                    if room:
                        if not dead_row:
                            grid_array[y].append(Room(y, x, dead=False))
                            if draw:
                                grid_array[y][-1].draw(self.screen, self.struct_config["cell_size"], BLACK)
                            room = False
                        else:
                            grid_array[y].append(Room(y, x, dead=True))
                            if draw:
                                grid_array[y][-1].draw(self.screen, self.struct_config["cell_size"], BLACK)
                            room = False
                    else:
                        grid_array[y].append(Passage(y, x))
                        if draw:
                            grid_array[y][-1].draw(self.screen, self.struct_config["cell_size"], WHITE)
                        room = not room
                if draw:
                    pygame.display.update()
                dead_row = not dead_row

            return grid_array

        # backtrack recursively
        def solve(grid_array, draw=False):

            cell = grid_array[random.randrange(2, self.struct_config['height'], 2)][random.randrange(2, self.struct_config['width'], 2)]

            # initialise the start point to begin creating the maze from
            cell_stack = [cell]

            # use to exit loop
            drawing_maze = True

            while drawing_maze:

                # define cell we finished on last time
                startroom = cell_stack[-1]

                x = startroom.x
                y = startroom.y

                # define lists for possible rooms to jump to and the passaeges inbetween
                possible_rooms = []
                possible_passages = []

                # populate lists above checking that the cell has not been visited before.
                try:
                    # WEST
                    room = grid_array[x + 2][y]
                    passage = grid_array[x + 1][y]
                    if isinstance(room, Room):
                        if not room.visited:
                            possible_rooms.append(room)
                            possible_passages.append(passage)
                        room.west_passage = passage
                        passage.east_room = room
                except IndexError:
                    print
                    pass
                try:
                    # EAST
                    room = grid_array[x - 2][y]
                    passage = grid_array[x - 1][y]
                    if isinstance(room, Room):
                        if not room.visited:
                            possible_rooms.append(room)
                            possible_passages.append(passage)
                        room.east_passage = passage
                        passage.west_room = room
                except IndexError:
                    pass
                try:
                    # SOUTH
                    room = grid_array[x][y + 2]
                    passage = grid_array[x][y + 1]
                    if isinstance(room, Room):
                        if not room.visited:
                            possible_rooms.append(room)
                            possible_passages.append(passage)
                        room.south_passage = passage
                        passage.north_room = room
                except IndexError:
                    pass
                try:
                    # NORTH
                    room = grid_array[x][y - 2]
                    passage = grid_array[x][y - 1]
                    if isinstance(room, Room):
                        if not room.visited:
                            possible_rooms.append(room)
                            possible_passages.append(passage)
                        room.north_passage = passage
                        passage.south_room = room
                except IndexError:
                    pass

                # mark visited
                startroom.visited = True

                # no dead end
                if len(possible_rooms) != 0:

                    # random number
                    r = random.randint(0, len(possible_rooms) - 1)

                    # choose a passage between cells to mark as usable
                    possible_passages[r].usable = True
                    
                    if draw:
                        possible_passages[r].draw(self.screen, self.struct_config["cell_size"], DARK_BLUE)
                    self.clock.tick()
                    pygame.display.update()

                    # append room to cell stack
                    cell_stack.append(possible_rooms[r])
                    print(possible_rooms[r])

                    self.reachable_rooms.append(possible_rooms[r])

                else:

                    # backtrack
                    room = cell_stack.pop()

                    # check finish
                    if len(cell_stack) == 0:
                        drawing_maze = False
                        self.finish = room
                        room.isExit = True

            return grid_array

        # create grid and draw maze out of it
        self.grid_array = solve(grid(self.struct_config["height"], self.struct_config["width"], True), True)

    def describe(self):
        for i in self.grid_array:
            for j in i:
                print(j.describe())
            print("""

            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            ROW
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

            """)

    def __init__(self, screen, struct_config, item_config, clock):
        self.struct_config = struct_config
        self.item_config = item_config
        self.screen = screen
        self.clock = clock