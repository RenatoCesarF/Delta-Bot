import random

async def whatsUp(message):
    channel = message.channel
    
    emojis = ['👻','😜','😜','👅']
    howManyU = random.randint(0,40)
    howManySymbles = random.randint(0,20)
    howManyEmojis = random.randint(0,30)

    message = "WHATS "

    for i in range(howManyU):
        message += "U"

    message +='PPP '

    for i in range(howManySymbles):
        message +='!'

    for i in range(howManyEmojis):
        randomIndex = random.randint(0,len(emojis) - 1)
        message += emojis[randomIndex]

    thisMessage = await channel.send(message)