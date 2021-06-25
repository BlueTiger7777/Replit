#sets up the bot
import discord
import random
import json
import datetime
from discord.ext import commands, tasks
from itertools import cycle
t = datetime.datetime.now()
TOP = True
RickRoll = True

#code to open prefixes.json
def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

#sets the prefix of the bot
client = commands.Bot(command_prefix = get_prefix)

#status strings
status = cycle(['Online And Working', 'Generating Solar Systems', '#help For Commands', 'Updated New Commands', 'Solar System Genorator Command FIXED', 'New Powers Calculator(Dosnt Do Floats(Decimale Points))'])

#says when bot is online
@client.event
async def on_ready():
    if TOP == True:
        t = datetime.datetime.now()
    else:
        t = ""
    change_status.start()
    await client.change_presence(status=discord.Status.offline)
    print(f'{t} - Booting P.I.E.S - 100%')

#says when an account joins a server with this bot in it
@client.event
async def on_member_join(member):
    if TOP == True:
        t = datetime.datetime.now()
    else:
        t = ""
    print(f'{t} - Reciving {member} data - 100%')

#says when an account leaves a server with this bot in it
@client.event
async def on_member_remove(member):
    if TOP == True:
        t = datetime.datetime.now()
    else:
        t = ""
    print(f'{t} - Deleating {member} data - 100%')

#command to see latency of the bot
@client.command()
async def ping(ctx):
    if TOP == True:
        t = datetime.datetime.now()
        if RickRoll == True:
            RRN = random.randrange(1, 101)
            if RRN == 45:
                await ctx.send("https://tenor.com/view/rick-astley-rick-roll-dancing-dance-moves-gif-14097983")
                print(f'{t} - P.I.E.S - Sending RickRoll... Done')
            else:
                await ctx.send(f'Pong - Calculating Latency... Done Latency Is {round(client.latency * 1000)}ms')
                print(f'{t} - P.I.E.S - Calculating Latency... Done Latency Is {round(client.latency * 1000)}ms')
    else:
        t = ""
        if Rickroll == True:
            RRN = random.randrange(1, 101)
            if RRN == 45:
                await ctx.send("https://tenor.com/view/rick-astley-rick-roll-dancing-dance-moves-gif-14097983")
                print(f'{f} - P.I.E.S - Sending RickRoll... Done')
            else:
                await ctx.send(f'Pong - Calculating Latency... Done Latency Is {round(client.latency * 1000)}ms')
                print(f'{t} - P.I.E.S - Calculating Latency... Done Latency Is {round(client.latency * 1000)}ms')

#genrates a random answer to the asked question
@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    if TOP == True:
        t = datetime.datetime.now()
    else:
        t = ""
    responses = ['It is certain.',
                'It is decidedly so.',
                'Without a doubt.',
                'Yes - definitely.',
                'You may rely on it.',
                'As I see it, yes.',
                'Most likely.',
                'Outlook good.',
                'Yes.',
                'Signs point to yes.',
                'Reply hazy, try again.',
                'Ask again later.',
                'Better not tell you now.',
                'Cannot predict now.',
                'Concentrate and ask again.',
                "Don't count on it.",
                'My reply is no.',
                'My sources say no.',
                'Outlook not so good.',
                'Very doubtful.']
    ResponseYes = ['It is certain.',
                'It is decidedly so.',
                'Without a doubt.',
                'Yes - definitely.',
                'You may rely on it.',
                'As I see it, yes.',
                'Most likely.',
                'Outlook good.',
                'Yes.',
                'Signs point to yes.',]
    ResponseNo = ["Don't count on it.",
                'My reply is no.',
                'My sources say no.',
                'Outlook not so good.',
                'Very doubtful.']
    #if question == "do you support the imperial party":
        #await ctx.send(f'Probability of Question: {question}\nIs: {random.choice(ResponseYes)}')
        #print(f'{t} - P.I.E.S - Calculating Probability Of Question `{question}`...\nP.I.E.S - Probability Calculated... Sending...')
    #elif question == "do you support the socialist party":
        #await ctx.send(f'Probability of Question: {question}\nIs: {random.choice(ResponseNo)}')
        #print(f'{t} - P.I.E.S - Calculating Probability Of Question `{question}`...\nP.I.E.S - Probability Calculated... Sending...')
    #else:
    await ctx.send(f'Probability of Question: {question}\nIs: {random.choice(responses)}')
    print(f'{t} - P.I.E.S - Calculating Probability Of Question `{question}`...\nP.I.E.S - Probability Calculated... Sending...')

#"""
#solar system gen command
@client.command(aliases=['SSG', 'ssg', 'GSS', 'gss', 'Sol Gen', 'Solar Gen', 'Sol System Gen', 'Solar System Gen'])
async def sol_system_gen(ctx):
    if TOP == True:
        t = datetime.datetime.now()
    else:
        t = ""
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

    #Code that genrates and prints result
    Planet_Num = random.randrange(3, 6)
    PI = 1

    #Genrates sol system name
    if SolOut == True:
        SNI = random.randrange(1, 3)
        while SNI == 1:
            SOP = "_>_ Sol Name - " + random.choice(SSNP1) + " " + random.choice(SSNP2) + " " + random.choice(SSNP3)
            SNI = 0
        while SNI == 2:
            SOP = "_>_ Sol Name - " + random.choice(SSNP1) + " " + random.choice(SSNP2)
            SNI = 0

    #Genrates sun type
    if SunOut == True:
        SOP = SOP + "\n_>_ Sun Type - " + random.choice(Sun_Type)


    #Genrates planets with a chance of a sub planet or moon
    if PlanetOut == True:
        while Planet_Num >= PI:
            SOP = SOP + "\n_>_ Planet Type - " + random.choice(Planet_Type)
            MI1 = random.randrange(1, 3)

            #Will make a sub planet or moon if set to true
            if MoonPlanetOut == True:
                while MI1 == 1:
                    PRM = random.randrange(1, 3)
                    SI = random.randrange(1, 6)
                    if PRM == 1:
                        SOP = SOP + "\n_>_ Moon"
                        MI1 = 0
                        MI2 = random.randrange(1, 11)
                    else:
                        SOP = SOP + "\n_>_ Sub Planet Type - " + random.choice(Planet_Type)
                        MI1 = 0
                        MI2 = random.randrange(1, 11)

                    #Chance to have a second sub planet or moon
                    while MI2 == 1:
                        PRM2 = random.randrange(1, 3)
                        if PRM2 == 1:
                            SOP = SOP + "\n_>_ Moon"
                            MI2 = 0
                            MI3 = random.randrange(1, 3)
                        else:
                            SOP = SOP + "\n_>_ Sub Planet Type - " + random.choice(Planet_Type)
                            MI2 = 0
                            MI3 = random.randrange(1, 16)

                        #Chance to have a third sub planet or moon
                        while MI3 == 1:
                            PRM3 = random.randrange(1, 3)
                            if PRM3 == 1:
                                SOP = SOP + "\n_>_ Moon"
                                MI3 = 0
                            else:
                                SOP = SOP + "\n_>_ Sub Planet Type - " + random.choice(Planet_Type)
                                MI3 = 0

                    #Chance to have a ship orbiting the planet
                    if ShipOut == True:
                        if SI == 1:
                            SOP = SOP + ("\n_>_ Ship ") + random.choice(Ship_Type)
            PI += 1

    #Chance to generate a black hole
    if BlackHoleOut == True:
        BHI1 = random.randrange(1, 6)
        while BHI1 == 1:
                BHL1 = "".join(random.choice(Letter) for i in range(BlackHoleLength))
                BHN1 = "".join(random.choice(Number) for i in range(BlackHoleLength))
                SOP = SOP + "\n_>_ " + BHL1 + "-" + BHN1
                BHI1 = 0
                BHI2 = random.randrange(1, 11)

                #Chance to make a second black hole
                while BHI2 == 1:
                    BHL2 = "".join(random.choice(Letter) for i in range(BlackHoleLength))
                    BHN2 = "".join(random.choice(Number) for i in range(BlackHoleLength))
                    SOP = SOP + "\n_>_ " + BHL2 + "-" + BHN2
                    BHI2 = 0
                    BHI3 = random.randrange(1, 16)

                    #Chance to make a third black hole
                    while BHI3 == 1:
                        BHL3 = "".join(random.choice(Letter) for i in range(BlackHoleLength))
                        BHN3 = "".join(random.choice(Number) for i in range(BlackHoleLength))
                        SOP = SOP + "\n_>_ " + BHL3 + "-" + BHN3
                        BHI3 = 0

    #Chance to genrate a astroid feild
    if AstroidFeildOut == True:
        AFI = random.randrange(1, 10)
        while AFI == 1:
            SOP = SOP + "\n_>_ Astroid Feild"
            AFI = 0

    #Chance to genrate a gateway
    if GateWayOut == True:
        GI = random.randrange(1,21)
        while GI == 1:
            SOP = SOP + "\n_>_ Gateway"
            GI = 0

    #Chance to genrate a space station
    if StationOut == True:
        SI = random.randrange(1, 6)
        while SI == 1:
            SST = random.choice(Station)
            SOP = SOP + "\n_>_ Space Station -" + SST
            SI = 0

    embed=discord.Embed(title="System Genarated", description=SOP, color=0x1c0f5b)
    embed.set_footer(text="Type The Same Command Again To Regenerate A System")
    await ctx.send(embed=embed)
    print(f'{t} - P.I.E.S - Genarating Sol System... Done Sending...')
#"""

#says what P.I.E.S is
@client.command(aliases=['P.I.E.S', 'pies'])
async def what_is_pies(ctx):
    if TOP == True:
        t = datetime.datetime.now()
    else:
        t = ""
    await ctx.send("Sending My Description... Done\nP.I.E.S is Python Intelligent Enviroment System")
    print(f'{t} - P.I.E.S - Sending My Description... Done')

#random number genorator in length
@client.command(aliases=['rolll'])
async def rnl(ctx, length : int):
    if TOP == True:
        t = datetime.datetime.now()
    else:
        t = ""
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    RNLOutput = "".join(random.choice(numbers) for i in range(length))
    await ctx.send(f'Generating Number In Length Of {length}\nGenerated {RNLOutput}')
    print(f'{t} - P.I.E.S - Genrating Random Number In Length Of `{length}`')

#random number genorator in range
@client.command(aliases=['rollr'])
async def rnr(ctx, range1 : int, range2 : int):
    if TOP == True:
        t = datetime.datetime.now()
    else:
        t = ""
    range2plus1 = range2 + 1
    RNROutput = random.randrange(range1, range2plus1)
    await ctx.send(f'Generating Number In Ranges {range1} - {range2}\nGenerated {RNROutput}')
    print(f'{t} - P.I.E.S - Generating Number In Ranges `{range1}` - `{range2}`')

#clear command
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount : int):
    if TOP == True:
        t = datetime.datetime.now()
    else:
        t = ""
    await ctx.channel.purge(limit=amount)
    print(f'{t} - P.I.E.S - Clearing Message Data... Done')

#status changer
@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

#error handler
#"""
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        if TOP == True:
            t = datetime.datetime.now()
        else:
            t = ""
        await ctx.send('Error...\nMissing 1 Or More Required Arguments')
        print(f'{t} - P.I.E.S - Command Missing Arguments...')
    if isinstance(error, commands.CommandNotFound):
        if TOP == True:
            t = datetime.datetime.now()
        else:
            t = ""
        await ctx.send('Error...\nInvalid Command Used... Check `help` Command For List Of Commands')
        print(f'{t} - P.I.E.S - Command Not Found...')
    if isinstance(error, commands.MissingPermissions):
        if TOP == True:
            t = datetime.datetime.now()
        else:
            t = ""
        await ctx.send("Error...\nYou Don't Have Permission To Use That Command")
        print(f'{t} - P.I.E.S - User Missing Permission To Command')
#"""

#creats defult prefix
@client.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '#'

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

#removes the prefix
@client.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

#command to change the prefix
@client.command()
async def change_prefix(ctx, prefix):
    if TOP == True:
        t = datetime.datetime.now()
    else:
        t = ""
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

    await ctx.send(f'Changed Prefix To - `{prefix}`')
    print(f'{t} - P.I.E.S - Changeing Prefix Of A Server... Done')

#@command
@client.command()
@commands.has_permissions(administrator=True)
async def at(ctx, user : discord.Member):
    if TOP == True:
        t = datetime.datetime.now()
    else:
        t = ""
    mention = 3
    await ctx.send('Hey Wake Up ')
    while mention >= 0:
        await ctx.send(user.mention)
        mention = mention-1
    print(f'{t} - P.I.E.S - Waking Up User... Done')

@client.command()
async def power(ctx, Valin, Powerin):
    if TOP == True:
        t = datetime.datetime.now()
    else:
        t = ""

    Val = int(Valin)
    Indices = int(Powerin)
    Out = Val
    power = Indices
    power -= 1
    while power > 0:
        Out = Out*Val
        power -= 1
    await ctx.send(f'Calculating Answer\nAnswer {Out}')
    print(f'{t} - P.I.E.S - Calculating Answer To {Val}^{Indices}... Done')

#specific command error handler
#@clear.error
#async def clear_error(ctx, error):
#    await ctx.send('`clear` Command Requiers An Amount Of Messages To Deleat')

#token to run the bot
client.run('Nzk2MzI5OTcwMjg3OTAyNzQw.X_WWFA.UBW4nTt0whwSMV13z2QCtXpBHrA')
