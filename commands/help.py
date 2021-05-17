import discord
from discord.ext import commands
from utils.memeTemplates import templates

class HelpCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.remove_command('help')

    @commands.command(name="help")
    async def _help(self, ctx,param = None):
        if param is None:
            embed=discord.Embed(title="Commands", url="https://realdrewdata.medium.com/", description="Some help commands to show all we have", color=0x69386d)
            embed.add_field(name="🔀 Random", value="`>help random`", inline=True)
            embed.add_field(name="🐸 Meme", value="`>help meme`", inline=True)
            embed.set_footer(text="footer")
            await ctx.send(embed=embed)

        if param == "meme":
            embed=discord.Embed(title="🐸 Meme Templates", description="some memes receive more than one parameter, separate each one with:`,` \nlike `>meme wtfMonkey <param1>, <param2>`", color=0x69386d)

            for template in templates:
                embed.add_field( name="`{}`".format(template['name']), value="** **",inline=True)

            embed.set_footer(text="use >meme before each template")
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(HelpCommand(bot))
