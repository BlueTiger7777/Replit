import random

print("Start Setup")
#Setup code
BlackHoleLength = 3

#Options to output
SolOut = True
SunOut = True
PlanetOut = True
MoonPlanetOut = True
ShipOut = True
BlackHoleOut = True
AstroidFeildOut = True
GateWayOut = True
StationOut = True

#Prefixes for Sol Name
Letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
Number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SSNP1 = ['Razz', 'Syrinx', 'Celestal', 'Sadalsuud', 'Apolo', 'Kepler', 'Milky', 'Sulafat', 'Acubens', 'Sharcedon', 'Alula', 'Tranguli', 'Aerocia', 'Magna', 'Kakkab', 'Zoinks', 'Pherkad', 'Epingi', 'Acubens', 'Ardentee', 'Menkib', 'Alphecca']
SSNP2 = ['Omega', 'Alpha', 'Bata', 'Prime', 'Rest', 'Mire', 'Legion', 'Way', 'Mass', 'Morass', 'Stream', 'Borealis', 'Rim', 'Lupo', 'Ridge', 'Traverse', 'Stand', 'Veil', 'Morass', 'Precipice', 'Swarm']
SSNP3 = ['Delta', 'Grasp']
Sun_Type = ['Red Dwarf', 'Brown Dwarf', 'White Dwarf', 'Subdwarf', 'Subgiant', 'Giant', 'Bright Giant', 'Supergiant', 'Hypergiant', 'Gentle', 'Tempearate', 'Radioactive', 'Frozen', 'Firey']
Planet_Type = ['Barren', 'Garden', 'Forest', 'Desert', 'Ocean', 'Savannah', 'Mutated', 'Toxic', 'Snow', 'Jungle', 'Artic', 'Midnight', 'Tundra', 'Decayed', 'Magma', 'Volcanic', 'Gas Giant']
Ship_Type = ['Friendly', 'Hostile']
Station = ['Yes', 'No']

print("End Setup - Start SolName")
#Code that genrates and prints result
Planet_Num = random.randrange(3, 6)
PI = 1

#Genrates sol system name
if SolOut == True:
    SNI = random.randrange(1, 3)
    while SNI == 1:
        SOP = "> Sol Name - " + random.choice(SSNP1) + " " + random.choice(SSNP2) + " " + random.choice(SSNP3)
        SNI = 0
    while SNI == 2:
        SOP = "> Sol Name - " + random.choice(SSNP1) + " " + random.choice(SSNP2)
        SNI = 0
print("End SolName - Start SunType")
#Genrates sun type
if SunOut == True:
    SOP = SOP + "\n> Sun Type - " + random.choice(Sun_Type)
#Genrates planets with a chance of a sub planet or moon
print("End SolType - Start Planet")
if PlanetOut == True:
    while Planet_Num >= PI:
        SOP = SOP + "\n> Planet Type - " + random.choice(Planet_Type)
        MI1 = random.randrange(1, 3)

        #Will make a sub planet or moon if set to true
        print("End Planet - Start MoonSubP1")
        if MoonPlanetOut == True:
            while MI1 == 1:
                PRM = random.randrange(1, 3)
                SI = random.randrange(1, 6)
                if PRM == 1:
                    SOP = SOP + "\n> Moon"
                    MI1 = 0
                    MI2 = random.randrange(1, 11)
                else:
                    SOP = SOP + "\n> Sub Planet Type - " + random.choice(Planet_Type)
                    MI1 = 0
                    MI2 = random.randrange(1, 11)

                #Chance to have a second sub planet or moon
                print("End MoonSubP1 - Start MoonSubP2")
                while MI2 == 1:
                    PRM2 = random.randrange(1, 3)
                    if PRM2 == 1:
                        SOP = SOP + "\n> Moon"
                        MI2 = 0
                        MI3 = random.randrange(1, 16)
                    else:
                        SOP = SOP + "\n> Sub Planet Type - " + random.choice(Planet_Type)
                        MI2 = 0
                        MI3 = random.randrange(1, 16)

                    #Chance to have a third sub planet or moon
                    print("End MoonSubP2 - Start MoonSubP3")
                    while MI3 == 1:
                        PRM3 = random.randrange(1, 3)
                        if PRM3 == 1:
                            SOP = SOP + "\n> Moon"
                            MI3 = 0
                        else:
                            SOP = SOP + "\n> Sub Planet Type - " + random.choice(Planet_Type)
                            MI3 = 0

                #Chance to have a ship orbiting the planet
                print("End MoonSubP1-3 - Start Ship")
                if ShipOut == True:
                    if SI == 1:
                        SOP = SOP + ("\n> Ship") + random.choice(Ship_Type)
        PI += 1

#Chance to generate a black hole
print("End Planet/MoonSubP1-3 - Start Blackhole1")
if BlackHoleOut == True:
    BHI1 = random.randrange(1, 6)
    while BHI1 == 1:
            BHL1 = "".join(random.choice(Letter) for i in range(BlackHoleLength))
            BHN1 = "".join(random.choice(Number) for i in range(BlackHoleLength))
            SOP = SOP + "\n> " + BHL1 + "-" + BHN1
            BHI1 = 0
            BHI2 = random.randrange(1, 11)

            #Chance to make a second black hole
            print("End Blackhole1 - Start Blackhole2")
            while BHI2 == 1:
                BHL2 = "".join(random.choice(Letter) for i in range(BlackHoleLength))
                BHN2 = "".join(random.choice(Number) for i in range(BlackHoleLength))
                SOP = SOP + "\n> " + BHL2 + "-" + BHN2
                BHI2 = 0
                BHI3 = random.randrange(1, 16)

                #Chance to make a third black hole
                print("End Blackhole2 - Start Blackhole3")
                while BHI3 == 1:
                    BHL3 = "".join(random.choice(Letter) for i in range(BlackHoleLength))
                    BHN3 = "".join(random.choice(Number) for i in range(BlackHoleLength))
                    SOP = SOP + "\n> " + BHL3 + "-" + BHN3
                    BHI3 = 0

#Chance to genrate a astroid feild
print("End Planet/MoonSubP1-3/Blackhole1-3 - Start Astroid")
if AstroidFeildOut == True:
    AFI = random.randrange(1, 10)
    while AFI == 1:
        SOP = SOP + "\n> Astroid Feild"
        AFI = 0

#Chance to genrate a gateway
print("End Planet/MoonSubP1-3/Blackhole1-3/Astroid - Start Gateway")
if GateWayOut == True:
    GI = random.randrange(1,21)
    while GI == 1:
        SOP = SOP + "\n> Gateway"
        GI = 0

#Chance to genrate a space station
print("End Planet/MoonSubP1-3/Blackhole1-3/Astroid/Gateway - Start Station")
if StationOut == True:
    SI = random.randrange(1, 6)
    while SI == 1:
        SST = random.choice(Station)
        SOP = SOP + "\n> Space Station -" + SST
        SI = 0
print("End")
print(SOP)
