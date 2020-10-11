import discord
import os
from discord.ext import commands

class roles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Reaction roles loaded.')

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        message_id = payload.message_id
        if message_id == 763932938194255873:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, self.bot.guilds)

            if payload.emoji.name == '🔴':
                role = discord.utils.get(guild.roles, name = 'Developer')

            if payload.emoji.name == '🟠':
                role = discord.utils.get(guild.roles, name = 'Friend')

            elif payload.emoji.name == '⚫':
                role = discord.utils.get(guild.roles, name = 'FivePD')

            else:
                role = discord.utils.get(guild.roles, name=payload.emoji.name)

            if role is not None:
                member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)

                await member.add_roles(role)
                print ("done")

            else:
                print ("role not found")

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        message_id = payload.message_id
        if message_id == 763932938194255873:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, self.bot.guilds)

            if payload.emoji.name == '🔴':
                role = discord.utils.get(guild.roles, name = 'Developer')

            if payload.emoji.name == '🟠':
                role = discord.utils.get(guild.roles, name = 'Friend')

            elif payload.emoji.name == '⚫':
                role = discord.utils.get(guild.roles, name = 'FivePD')

            else:
                role = discord.utils.get(guild.roles, name=payload.emoji.name)

            if role is not None:
                member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)
                    print ("done")
                else:
                    print ("member not found")
            else:
                print ("role not found")

def setup(bot):
    bot.add_cog(roles(bot))
