from .items import *
from .map import *


# user class
class Warrior:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.class_name = 'Warrior'
        self.strength = 4
        self.attack = self.strength
        self.lvl = 1
        self.experience = 0
        l = self.lvl + 1
        self.level_up = float(float(50) / float(3) * ((l ** 3) - 6 * (l ** 2) + 17 * l - 12))
        print(self.level_up)
        self.hp = 50
        self.max_hp = 50
        self.location = gridania
        self.inventory = []
        self.right_hand = [wooden_sword]
        self.left_hand = [wooden_shield]
        self.head = [cloth_head]
        self.chest = [cloth_chest]
        self.legs = [cloth_legs]
        self.feet = [cloth_feet]

    def getDefence(self):
        defence = self.strength
        if len(self.right_hand) > 0:
            defence = defence + self.right_hand[0].defence
        if len(self.left_hand) > 0:
            defence = defence + self.left_hand[0].defence
        if len(self.head) > 0:
            defence = defence + self.head[0].defence
        if len(self.chest) > 0:
            defence = defence + self.chest[0].defence
        if len(self.legs) > 0:
            defence = defence + self.legs[0].defence
        if len(self.feet) > 0:
            defence = defence + self.feet[0].defence
        return defence

    def getStrength_weaponAttack(self):
        attack = self.strength
        if len(self.right_hand) > 0:
            attack = attack + self.right_hand[0].attack
        return attack

    def getAttack(self):
        self.attack = 0
        if len(self.right_hand) > 0:
            self.attack += self.right_hand[0].attack
        self.attack += self.strength
        r = random.randint(0, 20)
        x = percentage(r, self.getStrength_weaponAttack())
        self.attack += x
        self.attack = round(self.attack, 0)
        self.attack = int(self.attack)


    def lifeBar(self):
        t = getLifeBar(self.hp, self.max_hp)
        return t

    # print name and gender
    def showCharacter(self):
        next_level = self.level_up - self.experience
        print('Name: ' + self.name)
        print('Gender: ' + self.gender)
        print('Class: ' + self.class_name)
        print('Attack: ' + str(self.strength) + ' + ' + str(self.getStrength_weaponAttack() - self.strength))
        print('Defence : ' + str(self.getDefence()-self.strength))
        print('Vitality: ' + str(self.max_hp))
        print('Level: ' + str(self.lvl))
        print('XP until next level: ' + str(next_level))
        line()

    # print inventory
    def showInventory(self):
        right_hand = []
        left_hand = []
        head = []
        chest = []
        legs = []
        feet = []
        rh_text = 'Weapons:  '
        lf_text = 'Shields:  '
        head_text = 'Head:     '
        chest_text = 'Chest:    '
        legs_text = 'legs:     '
        feet_text = 'Feet:     '
        for item in self.inventory:
            if item.style == 'weapon':
                right_hand.append(item)
            elif item.style == 'shield':
                left_hand.append(item)
            elif item.style == 'head':
                head.append(item)
            elif item.style == 'chest':
                chest.append(item)
            elif item.style == 'legs':
                legs.append(item)
            elif item.style == 'feet':
                feet.append(item)
        for x in right_hand:
            rh_text = rh_text + x.name + ', '
        for x in left_hand:
            lf_text = lf_text + x.name + ', '
        for x in head:
            head_text = head_text + x.name + ', '
        for x in chest:
            chest_text = chest_text + x.name + ', '
        for x in legs:
            legs_text = legs_text + x.name + ', '
        for x in feet:
            feet_text = feet_text + x.name + ', '
        lf_text = lf_text[:-2]
        rh_text = rh_text[:-2]
        head_text = head_text[:-2]
        chest_text = chest_text[:-2]
        legs_text = legs_text[:-2]
        feet_text = feet_text[:-2]
        print(rh_text)
        print(lf_text)
        print(head_text)
        print(chest_text)
        print(legs_text)
        print(feet_text)
        line()

    # equip any item in the inventory
    def equipItem(self, item):
        for x in self.inventory:
            if x.name.lower().replace(' ','') == item:
                if x.style == 'weapon':
                    if len(self.right_hand) == 1:
                        self.inventory.append(self.right_hand[0])
                        del self.right_hand[0]
                        self.right_hand.append(x)
                        self.inventory.remove(x)
                        print('item equipped')
                        line()
                        return 0
                    else:
                        self.right_hand.append(x)
                        self.inventory.remove(x)
                        print('item equipped')
                        line()
                        return 0
                elif x.style == 'shield':
                    if len(self.left_hand) == 1:
                        self.inventory.append(self.left_hand[0])
                        del self.left_hand[0]
                        self.left_hand.append(x)
                        self.inventory.remove(x)
                        print('item equipped')
                        line()
                        return 0
                    else:
                        self.left_hand.append(x)
                        self.inventory.remove(x)
                        print('item equipped')
                        line()
                        return 0
                elif x.style == 'head':
                    if len(self.head) == 1:
                        self.inventory.append(self.head[0])
                        del self.head[0]
                        self.head.append(x)
                        self.inventory.remove(x)
                        print('item equipped')
                        line()
                        return 0
                    else:
                        self.head.append(x)
                        self.inventory.remove(x)
                        print('item equipped')
                        line()
                        return 0
                elif x.style == 'chest':
                    if len(self.chest) == 1:
                        self.inventory.append(self.chest[0])
                        del self.chest[0]
                        self.chest.append(x)
                        self.inventory.remove(x)
                        print('item equipped')
                        line()
                        return 0
                    else:
                        self.chest.append(x)
                        self.inventory.remove(x)
                        print('item equipped')
                        line()
                        return 0
                elif x.style == 'legs':
                    if len(self.legs) == 1:
                        self.inventory.append(self.legs[0])
                        del self.legs[0]
                        self.legs.append(x)
                        self.inventory.remove(x)
                        print('item equipped')
                        line()
                        return 0
                    else:
                        self.legs.append(x)
                        self.inventory.remove(x)
                        print('item equipped')
                        line()
                        return 0
                elif x.style == 'feet':
                    if len(self.feet) == 1:
                        self.inventory.append(self.feet[0])
                        del self.feet[0]
                        self.feet.append(x)
                        self.inventory.remove(x)
                        print('item equipped')
                        line()
                        return 0
                    else:
                        self.feet.append(x)
                        self.inventory.remove(x)
                        print('item equipped')
                        line()
                        return 0
        print('item not found')

    # show equipped items
    def showArmory(self):
        try:
            print('Weapon: ' + self.right_hand[0].name)
        except:
            print('Weapon: ' + '')
        try:
            print('Shield: ' + self.left_hand[0].name)
        except:
            print('Shield: ')
        try:
            print('Head: ' + self.head[0].name)
        except:
            print('Head: ')
        try:
            print('Chest: ' + self.chest[0].name)
        except:
            print('Chest: ')
        try:
            print('Legs: ' + self.legs[0].name)
        except:
            print('Legs: ')
        try:
            print('Feet: ' + self.feet[0].name)
        except:
            print('Feet: ')

    def levelUp(self):
        if self.experience >= self.level_up:
            self.hp = self.max_hp
            self.lvl += 1
            l = self.lvl + 1
            self.level_up = float(float(50) / float(3) * ((l ** 3) - 6 * (l ** 2) + 17 * l - 12))
            self.max_hp += self.lvl
            self.strength += self.lvl
            print('Congratulations, you are now level ' + str(self.lvl) + '!')
            line()

    def recommendedArmory(self):
        right_hand = {}
        left_hand = {}
        head = {}
        chest = {}
        legs = {}
        feet = {}
        try:
            right_hand[self.right_hand[0]] = self.right_hand[0].attack
            del self.right_hand[0]
        except:
            pass

        try:
            left_hand[self.left_hand[0]] = self.left_hand[0].defence
        except:
            pass

        try:
            head[self.head[0]] = self.head[0].defence
        except:
            pass

        try:
            chest[self.chest[0]] = self.chest[0].defence
        except:
            pass

        try:
            legs[self.legs[0]] = self.legs[0].defence
        except:
            pass

        try:
            feet[self.feet[0]] = self.feet[0].defence
        except:
            pass

        for item in self.inventory:
            if item.style == 'weapon':
                right_hand[item] = item.attack
            elif item.style == 'shield':
                left_hand[item] = item.defence
            elif item.style == 'head':
                head[item] = item.defence
            elif item.style == 'chest':
                chest[item] = item.defence
            elif item.style == 'legs':
                legs[item] = item.defence
            elif item.style == 'feet':
                feet[item] = item.defence

        self.inventory = []
        x = max(right_hand, key=right_hand.get)
        self.right_hand.append(x)
        del right_hand[x]
        for item in right_hand:
            self.inventory.append(item)

        x = max(left_hand, key=left_hand.get)
        self.left_hand.append(x)
        del left_hand[x]
        for item in left_hand:
            self.inventory.append(item)

        x = max(head, key=head.get)
        self.head.append(x)
        del head[x]
        for item in head:
            self.inventory.append(item)

        x = max(chest, key=chest.get)
        self.chest.append(x)
        del chest[x]
        for item in chest:
            self.inventory.append(item)

        x = max(legs, key=legs.get)
        self.legs.append(x)
        del legs[x]
        for item in legs:
            self.inventory.append(item)

        x = max(feet, key=feet.get)
        self.feet.append(x)
        del feet[x]
        for item in feet:
            self.inventory.append(item)

    def explore(self):
        if self.lvl >= self.location.lvl :
            x = random.randint(0,100)
            if x <= self.location.chance:
                conf = False
                while not conf:
                    print('Do you want to proced to ' + self.location.next_location.name + '? | lvl ' \
                          + str(self.location.next_location.lvl))
                    user_input = getInput(True, True)
                    if user_input == 'yes':
                        self.location = shroud
                        print(self.location.description)
                        line()
                        conf = True
                    elif user_input == 'no':
                        conf = True
                    else:
                        line()
                        print('invalid input')
        else:
            monster = self.location.findMonster()
            if monster == 0:
                pass
            else:
                monster.hp = monster.max_hp
                monster.drop = []
                if monster is None or monster == 0:
                    return 0
                print('A wild ' + monster.name + ' Appeared!')
                print('Level: ' + str(monster.lvl))
                print(monster.lifeBar() + ' ' + str(monster.hp) + '/' + str(monster.max_hp))
                died = False
                while not died:
                    line()
                    print('Commands: Attack')
                    user_input = getInput(True, True)
                    if user_input == 'attack':
                        self.getAttack()
                        attack = self.attack
                        print('You dealt ' + str(attack) + ' damage')
                        attack = attack - monster.defence
                        if attack < 0:
                            attack = 0
                        monster.hp = monster.hp - attack
                        if monster.hp <= 0:
                            print('You killed the wild ' + monster.name + '!')
                            self.experience = self.experience + monster.experience
                            print('Gained ' + str(monster.experience) + ' XP!')
                            line()
                            self.levelUp()
                            monster.pick_loot()
                            if len(monster.drop) == 1:
                                print('Loot: ' + monster.drop[0].name)
                                conf = False
                                while not conf:
                                    print('Pick up the loot?')
                                    user_input = getInput(True, True)
                                    if user_input == 'yes':
                                        self.inventory.append(monster.drop[0])
                                        conf = True
                                    elif user_input == 'no':
                                        conf = True
                                    else:
                                        print('invalid command')
                            died = True
                        else:
                            defence = self.getDefence()
                            monster.getAttack()
                            enemy_damage = monster.attack - defence
                            if enemy_damage < 0:
                                enemy_damage = 0
                            print(monster.name + ' dealt ' + str(enemy_damage) + ' damage')
                            line()
                            self.hp = self.hp - enemy_damage
                            if self.hp <= 0:
                                print('You died')
                                died = True
                            else:
                                print('Your HP: ' + self.lifeBar() + ' ' + str(self.hp) + '/' + str(self.max_hp))
                                print(monster.name + ' HP: ' + monster.lifeBar() + ' ' + str(monster.hp) + '/' + str(monster.max_hp))
                    else:
                        print('Invalid Command')
