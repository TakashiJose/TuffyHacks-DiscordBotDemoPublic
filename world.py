import discord
from discord.ext import commands

class World(commands.Cog):
    def __init__(self, client):
        self.client=client

    @commands.command()
    async def world(self, ctx):
        """worship the potato"""
        await ctx.send('worship the potato')

def setup(client):
    client.add_cog(World(client))