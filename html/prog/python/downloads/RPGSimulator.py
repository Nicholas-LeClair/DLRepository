from random import *
Copper_Sword = "Unequipped" 
Copper_Helmet = "Unequipped" 
Copper_Chestplate = "Unequipped" 
Copper_Leggings = "Unequipped" 
Copper_Gauntlets = "Unequipped" 
Coppper_Boots = "Unequipped" 
Iron_Sword = "Unequipped" 
Iron_Helmet = "Unequipped" 
Iron_Chestplate = "Unequipped" 
Iron_Leggings = "Unequipped" 
Iron_Gauntlets = "Unequipped" 
Iron_Boots = "Unequipped" 
Gold_Sword = "Unequipped" 
Gold_Helmet = "Unequipped" 
Gold_Chestplate = "Unequipped" 
Gold_Leggings = "Unequipped" 
Gold_Gauntlets = "Unequipped" 
Gold_Boots = "Unequipped"
SwordModifierAttack = 0
HelmetModifierDefense = 0
ChestModifierDefense = 0
GlovesModifierDefense = 0
BootsModifierDefense = 0
LegsModifierDefense= 0
Gold = 0
FirstTime = 0
PlayerAttack = 1 + SwordModifierAttack
PlayerDefense = 0 + HelmetModifierDefense + ChestModifierDefense + LegsModifierDefense + GlovesModifierDefense + BootsModifierDefense
PlayerHealth = int(PlayerDefense) + 3
#Sets starter equipment
def StartingEquipment():
    global Copper_Sword, Copper_Helmet, Copper_Chestplate, Copper_Leggings, Copper_Gauntlets, Copper_Boots, Iron_Sword, Iron_Helmet, Iron_Chestplate, Iron_Leggings, Iron_Gauntlets, Iron_Boots, Gold_Sword, Gold_Helmet, Gold_Chestplate, Gold_Leggings, Gold_Gauntlets, Gold_Boots, SwordModifierAttack, HelmetModifierDefense, ChestModifierDefense, LegsModifierDefense, GlovesModifierDefense, BootsModifierDefense
    Copper_Sword = "Unequipped" 
    Copper_Helmet = "Unequipped" 
    Copper_Chestplate = "Unequipped" 
    Copper_Leggings = "Unequipped" 
    Copper_Gauntlets = "Unequipped" 
    Coppper_Boots = "Unequipped" 
    Iron_Sword = "Unequipped" 
    Iron_Helmet = "Unequipped" 
    Iron_Chestplate = "Unequipped" 
    Iron_Leggings = "Unequipped" 
    Iron_Gauntlets = "Unequipped" 
    Iron_Boots = "Unequipped" 
    Gold_Sword = "Unequipped" 
    Gold_Helmet = "Unequipped" 
    Gold_Chestplate = "Unequipped" 
    Gold_Leggings = "Unequipped" 
    Gold_Gauntlets = "Unequipped" 
    Gold_Boots = "Unequipped"
#Module that runs checks and modifies stats based on equipment
def Equipment():
    global Copper_Sword, Copper_Helmet, Copper_Chestplate, Copper_Leggings, Copper_Gauntlets, Copper_Boots, Iron_Sword, Iron_Helmet, Iron_Chestplate, Iron_Leggings, Iron_Gauntlets, Iron_Boots, Gold_Sword, Gold_Helmet, Gold_Chestplate, Gold_Leggings, Gold_Gauntlets, Gold_Boots, SwordModifierAttack, HelmetModifierDefense, ChestModifierDefense, LegsModifierDefense, GlovesModifierDefense, BootsModifierDefense
#-*-Copper equipment modifiers-*-
    if Copper_Sword == "Equipped":
        SwordModifierAttack= 1
    if Copper_Helmet == "Equipped":
        HelmetModifierDefense= 1
    if Copper_Chestplate == "Equipped":
        ChestModifierDefense= 1
    if Copper_Leggings == "Equipped":
        LegsModifierDefense= 1
    if Copper_Gauntlets == "Equipped":
        GlovesModifierDefense= 1
    if Coppper_Boots == "Equipped":
        BootsModifierDefense= 1
#-*-Iron equipment modifiers-*-
    if Iron_Sword == "Equipped":
        SwordModifierAttack= 5
    if Iron_Helmet == "Equipped":
        HelmetModifierDefense= 2
    if Iron_Chestplate == "Equipped":
        ChestModifierDefense= 2
    if Iron_Leggings == "Equipped":
        LegsModifierDefense= 2
    if Iron_Gauntlets == "Equipped":
        GlovesModifierDefense= 2
    if Iron_Boots == "Equipped":
        BootsModifierDefense= 2
#-*-Gold equipment modifiers-*-
    if Gold_Sword == "Equipped":
        SwordModifierAttack= 10
    if Gold_Helmet == "Equipped":
        HelmetModifierDefense= 3
    if Gold_Chestplate == "Equipped":
        ChestModifierDefense= 3
    if Gold_Leggings == "Equipped":
        LegsModifierDefense= 3
    if Gold_Gauntlets == "Equipped":
        GlovesModifierDefense= 3
    if Gold_Boots == "Equipped":
        BootsModifierDefense= 3
#Module that controls player stats according to equipment
def Stats():
#Assigns global variables
    global SwordModifierAttack, HelmetModifierDefense, ChestModifierDefense, LegsModifierDefense, GlovesModifierDefense, BootsModifierDefense
    PlayerAttack = 1 + SwordModifierAttack
    PlayerDefense = 0 + HelmetModifierDefense + ChestModifierDefense + LegsModifierDefense + GlovesModifierDefense + BootsModifierDefense
    PlayerHealth = int(PlayerDefense) + 3
#Module that prints the title screen
def Title():
#Prints starter text and title graphic
    print("____________ _____   _____ _                 _       _               _____  _____  __   _____ ")
    print("| ___ \ ___ \  __ \ /  ___(_)               | |     | |             / __  \|  _  |/  | |  _  |")
    print("| |_/ / |_/ / |  \/ \ `--. _ _ __ ___  _   _| | __ _| |_ ___  _ __  `' / /'| |/' |`| |  \ V / ")
    print("|    /|  __/| | __   `--. \ | '_ ` _ \| | | | |/ _` | __/ _ \| '__|   / /  |  /| | | |  / _ \ ")
    print("| |\ \| |   | |_\ \ /\__/ / | | | | | | |_| | | (_| | || (_) | |    ./ /___\ |_/ /_| |_| |_| |")
    print("\_| \_\_|    \____/ \____/|_|_| |_| |_|\__,_|_|\__,_|\__\___/|_|    \_____/ \___/ \___/\_____/")
    print("    -*-Made by Ian Watkins, with help from Mr.Philips, StackOverflow.com, and Codecademy-*-   ")
    print("-*-Ascii art generated by http://patorjk.com/software/taag/#p=display&f=Doom&t=RPG%20Simulator%202018-*-   ")
    print(" ")
    input('''We're gonna start this off right by throwing you into a battle with little to no context and zero explanation.
Good luck!''')
#Overall module that controls the combat
def CombatModule():
#Sets global variables
    global PlayerAttack,EnemyHealth, Damage, GoldGained, Gold, EnemyDamage, PlayerHealth,FirstTime
    #Takes user input and converts it into its rawest form (ignoring capitals and spaces)
    EnemyEncounter()
    Input= input("What would you like to do? [Attack/Flee]: ").upper()
    Input= ("%s" % ("".join(Input.upper().split(" "))))
#Detects input from 2 options and asks for proper input if anything else is entered
    if Input == "ATTACK":
        Damage= 0
        Damage= randint(0, PlayerAttack)
#Detects if damage is greater than 0 to print damage and remove it from the enemy's health
        if Damage > 0:
            print("You did " + str(Damage) + " " + "damage!")
            EnemyHealth -= Damage
#Detects if the enemy's health is less than or equal to 0, then tells you it was slain and returns a random amount of gold which is added to your gold
            if EnemyHealth <= 0:
                print("You have slain the monster!")
                GoldGain()
                Gold += GoldGained
                print("You looted " + str(GoldGained) + " gold! You now have " + str(Gold) + ".")
                print("You then return to the shop to spend your newfound splendors.")
                Shop()
#If the enemy's health is greater than or eqaul to 0 after damage, the enemy will attack back
            elif EnemyHealth >= 1:
                EnemyDamage= randint(0, EnemyAttack)
                print("The " + EnemyEncountered + " did " + str(EnemyDamage) + " damage!")
#Death code, detects if your health is less than or equal to 0 after the enemy hits
                if EnemyDamage >= PlayerHealth:
                    print("You have been slain!")
                elif EnemyDamage < PlayerHealth:
                    PlayerHealth -= EnemyDamage
                    print("You have " + str(PlayerHealth) + " health.")
                    CombatModule()
        elif Damage == 0:
            print("You did 0 damage!")
            EnemyDamage= randint(0, EnemyAttack)
            print("The monster"  + " did " + str(EnemyDamage) + " damage!")
            if EnemyDamage >= PlayerHealth:
                print("You have been slain!")
            elif EnemyDamage < PlayerHealth:
                PlayerHealth -= EnemyDamage
                print("You have " + str(PlayerHealth) + " health.")
                CombatModule()
#Option to leave battle and return to the shop
    elif Input == "FLEE":
        print("You fled the battle and retreated to the shop!")
        Shop()
    else:
        print("Choose a valid response.")
#Module to control names and stats of enemies
def EnemyEncounter():
#Defines global variables
    global EnemyHealth, EnemyAttack
    EnemyAttack = PlayerAttack
    EnemyHealth = PlayerHealth - 2
#Module to randomly generate gold amounts after a battle
def GoldGain():
    global GoldGained
    GoldGained = randint(0, 2)
#Module designed to serve as shop, allowing user to use gold to purchase new and stronger equipment
#Module that runs checks and modifies stats based on equipment
def Shop():
    global Gold, Copper_Sword, Copper_Sword, Copper_Helmet, Copper_Chestplate, Copper_Leggings, Copper_Gauntlets, Copper_Boots, Iron_Sword, Iron_Helmet, Iron_Chestplate, Iron_Leggings, Iron_Gauntlets, Iron_Boots, Gold_Sword, Gold_Helmet, Gold_Chestplate, Gold_Leggings, Gold_Gauntlets, Gold_Boots
    FirstTime = 0
    Copper_Helmet= "Unequipped"
    Iron_Helmet= "Unequipped"
    Gold_Helmet= "Unequipped"
    runForever = True
    #Module takes raw input to decide what user wishes to purchase
    while runForever == True:
        print("You have " + str(Gold) + " gold.")
        Input= input('''What would you like to buy?
    [Copper Sword: 1 gold]
    [Copper Helmet: 1 gold]
    [Copper Chestplate: 1 gold]
    [Copper Leggings: 1 gold]
    [Copper Gauntlets: 1 gold]
    [Coppper Boots: 1 gold]
    [Iron Sword: 5 gold]
    [Iron Helmet: 5 gold]
    [Iron Chestplate: 5 gold]
    [Iron Leggings: 5 gold]
    [Iron Gauntlets: 5 gold]
    [Iron Boots: 5 gold]
    [Gold Sword: 15 gold]
    [Gold Helmet: 15 gold]
    [Gold Chestplate: 15 gold]
    [Gold Leggings: 15 gold]
    [Gold Gauntlets: 15 gold]
    [Gold Boots: 15 gold]
    [Leave]
    ''').upper()

#------------------------------------------------------------------------------------------------------------------------#
    #Code checks for raw input by converting text to caps and removing spaces, provided by "drinking" on StackOverflow.com
        Input= ("%s" % ("".join(Input.upper().split(" "))))
    #Code checks for a raw input of Copper Sword in any variance of capitalization or spaces
        if Input == "COPPERSWORD":
    #Code checks for if user has enough gold and does not have a better variant equipped
            if Gold >= 1 and Iron_Sword != "Equipped" and Gold_Sword != "Equipped" and Copper_Sword != "Equipped":
                Input= input("You would like to purchase the Copper sword for 1 gold?: ")
                Input= ("%s" % ("".join(Input.upper().split(" "))))
    #Second check for a yes/other response
                if Input == "YES":
                    print("You have purchased and equipped the Copper sword.")
                    Copper_Sword = "Equipped"
                    Gold -= 1
                else:
                    print("So would you like to purchase something else?:")
            else:
                print("You do not have enough gold and/or you already have a better weapon equipped.")
#------------------------------------------------------------------------------------------------------------------------#

#------------------------------------------------------------------------------------------------------------------------#
    #Code checks for a raw input of Copper Helmet in any variance of capitalization or spaces
        elif Input == "COPPERHELMET":
    #Code checks for if user has enough gold and does not have a better variant equipped
            if Gold >= 1 and Iron_Helmet != "Equipped" and Gold_Helmet != "Equipped" and Copper_Helmet != "Equipped":
                Input= input("You would like to purchase the Copper helmet for 1 gold?: ")
                Input= ("%s" % ("".join(Input.upper().split(" "))))
    #Second check for a yes/other response
                if Input == "YES":
                    print("You have purchased and equipped the Copper helmet.")
                    Copper_Helmet = "Equipped"
                    Gold -=1
                else:
                    print("So would you like to purchase something else?:")
            else:
                print("You do not have enough gold and/or you already have a better helmet equipped.")
#------------------------------------------------------------------------------------------------------------------------#

#------------------------------------------------------------------------------------------------------------------------#
    #Code checks for a raw input of Copper Chestplate in any variance of capitalization or spaces
        elif Input == "COPPERCHESTPLATE":
    #Code checks for if user has enough gold and does not have a better variant equipped
            if Gold >= 1 and Iron_Chestplate != "Equipped" and Gold_Chestplate != "Equipped" and Copper_Chestplate != "Equipped":
                Input= input("You would like to purchase the Copper chestplate for 1 gold?: ")
                Input= ("%s" % ("".join(Input.upper().split(" "))))
    #Second check for a yes/other response
                if Input == "YES":
                    print("You have purchased and equipped the Copper chestplate.")
                    Copper_Chestplate = "Equipped"
                    Gold -=1
                else:
                    print("So would you like to purchase something else?: ")
            else:
                print("You do not have enough gold and/or you already have a better chestplate equipped.")
#------------------------------------------------------------------------------------------------------------------------#

#------------------------------------------------------------------------------------------------------------------------#    
    #Code checks for a raw input of Copper Leggings in any variance of capitalization or spaces
        elif Input == "COPPERLEGGINGS":
    #Code checks for if user has enough gold and does not have a better variant equipped
            if Gold >= 1 and Iron_Leggings != "Equipped" and Gold_Leggings != "Equipped" and Copper_Leggings != "Equipped":
                Input= input("You would like to purchase the Copper leggings for 1 gold?: ")
                Input= ("%s" % ("".join(Input.upper().split(" "))))
    #Second check for a yes/other response
                if Input == "YES":
                    print("You have purchased and equipped the Copper leggings.")
                    Copper_Leggings = "Equipped"
                    Gold -=1
                else:
                    print("So would you like to purchase something else?: ")
            else:
                print("You do not have enough gold and/or you already have a better set of leggings equipped.")
#------------------------------------------------------------------------------------------------------------------------#

#------------------------------------------------------------------------------------------------------------------------#
    #Code checks for a raw input of Copper Gauntlets in any variance of capitalization or spaces
        elif Input == "COPPERGAUNTLETS":
    #Code checks for if user has enough gold and does not have a better variant equipped
            if Gold >= 1 and Iron_Gauntlets != "Equipped" and Gold_Gauntlets != "Equipped" and Copper_Gauntlets != "Equipped":
                Input= input("You would like to purchase the Copper gauntlets for 1 gold?: ")
                Input= ("%s" % ("".join(Input.upper().split(" "))))
    #Second check for a yes/other response
                if Input == "YES":
                    print("You have purchased and equipped the Copper gauntlets.")
                    Copper_Gauntlets = "Equipped"
                    Gold -=1
                else:
                    print("So would you like to purchase something else?: ")
            else:
                print("You do not have enough gold and/or you already have a better set of gauntlets equipped.")
#------------------------------------------------------------------------------------------------------------------------#

#------------------------------------------------------------------------------------------------------------------------#
    #Code checks for a raw input of Copper Boots in any variance of capitalization or spaces
        elif Input == "COPPERBOOTS":
    #Code checks for if user has enough gold and does not have a better variant equipped
            if Gold >= 1 and Iron_Boots != "Equipped" and Gold_Boots != "Equipped" and Copper_Boots != "Equipped":
                Input= input("You would like to purchase the Copper boots for 1 gold?: ")
                Input= ("%s" % ("".join(Input.upper().split(" "))))
    #Second check for a yes/other response
                if Input == "YES":
                    print("You have purchased and equipped the Copper boots.")
                    Copper_Boots = "Equipped"
                    Gold -=1
                else:
                    print("So would you like to purchase something else?: ")
            else:
                print("You do not have enough gold and/or you already have a better set of boots equipped.")
#------------------------------------------------------------------------------------------------------------------------#

#------------------------------------------------------------------------------------------------------------------------#
    #Code checks for a raw input of Iron Sword in any variance of capitalization or spaces
        if Input == "IRONSWORD":
    #Code checks for if user has enough gold and does not have a better variant equipped
            if Gold >= 5 and Gold_Sword != "Equipped" and Iron_Sword != "Equipped":
                Input= input("You would like to purchase the Iron sword for 5 gold?: ")
                Input= ("%s" % ("".join(Input.upper().split(" "))))
    #Second check for a yes/other response
                if Input == "YES":
                    print("You have purchased and equipped the Iron sword.")
                    Iron_Sword = "Equipped"
                    Copper_Sword = "Unequipped"
                    Gold -=5
                else:
                    print("So would you like to purchase something else?: ")
            else:
                print("You do not have enough gold and/or you already have a better weapon equipped.")
#------------------------------------------------------------------------------------------------------------------------#

#------------------------------------------------------------------------------------------------------------------------#
    #Code checks for a raw input of Iron Helmet in any variance of capitalization or spaces
        elif Input == "IRONHELMET":
    #Code checks for if user has enough gold and does not have a better variant equipped
            if Gold >= 5 and Gold_Helmet != "Equipped" and Iron_Helmet != "Equipped":
                Input= input("You would like to purchase the Iron helmet for 5 gold?: ")
                Input= ("%s" % ("".join(Input.upper().split(" "))))
    #Second check for a yes/other response
                if Input == "YES":
                    print("You have purchased and equipped the Iron helmet.")
                    Iron_Helmet = "Equipped"
                    Copper_Helmet = "Unequipped"
                    Gold -=5
                else:
                    print("So would you like to purchase something else?: ")
            else:
                print("You do not have enough gold and/or you already have a better helmet equipped.")
#------------------------------------------------------------------------------------------------------------------------#

#------------------------------------------------------------------------------------------------------------------------#
    #Code checks for a raw input of Iron Chestplate in any variance of capitalization or spaces
        elif Input == "IRONCHESTPLATE":
    #Code checks for if user has enough gold and does not have a better variant equipped
            if Gold >= 5 and Gold_Chestplate != "Equipped" and Iron_Helmet != "Equipped":
                Input= input("You would like to purchase the Iron chestplate for 5 gold?: ")
                Input= ("%s" % ("".join(Input.upper().split(" "))))
    #Second check for a yes/other response
                if Input == "YES":
                    print("You have purchased and equipped the Iron chestplate.")
                    Iron_Chestplate = "Equipped"
                    Copper_Chestplate = "Unequipped"
                    Gold -=5
                else:
                    print("So would you like to purchase something else?: ")
            else:
                print("You do not have enough gold and/or you already have a better chestplate equipped.")
#------------------------------------------------------------------------------------------------------------------------#

#------------------------------------------------------------------------------------------------------------------------#
    #Code checks for a raw input of Iron Leggings in any variance of capitalization or spaces
        elif Input == "IRONLEGGINGS":
    #Code checks for if user has enough gold and does not have a better variant equipped
            if Gold >= 5 and Iron_Leggings != "Equipped" and Gold_Leggings != "Equipped":
                Input= input("You would like to purchase the Iron leggings for 5 gold?: ")
                Input= ("%s" % ("".join(Input.upper().split(" "))))
    #Second check for a yes/other response
                if Input == "YES":
                    print("You have purchased and equipped the Iron leggings.")
                    Iron_Leggings = "Equipped"
                    Copper_Leggings = "Unequipped"
                    Gold -=5
                else:
                    print("So would you like to purchase something else?: ")
            else:
                print("You do not have enough gold and/or you already have a better set of leggings equipped.")
#------------------------------------------------------------------------------------------------------------------------#

#------------------------------------------------------------------------------------------------------------------------#
    #Code checks for a raw input of Iron Gauntlets in any variance of capitalization or spaces
        elif Input == "IRONGAUNTLETS":
    #Code checks for if user has enough gold and does not have a better variant equipped
            if Gold >= 5 and Iron_Gauntlets != "Equipped" and Gold_Gauntlets != "Equipped":
                Input= input("You would like to purchase the Iron gauntlets for 5 gold?: ")
                Input= ("%s" % ("".join(Input.upper().split(" "))))
    #Second check for a yes/other response
                if Input == "YES":
                    print("You have purchased and equipped the Iron gauntlets.")
                    Iron_Gauntlets = "Equipped"
                    Copper_Gauntlets = "Unequipped"
                    Gold -=5
                else:
                    print("So would you like to purchase something else?: ")
            else:
                print("You do not have enough gold and/or you already have a better set of gauntlets equipped.")
#------------------------------------------------------------------------------------------------------------------------#

#------------------------------------------------------------------------------------------------------------------------#
    #Code checks for a raw input of Iron Boots in any variance of capitalization or spaces
        elif Input == "IRONBOOTS":
    #Code checks for if user has enough gold and does not have a better variant equipped
            if Gold >= 5 and Iron_Boots != "Equipped" and Gold_Boots != "Equipped":
                Input= input("You would like to purchase the Iron gauntlets for 5 gold?: ")
                Input= ("%s" % ("".join(Input.upper().split(" "))))
    #Second check for a yes/other response
                if Input == "YES":
                    print("You have purchased and equipped the Iron boots.")
                    Iron_Boots = "Equipped"
                    Copper_Boots = "Unequipped"
                    Gold -=5
                else:
                    print("So would you like to purchase something else?: ")
            else:
                print("You do not have enough gold and/or you already have a better set of boots equipped.")
#------------------------------------------------------------------------------------------------------------------------#

#------------------------------------------------------------------------------------------------------------------------#
    #Code checks for a raw input of Gold Sword in any variance of capitalization or spaces
        if Input == "GOLDSWORD":
    #Code checks for if user has enough gold and does not have a better variant equipped
            if Gold >= 15 and Gold_Sword != "Equipped":
                Input= input("You would like to purchase the Gold sword for 15 gold?: ")
                Input= ("%s" % ("".join(Input.upper().split(" "))))
    #Second check for a yes/other response
                if Input == "YES":
                    print("You have purchased and equipped the Gold sword.")
                    Gold_Sword = "Equipped"
                    Copper_Sword = "Unequipped"
                    Iron_Sword = "Unequipped"
                    Gold -=15
                else:
                    print("So would you like to purchase something else?: ")
            else:
                print("You do not have enough gold and/or you already have a better weapon equipped.")
#------------------------------------------------------------------------------------------------------------------------#

#------------------------------------------------------------------------------------------------------------------------#
    #Code checks for a raw input of Gold Helmet in any variance of capitalization or spaces
        elif Input == "GOLDHELMET":
    #Code checks for if user has enough gold and does not have a better variant equipped
            if Gold >= 15 and Gold_Helmet != "Equipped":
                Input= input("You would like to purchase the Gold helmet for 15 gold?: ")
                Input= ("%s" % ("".join(Input.upper().split(" "))))
    #Second check for a yes/other response
                if Input == "YES":
                    print("You have purchased and equipped the Gold helmet.")
                    Gold_Helmet = "Equipped"
                    Copper_Helmet = "Unequipped"
                    Iron_Helmet = "Unequipped"
                    Gold -=15
                else:
                    print("So would you like to purchase something else?: ")
            else:
                print("You do not have enough gold and/or you already have a better helmet equipped.")
#------------------------------------------------------------------------------------------------------------------------#

#------------------------------------------------------------------------------------------------------------------------#
    #Code checks for a raw input of Gold Chestplate in any variance of capitalization or spaces
        elif Input == "GOLDCHESTPLATE":
    #Code checks for if user has enough gold and does not have a better variant equipped
            if Gold >= 15 and Gold_Chestplate != "Equipped":
                Input= input("You would like to purchase the Gold chestplate for 15 gold?: ")
                Input= ("%s" % ("".join(Input.upper().split(" "))))
    #Second check for a yes/other response
                if Input == "YES":
                    print("You have purchased and equipped the Gold chestplate.")
                    Gold_Chestplate = "Equipped"
                    Copper_Chestplate = "Unequipped"
                    Gold -=15
                else:
                    print("So would you like to purchase something else?: ")
            else:
                print("You do not have enough gold and/or you already have a better chestplate equipped.")
#------------------------------------------------------------------------------------------------------------------------#

#------------------------------------------------------------------------------------------------------------------------#
    #Code checks for a raw input of Gold Leggings in any variance of capitalization or spaces
        elif Input == "GOLDLEGGINGS":
    #Code checks for if user has enough gold and does not have a better variant equipped
            if Gold >= 15 and Gold_Leggings != "Equipped":
                Input= input("You would like to purchase the Gold leggings for 15 gold?: ")
                Input= ("%s" % ("".join(Input.upper().split(" "))))
    #Second check for a yes/other response
                if Input == "YES":
                    print("You have purchased and equipped the Gold leggings.")
                    Gold_Leggings = "Equipped"
                    Copper_Leggings = "Unequipped"
                    Iron_Leggings = "Unequipped"
                    Gold -=15
                else:
                    print("So would you like to purchase something else?: ")
            else:
                print("You do not have enough gold and/or you already have a better set of leggings equipped.")
#------------------------------------------------------------------------------------------------------------------------#

#------------------------------------------------------------------------------------------------------------------------#
    #Code checks for a raw input of Gold Gauntlets in any variance of capitalization or spaces
        elif Input == "GOLDGAUNTLETS":
    #Code checks for if user has enough gold and does not have a better variant equipped
            if Gold >= 15 and Gold_Gauntlets != "Equipped":
                Input= input("You would like to purchase the Gold gauntlets for 15 gold?: ")
                Input= ("%s" % ("".join(Input.upper().split(" "))))
    #Second check for a yes/other response
                if Input == "YES":
                    print("You have purchased and equipped the Gold gauntlets.")
                    Gold_Gauntlets = "Equipped"
                    Copper_Gauntlets = "Unequipped"
                    Iron_Gauntlets = "Unequipped"
                    Gold -=15
                else:
                    print("So would you like to purchase something else?: ")
            else:
                print("You do not have enough gold and/or you already have a better set of gauntlets equipped.")
#------------------------------------------------------------------------------------------------------------------------#

#------------------------------------------------------------------------------------------------------------------------#
    #Code checks for a raw input of Gold Boots in any variance of capitalization or spaces
        elif Input == "GOLDBOOTS":
    #Code checks for if user has enough gold and does not have a better variant equipped
            if Gold >= 15 and Gold_Boots != "Equipped":
                Input= input("You would like to purchase the Gold boots for 15 gold?: ")
                Input= ("%s" % ("".join(Input.upper().split(" "))))
    #Second check for a yes/other response
                if Input == "YES":
                    print("You have purchased and equipped the Gold boots.")
                    Gold_Boots = "Equipped"
                    Copper_Boots = "Unequipped"
                    Iron_Boots = "Unequipped"
                    Gold -=15
                else:
                    print("So would you like to purchase something else?: ")
            else:
                print("You do not have enough gold and/or you already have a better set of boots equipped.")
#------------------------------------------------------------------------------------------------------------------------#

#------------------------------------------------------------------------------------------------------------------------#
    #Code checks for a raw input of Leave in any variance of capitalization or spaces
        elif Input == "LEAVE":
            Input= input("You would like to leave?: ")
            Input= ("%s" % ("".join(Input.upper().split(" "))))
    #Code checks for a yes/other response
            if Input == "YES":
                    Equipment()
                    Stats()
                    EnemyEncountered= 0
                    CombatModule()
            else:
                print("So would you like to purchase something else?: ")
    Equipment()
    Stats()
    EnemyEncountered = 0
    Shop()
#------------------------------------------------------------------------------------------------------------------------#
Equipment()
Stats()
Title()
CombatModule()
