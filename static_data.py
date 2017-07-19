import asyncio
from discord import Embed
from discord.ext import commands


class Help:
    """Commands that return helpful information."""

    def __init__(self, bot):
        self.bot = bot
        bot.remove_command("help")

    @commands.group()
    async def help(self, ctx):
        if ctx.invoked_subcommand is None:
            embed=Embed(colour=0x00ff00)
            embed.set_author(name="Blitzcrank Bot - Commands:", icon_url=self.bot.user.avatar_url)
            embed.add_field(name="b!search 'User'", value="Show a user's ranked statistics", inline=True)
            embed.add_field(name="Example:", value="b!search Riviere", inline=True)
            embed.add_field(name="b!mastery 'User' 'Champ'", value="Shows a user's champ mastery", inline=True)
            embed.add_field(name="Example:", value="b!mastery Riviere Sivir", inline=True)
            embed.add_field(name="b!region view", value="Show the default region", inline=False)
            embed.add_field(name="b!region set 'region'", value="Set the server's default region", inline=True)
            embed.add_field(name="Example:", value="b!region set OCE", inline=True)
            embed.add_field(name="b!region update 'region'", value="Update server's default region", inline=True)
            embed.add_field(name="Example:", value="b!region update NA", inline=True)
            embed.add_field(name="b!region remove", value="Removes server's default region", inline=True)
            embed.add_field(name="b!regions", value="Show a list of all valid regions", inline=False)
            embed.add_field(name="Other commands:", value="Other commands can be listed with b!help more", inline=True)
            await ctx.send("", embed=embed)
    
    @help.command()
    async def more(self, ctx):
        await ctx.send("Coming later! Don't worry, all the important commands are already listed!")

    @commands.command(no_pm=True)
    async def regions(self, ctx):
        """Lists valid regions"""
        msg = "BR, EUNE, EUW, JP, KR, LAN, LAS, NA, OCE, RU, TR"
        await ctx.send("```fix\n" + msg + "\n```")

    @commands.command(no_pm=True)
    async def invite(self, ctx):
        """Add Blitzcrank to your server with this link!"""
        link = "https://discordapp.com/oauth2/authorize?client_id=282765243862614016&scope=bot&permissions=19456"
        await ctx.send("Invite me to your server with this link!\n" + link)

    @commands.command(no_pm=True)
    async def support(self, ctx):
        """Join the support server to ask for help!"""
        link = "https://discord.gg/J78uAgZ"
        await ctx.send("Join my support server if you need help with commands!\n " + link)


def setup(bot):
    """Adds cog to bot"""
    bot.add_cog(Help(bot))

# Base finished
