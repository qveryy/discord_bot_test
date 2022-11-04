import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()


client = commands.Bot(command_prefix="--", intents=discord.Intents.all())

@client.event
async def on_ready():
    print("Der Bot ist eingeloggt als {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("-hello"):
        await message.channel.send("Hello!")

    if message.content.startswith("-dm"):
        await message.author.send("This is my private Message!")


@client.command #doesnt work
async def hello(ctx):
    await ctx.send("hello")


#client.run("MTAzMjcwMTYxMDY0MTYwODc1Nw.GjX6qP.IuWX--Hk1NYRJXOTfLv7jpDkiBPRkRlSlMC_JU")
client.run(os.getenv("TOKEN"))