import discord
from discord.ext import commands

BASE_LINK='https://api.memegen.link/images'
templates = [ 'mini-keanu',]



class MemeCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command(name="meme")
    async def _meme(self, ctx, template, *, params):
        if template in templates:
            await ctx.send(f"{BASE_LINK}/{template}/{'/'.join(param for param in params.split(' '))}.png")


def setup(bot):
    bot.add_cog(MemeCommand(bot))
