import discord

from commands.whatsup import whatsUp
from commands.meme import meme

async def commandHandler(message):
    if message.content[0] == '>':
        tokens = message.content.split(' ')
        command = tokens[0][1:]#the command is the first word starting from the second character

        arguments = tokens[1:] #the arguments are everything after the command

        if command.startswith('hi'):
            channel = message.channel
            
            thisMessage = await channel.send("hi")

        if command.startswith('meme'):
            await meme(message,arguments)

        if command.startswith('whatsup') or command.startswith('>WHATSUP'):
            await whatsUp(message)
        
