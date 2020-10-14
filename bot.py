#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.8
import discord
import os
import json
from discord.ext import commands

# Config file - Will create a config file if one is not already present.
# Config file contains Discord Bot Token and Prefix (V1)
if os.path.exists(os.getcwd() + "/config.json"):
    with open("./config.json") as f:
        configData = json.load(f)
else:
    configTemplate = {"Token":"", "Prefix": "!"}

    with open(os.getcwd() + "/config.json", "w+") as f:
        json.dump(configTemplate, f)

# Pulls data from Config file for use
token = configData["Token"]
prefix = configData["Prefix"]

bot = commands.Bot(command_prefix=prefix)
bot.remove_command('help')

# On Launch, bot will load the JSON Config file.
@bot.event
async def on_ready():
    with open('config.json') as config_file:
        data = json.load(config_file)

    print ("Bot main core is ready.")

# Series of commands to control the Cogs
# l - Load, u - Unload, r - Reload
@bot.command()
@commands.has_role('Administrator')
async def l(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    print("Load complete.")

@bot.command()
@commands.has_role('Administrator')
async def r(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')
    print("Reload complete.")

@bot.command()
@commands.has_role('Administrator')
async def u(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    print("Unload complete.")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')


bot.run(token)
