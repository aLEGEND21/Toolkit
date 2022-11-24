import discord
import os
from discord.ext import commands

class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix=('rt '), intents=intents)
        
    async def setup_hook(self):
        # Load cogs
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                await self.load_extension(f'cogs.{filename[:-3]}')

bot = Bot()
bot.run("Nzg4MTM0NjI2MTc0MTczMjA1.GxFx6e.IUmaxHkxEbYcv0jztDtJPr5bEN2DAKfbtajkq4") # Replace with your token