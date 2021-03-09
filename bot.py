import discord
from discord.ext import commands
from discord.ext.commands import Bot
import json
import os 
import random
import requests









    

#bot prefix
bot = commands.Bot(command_prefix = 'l!', case_insensitive=True)
bot.remove_command('help')




extentions = [
'ping',
]

print('loading')





@bot.event
async def on_ready():
    os.system('cls' if os.name == 'nt' else 'clear')
    await bot.change_presence(activity=discord.Game(name='Literally datamining you.',type=1))
    print("  ")
    print(" ")
    print("                                        Ready to datamine!")

@bot.command(pass_context=True)
async def cls(ctx):
    if ctx.message.author.id == 204721061411946496:
        await ctx.send(":ballot_box_with_check: **Console cleared!**")
        os.system('cls' if os.name == 'nt' else 'clear')
        print(" ")
        print("                                                     Console Cleared")




@bot.command(hidden=True, pass_context=True)
async def load(ctx, extension):
    """Loads a module."""
    if ctx.message.author.id == 204721061411946496:
        try:
            bot.load_extension(extension)

            colors = [0xff0000, 0xff8100, 0xfdff00, 0x15ff00, 0x15ff00, 0x0045ff, 0x9600ff, 0xff00b4]

            embed = discord.Embed(name='Loaded', color=random.choice(colors))
            embed.add_field(name='Loaded', value='Loaded {}'.format(extension))
            await ctx.send(embed=embed)
        except Exception as error:
            print("{} Can't be loaded. [{}]".format(extension, error))

@bot.command(hidden=True, pass_context=True)
async def unload(ctx, extension):
    """Unloads a module."""
    if ctx.message.author.id == 204721061411946496:
        try:
            bot.unload_extension(extension)

            colors = [0xff0000, 0xff8100, 0xfdff00, 0x15ff00, 0x15ff00, 0x0045ff, 0x9600ff, 0xff00b4]

            embed = discord.Embed(name='Unloaded', color=random.choice(colors))
            embed.add_field(name='Unloaded', value='Unloaded {}'.format(extension))
            await ctx.send(embed=embed)
        except Exception as error:
            print("{} Can't be unloaded. [{}]".format(extension, error))

@bot.command(hidden=True, pass_context=True)
async def reload(ctx, extension):
    """Reloads a module."""
    if ctx.message.author.id == 204721061411946496:
        try:

            bot.unload_extension(extention)
            bot.load_extension(extension)

            colors = [0xff0000, 0xff8100, 0xfdff00, 0x15ff00, 0x15ff00, 0x0045ff, 0x9600ff, 0xff00b4]

            embed = discord.Embed(name='Reloaded', color=random.choice(colors))
            embed.add_field(name='Reloaded', value='Reloaded {}'.format(extension))
            await ctx.send(embed=embed)
        except Exception as error:
            print("{} Can't be reloaded. [{}]".format(extension, error))





if __name__ == "__main__":
    for extention in extentions:
        try:
            bot.load_extension(extention)
        except Exception as error:
            print("{} couldn't be loaded! [{}]".format(extention, error))






    @bot.event
    async def on_message(message):
        channelID = 699746057411624972  #Replace this if you want to use this in a different channel. 
        if message.channel.id == channelID:
            currentMsg = [message.content]
            currentMsg = currentMsg[0].split()
            with open("messages.json") as data:
                Jdata = json.load(data)
            for x in currentMsg:
                Jdata["messages"].append(x)
            with open("messages.json", "w") as f:
                f.write(json.dumps(Jdata, indent=4, sort_keys=True))
            await bot.process_commands(message)
        else:
            await bot.process_commands(message)





    @bot.command()
    async def check(ctx):
            with open("messages.json") as data:
                Jdata = json.load(data)
            i = 0
            while i != len(Jdata["messages"]):
                i = i+1
            await ctx.send("Currently " + str(i) + " individual words logged.")



















bot.run('TOKEN')