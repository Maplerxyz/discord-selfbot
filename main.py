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

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        maplerxyz.load_extension(f"cogs.{filename[:-3]}")
  

maplerxyz.run(token, bot=False)