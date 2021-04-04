import discord
import random

async def commandHandler(message):
    if message.content == '>hi':
        channel = message.channel
        
        thisMessage = await channel.send("hi")

    if message.content.startswith('>meme'):
        channel = message.channel

        firstPart = message.content[1]
        secondPart = message.content[2]

        print(firstPart)
        print(secondPart)
        
        thisMessage = await channel.send("https://via.placeholder.com/150")

        await thisMessage.add_reaction('👍')
        await thisMessage.add_reaction('👎')



    if message.content.startswith('>whatsup') or message.content.startswith('>whats up'):
        channel = message.channel

        howManyU = random.randint(0,40)
        howManySymbles = random.randint(0,20)

        message = "WHATS "

        for i in range(howManyU):
            message += "U"


        message +='PPP '

        for i in range(howManySymbles):
            message +='!'

        message +='\n👻😜😜😜👅'

        thisMessage = await channel.send(message)

    
