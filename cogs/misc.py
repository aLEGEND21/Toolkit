import discord
import random
import time
from discord.ext import commands


class Misc(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.command()
    async def ping(self, ctx):
        """ Pings the bot. """        
        t1 = time.monotonic()
        msg = await ctx.send("Pong!")
        t2 = time.monotonic()
        
        latency = round((t2-t1)*1000)
        heartbeat = round(self.bot.latency * 1000)
        
        e = discord.Embed(title="Rok Toolkit Ping")
        e.add_field(name=f"⏱️ Latency", value=f"{latency}ms")
        e.add_field(name="💓 Heartbeat", value=f"{heartbeat}ms")
        await msg.edit(content="", embed=e)

    @commands.has_role(886780809976107068)
    @commands.command(hidden=True)  
    async def fight(self, ctx, user: discord.Member):
        """ Fights a user """
        potatoes = random.randint(1, 1000)
        await ctx.send(f"{ctx.author.mention} fought {user.mention} with {potatoes} potatoes!")

    @fight.error
    async def fight_error(self, ctx, error):
        if isinstance (error, commands.MissingRole):
            return print("Missing role to run `fight` command.")
        raise error


async def setup(bot):
    await bot.add_cog(Misc(bot))