import requests
import discord
import os
import asyncio
from discord.ext import commands


class status(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


# Checks status of the Hollowlake server once every 60 seconds.
# Status is then posted in the bot's status.

# Currently disabled

#    @commands.Cog.listener()
#    async def on_ready(self):
#        await asyncio.sleep(60) #waits 60 seconds before running command.
#        try:
#            r = requests.get('http://76.91.84.75:30120', timeout=1)
#            if r.ok: #if passes, submits online message.
#
#                await self.bot.change_presence(activity=discord.Game('Server is online!'))
#
#        except Exception: #if fail, will return exception. Will post offline status.
#            pass
#
#            await self.bot.change_presence(activity=discord.Game('Server is offline!'))
#
#        await self.on_ready() #will call itself and rerun command.
#
#


def setup(bot):
    bot.add_cog(status(bot))
