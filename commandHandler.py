import discord

from commands.whatsup import whatsUp
from commands.meme import meme
from commands.help import help

async def commandHandler(message):
    if message.content[0] == '>':
        tokens = message.content.split(' ')
        command = tokens[0][1:]#the command is the first word starting from the second character

        arguments = tokens[1:] #the arguments are everything after the command

        if command == 'hi':
            channel = message.channel
            await channel.send("hi")
            

        elif command == 'meme':
            await meme(message,arguments)

        elif command == 'whatsup' or command == '>WHATSUP':
            await whatsUp(message)
        
        elif command == 'help':
            await help(message)