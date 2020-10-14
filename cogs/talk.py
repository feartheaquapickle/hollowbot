import discord
import os
import requests
import re
from discord.ext import commands

class talk(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Talk Panel is online.')

# Will listen for "heck". If found, will generate response.
    @commands.Cog.listener()
    async def on_message(self, message):
        if re.search(r'\bheck\b', message.content.lower()):
            response = "Hey, watch your fucking languge."
            await message.channel.send(f'```{(response)}```')
            print('--heck detected.')

            return

# Completes ping command.
    @commands.command(brief=" | Use to check your ping rate.")
    async def ping(self, ctx):
        await ctx.send(f'```pong! That took {round(self.bot.latency * 10000)}ms!```')

# Checks status of the server.

    @commands.command()
    async def s(self, ctx):
        try:
            r = requests.get('http://76.91.84.75:30120', timeout=1)
            if r.ok:
                print('Hollowlake is online.')

            embed=discord.Embed(title="Server is online.", color=0x00f900)
            embed.set_author(name="Hollowlake", icon_url="https://i.imgur.com/8l0UOzc.png")
            await ctx.message.delete()
            await ctx.send(embed=embed)

        except Exception:
            pass
            print('Hollowlake is offline.')

            embed=discord.Embed(title="Server is offline.", color=0x000000)
            embed.set_author(name="Hollowlake", icon_url="https://i.imgur.com/8l0UOzc.png")
            await ctx.message.delete()
            await ctx.send(embed=embed)

# Standard help menu for users.
    @commands.command(pass_context=True)
    async def help(self, ctx):
        author = ctx.message.author

        embed = discord.Embed(colour = discord.Colour.gold())
        embed.set_author(name='Help Menu')
        embed.add_field(name='.ping', value='Test your ping rate.', inline=False)
        embed.add_field(name='.s', value='Checks status of the Hollowlake FivePD server.', inline=False)
        embed.add_field(name='.c', value='Will generate a random callsign formatted NL-NN.', inline=False)
        embed.add_field(name='.f', value='Generates a random quote from Futurama.', inline=False)
        embed.add_field(name='.fp', value='Generates a random quote from Professor Farnsworth.', inline=False)
        embed.add_field(name='.fb', value='Generates a random quote from Bender Rodriquez.', inline=False)
        embed.add_field(name='.fz', value='Generates a random quote from Zapp Brannigan', inline=False)
        embed.add_field(name='.ff', value='Generates a random quote from Philip J. Fry', inline=False)

        await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(talk(bot))
