import random

def percentage(per, whole):
    return float(per) / 100 * whole

def getPercentage(part, whole):
    return float(part) / float(whole) * 100

def getLifeBar(hp, max_hp):
    per = getPercentage(hp, max_hp)
    full_bar = ['[', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
    t = ''
    if per > 95:
        for x in full_bar:
            t += x
        t += ']'
    elif per <= 95 and per > 90:
        full_bar = ['[', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#',
                    '#', '-']
        for x in full_bar:
            t += x
        t += ']'
    elif per <= 90 and per > 85:
        full_bar = ['[', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#',
                    '-', '-']
        for x in full_bar:
            t += x
        t += ']'
    elif per <= 85 and per > 80:
        full_bar = ['[', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '-',
                    '-', '-']
        for x in full_bar:
            t += x
        t += ']'
    elif per <= 80 and per > 75:
        full_bar = ['[', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '-',
                    '-', '-', '-']
        for x in full_bar:
            t += x
        t += ']'
    elif per <= 75 and per > 70:
        full_bar = ['[', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '-', '-',
                    '-', '-', '-']
        for x in full_bar:
            t += x
        t += ']'
    elif per <= 70 and per > 65:
        full_bar = ['[', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '-', '-', '-',
                    '-', '-', '-']
        for x in full_bar:
            t += x
        t += ']'
    elif per <= 65 and per > 60:
        full_bar = ['[', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '-', '-', '-', '-',
                    '-', '-', '-']
        for x in full_bar:
            t += x
        t += ']'
    elif per <= 60 and per > 55:
        full_bar = ['[', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '-', '-', '-', '-', '-',
                    '-', '-', '-']
        for x in full_bar:
            t += x
        t += ']'
    elif per <= 55 and per > 50:
        full_bar = ['[', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '-', '-', '-', '-', '-', '-',
                    '-', '-', '-']
        for x in full_bar:
            t += x
        t += ']'
    elif per <= 50 and per > 45:
        full_bar = ['[', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '-', '-', '-', '-', '-', '-', '-',
                    '-', '-', '-']
        for x in full_bar:
            t += x
        t += ']'
    elif per <= 45 and per > 40:
        full_bar = ['[', '#', '#', '#', '#', '#', '#', '#', '#', '# ', '-', '-', '-', '-', '-', '-', '-',
                    '-', '-', '-', '-']
        for x in full_bar:
            t += x
        t += ']'
    elif per <= 40 and per > 35:
        full_bar = ['[', '#', '#', '#', '#', '#', '#', '#', '#', '-', '-', '-', '-', '-', '-', '-', '-',
                    '-', '-', '-', '-']
        for x in full_bar:
            t += x
        t += ']'
    elif per <= 35 and per > 30:
        full_bar = ['[', '#', '#', '#', '#', '#', '#', '#', '-', '-', '-', '-', '-', '-', '-', '-', '-',
                    '-', '-', '-', '-']
        for x in full_bar:
            t += x
        t += ']'
    elif per <= 30 and per > 25:
        full_bar = ['[', '#', '#', '#', '#', '#', '#', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-',
                    '-', '-', '-', '-']
        for x in full_bar:
            t += x
        t += ']'
    elif per <= 25 and per > 20:
        full_bar = ['[', '#', '#', '#', '#', '#', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-',
                    '-', '-', '-', '-']
        for x in full_bar:
            t += x
        t += ']'
    elif per <= 20 and per > 15:
        full_bar = ['[', '#', '#', '#', '#', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-',
                    '-', '-', '-', '-']
        for x in full_bar:
            t += x
        t += ']'
    elif per <= 15 and per > 10:
        full_bar = ['[', '#', '#', '#', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-',
                    '-', '-', '-', '-']
        for x in full_bar:
            t += x
        t += ']'
    elif per <= 10 and per > 5:
        full_bar = ['[', '#', '#', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-',
                    '-', '-', '-', '-']
        for x in full_bar:
            t += x
        t += ']'
    elif per <= 5 and per > 0:
        full_bar = ['[', '#', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-',
                    '-', '-', '-', '-']
        for x in full_bar:
            t += x
        t += ']'
    elif per <= 0:
        full_bar = ['[', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-',
                    '-', '-', '-', '-']
        for x in full_bar:
            t += x
        t += ']'
    return t


def line():
    print('-----------------------------------------------------------------------------------------------------------')


# returns user input
# if space = True: user input W/O spaces
# if lower = True: user input will be all lower cased
def getInput(space, lower):
    line()
    user_input = input('-> ')
    line()
    if space:
        user_input = user_input.replace(' ', '')
    if lower:
        user_input = user_input.lower()
    return user_input


# first letter in all words in user input will be high cased
def getTitle():
    line()
    user_input = input('-> ')
    line()
    user_input = user_input.title()
    return user_input


# it picks a random object in a dictionary
def pick_random_dict(dictionary):
    r = random.uniform(0, 1)
    r = round(r, 2)
    for x in dictionary:
        r = r - dictionary[x]
        if r <= 0:
            cho = x
            return cho
    return 0
