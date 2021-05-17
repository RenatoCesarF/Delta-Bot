#Base Structure of a command
import discord
from discord.ext import commands
from help import help

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.remove_command('help')
        print("Commands initialized")


def setup(bot):
    bot.add_cog(Commands(bot))
'''

     
    if command.startswith('help'):
        await help(message)

    if command.startswith('hi'):
        channel = message.channel
        thisMessage = await channel.send("hi")

    if command.startswith('meme'):
        await meme(message,params)

    if command.startswith('whatsup') or command.startswith('>WHATSUP'):
        await whatsUp(message)

'''