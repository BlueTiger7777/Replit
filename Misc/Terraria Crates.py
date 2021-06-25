import random

#Text Based Menu
def menu():
    # Calls for an infinite loop that keeps executing
    # until an exception occurs
    while True:
        try:
            print("Terraria Crate Generator\n1 - Wooden Crate\n2 - Iron Crate\n3 - Golden Crate\n4 - Jungle Crate\n5 - Sky Crate\n6 - Corrupt Crate\n7 - Crimson Crate\n8 - Hallowed Crate\n9 - Dungeon Crate\n10 - Frozen Crate\n11 - Oasis Crate\n12 - Obsidian Crate\n13 - Ocean Crate\n14 - Pearlwood Crate\n15 - Mythril Crate\n16 - Titanium Crate\n17 - Bramble Crate\n18 - Azure Crate\n19 - Defiled Crate\n20 - Hematic Crate\n21 - Divine Crate\n22 - Stockade Crate\n23 - Boreal Crate\n24 - Mirage Crate\n25 - Hellstone Crate\n26 - Seaside Crate")
            Crate = int(input("Crate: " ))
        # If something else that is not the string
        # version of a number is introduced, the
        # ValueError exception will be called.
        except ValueError:
            # The cycle will go on until validation
            print("Error! This is not a number. Try again.")
        else:
            if Crate == 1:
                WoodenCrate()
            elif Crate == 2:
                print("test 2")

def WoodenCrate():
    def WoodenCrateMI():
        #Defines the main items
        SailfishBoots = random.randrange(1, 41)
        TsunamiInABottle = random.randrange(1, 1601)
        Extractinator = random.randrange(1, 53)
        #Generates a main item
        if SailfishBoots == 1:
            print("Sailfish Boots")
            WoodenCrateSI()
        elif TsunamiInABottle <= 39:
            print("Tsunami In A Bottle")
            WoodenCrateSI()
        elif Extractinator == 1:
            print("Extractinator")
            WoodenCrateSI()
        else:
            WoodenCrateMI()

    def WoodenCrateSI():
        #Defines the sub items
        SubItem = random.randrange(1, 46)
        #Generates a sub item
        if SubItem == 1:
            print("Aglet")
            WoodenCrateC()
        elif SubItem == 2:
            print("Umbrella")
            WoodenCrateC()
        elif SubItem == 3:
            print("Climbing Claws")
            WoodenCrateC()
        elif SubItem == 4:
            print("Guide to Plant Fiber Cordage")
            WoodenCrateC()
        elif SubItem == 5:
            print("Radar")
            WoodenCrateC()
        else:
            WoodenCrateSI()
    def WoodenCrateC():
        #Defines the coins
        Coins = random.randrange(1, 22)
        #Generates coins
        if Coins <= 2:
            print(random.randrange(20, 91), "Silver Coins")
            WoodenCrateO()
        elif Coins == 3:
            print(random.randrange(1, 6), "Gold Coins")
            WoodenCrateO()
        else:
            WoodenCrateC()
    def WoodenCrateO():
        #Defines the ores
        Ores = random.randrange(1, 8)
        #Generates ores
        if Ores == 1:
            print(random.randrange(6, 24), "Copper Ore")
            WoodenCrateB()
        elif Ores == 2:
            print(random.randrange(6, 24), "Tin Ore")
            WoodenCrateB()
        elif Ores == 3:
            print(random.randrange(6, 24), "Iron Ore")
            WoodenCrateB()
        elif Ores == 4:
            print(random.randrange(6, 24), "Lead Ore")
            WoodenCrateB()
        else:
            WoodenCrateO()
    def WoodenCrateB():
        #Defines the bars
        Bars = random.randrange(1, 29)
        #Generates bars
        if Bars <= 3:
            print(random.randrange(2, 8), "Copper Bars")
            WoodenCrateP()
        elif Bars <= 6:
            print(random.randrange(2, 8), "Tin Bars")
            WoodenCrateP()
        elif Bars <= 9:
            print(random.randrange(2, 8), "Iron Bars")
            WoodenCrateP()
        elif Bars <= 12:
            print(random.randrange(2, 8), "Lead Bars")
            WoodenCrateP()
        else:
            WoodenCrateB()
    def WoodenCrateP():
        #Defines the potions
        Potions = random.randrange(1, 11)
        #Generates potions
        if Potions == 1:
            print(random.randrange(1, 4), "Obsidian Skin Potion")
            WoodenCrateHMP()
        elif Potions == 2:
            print(random.randrange(1, 4), "Swiftness Potion")
            WoodenCrateHMP()
        elif Potions == 3:
            print(random.randrange(1, 4), "Ironskin Potion")
            WoodenCrateHMP()
        elif Potions == 4:
            print(random.randrange(1, 4), "Night Owl Potion")
            WoodenCrateHMP()
        elif Potions == 5:
            print(random.randrange(1, 4), "Shine Potion")
            WoodenCrateHMP()
        elif Potions == 6:
            print(random.randrange(1, 4), "Hunter Potion")
            WoodenCrateHMP()
        elif Potions == 7:
            print(random.randrange(1, 4), "Gills Potion")
            WoodenCrateHMP()
        elif Potions == 8:
            print(random.randrange(1, 4), "Mining Potion")
            WoodenCrateHMP()
        elif Potions == 9:
            print(random.randrange(1, 4), "Heartreach Potion")
            WoodenCrateHMP()
        elif Potions == 10:
            print(random.randrange(1, 4), "Dangersense Potion")
            WoodenCrateHMP()
        else:
            WoodenCrateP()
    def WoodenCrateHMP():
        #Defines health/mana potions
        HMP = random.randrange(1, 4)
        #Generates health/mana potions
        if HMP == 1:
            print(random.randrange(5, 16), "Lesser Healing Potions")
            WoodenCrateBait()
        elif HMP == 2:
            print(random.randrange(5, 16), "Lesser Mana Potions")
            WoodenCrateBait()
        else:
            WoodenCrateHMP()
    def WoodenCrateBait():
        #Defines baits
        Bait = random.randrange(1, 10)
        #Generates bait
        if Bait <= 2:
            print(random.randrange(1, 5), "Apprentice Bait")
            input("Press ENTER To Go Back To The Menu")
            menu()
        elif Bait == 3:
            print(random.randrange(1, 4), "Journeyman Bait")
            input("Press ENTER To Go Back To The Menu")
            menu()
        else:
            WoodenCrateBait()
    WoodenCrateMI()
menu()
