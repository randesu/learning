
import discord
import random
from discord.ext import commands
from discord.ext.commands import Bot
import pandas as pd
import sys
from time import sleep
#from dotenv import load_dotenv

#load_dotenv()

TOKEN = 'OTExMDc4ODQzMzcxMTI2ODM2.GBFIoe.Jbu-FyYewZWoOaeO94FtBBfR4df7eMhtqYySu0'

#client = commands.Bot(command_prefix='!')
dc = discord.Client()
bot = Bot("!")
@bot.event
async def on_ready():
    print("kizuna is ready to serve you")
    




@bot.command()
async def gf(ctx, *, message):
    data = [['karan', 23], ['Rohit', 22], ['Sahil', 21], ['Aryan', 24]]
    df1 = pd.DataFrame(data, columns=['Name', 'Age'])
    
    dd = ctx.message.content.replace('!gf ','')
    doll = df1[df1['Name'].str.contains(dd)]
    
    await ctx.message.delete()
    await ctx.send(doll)

bot.run(TOKEN)