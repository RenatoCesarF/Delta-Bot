from dotenv import load_dotenv
import utils.enviroment as enviroment

import locale
import time


import sys
import discord
from discord import utils
from discord.ext import commands

locale.setlocale(locale.LC_ALL, "en_US.utf8")
start_time = time.time()
env =  enviroment.EnvVars()

MODULES = [
    'commands.help',
    'commands.meme'
]

class Bot(commands.AutoShardedBot):
    def __init__(self):
        super(Bot, self).__init__(
            command_prefix=">",
            case_insensitive=True, owner_id=[owner for owner in [1234567890]],
            max_messages=5000,
            intents=discord.Intents.default())

        for module in MODULES:
            try:
                self.load_extension(module)
            except Exception as e:
                print(f'{module} not loaded.')
                print("_____________________")
                print(e)

    async def on_ready(self):
        print("\n It's  Alive!! \n")
        sys.stdout.flush()
        end_time = time.time() - start_time
        await self.change_presence(status=discord.Status.online)

  
                         
    # @commands.Cog.listener()
    # async def on_raw_reaction_add(self, event: RawReactionActionEvent):
    #     print(event)
        # channel = self.reaction.message.channel
            
        #     #828078138277888000 is the bot ID
        #     if user.id != 828078138277888000 and reaction.message.author.name == client.user.name:
        #         if reaction.emoji == "👍":
        #             await channel.send("Thanks for your feedback")

        #         if reaction.emoji == "👎":
        #             await channel.send("Ok.. I will try to improve")
            

DeltaBot = Bot()

DeltaBot.run(env.TOKEN)



