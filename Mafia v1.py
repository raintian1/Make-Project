#MAFIA PROJECT
import random, time, xlwt
from xlwt import Workbook

print('\033[1m' + '''Welcome to the Mafia Narrator Helper! This program is used to help the story master better keep track of the progress. 
This is an early version of the prgram that supports 10 players. Please record your 10 names.''' + '\033[0m')

roles = ['Sheriff', 'Doctor', 'Mayor', 'Jailor', 'Godfather', 'Framer', 'Jester', 'Tracker', 'Mafioso', 'Executioner'] #, 'Vigilante']
playerList = []

global mafiaside_target
#global vigilante_target

def transfromList():
    global playerNumber
    global roles_transformed

    playerNumber = 10

    #if int(playerNumber) > 10:
        #print('Maximum player limit (10) reached, try again.')
        #transfromList()
    #if int(playerNumber) < 5:
        #print('You need at least 5 players to play the game.')
        #transfromList()
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
    global merged_dct2
    global random_role
    random_role = random.sample(roles_transformed, k = playerNumber)
    #print(playerList)
    #print(random_role)
    print()
    print('\033[1m' + 'Role assignment as follows: ' + '\033[0m')
    merged_list = [name + ': ' + role for name, role in zip(random_role, playerList)]
    #tuple(zip(playerList, random_role)) - Alternative method using tuples
    merged_dct = dict(zip(random_role, playerList))
    #print(merged_dct)
    merged_dct2 ={y: x for x, y in merged_dct.items()}
    for key, value in merged_dct.items():
        print(key, ':', value)

def writeToExcel1():
    wb = xlwt.Workbook()
    sheet1 = wb.add_sheet('Role Assignment')
    sheet1.write(0, 0, 'Player Name')
    sheet1.write(1, 0, playerList[0])
    sheet1.write(2, 0, playerList[1])
    sheet1.write(3, 0, playerList[2])
    sheet1.write(4, 0, playerList[3])
    sheet1.write(5, 0, playerList[4])
    sheet1.write(6, 0, playerList[5])
    sheet1.write(7, 0, playerList[6])
    sheet1.write(8, 0, playerList[7])
    sheet1.write(9, 0, playerList[8])
    sheet1.write(10, 0, playerList[9])
    sheet1.write(11, 0, playerList[10])

    sheet1.write(0, 1, 'Role')
    sheet1.write(1, 1, random_role[0])
    sheet1.write(2, 1, random_role[1])
    sheet1.write(3, 1, random_role[2])
    sheet1.write(4, 1, random_role[3])
    sheet1.write(5, 1, random_role[4])
    sheet1.write(6, 1, random_role[5])
    sheet1.write(7, 1, random_role[6])
    sheet1.write(8, 1, random_role[7])
    sheet1.write(9, 1, random_role[8])
    sheet1.write(10, 1, random_role[9])
    sheet1.write(11, 1, random_role[10])

    wb.save('Mafia Game Log')

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
            if jailor_alive == 'y':
                if merged_dct["Godfather"] != jailor_target:
                    print('Who will the Godfather appoint to kill?')
                    godfather_target = ''
                    godfatherTarget()
                if  merged_dct["Godfather"] == jailor_target:
                    print("You were jailed by the jailor tonight")
                    mafiosoNightCycle()
            else:
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
        elif godfather_target == merged_dct["Godfather"] or godfather_target == merged_dct["Mafioso"] or godfather_target == merged_dct["Framer"]:
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
            if jailor_alive == 'y':
                if merged_dct["Mafioso"] != jailor_target:
                    print('Who will the Mafioso kill?')
                    mafioso_target = ''
                    mafiosoTarget()
                if merged_dct["Mafioso"] == jailor_target:
                    print("You were jailed by the jailor tonight")
                    mafiaTargetCheck()
                    framerNightCycle()
            else:
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
        elif mafioso_target == merged_dct["Mafioso"] or mafioso_target == merged_dct["Godfather"] or mafioso_target == merged_dct["Framer"]:
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
            if jailor_alive == 'y':
                if merged_dct["Framer"] != jailor_target:
                    print('Who will the Framer frame?')
                    framer_target = ''
                    framerTarget()
                if merged_dct["Framer"] == jailor_target:
                    print("You were jailed by the jailor tonight")
                    sheriffNightCycle()
            else:
                print('Who will the Framer frame?')
                framer_target = ''
                framerTarget()
        elif framer_alive == 'n':
            print('The Framer is dead')
            sheriffNightCycle()
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
        elif framer_target == merged_dct["Framer"] or framer_target == merged_dct["Godfather"] or framer_target == merged_dct["Mafioso"]:
            print('Cannot target a member of the Mafia. Try again')
        else:
            sheriffNightCycle()
    return framer_target

def mafiaTargetCheck():
    print()
    time.sleep(1)
    global mafiaside_target
    mafiaside_target = 'N/A'
    if godfather_alive == 'n' and mafioso_alive == 'n':
        print('\033[1m' + 'The Mafia cannot kill anymore, the town has won!' + '\033[1m')
        exit()
    if jailor_alive == 'y':
        if jailor_target != merged_dct["Godfather"] and jailor_target != merged_dct["Mafioso"]:
            if godfather_alive == 'y' and mafioso_alive == 'y':
                if godfather_target != mafioso_target:
                    mafiaside_target = godfather_target
                    print('The Mafioso must comply with the Godfather, ' + mafiaside_target + ''' is tonight's target.''')
                    if mafiaside_target == jailor_target:
                        print('However, the target was immune tonight.')
                    elif mafiaside_target == merged_dct["Executioner"]:
                        print('However, the target was immune tonight.')
                else:
                    mafiaside_target = godfather_target
                    print('The Mafia came to an agreement, ' + mafiaside_target + ''' is tonight's target.''')
                    if mafiaside_target == jailor_target:
                        print('However, the target was immune tonight.')
                    elif mafiaside_target == merged_dct["Executioner"]:
                        print('However, the target was immune tonight.')
            elif godfather_alive == 'y' and mafioso_alive == 'n':
                mafiaside_target = godfather_target
                print('With no Mafioso, ' + mafiaside_target + ''' is tonight's target.''')
                if mafiaside_target == jailor_target:
                    print('However, the target was immune tonight.')
                elif mafiaside_target == merged_dct["Executioner"]:
                    print('However, the target was immune tonight.')
            elif godfather_alive == 'n' and mafioso_alive == 'y':
                mafiaside_target = mafioso_target
                print('With no Godfather, ' + mafiaside_target + ''' is tonight's target.''')
                if mafiaside_target == jailor_target:
                    print('However, the target was immune tonight.')
                elif mafiaside_target == merged_dct["Executioner"]:
                    print('However, the target was immune tonight.')
        elif jailor_target == merged_dct["Godfather"]:
            if godfather_alive == 'y' and mafioso_alive == 'y':
                mafiaside_target = mafioso_target
                print('The Godfather was jailed, ' + mafiaside_target + ''' is tonight's target.''')
                if mafiaside_target == jailor_target:
                    print('However, the target was immune tonight.')
                elif mafiaside_target == merged_dct["Executioner"]:
                    print('However, the target was immune tonight.')
            elif godfather_alive == 'y' and mafioso_alive == 'n':
                mafiaside_target = 'N/A'
                print('With no Mafioso and the Godfather jailed, the mafia could not kill tonight.' )
        elif jailor_target == merged_dct["Mafioso"]:
            if godfather_alive == 'y' and mafioso_alive == 'y':
                mafiaside_target = godfather_target
                print('The Mafioso was jailed, ' + mafiaside_target + ''' is tonight's target.''')
                if mafiaside_target == jailor_target:
                    print('However, the target was immune tonight.')
                elif mafiaside_target == merged_dct["Executioner"]:
                    print('However, the target was immune tonight.')
            elif godfather_alive == 'n' and mafioso_alive == 'y':
                mafiaside_target = 'N/A'
                print('With no Godfather and the Mafioso jailed, the mafia could not kill tonight.' )
    else:
        if godfather_alive == 'y' and mafioso_alive == 'y':
            if godfather_target != mafioso_target:
                mafiaside_target = godfather_target
                print('The Mafioso must comply with the Godfather, ' + mafiaside_target + ''' is tonight's target.''')
                if mafiaside_target == merged_dct["Executioner"]:
                    print('However, the target was immune tonight.')
            else:
                mafiaside_target = godfather_target
                print('The Mafia came to an agreement, ' + mafiaside_target + ''' is tonight's target.''')
                if mafiaside_target == merged_dct["Executioner"]:
                    print('However, the target was immune tonight.')
        elif godfather_alive == 'y' and mafioso_alive == 'n':
            mafiaside_target = godfather_target
            print('With no Mafioso, ' + mafiaside_target + ''' is tonight's target.''')
            if mafiaside_target == merged_dct["Executioner"]:
                print('However, the target was immune tonight.')
        elif godfather_alive == 'n' and mafioso_alive == 'y':
            mafiaside_target = mafioso_target
            print('With no Godfather, ' + mafiaside_target + ''' is tonight's target.''')
            if mafiaside_target == merged_dct["Executioner"]:
                print('However, the target was immune tonight.')

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
            jailor_target = 'N/A'
            godfatherNightCycle()
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
            print('You cannot target yourself, try again')
        else:
            godfatherNightCycle()
    return jailor_target

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
            if jailor_alive == 'y':
                if merged_dct["Sheriff"] != jailor_target:
                    print('Who will the Sheriff investigate?')
                    sheriff_target = ''
                    sheriffTarget()
                if merged_dct["Sheriff"] == jailor_target:
                    print("You were jailed by the jailor tonight")
                    #vigilanteNightCycle()
                    doctorNightCycle()
            else:
                print('Who will the Sheriff investigate?')
                sheriff_target = ''
                sheriffTarget()
        elif sheriff_alive == 'n':
            print('The Sheriff is dead')
            #vigilanteNightCycle()
            doctorNightCycle()
        else:
            print('Select y/n, try again')
    return sheriff_alive

def sheriffTarget():
    global sheriff_target

    sheriff_target = ''
    while sheriff_alive == "y":
        sheriff_target = str(input())
        if jailor_alive == 'y':
            if sheriff_target not in playerList:
                print('Player not found, try again')
            elif sheriff_target == merged_dct["Sheriff"]:
                print('You cannot target yourself. Please try again.')
            elif framer_alive == 'y' and jailor_target == merged_dct["Framer"]:
                if sheriff_target == merged_dct["Mafioso"]:
                    print('Your target appears to be aligned with the Mafia.')
                    # vigilanteNightCycle()
                    doctorNightCycle()
                elif sheriff_target == merged_dct["Framer"]:
                    print('Your target appears to be aligned with the Mafia.')
                    # vigilanteNightCycle()
                    doctorNightCycle()
                else:
                    print('Your target appears to be aligned with the Town.')
                    # vigilanteNightCycle()
                    doctorNightCycle()
            elif framer_alive == 'y' and jailor_target != merged_dct["Framer"]:
                if sheriff_target == framer_target:
                    print('Your target appears to be aligned with the Mafia.')
                    # vigilanteNightCycle()
                    doctorNightCycle()
                elif sheriff_target == merged_dct["Mafioso"]:
                    print('Your target appears to be aligned with the Mafia.')
                    # vigilanteNightCycle()
                    doctorNightCycle()
                elif sheriff_target == merged_dct["Framer"]:
                    print('Your target appears to be aligned with the Mafia.')
                    # vigilanteNightCycle()
                    doctorNightCycle()
                else:
                    print('Your target appears to be aligned with the Town.')
                    # vigilanteNightCycle()
                    doctorNightCycle()
            elif framer_alive == 'n':
                if sheriff_target == merged_dct["Mafioso"] or sheriff_target == merged_dct["Framer"]:
                    print('Your target appears to be aligned with the Mafia.')
                    # vigilanteNightCycle()
                    doctorNightCycle()
                else:
                    print('Your target appears to be aligned with the Town.')
                    # vigilanteNightCycle()
                    doctorNightCycle()
            else:
                # vigilanteNightCycle()
                doctorNightCycle()
        else:
            if sheriff_target not in playerList:
                print('Player not found, try again')
            elif sheriff_target == merged_dct["Sheriff"]:
                print('You cannot target yourself. Please try again.')
            elif framer_alive == 'y':
                if sheriff_target == framer_target:
                    print('Your target appears to be aligned with the Mafia.')
                    # vigilanteNightCycle()
                    doctorNightCycle()
                elif sheriff_target == merged_dct["Mafioso"]:
                    print('Your target appears to be aligned with the Mafia.')
                    # vigilanteNightCycle()
                    doctorNightCycle()
                elif sheriff_target == merged_dct["Framer"]:
                    print('Your target appears to be aligned with the Mafia.')
                    # vigilanteNightCycle()
                    doctorNightCycle()
                else:
                    print('Your target appears to be aligned with the Town.')
                    # vigilanteNightCycle()
                    doctorNightCycle()
            elif framer_alive == 'n':
                if sheriff_target == merged_dct["Mafioso"] or sheriff_target == merged_dct["Framer"]:
                    print('Your target appears to be aligned with the Mafia.')
                    # vigilanteNightCycle()
                    doctorNightCycle()
                else:
                    print('Your target appears to be aligned with the Town.')
                    # vigilanteNightCycle()
                    doctorNightCycle()
            else:
                # vigilanteNightCycle()
                doctorNightCycle()
    return sheriff_target

def vigilanteNightCycle():
    print()
    print('Now entering Vigilante action phase...')

    vigilanteAlive()

def vigilanteAlive():
    global vigilante_alive

    print('Is the Vigilante still alive? (y/n)')
    vigilante_alive = ''
    while vigilante_alive != 'y' or vigilante_alive != 'n':
        vigilante_alive = str(input())
        if vigilante_alive == 'y':
            if jailor_alive == 'y':
                if merged_dct["Vigilante"] != jailor_target:
                    print('Who will the Vigilante execute?')
                    vigilante_target = 'N/A'
                    vigilanteTarget()
                if merged_dct["Vigilante"] == jailor_target:
                    print("You were jailed by the jailor tonight")
                    doctorNightCycle()
            else:
                print('Who will the Vigilante execute?')
                vigilante_target = 'N/A'
                vigilanteTarget()
        elif vigilante_alive == 'n':
            print('The Vigilante is dead')
            doctorNightCycle()
        else:
            print('Select y/n, try again')
    return vigilante_alive

def vigilanteTarget():
    global vigilante_target

    vigilante_target = 'N/A'
    while vigilante_alive == "y":
        vigilante_target = str(input())
        if jailor_alive == 'y':
            if vigilante_target not in playerList:
                print('Player not found, try again')
            elif vigilante_target == merged_dct["Vigilante"]:
                print('You cannot target yourself. Please try again.')
            elif vigilante_target == jailor_target:
                print('Your target was immune tonight.')
                vigilante_target = 'N/A'
                doctorNightCycle()
            elif vigilante_target == merged_dct["Godfather"]:
                print('Your target was immune tonight.')
                vigilante_target = 'N/A'
                doctorNightCycle()
            elif vigilante_target == merged_dct["Executioner"]:
                print('Your target was immune tonight.')
                vigilante_target = 'N/A'
                doctorNightCycle()
            else:
                doctorNightCycle()
        else:
            if vigilante_target not in playerList:
                print('Player not found, try again')
            elif vigilante_target == merged_dct["Vigilante"]:
                print('You cannot target yourself. Please try again.')
            elif vigilante_target == merged_dct["Godfather"]:
                print('Your target was immune tonight.')
                vigilante_target = 'N/A'
                doctorNightCycle()
            elif vigilante_target == merged_dct["Executioner"]:
                print('Your target was immune tonight.')
                vigilante_target = 'N/A'
                doctorNightCycle()
            else:
                doctorNightCycle()
    return vigilante_target

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
            if jailor_alive == 'y':
                if merged_dct["Doctor"] != jailor_target:
                    print('Who will the Doctor heal?')
                    doctor_target = ''
                    doctorTarget()
                if merged_dct["Doctor"] == jailor_target:
                    print("You were jailed by the jailor tonight")
                    trackerNightCycle()
            else:
                print('Who will the Doctor heal?')
                doctor_target = ''
                doctorTarget()
        elif doctor_alive == 'n':
            print('The Doctor is dead')
            trackerNightCycle()
        else:
            print('Select y/n, try again')
    return doctor_alive

def doctorTarget():
    global doctor_target #, vigilante_target

    doctor_target = ''
    while doctor_alive == "y":
        doctor_target = str(input())
        if jailor_alive == 'y':
            if doctor_target not in playerList:
                print('Player not found, try again')
            elif doctor_target == jailor_target:
                if jailor_target != mafiaside_target:
                    print('Your target was jailed tonight.')
                    trackerNightCycle()
            elif doctor_target == mafiaside_target:
                print('Your target was attacked last night.')
                trackerNightCycle()
            #elif doctor_target == vigilante_target:
                #print('Your target was attacked last night.')
                #vigilante_target = 'N/A'
                #trackerNightCycle()
            else:
                trackerNightCycle()
        else:
            if doctor_target not in playerList:
                print('Player not found, try again')
            elif doctor_target == mafiaside_target:
                print('Your target was attacked last night.')
                trackerNightCycle()
            #elif doctor_target == vigilante_target:
                #print('Your target was attacked last night.')
                #vigilante_target = 'N/A'
                #trackerNightCycle()
            else:
                trackerNightCycle()
    return doctor_target

def trackerNightCycle():
    print()
    print('Now entering Tracker action phase...')

    trackerAlive()

def trackerAlive():
    global tracker_alive

    print('Is the Tracker still alive? (y/n)')
    tracker_alive = ''
    while tracker_alive != 'y' or tracker_alive != 'n':
        tracker_alive = str(input())
        if tracker_alive == 'y':
            if jailor_alive == 'y':
                if merged_dct["Tracker"] != jailor_target:
                    print('Who will the Tracker follow?')
                    tracker_target = ''
                    trackerTarget()
                if merged_dct["Tracker"] == jailor_target:
                    print("You were jailed by the jailor tonight")
                    dayAnnouncement()
            else:
                print('Who will the Tracker follow?')
                tracker_target = ''
                trackerTarget()
        elif tracker_alive == 'n':
            print('The Tracker is dead')
            dayAnnouncement()
        else:
            print('Select y/n, try again')
    return tracker_alive

def trackerTarget():
    global tracker_target

    tracker_target = ''
    while tracker_alive == 'y':
        tracker_target = str(input())
        if jailor_alive == 'y':
            if tracker_target not in playerList:
                print('Player not found, try again')
            elif tracker_target == merged_dct["Tracker"]:
                print('You cannot target yourself. Please try again.')
            elif tracker_target == merged_dct['Jester'] or tracker_target == merged_dct['Mayor'] or tracker_target == merged_dct['Executioner']:
                print(tracker_target + ' did not visit anyone tonight.')
                dayAnnouncement()
            elif tracker_target != jailor_target:
                if tracker_target == merged_dct["Jailor"]:
                    print(tracker_target + ' visited ' + jailor_target + ' tonight.')
                    dayAnnouncement()
                elif tracker_target == merged_dct["Godfather"]:
                    if mafiaside_target != '':
                        print(tracker_target + ' visited ' + mafiaside_target + ' tonight.')
                        dayAnnouncement()
                    else:
                        print(tracker_target + ' did not visit anyone tonight.')
                        dayAnnouncement()
                elif tracker_target == merged_dct["Mafioso"]:
                    if mafiaside_target != '':
                        print(tracker_target + ' visited ' + mafiaside_target + ' tonight.')
                        dayAnnouncement()
                    else:
                        print(tracker_target + ' did not visit anyone tonight.')
                        dayAnnouncement()
                elif tracker_target == merged_dct["Sheriff"]:
                    print(tracker_target + ' visited ' + sheriff_target + ' tonight.')
                    dayAnnouncement()
                #elif tracker_target == merged_dct["Vigilante"]:
                    #print(tracker_target + ' visited ' + vigilante_target + ' tonight.')
                    #dayAnnouncement()
                elif tracker_target == merged_dct["Doctor"]:
                    print(tracker_target + ' visited ' + doctor_target + ' tonight.')
                    dayAnnouncement()
            elif tracker_target == jailor_target:
                print(tracker_target + ' did not visit anyone tonight.')
                dayAnnouncement()
        else:
            if tracker_target not in playerList:
                print('Player not found, try again')
            elif tracker_target == merged_dct["Tracker"]:
                print('You cannot target yourself. Please try again.')
            elif tracker_target == merged_dct['Jester'] or tracker_target == merged_dct['Mayor'] or tracker_target == \
                    merged_dct['Executioner']:
                print(tracker_target + ' did not visit anyone tonight.')
                dayAnnouncement()
            elif tracker_target == merged_dct["Godfather"]:
                if mafiaside_target != '':
                    print(tracker_target + ' visited ' + mafiaside_target + ' tonight.')
                    dayAnnouncement()
                else:
                    print(tracker_target + ' did not visit anyone tonight.')
                    dayAnnouncement()
            elif tracker_target == merged_dct["Mafioso"]:
                if mafiaside_target != '':
                    print(tracker_target + ' visited ' + mafiaside_target + ' tonight.')
                    dayAnnouncement()
                else:
                    print(tracker_target + ' did not visit anyone tonight.')
                    dayAnnouncement()
            elif tracker_target == merged_dct["Sheriff"]:
                print(tracker_target + ' visited ' + sheriff_target + ' tonight.')
                dayAnnouncement()
            #elif tracker_target == merged_dct["Vigilante"]:
                #print(tracker_target + ' visited ' + vigilante_target + ' tonight.')
                #dayAnnouncement()
            elif tracker_target == merged_dct["Doctor"]:
                print(tracker_target + ' visited ' + doctor_target + ' tonight.')
                dayAnnouncement()
    return tracker_target

def dayAnnouncement():
    print()
    time.sleep(1)
    global mafiaside_target

    checker = str('N/A')
    if sheriff_alive == 'n' and doctor_alive == 'n' and tracker_alive == 'n' and jailor_alive == 'n':
        print('\033[1m'+ 'With insufficient town members remaining, the Mafia has won!' + '\033[0m')
        exit()

    elif mafiaside_target == checker:
        print('\033[1m' + 'Nobody was killed tonight.' + '\033[0m')
        dayVote()
    elif mafiaside_target != checker:
        print('\033[1m' + mafiaside_target + ', the ' + merged_dct2[mafiaside_target] + ', was killed last night.' + '\033[0m')
        dayVote()

def dayVote():
    time.sleep(1)
    print()
    print('Who did the town decide to vote out today?')
    townvote = input()
    print(townvote + ' has been voted off. ')
    jailorNightCycle()
    time.sleep(1)
    print()

def main():
    global mafiaside_target
    #global vigilante_target
    nightTime()
    jailorNightCycle()
    godfatherNightCycle()
    if int(playerNumber) >= 9:
        mafiosoNightCycle()
    if int(playerNumber) >= 6:
        framerNightCycle()
    sheriffNightCycle()
    #vigilanteNightCycle()
    doctorNightCycle()
    if int(playerNumber) >= 8:
        trackerNightCycle()
    dayAnnouncement()
    dayVote()

transfromList()
inputPlayers()
assignRoles()
main()
