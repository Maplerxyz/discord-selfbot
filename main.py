import discord
from discord.ext import commands
import random
from discord import Permissions
from colorama import Fore, Style
import asyncio
import schedule 
from discord.ext.commands import has_permissions
from colorama import Fore as Color
import os
from dotenv import load_dotenv
from datetime import datetime
from time import time
import discord, datetime, time

intents = discord.Intents.all()
intents.members = True

# Thank you for using my selfbot, good sir! I really hope you don't skid this. UwU

token = ""
prefix = ">"
channel_name = "UWU-MAPLER-ON-TOP"
ban_reason = "Maplerxyz's Selfbot Was Here"
role_name = "Maplerxyz's Selfbot Was Here"

maplerxyz = commands.Bot(command_prefix=prefix,
                    case_sensitive=False,
                    self_bot=True,
                    intents=intents)
maplerxyz.remove_command("help")


@maplerxyz.event
async def on_ready():
    print(f''' {Color.RED} Logged in as {maplerxyz.user}
             {Color.RED} Made by Mapler#4986
             {Color.RED} 不和への愛を込めて作られた
             {Color.RED} SB Status : Online
             {Color.RED} Prefix = {prefix}
             {Color.RED} Version : V1 



                          
 ███▄ ▄███▓ ▄▄▄       ██▓███   ██▓    ▓█████  ██▀███     
▓██▒▀█▀ ██▒▒████▄    ▓██░  ██▒▓██▒    ▓█   ▀ ▓██ ▒ ██▒   
▓██    ▓██░▒██  ▀█▄  ▓██░ ██▓▒▒██░    ▒███   ▓██ ░▄█ ▒   
▒██    ▒██ ░██▄▄▄▄██ ▒██▄█▓▒ ▒▒██░    ▒▓█  ▄ ▒██▀▀█▄     
▒██▒   ░██▒ ▓█   ▓██▒▒██▒ ░  ░░██████▒░▒████▒░██▓ ▒██▒   
░ ▒░   ░  ░ ▒▒   ▓▒█░▒▓▒░ ░  ░░ ▒░▓  ░░░ ▒░ ░░ ▒▓ ░▒▓░   
░  ░      ░  ▒   ▒▒ ░░▒ ░     ░ ░ ▒  ░ ░ ░  ░  ░▒ ░ ▒░   
░      ░     ░   ▒   ░░         ░ ░      ░     ░░   ░    
       ░         ░  ░             ░  ░   ░  ░   ░        
                                                         
  ██████ ▓█████  ██▓      █████▒▄▄▄▄    ▒█████  ▄▄▄█████▓
▒██    ▒ ▓█   ▀ ▓██▒    ▓██   ▒▓█████▄ ▒██▒  ██▒▓  ██▒ ▓▒
░ ▓██▄   ▒███   ▒██░    ▒████ ░▒██▒ ▄██▒██░  ██▒▒ ▓██░ ▒░
  ▒   ██▒▒▓█  ▄ ▒██░    ░▓█▒  ░▒██░█▀  ▒██   ██░░ ▓██▓ ░ 
▒██████▒▒░▒████▒░██████▒░▒█░   ░▓█  ▀█▓░ ████▓▒░  ▒██▒ ░ 
▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒░▓  ░ ▒ ░   ░▒▓███▀▒░ ▒░▒░▒░   ▒ ░░   
░ ░▒  ░ ░ ░ ░  ░░ ░ ▒  ░ ░     ▒░▒   ░   ░ ▒ ▒░     ░    
░  ░  ░     ░     ░ ░    ░ ░    ░    ░ ░ ░ ░ ▒    ░      
      ░     ░  ░    ░  ░        ░          ░ ░           
                                     ░                   
░'''
          )


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
    await ctx.send(embed=embed)


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


@maplerxyz.command()
async def ping(ctx):
    embed = discord.Embed(
        title="Ping",
        description=f"Maplerxyz's Selfbot by Mapler#4986: {round(maplerxyz.latency * 1000)}ms",
        colour=discord.Colour.dark_purple())
    await ctx.send(embed=embed)


@maplerxyz.command()
async def coinflip(ctx):
    await ctx.message.delete()
    choices = ["heads", "Tails"]
    rancoin = random.choice(choices)
    await ctx.send(rancoin)

@maplerxyz.command()
async def bump(ctx):
        await ctx.send("!d bump")
        schedule.every(2).hours.do(bump)

@maplerxyz.command()
async def gcleave(ctx):
    for gc in maplerxyz.private_channels:
        if isinstance(gc, discord.GroupChannel):
            try:
                await gc.leave()
                print(f'Successfull: {gc.name}')
            except:
                print(f'Failed: {gc.name}')
    print(f"You have finished leaving!")

@maplerxyz.command()
async def dm(ctx):
    for user in maplerxyz.user.friends:
        try:
            await user.send(
                '')
            print(f"{Fore.GREEN}Sent message to {Fore.RED}{user.name}")
        except:
            print(f"couldnt message: {user.friends}")

maplerxyz.run(token, bot=False)