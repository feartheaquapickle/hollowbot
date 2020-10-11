import discord
import os
from discord.ext import commands

class news(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('News loaded.')


# Update with news and post to channel.
    @commands.command(pass_context=True)
    @commands.has_role('Administrator')
    async def news(self, ctx):
        await ctx.message.delete()

        author = ctx.message.author

        embed=discord.Embed(title="Updates & General News", description="See below for the following updates. ", color=0x008080)
        embed.set_author(name="Announcements!")
        embed.add_field(name="Discord Open!", value="The Discord service has been renamed Hollowlake Community! Use it as a hub for game sessions, invite your friends, chill - whatever. It's open! ", inline=False)
        embed.set_footer(text="Update released September 19th, 2020. ")

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(news(bot))
