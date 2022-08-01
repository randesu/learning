
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
async def gf(ctx):# *, message
    data=pd.read_csv('gff.csv', delimiter=';', index_col=False)
    dd = ctx.message.content.replace('!gf ','').upper()
    doll = data[data['name'].str.contains(dd)]
    intro1=[
    doll.intro.to_string()[2:] +'\n',
    doll.timer.to_string()[2:] +'\n',
    doll.hp.to_string()[2:] +'\n',
    doll.ammo.to_string()[2:] +'\n',
    doll.ration.to_string()[2:] +'\n'
    ]

    data1=[
    doll.damage.to_string()[2:]+'\n',
    doll.accuracy.to_string()[2:]+'\n',
    doll.move.to_string()[2:]+'\n',
    doll.critrate.to_string()[2:]+'\n',
    doll.critdam.to_string()[2:]+'\n',
    doll.armorpen.to_string()[2:]+'\n',
    doll.evasion.to_string()[2:]+'\n',
    doll.rof.to_string()[2:]+'\n',
    doll.armor.to_string()[2:]+'\n',
    ]

    tilebuff=[
    doll.tile1.to_string()[2:]+'\n',
    doll.tile2.to_string()[2:]+'\n',
    ]

    tilepng1=(doll.shorttile.to_string()[3:])


    embed = discord.Embed(title=doll.name.to_string()[2:], description="".join(intro1),color=0xffff4d)
    embed.set_thumbnail(url="".join(tilepng1))
    embed.add_field(name="Combat Data: ",value="".join(data1), inline=False)
    embed.add_field(name="Tiles buff", value="".join(tilebuff),inline=False)
    embed.add_field(name=doll.skillname.to_string()[2:], value="".join(doll.skillbuff),inline=False)
    print(doll.tilepng)
    embed.set_image(url=doll.image.to_string()[2:])

    await ctx.send(embed=embed)

bot.run(TOKEN)