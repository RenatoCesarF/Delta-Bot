

async def meme(message,arguments):
    channel = message.channel
    messageLenght = len(message.content)
    firstPart = message.content[0]
    secondPart = message.content[2]

    print(messageLenght)
    print(firstPart)
    print(secondPart)
    
    thisMessage = await channel.send("https://via.placeholder.com/150")

    await thisMessage.add_reaction('👍')
    await thisMessage.add_reaction('👎')