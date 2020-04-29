#MAFIA PROJECT
import random, time

print('\033[1m' + '''Welcome to Mafia! Input the number of players:''' + '\033[0m')

# Change this to dictionary (or dictionary containing a dictionary, ie: when you look up John, it will display his role, dead/alive, framed status etc.)
# Or create a class variable for role? for XXX in class: if status == 'alive'...
roles = ['Sheriff', 'Doctor', 'Mayor', 'Escort', 'Amnesiac', 'Godfather', 'Framer', 'Jester', 'Jailor', 'Mafioso', 'Vigilante', 'Executioner']
playerList = []

def transfromList():
    global playerNumber
    global roles_transformed

    playerNumber = input()
    while True:
        try:
            playerNumber = int(playerNumber)
            break
        except ValueError:
            print('Please enter an integer, try again.')
            transfromList()

    if int(playerNumber) > 12:
        print('Maximum player limit (12) reached, try again.')
        transfromList()
    roles_transformed = roles[0:int(playerNumber)]
    #print(roles_transformed)

def inputPlayers():
    print()
    print('''Input player names:''')
    for i in range(int(playerNumber)):
        players = input()
        playerList.append(players)

# Maybe use dictionary here (call on integer values instead of looking up a word)
def assignRoles():
    global merged_list
    global merged_dct
    random_role = random.sample(roles_transformed, k = playerNumber)
    #print(playerList)
    #print(random_role)
    print()
    print('\033[1m' + 'Role assignment as follows: ' + '\033[0m')
    merged_list = [name + ': ' + role for name, role in zip(playerList, random_role)]
    #tuple(zip(playerList, random_role)) - Alternative method using tuples
    merged_dct = dict(zip(playerList, random_role))
    #print(merged_dct)
    for key, value in merged_dct.items():
        print(key, ':', value)

def nightTime():
    time.sleep(1)
    print()
    print('\033[1m' + 'Night Time...' + '\033[0m')

def godfatherNightCycle():
    global godfather_alive
    global godfather_target

    print()
    print('Now entering Godfather action phase...')
    print('Is the Godfather still alive? (y/n)')
    godfather_alive = ''
    godfather_target = ''

    while godfather_alive != 'y' or godfather_alive != 'n':
        godfather_alive = str(input())
        if godfather_alive == 'y':
            print('Who will the Godfather appoint to kill?')
            godfather_target = ''
            while godfather_target not in playerList:
                godfather_target = str(input())
                if godfather_target not in playerList:
                    print('Player not found, try again')
                elif godfather_target == merged_list[int(godfather_target)-1]:
                    print('Cannot target self.')
            return godfather_target
        elif godfather_alive == 'n':
            print('The Godfather is dead')
            return godfather_alive
        else:
            print('Select y/n, try again')
    return godfather_alive

def mafiosoNightCycle():
    global mafioso_alive
    global mafioso_target

    print()
    print('Now entering Mafioso action phase...')
    print('Is the Mafioso still alive? (y/n)')
    mafioso_alive = ''
    mafioso_target = ''

    while mafioso_alive != 'y' or mafioso_alive != 'n':
        mafioso_alive = str(input())
        if mafioso_alive == 'y':
            print('Who will the Mafioso kill?')
            mafioso_target = ''
            while mafioso_target not in playerList:
                mafioso_target = str(input())
                if mafioso_target not in playerList:
                    print('Player not found, try again')
            return mafioso_target
        elif mafioso_alive == 'n':
            print('The Mafioso is dead')
            return mafioso_alive
        else:
            print('Select y/n, try again')
    return mafioso_alive

def framerNightCycle():
    global framer_alive
    global framer_target

    print()
    print('Now entering Framer action phase...')
    print('Is the Framer still alive? (y/n)')
    framer_alive = ''
    while framer_alive != 'y' or framer_alive != 'n':
        framer_alive = str(input())
        if framer_alive == 'y':
            print('Who will the Framer frame?')
            framer_target = ''
            while framer_target not in playerList:
                framer_target = str(input())
                if framer_target not in playerList:
                    print('Player not found, try again')
            return framer_target
        elif framer_alive == 'n':
            print('The Framer is dead')
            return framer_alive
        else:
            print('Select y/n, try again')
    return framer_alive

def mafiaTargetCheck():
    print()
    time.sleep(1)
    if godfather_alive == 'n':
        print('With no Godfather, ' + mafioso_target + ''' becomes tonight's target.''')
    elif mafioso_alive == 'n':
        print('With no Mafioso, ' + godfather_target + ''' becomes tonight's target.''')
    elif godfather_target != mafioso_target:
        print('The Mafioso must comply with the Godfather, ' + godfather_target + ''' is tonight's target.''')
    else:
        print('The Mafia came to an agreement, ' + godfather_target + ''' is tonight's target.''')

transfromList()
inputPlayers()
assignRoles()
nightTime()
godfatherNightCycle()
mafiosoNightCycle()
framerNightCycle()
mafiaTargetCheck()
