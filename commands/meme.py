import discord
from discord.ext import commands

templates = [ 'mini-keanu','sparta','buzz']



class MemeCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command(name="meme")
    async def _meme(self, ctx, template = '', *, params = ''):
        
        if template == '' or template == 'help':
            await ctx.send("You need to Add a **template** followed by some **params**, write `>help meme` to see some templates")

        if template in templates:
            link = f"https://api.memegen.link/images/{template}/{'/'.join(param.replace(' ', '_') for param in params.split(','))}.png"
            await ctx.send(link)
          


def setup(bot):
    bot.add_cog(MemeCommand(bot))
