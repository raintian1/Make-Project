#MAFIA PROJECT
import random, time

print('\033[1m' + '''Welcome to Mafia! Input the number of players:''' + '\033[0m')

# Change this to dictionary (or dictionary containing a dictionary, ie: when you look up John, it will display his role, dead/alive, framed status etc.)
# Or create a class variable for role? for XXX in class: if status == 'alive'...
roles = ['Sheriff', 'Doctor', 'Mayor', 'Escort', 'Amnesiac', 'Godfather', 'Framer', 'Jester', 'Jailor', 'Mafioso', 'Vigilante', 'Executioner']
playerList = []
alive = {}

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

def assignRoles():
    global merged_list
    global merged_dct
    random_role = random.sample(roles_transformed, k = playerNumber)
    #print(playerList)
    #print(random_role)
    print()
    print('\033[1m' + 'Role assignment as follows: ' + '\033[0m')
    merged_list = [name + ': ' + role for name, role in zip(random_role, playerList)]
    #tuple(zip(playerList, random_role)) - Alternative method using tuples
    merged_dct = dict(zip(random_role, playerList))
    print(merged_dct)
    for key, value in merged_dct.items():
        print(key, ':', value)

def nightTime():
    time.sleep(1)
    print()
    print('\033[1m' + 'Night Time...' + '\033[0m')

def godfatherNightCycle():
    print()
    print('Now entering Godfather action phase...')

    godfatherAlive()

def godfatherAlive():
    global godfather_alive

    print('Is the Godfather still alive? (y/n)')
    godfather_alive = ''
    while godfather_alive != 'y' or godfather_alive != 'n':
        godfather_alive = str(input())
        if godfather_alive == 'y':
            print('Who will the Godfather appoint to kill?')
            godfather_target = ''
            godfatherTarget()
        elif godfather_alive == 'n':
            print('The Godfather is dead')
            mafiosoNightCycle()
        else:
            print('Select y/n, try again')
    return godfather_alive

def godfatherTarget():
    global godfather_target

    godfather_target = ''
    while godfather_alive == "y":
        godfather_target = str(input())
        if godfather_target not in playerList:
            print('Player not found, try again')
        elif godfather_target == merged_dct["Godfather"]:
            print('Cannot target a member of the Mafia. Try again')
        else:
            mafiosoNightCycle()
    return godfather_target

def mafiosoNightCycle():
    print()
    print('Now entering Mafioso action phase...')

    mafiosoAlive()

def mafiosoAlive():
    global mafioso_alive

    print('Is the Mafioso still alive? (y/n)')
    mafioso_alive = ''
    while mafioso_alive != 'y' or mafioso_alive != 'n':
        mafioso_alive = str(input())
        if mafioso_alive == 'y':
            print('Who will the Mafioso kill?')
            mafioso_target = ''
            mafiosoTarget()
        elif mafioso_alive == 'n':
            print('The Mafioso is dead')
            mafiaTargetCheck()
            framerNightCycle()
        else:
            print('Select y/n, try again')
    return mafioso_alive

def mafiosoTarget():
    global mafioso_target

    mafioso_target = ''
    while mafioso_alive == "y":
        mafioso_target = str(input())
        if mafioso_target not in playerList:
            print('Player not found, try again')
        elif mafioso_target == merged_dct["Mafioso"]:
            print('Cannot target a member of the Mafia. Try again')
        else:
            mafiaTargetCheck()
            framerNightCycle()
    return mafioso_target

def framerNightCycle():
    print()
    print('Now entering Framer action phase...')

    framerAlive()

def framerAlive():
    global framer_alive

    print('Is the Framer still alive? (y/n)')
    framer_alive = ''
    while framer_alive != 'y' or framer_alive != 'n':
        framer_alive = str(input())
        if framer_alive == 'y':
            print('Who will the Framer frame?')
            framer_target = ''
            framerTarget()
        elif framer_alive == 'n':
            print('The Framer is dead')
            jailorNightCycle()
        else:
            print('Select y/n, try again')
    return framer_alive

def framerTarget():
    global framer_target

    framer_target = ''
    while framer_alive == "y":
        framer_target = str(input())
        if framer_target not in playerList:
            print('Player not found, try again')
        elif framer_target == merged_dct["Framer"]:
            print('Cannot target a member of the Mafia. Try again')
        else:
            jailorNightCycle()
    return framer_target

def mafiaTargetCheck():
    print()
    time.sleep(1)
    global mafiaside_target

    if godfather_alive == 'n':
        print('With no Godfather, ' + mafioso_target + ''' becomes tonight's target.''')
        mafiaside_target = mafioso_target
    elif mafioso_alive == 'n':
        print('With no Mafioso, ' + godfather_target + ''' becomes tonight's target.''')
        mafiaside_target = godfather_target
    elif godfather_target != mafioso_target:
        print('The Mafioso must comply with the Godfather, ' + godfather_target + ''' is tonight's target.''')
    else:
        print('The Mafia came to an agreement, ' + godfather_target + ''' is tonight's target.''')

def jailorNightCycle():
    print()
    print('Now entering Jailor action phase...')

    jailorAlive()

def jailorAlive():
    global jailor_alive

    print('Is the Jailor still alive? (y/n)')
    jailor_alive = ''
    while jailor_alive != 'y' or jailor_alive != 'n':
        jailor_alive = str(input())
        if jailor_alive == 'y':
            print('Who will the Jailor jail?')
            jailor_target = ''
            jailorTarget()
        elif jailor_alive == 'n':
            print('The Jailor is dead')
            escortNightCycle()
        else:
            print('Select y/n, try again')
    return jailor_alive

def jailorTarget():
    global jailor_target

    jailor_target = ''
    while jailor_alive == "y":
        jailor_target = str(input())
        if jailor_target not in playerList:
            print('Player not found, try again')
        elif jailor_target == merged_dct["Jailor"]:
            print('You cannot target yourself. Try again')
        else:
            escortNightCycle()
    return jailor_target

def escortNightCycle():
    print()
    print('Now entering Escort action phase...')

    escortAlive()

def escortAlive():
    global escort_alive

    print('Is the Escort still alive? (y/n)')
    escort_alive = ''
    while escort_alive != 'y' or escort_alive != 'n':
        escort_alive = str(input())
        if escort_alive == 'y':
            print('Who will the Escort distract?')
            escort_target = ''
            escortTarget()
        elif escort_alive == 'n':
            print('The Escort is dead')
            sheriffNightCycle()
        else:
            print('Select y/n, try again')
    return escort_alive

def escortTarget():
    global escort_target

    escort_target = ''
    while escort_alive == "y":
        escort_target = str(input())
        if escort_target not in playerList:
            print('Player not found, try again')
        elif escort_target == merged_dct["Escort"]:
            print('You cannot target yourself. Please try again.')
        else:
            sheriffNightCycle()
    return escort_target

def sheriffNightCycle():
    print()
    print('Now entering Sheriff action phase...')

    sheriffAlive()

def sheriffAlive():
    global sheriff_alive

    print('Is the Sheriff still alive? (y/n)')
    sheriff_alive = ''
    while sheriff_alive != 'y' or sheriff_alive != 'n':
        sheriff_alive = str(input())
        if sheriff_alive == 'y':
            print('Who will the Sheriff investigate?')
            sheriff_target = ''
            sheriffTarget()
        elif sheriff_alive == 'n':
            print('The Sheriff is dead')
            doctorNightCycle()
        else:
            print('Select y/n, try again')
    return sheriff_alive

def sheriffTarget():
    global sheriff_target

    sheriff_target = ''
    while sheriff_alive == "y":
        sheriff_target = str(input())
        if sheriff_target not in playerList:
            print('Player not found, try again')
        elif sheriff_target == merged_dct["Sheriff"]:
            print('You cannot target yourself. Please try again.')
        else:
            doctorNightCycle()
    return doctor_target

def doctorNightCycle():
    print()
    print('Now entering Doctor action phase...')

    doctorAlive()

def doctorAlive():
    global doctor_alive

    print('Is the Doctor still alive? (y/n)')
    doctor_alive = ''
    while doctor_alive != 'y' or doctor_alive != 'n':
        doctor_alive = str(input())
        if doctor_alive == 'y':
            print('Who will the Doctor heal?')
            doctor_target = ''
            doctorTarget()
        elif doctor_alive == 'n':
            print('The Doctor is dead')
            exit()
        else:
            print('Select y/n, try again')
    return doctor_alive

def doctorTarget():
    global doctor_target

    doctor_target = ''
    while doctor_alive == "y":
        doctor_target = str(input())
        if doctor_target not in playerList:
            print('Player not found, try again')
        if doctor_target == mafiaside_target:
            print("Your target was attacked last night but you were able to save them.")
            exit()
        else:
            exit()
    return doctor_target

transfromList()
inputPlayers()
assignRoles()
nightTime()
godfatherNightCycle()
mafiosoNightCycle()
framerNightCycle()
jailorNightCycle()
escortNightCycle()
sheriffNightCycle()
doctorNightCycle()
