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
import random
import datetime

intents = discord.Intents.all()
intents.members = True

maplerxyz = commands.Bot(command_prefix=prefix,
                    case_sensitive=False,
                    self_bot=True,
                    intents=intents)

@maplerxyz.command()
async def coinflip(ctx):
    await ctx.message.delete()
    choices = ["heads", "Tails"]
    rancoin = random.choice(choices)
    await ctx.send(rancoin)

    
    def setup(bot):
    bot.add_cog(System(bot))