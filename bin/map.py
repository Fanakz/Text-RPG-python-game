from .functions import *
from .monsters import imp, goblin


class Shroud:
    def __init__(self):
        self.name = 'Black Shroud'
        self.description = 'You arrived at Shroud. Be aware of monsters!'
        self.NPCs = []
        self.monsters = {imp: 0.80, goblin: 0.20}
        self.next_locations = []
        self.lvl = 5
        self.chance = 30

    def findMonster(self):
        x = pick_random_dict(self.monsters)
        if x == 0:
            return 0
        return x


shroud = Shroud()


class Gridania:
    def __init__(self):
        self.name = 'Gridania'
        self.description = 'You are in the city of Gridania. Try exploring the city to proceed.'
        self.NPCs = []
        self.monsters = []
        self.next_location = shroud
        self.lvl = 1
        self.chance = 100

    def findMonster(self):
        x = pick_random_dict(self.monsters)
        if x == 0:
            return 0
        return x


gridania = Gridania()
