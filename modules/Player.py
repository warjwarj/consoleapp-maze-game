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




# DIFFERENT ROOM EVERY LOOP, PPRRROPPPER RECURSION