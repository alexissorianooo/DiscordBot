'''
https://betterprogramming.pub/coding-a-discord-bot-with-python-64da9d6cade7
'''

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
    
    if messageContent.startswith(",test"):
        # for item in:
        await message.channel.send(guild_var.members)



# My methods/functions
def generatemapval():
  map = random.choice(Maps)
  return map

# RUNS THE BOT VIA TOKEN
bot.run(DISCORD_TOKEN)