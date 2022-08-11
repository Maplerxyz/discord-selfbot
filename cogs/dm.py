import discord
from discord.ext import commands
from discord import Permissions
from discord.ext.commands import has_permissions
import os
from dotenv import load_dotenv
import discord, datetime, time, prefix
import colorama 
from colorama import Fore, Back, Style
import datetime
import datetime

intents = discord.Intents.all()
intents.members = True

maplerxyz = commands.Bot(command_prefix=prefix,
                    case_sensitive=False,
                    self_bot=True,
                    intents=intents)


@maplerxyz.command()
async def dm(ctx):
    for user in maplerxyz.user.friends:
        try:
            await user.send(
                '')
            print(f"{Fore.GREEN}Sent message to {Fore.RED}{user.name}")
        except:
            print(f"couldnt message: {user.friends}")

    
    def setup(bot):
    bot.add_cog(System(bot))