import discord
from discord.ext import commands

class HelpCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.remove_command('help')

    @commands.command(name="help")
    async def _help(self, ctx):
        await ctx.send( """ >>> 
                ** Comands **
          
                    `hi` Say Hi!  `whatsup` Say !
          
        """)

def setup(bot):
    bot.add_cog(HelpCommand(bot))
