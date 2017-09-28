import random

from .functions import pick_random_dict, percentage, getLifeBar
from .items import *


class Monster:
    def __init__(self, name, strength, defence, hp, lvl, exp):
        self.name = name
        self.strength = strength
        self.attack = strength
        self.defence = defence
        self.hp = hp
        self.max_hp = self.hp
        self.lvl = lvl
        self.experience = exp
        self.loot = {}
        self.drop = []

    def pick_loot(self):
        x = pick_random_dict(self.loot)
        if x == 0:
            self.drop = []
        else:
            self.drop = [x]

    def getAttack(self):
        r = random.randint(0, 20)
        x = percentage(r, self.strength)
        self.attack = x + self.strength
        self.attack = round(self.attack, 0)
        self.attack = int(self.attack)

    def lifeBar(self):
        t = getLifeBar(self.hp, self.max_hp)
        return t

        # Name, attack, defence, hp, lvl, exp
imp = Monster('Imp', 12, 2, 15, 1, 30)
imp.loot = {iron_sword: 0.10}

goblin = Monster('Goblin', 14, 5, 20, 3, 50)
goblin.loot = {iron_sword: 0.20}
