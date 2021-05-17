import discord
from discord.ext import commands

class HelpCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.remove_command('help')

    @commands.command(name="help")
    async def _help(self, ctx):
        embed=discord.Embed(title="Commands", url="https://realdrewdata.medium.com/", description="Some help commands to show all we have", color=0x69386d)
        embed.add_field(name="🔀 Random", value="`>help random`", inline=True)
        embed.add_field(name="🐸 Meme", value="`>help meme`", inline=True)
        embed.set_footer(text="footer")
        await ctx.send(embed=embed)

        #  Commands


def setup(bot):
    bot.add_cog(HelpCommand(bot))
