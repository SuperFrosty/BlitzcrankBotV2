import time
import logging
from discord.ext import commands
from datetime import timedelta
log = logging.getLogger()
startTime = time.localtime()
ownerID = '66141201631285248'
class Utilities:
    """ Commands relating to the Blitzcrank Bot's operations."""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(no_pm=True)
    async def ping(self, ctx):
        """Tests response time."""
        pingStart = time.time()
        msg = await ctx.send('Pong!')
        pingEnd = time.time()
        pingDiff = pingEnd - pingStart
        response = 'Pong! completed in {}s.'.format(pingDiff)
        print(response)
        await msg.edit(content=response)

    @commands.command(no_pm=True)
    async def uptime(self, ctx):
        """Return's Blitzcrank Bot's uptime."""
        compareTime = time.localtime()
        elapsedTime = time.mktime(compareTime) - time.mktime(startTime)
        response = "Running for {}".format(timedelta(seconds=elapsedTime))
        await ctx.send(response)

    @commands.command(no_pm=True)
    async def shutdown(self, ctx):
        if ctx.author.id == ownerID:
            await self.bot.logout()
        else:
            await ctx.send("Sorry, you don't have permission to use that command!")

    @commands.command(pass_context=True, no_pm=True)
    async def info(self, ctx):
        info = ("A simple bot in it's first iteration for League of Legends "
                "summoner look ups. Written using discord.py by "
                "Frosty ☃#5263.")
        await ctx.send(ctx.message.channel, info)
def setup(bot):
    bot.add_cog(Utilities(bot))

#TODO: fix ping command not editing.
#Fix on_command errors