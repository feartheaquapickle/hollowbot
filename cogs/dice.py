#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.8
import discord
import random
import os
from discord.ext import commands

class dice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Dice function loaded.')

# Simple d6 dice function

    @commands.command()
    async def roll(self,ctx):

        dice = random.randint(1,6)

        await ctx.send(f'Result: {(dice)}')

def setup(bot):
    bot.add_cog(dice(bot))
