import discord
import os
from discord.ext import commands

class rules(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Rules loaded.')

    @commands.command(pass_context=True)
    @commands.has_role('Administrator')
    async def rules(self, ctx):
        await ctx.message.delete()

        author = ctx.message.author

        embed=discord.Embed(title="The Complete Guide to Hollowlake!", description="Includes rules, roles, and control.", color=0xfd3f58)
        embed.set_author(name="Hollowlake: FivePD Server", icon_url="https://i.imgur.com/8l0UOzc.png")
        embed.add_field(name="===========================================================\nGeneral Information", value="**===========================================================**", inline=False)
        embed.add_field(name="Hours", value="Currently the server is not 24/7. The hours are random at the moment due to the development process and IRL requirements.", inline=False)
        embed.add_field(name="Staff", value="Makubex is the owner of the server and maintains everything. At present time there are no other staff nembers. Incidents that require staff intervention may take time.", inline=False)
        embed.add_field(name="===========================================================\nRules & Conduct", value="**===========================================================**", inline=False)
        embed.add_field(name="Use Common Sense", value="Self explanatory.", inline=False)
        embed.add_field(name="Harassament & Bullying", value="This will not be tolerated in any context. Any racist, sexist or derogetory remarks will be enforced with a zero tolerance policy.", inline=False)
        embed.add_field(name="No Spam", value="Spam includes posting the same thing repeatedly as well as random gifs/images without any context.", inline=False)
        embed.add_field(name="Advertising", value="Keep advertising in the advertising channel and there won't be an issue.", inline=False)
        embed.add_field(name="Discord Guidelines", value="We follow all Discord Community Guidelines. Don't get caught up.", inline=False)
        embed.add_field(name="===========================================================\nRoleplay Guidlines", value="**===========================================================**", inline=False)
        embed.add_field(name="No Meta-roleplay", value="Your character is not God and will not know things going on miles away. Use common sense when roleplaying to stay in character.", inline=False)
        embed.add_field(name="RDM/VDM", value="No random killing of any kind, NPC or Player. FivePD is the main source of play, so use it as it is intended. Callouts will be updated and rotated to keep things from getting stale.", inline=False)
        embed.add_field(name="Be realistic", value="An emergency responder is not going to drive 200mph through a neighborhood while responding. Do things that make sense. If there is an issue, you can requests staff assistance at your postal code.", inline=False)
        embed.add_field(name="Minimized Arguing", value="This is a game, it's not super important. If there is an argument that can't be settled, take a break. Staff will kick/ban those who cannot follow guidelines.", inline=False)
        embed.add_field(name="Stay Mature.", value="It's impossible to know the age of everyone on the server. Keep the conversations appropriate and keep NSFW topics out. Understand at any given time, there could be minors in the server.", inline=False)
        embed.add_field(name="General Roleplay", value="This server is only a casual roleplay community. Out-Of-Character (OOC) conversations are not regulated and can happen at any time. If the server takes a more serious base, that can change.", inline=True)
        embed.add_field(name="===========================================================\nRoles & Positions", value="**===========================================================**", inline=False)
        embed.add_field(name="Los Santos Police Department", value="The LSPD has jurisdiction is the city itself, the port, as well as the suburbs along the county line. They are commonly seen on mutual-aid calls with county.", inline=False)
        embed.add_field(name="Tri-County Sheriff's Office", value="The TCSO has jurisdiction over the whole of San Andreas as they are a condensed office of all three Sheriff departments. Their main focus is in the country but can be found on patrol in the city.", inline=False)
        embed.add_field(name="San Andreas State Troopers", value="The main focus of the SAST is the highways and unpatrolled roads in the mountains but their jurisdiction is over the whole of San Andreas.", inline=False)
        embed.add_field(name="San Andreas Fire", value="Law Enforcement not your style? Respond to calls for service as a firefighter! Currently this role is pretty limited to responding to traffic accidents but could evolve in the future.", inline=False)
        embed.add_field(name="Civilian", value="Your average citizen. Not sure if you really want to do LE work? Citizen is for you! Play the game as a standard person, you can even interact with the officers!", inline=False)

        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    @commands.has_role('Administrator')
    async def cad(self, ctx):
        await ctx.message.delete()

        author = ctx.message.author

        embed=discord.Embed(title="Computer Aided Dispatch (CAD)", description="How to use the CAD", color=0xfd3f58)
        embed.set_author(name="San Andreas Crime Records Management System", icon_url="https://i.imgur.com/8l0UOzc.png")
        embed.set_thumbnail(url="https://i.imgur.com/P1zjWjZ.png")
        embed.add_field(name="Logging In", value="When you go on duty and open the CAD, you'll see there is only one department, called the San Andreas Crime Records Management System. "
        "\n\nFor the time being, there is only one department as it makes it easier for people to play different departments without needing to leave and rejoin. This also makes things more efficient as the server is still small. If demand for it increases in the future, dedicated departments may be registered.", inline=False)
        embed.add_field(name="Call-Signs", value="There is no requirement on callsigns. For the time being, you can pick your call sign. The format is NL-NN (1A-11). \n\n When you registered with the CAD, it will auto generate a Call-Sign for you. If you don't like this Call-Sign, you are free to change it. There is also a generator built into botski (.callsign) that will generate a random one as well.", inline=False)
        embed.add_field(name="Ranks", value="Inside the CAD there is a section for Rank. Normally this would make sense with a standard department structure, however with how we're using it - it does not make sense. Instead, there will be one of three inputs: State, County, or City. \n\n SAST is State, Sheriff is 'County', and LSPD is 'City'. ", inline=False)
        embed.add_field(name="Use", value="The rest of the CAD is self explanatory. Use the buttons on the left side of the cosole to view their contents. When a callout is done, you can write a 'report' and submit it. That report (or citation) should show in the database records for future reference. \n\n This is the only CAD we use as FivePD is the main source of play. If roleplaying with Civilians is ever in demand, a proper CAD may be purchased with dontations from the server.", inline=False)
        embed.add_field(name="Dispatch bot", value="The dispatch bot is provided by the FivePD bot. In their respective channels you'll see callouts, on-duty and off-duty logs, and when reports are submitted.", inline=False)

        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    @commands.has_role('Administrator')
    async def role(self, ctx):
        await ctx.message.delete()

        author = ctx.message.author

        embed=discord.Embed(title="Roles & Positions", description="Pick your poison!", color=0xfd3f58)
        embed.set_author(name="Hollowlake Job Center", icon_url="https://i.imgur.com/8l0UOzc.png")
        embed.add_field(name="Los Santos Police Department", value="The LSPD has jurisdiction is the city itself, the port, as well as the suburbs along the county line. They are commonly seen on mutual-aid calls with county.", inline=False)
        embed.add_field(name="Tri-County Sheriff's Office", value="The TCSO has jurisdiction over the whole of San Andreas as they are a condensed office of all three Sheriff departments. Their main focus is in the country but can be found on patrol in the city.", inline=False)
        embed.add_field(name="San Andreas State Troopers", value="The main focus of the SAST is the highways and unpatrolled roads in the mountains but their jurisdiction is over the whole of San Andreas.", inline=False)
        embed.add_field(name="LEO", value="Don't know what department you want yet? No worries. LEO is a temporary catch-all for those who want to try everything before settling in.", inline=False)
        embed.add_field(name="San Andreas Fire & EMS", value="Law Enforcement not your style? Respond to calls for service as a firefighter! Currently this role is pretty limited to responding to traffic accidents but could evolve in the future.", inline=False)
        embed.add_field(name="Civilian", value="Your average citizen. Not sure if you really want to do LE work? Citizen is for you! Play the game as a standard person, you can even interact with the officers!", inline=False)
        embed.add_field(name="Claim Your Role!", value=" So, what will it be? Reply below and a staff member will assign you a role!", inline=False)

        await ctx.send(embed=embed)


    @commands.command(pass_context=True)
    @commands.has_role('Administrator')
    async def role2(self, ctx):
        await ctx.message.delete()

        author = ctx.message.author

        embed=discord.Embed(title="Discord Roles!", description="", color=0xfd3f58)
        embed.add_field(name="[🔴] Developer", value="Make stuff? Developer is for you.", inline=False)
        embed.add_field(name="[🟠] Friend", value="Just here to chill? This is yours!", inline=False)
        embed.add_field(name="[⚫] FivePD", value="Play on my FivePD Server? Pick this one!", inline=False)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(rules(bot))
