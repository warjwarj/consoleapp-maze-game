import random
from modules.Config import Config

class Item:

    def random(self):
        treasure = random.choice(list(self.config["Treasure"].items()))
        trap = random.choice(list(self.config["Trap"].items()))
        r = random.randint(0, 1)
        if r == 0:
            self.item_nature = "treasure"
            return treasure
        elif r == 1:
            self.item_nature = "trap"
            return trap
        
    def pickup(self, wealth):
        wealth += self.item[1]
        if self.pickedup == False:
            print(f"""
                you interacted with: { self.item_nature }
                your wealth is now:  { wealth } \n
            """)
        else: 
            print("""
                you have already interacted with this item.
            """)
        self.pickedup = True
        return wealth
    
    def describe(self):
        return f"""
        { self.item[0] }
        """

    def __init__(self):
        self.config = Config.read("Item")
        self.item = self.random()
        self.pickedup = False