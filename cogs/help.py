import discord
from discord.ext import commands


class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.help_command = HelpCommand()
        
        
class HelpCommand(commands.DefaultHelpCommand):
    def __init__(self):
        super().__init__()
    
    def get_command_signature(self, command: commands.Command):
        cmd_sig = command.signature
        start_bracket = cmd_sig.find("[")
        end_bracket = cmd_sig.find("]")
        if start_bracket != -1 and end_bracket != -1:
            equal = cmd_sig[start_bracket:end_bracket].find("=")
            if equal != -1:
                cmd_sig = cmd_sig[:equal] + cmd_sig[end_bracket:]
        return cmd_sig
    
    async def send_command_help(self, command: commands.Command):
        await self.context.send(f"```{self.context.prefix}{command.name} {self.get_command_signature(command)}\n\n{command.short_doc}```")
        commands.MinimalHelpCommand.get_command_signature
        commands.DefaultHelpCommand.get_command_signature
        

async def setup(bot):
    await bot.add_cog(HelpCog(bot))