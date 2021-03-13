import discord
from discord.ext import commands

class World(commands.Cog):
    def __init__(self, client):
        self.client=client

    @commands.command()
    async def world(self, ctx):
        await ctx.send('potato')

def setup(client):
    client.add_cog(World(client))