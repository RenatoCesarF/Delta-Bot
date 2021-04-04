from dotenv import load_dotenv
import utils.enviroment as enviroment
from commandHandler import commandHandler
import discord
import os


env =  enviroment.EnvVars()
client = discord.Client()


@client.event
async def on_ready():
    print("It is Alive!!! 🤖 {0.user}".format(client))

@client.event
async def on_reaction_add(reaction,user):
    channel = reaction.message.channel
    
    #828078138277888000 is the bot ID
    if user.id != 828078138277888000 and reaction.message.author.name == client.user.name:
        if reaction.emoji == "👍":
            await channel.send("Thanks for your feedback")

        if reaction.emoji == "👎":
            await channel.send("Ok.. I will try to improve")
    
@client.event
async def on_message(message):
    await commandHandler(message)


client.run(env.TOKEN)