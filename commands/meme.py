

async def meme(message,arguments):
    channel = message.channel

    #use the arguments to make the memes

    thisMessage = await channel.send("https://via.placeholder.com/150")

    await thisMessage.add_reaction('👍')
    await thisMessage.add_reaction('👎')