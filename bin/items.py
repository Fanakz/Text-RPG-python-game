class Item:
    def __init__(self, name, style):
        self.name = name
        self.style = style
        self.attack = 0
        self.defence = 0
        self.critic = 0


class Weapon(Item):
    def __init__(self, name, attack, critic):
        Item.__init__(self, name, 'weapon')
        self.attack = attack
        self.critic = critic


class Shield(Item):
    def __init__(self, name, defence):
        Item.__init__(self, name, 'shield')
        self.defence = defence


class Chest(Item):
    def __init__(self, name, defence):
        Item.__init__(self, name, 'chest')
        self.defence = defence


class Head(Item):
    def __init__(self, name, defence):
        Item.__init__(self, name, 'head')
        self.defence = defence


class Legs(Item):
    def __init__(self, name, defence):
        Item.__init__(self, name, 'legs')
        self.defence = defence


class Feet(Item):
    def __init__(self, name, defence):
        Item.__init__(self, name, 'feet')
        self.defence = defence


# Weapons
wooden_sword = Weapon('Wooden Sword', 5, 3)
iron_sword = Weapon('Iron Sword', 7, 5)

# shields
wooden_shield = Shield('Wooden Shield', 2)

# head
cloth_head = Head('Cloth Head Armor', 1)

# chest
cloth_chest = Chest('Cloth Chest Armor', 1)

# legs
cloth_legs = Legs('Cloth Leg Armor', 1)

# Feet
cloth_feet = Feet('Cloth Boots', 1)
