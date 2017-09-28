import sys

from .warrior import *
from .functions import *

user1 = Warrior('', '')
haveCharacter = False  # If false creates a character
game_exit = False  # If true exit games


# Creates a character
def start():
    global user1
    exitName = False
    exitGender = False
    user_name = 'None'
    user_gender = 'None'
    while not exitName:
        exitConfirmation = False
        print('what is your name?')
        user_input_name = getTitle()
        while not exitConfirmation:
            print('Is your name ' + user_input_name + '?')
            user_input = getInput(True, True)
            if user_input == 'yes':
                user_name = user_input_name
                exitName = True
                exitConfirmation = True
            elif user_input == 'no':
                exitConfirmation = True
            else:
                print('invalid input')
    while not exitGender:
        print('Are you male or female?')
        user_input = getInput(True, True)
        if user_input == 'male':
            user_gender = 'Male'
            exitGender = True
        elif user_input == 'female':
            user_gender = 'Female'
            exitGender = True
        else:
            print('invalid input')
    user1 = Warrior(user_name, user_gender)
    print(gridania.description)
    line()
    return user1


# If user doesn't have a character (haveCharacter = False)
# It creates a new character with the Warrior Class
# returns: user = Warrior()
def checkCharacter():
    global haveCharacter
    global user1
    if not haveCharacter:
        haveCharacter = True
        user1 = start()


# Do functions user types in input
def doInput():
    user_input = getInput(True, True)
    if user_input == 'exit':
        sys.exit()
    elif 'char' in user_input:
        user1.showCharacter()
    elif user_input == 'equip':
        user1.showInventory()
        print('What item you want to equip?')
        user_input = getInput(True, True)
        user1.equipItem(user_input)
    elif user_input == 'explore':
        user1.explore()
    elif 'inv' in user_input:
        user1.showInventory()
    elif 'armor' in user_input:
        user1.showArmory()
        line()
    elif 'recommended' in user_input or 'gear' in user_input:
        user1.recommendedArmory()
        print('Recommended gear equipped')
        line()
    else:
        print('Invalid Command')
        line()


def showOptions():
    print('Commands || Explore || Inv || Equip || Recommended Gear || Char || Armory || Exit')


# Main game function
def playGame():
    while not game_exit:
        checkCharacter()
        showOptions()
        doInput()
