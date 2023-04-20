import random

class Player():

    def randomRoom(self):

        room = random.choice(self.structure.reachable_rooms)

        while True:
            
            if room.east_passage == "blocked." and room.west_passage == "blocked." and room.north_passage == "blocked." and room.south_passage == "blocked.":
                room = random.choice(self.structure.reachable_rooms)
            else:
                return room
            
    # def moveRoom(self):
        
    def __init__(self, structure, screen):

        super().__init__()
        self.structure = structure
        self.screen = screen
        self.speed = 4
        self.wealth = 0
        self.room = self.randomRoom()

    def move(self, direction):

        error_advice = ""

        # choice
        if direction == "e" or direction == "east":
            try:
                #print(self.structure.grid_array[x - 1][y])
                if not type(self.room.east_passage) == str:
                    self.room = self.room.east_passage.east_room
                    self.room.draw()
                    return
                else:
                    error_advice = "you cannot go in that direction"
                    return error_advice
            except IndexError:
                print("at edge of grid")
                pass
        elif direction == "w" or direction == "west":
            try:
                #print(self.structure.grid_array[x + 1][y])
                if not type(self.room.west_passage) == str:
                    self.room = self.room.west_passage.west_room
                    return
                else:
                    error_advice = "you cannot go in that direction"
                    return error_advice
            except IndexError:
                print("at edge of grid")
                pass
        elif direction == "s" or direction == "south":
            try:
                #print(self.structure.grid_array[x][y + 1])
                if not type(self.room.south_passage) == str:
                    self.room = self.room.south_passage.south_room
                    return
                else:
                    error_advice = "you cannot go in that direction"
                    return error_advice
            except IndexError:
                print("at edge of grid")
                pass
        elif direction == "n" or direction == "north":
            try:
                #print(self.structure.grid_array[x][y - 1])
                if not type(self.room.north_passage) == str:
                    self.room = self.room.north_passage.north_room
                    return
                else:
                    self.error_advice = "you cannot go in that direction"
                    return error_advice
            except IndexError:
                print("at edge of grid")
                pass
        else:
            self.error_advice = "invalid input, make sure your input is e, w, s, or n."
            return error_advice




# DIFFERENT ROOM EVERY LOOP, PPRRROPPPER RECURSION