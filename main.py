from dotenv import load_dotenv
import utils.enviroment as enviroment
import discord
import os


env =  enviroment.EnvVars()
client = discord.Client()


@client.event
async def on_ready():
    print("I'm.. \n Alive {0.user}".format(client))

    

@client.event
async def on_reaction_add(reaction,user):
    print("TESTING")
    channel = reaction.message.channel
    await channel.send("REACTION ADDED")

    def check(m):
        return m.content == 'hello' and m.channel == channel

    msg = await client.wait_for('message', check=check)
    await channel.send('Hello {.author}!'.format(msg))
    
@client.event
async def on_message(message):
    if message.content.startswith('>hi'):
        channel = message.channel
        await channel.send("hi")

        def check(m):
            return m.content == 'hello' and m.channel == channel
        msg = await client.wait_for('message', check=check)
        await channel.send('Hello {.author}!'.format(msg))


    if message.content.startswith('>img'):
        channel = message.channel
        
        await channel.send("https://via.placeholder.com/150")


        msg = await client.wait_for('message', check=check)
        await channel.send('Hello {.author}!'.format(msg))


client.run(env.TOKEN)