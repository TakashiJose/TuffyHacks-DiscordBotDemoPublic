#IMPORT: importing discord bot libraries
import discord
from discord.ext import commands

#IMPORT: importing random generator
import random
import os
import json

client = commands.Bot(command_prefix='.')
client.remove_command('help')

token = open("token.txt")
TOKEN = token.read()

#EVENT: when the client is ready
@client.event
async def on_ready():
    print('Client running')

#EVENT: when a message is received
@client.event
async def on_message(ctx):
    #checks if sender of the message is the client
    if ctx.author == client.user:
        return
    if ctx.content.startswith('.') == False:
        await ctx.channel.send(ctx.content)
    if ctx.content.find("69") !=-1: 
        await ctx.channel.send("Nice")
    await client.process_commands(ctx)

#EVENT: when the prefix is used, but not a proper command is used
@client.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommmandNotFound):
		await ctx.send('Invalid command')

#COMMAND: hello, will respond with 'world' 
@client.command()
async def hello(ctx):
    """Send text message 'world'"""
    await ctx.send("world")
    return

#COMMAND: happy, will respond with the slight_smile emoji
@client.command()
async def happy(ctx):
    """Send :slight_smile: Emoji"""
    await ctx.send(":slight_smile:")
    return

#COMMAND: dice, will send value found by random generation
@client.command()
async def dice(ctx, *,arg):
    """Roll Dice"""
    dice_result=0
    if arg == "help":
        await ctx.send(".dice <dicetype>")
        await ctx.send("dicetype: d4, d6, d8, d10, d12, d20")
        return
    if arg == "d4":
        dice_result = random.randint(1,4)
    if arg == "d6":
        dice_result = random.randint(1,6)
    if arg == "d8":
        dice_result = random.randint(1,8)
    if arg == "d10":
        dice_result = random.randint(1,10)
    if arg == "d12":
        dice_result = random.randint(1,12)
    if arg == "d20":
        dice_result = random.randint(1,20)
    await ctx.send(dice_result)
    return

#COMMAND: find, will send the first image found by keyword or phrase
@client.command()
async def find(ctx, *, arg): #not yet implemented
    print(f'searching by keyword/keyphrase: {arg}')
    return

#COG EXTENSION management
#COMMAND: reload, will reload extension
@client.command()
async def reload(ctx):
    """Reloads cog: world"""
    client.reload_extension('world')
#loads COG EXTENSION
client.load_extension('world')

#RUN: run client
client.run(TOKEN)