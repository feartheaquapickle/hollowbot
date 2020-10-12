#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.8
import discord
import os
import json
from discord.ext import commands

if os.path.exists(os.getcwd() + "/config.json"):
    with open("./config.json") as f:
        configData = json.load(f)
else:
    configTemplate = {"Token":"", "Prefix": "!"}

    with open(os.getcwd() + "/config.json", "w+") as f:
        json.dump(configTemplate, f)

token = configData["Token"]
prefix = configData["Prefix"]

bot = commands.Bot(command_prefix=prefix)
bot.remove_command('help')

@bot.event
async def on_ready():
    with open('config.json') as config_file:
        data = json.load(config_file)

    print ("Bot main core is ready.")


@bot.command()
async def email(ctx):
   await ctx.invoke(bot.get_command('email_alert'))

@bot.command()
@commands.has_role('Administrator')
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    print("Load complete.")

@bot.command()
@commands.has_role('Administrator')
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')
    print("Reload complete.")

@bot.command()
@commands.has_role('Administrator')
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    print("Unload complete.")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')


bot.run(token)
