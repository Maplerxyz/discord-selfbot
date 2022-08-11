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
async def help(ctx):
    embed = discord.Embed(title="Help Page",
                          description="Maplerxyz's Selfbot by Mapler#4986",
                          colour=discord.Colour.dark_purple())
    embed.add_field(name="Nuke",
                    value="Displays list of nuke commands",
                    inline=False)
    embed.add_field(name="Status",
                    value="Displays Status commands",
                    inline=False)
    embed.add_field(name="Fun", value="Displays fun commands", inline=False)
    embed.add_field(name="Utility",
                    value="Displays utility commands",
                    inline=True)
    embed.set_thumbnail(url=ctx.author.avatar_url)
    embed.set_footer(text=f"Requested By {ctx.author}")
    await ctx.send(embed=embed

    @maplerxyz.command()
async def wizz(ctx):
    embed = discord.Embed(title="Nuke Commands",
                          description="List of nuke commands",
                          colour=discord.Colour.dark_purple())
    embed.add_field(name="Banall",
                    value="Bans everyone in the server",
                    inline=False)
    embed.add_field(name="Kickall",
                    value="Kicks everyone in the server",
                    inline=False)
    embed.add_field(name="Createchan",
                    value="Mass Creates channels",
                    inline=False)
    embed.add_field(name="Deletechan", value="Mass deletes channels")
    embed.add_field(name="Createrole",
                    value="Spam creates Roles",
                    inline=False)
    embed.add_field(name="Deleterole",
                    value="Mass Deletes roles",
                    inline=False)
    embed.add_field(name="Spam",
                    value="Spams a message and amount given #",
                    inline=False)
    embed.add_field(name="dm",
                    value="Dms everyone on your friendslist",
                    inline=False)
    embed.set_thumbnail(url=ctx.author.avatar_url)
    embed.set_footer(text=f"Requested By {ctx.author}")
    await ctx.send(embed=embed)


@maplerxyz.command()
async def utility(ctx):
    embed = discord.Embed(title="Utility Commands",
                          description="List of Utility commands",
                          colour=discord.Colour.dark_purple())
    embed.add_field(name="snipe",
                    value="Snipes the last deleted message",
                    inline=False)
    embed.add_field(name="ping", value="Returns SB Ping", inline=False)
    embed.add_field(name="stopsb", value="Shuts down selfbot", inline=False)
    embed.add_field(name="gcleave", value="Leaves all the group chats you are in.", inline=False)
    embed.add_field(name="bump", value="Bump's disboard every 2 hours", inline=False)
    embed.set_thumbnail(url=ctx.author.avatar_url)
    embed.set_footer(text=f"Requested By {ctx.author}")
    await ctx.send(embed=embed)


@maplerxyz.command()
async def fun(ctx):
    embed = discord.Embed(title="Fun Commands",
                          description="Displays fun commands",
                          colour=discord.Colour.dark_purple())
    embed.add_field(name="coinflip", value="Flips a coin", inline=False)
    embed.set_thumbnail(url=ctx.author.avatar_url)
    embed.set_footer(text=f"Requested By {ctx.author}")
    await ctx.send(embed=embed)


@maplerxyz.command()
async def status(ctx):
    embed = discord.Embed(title="Status commands",
                          description="Displays status commands",
                          colour=discord.Colour.dark_purple())
    embed.add_field(name="stream",
                    value="Sets custom status to streaming",
                    inline=False)
    embed.add_field(name="game",
                    value="Sets custom status to playing",
                    inline=False)
    embed.set_thumbnail(url=ctx.author.avatar_url)
    embed.set_footer(text=f"Requested By {ctx.author}")
    await ctx.send(embed=embed)
    
    def setup(bot):
    bot.add_cog(System(bot))