import discord
from discord.ext import commands
from utils.memeTemplates import templates


class MemeCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command(name="meme")
    async def _meme(self, ctx, template = '', *, params = ''):
        if template == '' or template == 'help':
            await ctx.send("You need to Add a **template** followed by some **params**, write `>help meme` to see some templates")

        if next(item for item in templates if item["name"] == template) in templates:
            templateLink = next(item for item in templates if item["name"] == template)['link']
            link = f"https://api.memegen.link/images/{templateLink}/{'/'.join(param.replace(' ', '_') for param in params.split(','))}.png"
            await ctx.send(link)
          


def setup(bot):
    bot.add_cog(MemeCommand(bot))
