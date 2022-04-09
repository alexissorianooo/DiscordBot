'''
https://betterprogramming.pub/coding-a-discord-bot-with-python-64da9d6cade7
'''

from lib2to3.pgen2.token import EQUAL
import os
import discord
from dotenv import load_dotenv
import random

intents = discord.Intents.default()
intents.members = True
intents.typing = False
intents.presences = True

# LOADS THE .env FIILE THE RESIDES ON THE SAME LVEL AS THE SCRIPT
load_dotenv()
# GRABS THE API TOKEN FROM .env FILE 
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# GETS THE OBJECTS FROM DISCORD.PY 
bot = discord.Client(intents=intents)
guild_var = discord.Guild


# My Variables
Maps=["Ascent", "Bind", "Haven", "Split", "Icebox", "Breeze", "Fracture"]
valorantWar = ["5v5"]

lockedin = []
serverName="none"
team1 = []


# EVENT LISTENER FOR WHEN THE BOT IS READY/ONLINE
@bot.event
async def on_ready():
    print(bot.user)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    # MY SHORTCUTS
    messageContent = message.content
    author = message.author

    if message.content.startswith(",help"):
        await message.channel.send("Oy pre, baket? ")
        await message.channel.send("```,map = random map generator for valorant.```")
  
    if message.content.startswith(",map"):
        maps = generatemapval()
        await message.channel.send(maps)

    if message.content.startswith(",happy"):
        await message.channel.send("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

    if any(word in messageContent.lower() for word in valorantWar):
        await message.channel.send("nakarinig ako ng 5v5???")

    if message.content.startswith(",serverName"):
        await message.channel.send(author.guild.name)

    if messageContent.startswith(",servers"):
        await message.channel.send("I am a member of the following servers:")
        async for item in bot.fetch_guilds():
            await message.channel.send(item.name)
    
    if messageContent.startswith(",g"):
        global serverName
        serverName = str(author.guild.name)
        
        if "<@"+str(author.id)+">" in lockedin:
            await message.channel.send("<@"+str(author.id)+">" + " is already locked in")
        else:
            await message.channel.send("<@"+str(author.id)+">" + " is ready.")
            lockedin.append("<@"+str(author.id)+">")
    
    if messageContent.startswith(",whog"):
        if serverName == author.guild.name:
            await message.channel.send("Locked in players: " + str(len(lockedin)))
            for items in lockedin:
                await message.channel.send(items)
        else:
            await message.channel.send("No players are ready, sadge :( ")
    
    if messageContent.startswith(",team"):
        if serverName == author.guild.name:
            global team1
            even = len(lockedin)/2
            
            balanceTeam(even)
            
            await message.channel.send("Team 1:")
            for items in team1:
                await message.channel.send(items)

            await message.channel.send("Team 2:")
            for items in lockedin:
                await message.channel.send(items)
        else:
            await message.channel.send("No players are ready, sadge :( ")

    if messageContent.startswith(",reteam"):
        if serverName == author.guild.name:
            

            for item in team1:
                lockedin.append(item)
                team1.remove(item)
            
            even = len(lockedin)/2
            
            balanceTeam(even)
            
            await message.channel.send("Team 1:")
            for items in team1:
                await message.channel.send(items)

            await message.channel.send("Team 2:")
            for items in lockedin:
                await message.channel.send(items)
        else:
            await message.channel.send("No players are ready, sadge :( ")




# My methods/functions
def generatemapval():
  map = random.choice(Maps)
  return map

def balanceTeam(even):
    if even == 0:
        while len(team1) != len(lockedin):
            player = random.choice(lockedin)
            team1.append(player)
            lockedin.remove(player)
    else:
        
        while len(team1) < len(lockedin):
            player = random.choice(lockedin)
            team1.append(player)
            lockedin.remove(player)


# RUNS THE BOT VIA TOKEN
bot.run(DISCORD_TOKEN)