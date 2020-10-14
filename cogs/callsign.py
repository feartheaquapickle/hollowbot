import random
import discord
import os
from discord.ext import commands

class callsign(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Callsign Generator loaded.')

# Generates a random callsign in the format of NL-NN.
# Created for use with FivePD/FiveM - may be removed later.

    @commands.command()
    async def c(self, ctx):
        await ctx.message.delete()

        if ctx.channel.id == 752980348287320185:


            N = [ '1', '2', '3', '4','5','6','7','8','9']
            L = ['A','B','C','D','E','F','G','H','I','J','K',
                     'L','M','N','O','P','Q','R','S','T','U','V',
                     'W','X','Y','Z']

            result = (f'```{random.choice(N)}{random.choice(L)}-{random.choice(N)}{random.choice(N)}```')

            await ctx.send(result)
            print ('Callsign generated')
        else:
            await ctx.send(f'```Use the #callsign-generator channel!```', delete_after=5)

def setup(bot):
    bot.add_cog(callsign(bot))
