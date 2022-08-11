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
async def ping(ctx):
    embed = discord.Embed(
        title="Ping",
        description=f"Maplerxyz's Selfbot by Mapler#4986: {round(maplerxyz.latency * 1000)}ms",
        colour=discord.Colour.dark_purple())
    await ctx.send(embed=embed)

    
    def setup(bot):
    bot.add_cog(System(bot))