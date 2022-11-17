####################
#  Peyton Germann  #
#  External Files  #
# November 17 2022 #
#   Summative      #
####################
import random
import time
yes = ("yes", "Yes", "Y", "y", "sure", "Sure")
# dictionary for monsters
monsters = {}
# dictionary for player
player = {}
# takes text from text file and adds it to list
def lists():
    file = open('char.txt', 'r')
    filelist = file.readline().split(", ")
    item = 0
    while item < (len(filelist)): 
        monsters[filelist[item]] = filelist[item + 1]
        item += 2
    file.close()

# function for writing to the history board
def writing(name, health, attacknm, damage, speed, enemy, winorlose):
    file = open('history.txt', 'a')
    file.write(f"New Game Log:\nCharacter: Fought: {enemy}\n{winorlose}\n{name}\nHealth after battle: {health}\nAttack Name: {attacknm}\nDamage: {damage}\nSpeed:{speed}\n\n")
    file.close()

def time(n):
    from time import sleep
    sleep(n)
    
# gets a random number from 0 100
def randomnum():
    r = random.randint(0,100)
    return r

# gets character stats and moveset
def moveset(m):
    print("It is time to make your moveset.")
    print("What is your main attack?")
    attack = input(">")
    print(f"Lets see how much damage {attack} does.")
    dmg = randomnum()
    # gets your attack name and amount of damage
    time(2)
    print(f"{attack} does {dmg}dmg")
    time(1)
    if int(dmg) > 50:
        print("Thats alot of damage.")
    elif int(dmg) < 50:
        print("Could be better.")
    # Gets health stat
    print("Now that you have your main attack its time to see how much health you have.")
    hth = randomnum()
    time(2)
    print(f"You have {hth}hp.")
    if int(hth) < 30:
        print("Lets hope your a glass cannon and not just glass.")
    time(2)
    print("Lets see how fast you are.")
    # gets speed stat
    spd = randomnum()
    if int(spd) > 50:
        print("You are pretty fast.")
    elif int(spd) < 50:
        print("You are slow. L")
    time(2)
    # adds stats to player dictionary
    player["name"] = m
    player["health"] = hth
    player["attack_name"] = attack
    player["damage"] = dmg 
    player["speed"] = spd
    
def battle(n):
    # gets monster name
    enemy = monsters["name"]
    print("You get one heal per match of 20 health.")
    print("You get one mystery potion")
    time(2)
    print(f"Hey siri play pokemon battle music.")
    time(2)
    print(f"{n} enters the ring with {enemy}!")
    print("Its time to battle!")
    # saves all stats so we can change them and use them
    playerhp = player["health"]
    playerat = player["attack_name"]
    playerdm = player["damage"]
    playersp = player["speed"]
    enemyhp = int(monsters["health"])
    enemyat = monsters["attack_name"]
    enemydm = int(monsters["damage"])
    enemysp = int(monsters["speed"])
    time(2)
    # makes loop so that while they both are alive the battle continues
    while playerhp > 0 and enemyhp > 0:
        # for if the player is faster than the enemy
        if playersp > enemysp:
            # makes unbreakable
            while True:
                # asks for what you want to do
                print("What would you like to do?")
                print("1 - Attack 2 - Heal 3 - Drink mystery potion")
                option = input(">")
                # player attacks
                if option == "1":
                    print(f"{n} uses {playerat} which does {playerdm}")
                    time(1)
                    # lowers the enemys health using attack damage
                    enemyhp = enemyhp - playerdm
                    # says amount of health left or breaks loop because enemy dead
                    if enemyhp > 0:
                        print(f"{enemy} has {enemyhp} left")
                        time(2)
                    elif enemyhp < 0:
                        break
                    # enemy attacks and changes player health stat
                    print(f"{enemy} attacks using {enemyat}.")
                    playerhp = playerhp - enemydm
                    time(2)
                    # if player is alive says hp if not breaksk loop
                    if playerhp > 0:
                        print(f"{n} has {playerhp} left")
                    elif playerhp < 0:
                        break
                    break
                # heals
                if option == "2":
                    print(f"{n} healed 20hp.")
                    # increases health
                    playerhp = playerhp + 20
                    print(f"{n} has {playerhp}hp.")
                    time(2)
                    # enemy attacks same as before
                    print(f"{enemy} attacks using {enemyat}.")
                    playerhp = playerhp - enemydm
                    time(2)
                    if playerhp > 0:
                        print(f"{n} has {playerhp} left")
                    elif playerhp < 0:
                        break
                    print(f"{enemy} attacks using {enemyat}.")
                    playerhp = playerhp - enemydm
                    time(2)
                    if playerhp > 0:
                        print(f"{n} has {playerhp} left")
                    elif playerhp < 0:
                        break
                # mystery potion???
                elif option == "3":
                    # have a chance to get full health or to lose hp
                    rando = randomnum()
                    print("You take a sip of the mystery potion.")
                    if rando > 90:
                        print("You now have 100hp!")
                        playerhp = 100
                    elif rando < 90:
                        print("You lost 10hp.")
                        playerhp = playerhp - 10
                    time(2)
                    # enemy attacks
                    print(f"{enemy} attacks using {enemyat}.")
                    playerhp = playerhp - enemydm
                    time(2)
                    if playerhp > 0:
                        print(f"{n} has {playerhp}hp left.")
                    elif playerhp < 0:
                        break
                    break
                # for if you type a wrong input
                elif option == "4":
                    print("Not a valid input.")
        # same as everything before this except enemy attacks first because of speed
        elif enemysp > playersp:
            print(f"{enemy} attacks using {enemyat}.")
            playerhp = playerhp - enemydm
            if playerhp > 0:
                print(f"{n} has {playerhp}hp left")
            elif playerhp < 0:
                break
            while True:
                print("What would you like to do?")
                print("1 - Attack 2 - Heal 3 - Drink mystery potion")
                option = input(">")
                if option == "1":
                    print(f"{n} uses {playerat} which does {playerdm}")
                    time(1)
                    enemyhp = enemyhp - playerdm
                    if enemyhp > 0:
                        print(f"{enemy} has {enemyhp} left")
                        time(2)
                    elif enemyhp < 0:
                        break
                    break
                if option == "2":
                    print(f"{n} healed 20hp.")
                    playerhp = playerhp + 20
                    print(f"{n} has {playerhp}hp.")
                    time(2)
                    break
                if option == "3":
                    rando = randomnum()
                    print("You take a sip of the mystery potion.")
                    if rando > 90:
                        print("You now have 100hp!")
                        playerhp = 100
                    elif rando < 90:
                        print("You lost 10hp.")
                        playerhp = playerhp - 10
                    time(2)
                    break
                elif option == "4":
                    print("Not a valid input.")
    if playerhp < 0:
        print(f"{n} is unable to continue.")
        wl = "lost"
    elif enemyhp < 0:
        print(f"{enemy} is unable to continue.")
        wl = "won"
    time(2)
    print("Data from this battle is saved")
    time(2)
    print("So check history.txt for your battles.")
    # runs writing function so these variables can be written in history.txt
    writing(n, playerhp, playerat, playerdm, playersp, enemy, wl) 
    
def intro():
    # asks for name and starts the simulator
    name = input("Who is fighting in the arena today?\n")
    cap = randomnum()
    if int(cap) > 50:
        print(f"Interesting, good luck {name}.")
    elif int(cap) < 50:
        print(f"Lets hope you get an easy opponent {name}. :)")
    moveset(name)
    battle(name)
    
lists()
while True:
    print("This is a python battle simulator! where you can battle it out with famous characters and creatures.")
    intro() 
    # asks if you want to run program again
    yes_no = input("Want to enter the ring again?")
    if yes_no in yes:
        print("Awesome!")
    elif yes_no not in yes:
        print("Bye.")
        break

