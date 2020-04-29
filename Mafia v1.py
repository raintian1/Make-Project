import random, time

print('\033[1m' + '''Welcome to Mafia! Input the number of players:''' + '\033[0m')

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

def assignRoles():
    global merged_list
    random_role = random.sample(roles_transformed, k = playerNumber)
    #print(playerList)
    #print(random_role)
    print()
    print('\033[1m' + 'Role assignment as follows: ' + '\033[0m')
    merged_list = [name + ': ' + role for name, role in zip(playerList, random_role)]
    #tuple(zip(playerList, random_role)) - Alternative method using tuples
    print(*merged_list, sep = '\n')

def nightTime():
    time.sleep(1)
    print()
    print('\033[1m' + 'Night Time...' + '\033[0m')

def godfatherNightCycle():
    global Godfather_alive
    global Godfather_target

    print('Is the Godfather still alive? (y/n)')
    Godfather_alive = ''
    while Godfather_alive != 'y' or Godfather_alive != 'n':
        Godfather_alive = str(input())
        if Godfather_alive == 'y':
            print('Who will the Godfather appoint to kill?')
            Godfather_target = ''
            while Godfather_target not in playerList:
                Godfather_target = str(input())
                if Godfather_target not in playerList:
                    print('Player not found, try again.')
            return Godfather_target
        elif Godfather_alive == 'n':
            mafiosoNightCycle()
        else:
            print('Select y/n, try again')
    return Godfather_alive

# Fix from here down!!!
def mafiosoNightCycle():
    print('Who will the Mafioso shoot?')
    Mafioso_target = str(input())

    if Godfather_target != Mafioso_target:
        Mafia_side_target = Godfather_target
        print('The Mafioso must comply with the Godfather, ' + Godfather_target + ''' is tonight's target.''')
    else:
        print('The Mafia came to an agreement, ' + Godfather_target + ''' is tonight's target.''')

def framerNightCycle():
    print()
    print('Who will the framer choose to frame?')
    Framer_target = str(input())
    roles[Framer_target] == 'framed'
    print(Framer_target + ', the ' + roles[Framer_target] + ' , will appear guilty under investigation tonight.')

transfromList()
inputPlayers()
assignRoles()
nightTime()
godfatherNightCycle()
mafiosoNightCycle()
