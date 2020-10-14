import discord
import os
from discord.ext import commands

class admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Admin panel ready.')

# Clears amount of messages entered by user !clear 5 will clear 5 messages
# including the issuing command.

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount)

#kick members
    @commands.command()
    @commands.has_role('Administrator')
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)

#ban members
    @commands.command()
    @commands.has_role('Administrator')
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send (f'Banned {member.mention}')

#unban members
    @commands.command()
    @commands.has_role('Administrator')
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
                user = ban_entry.user

                if (user.name, user.discriminator) == (member_name, member_discriminator):
                    await ctx.guild.unban(user)
                    await ctx.send (f'Unbanned {user.mention}')
                    return


def setup(bot):
    bot.add_cog(admin(bot))
