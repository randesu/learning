#from tokenize import Name
import discord
import random
from discord.ext import commands
import pandas as pd
import sys
from time import sleep
#from dotenv import load_dotenv

#load_dotenv()
TOKEN = 'OTExMDc4ODQzMzcxMTI2ODM2.GBFIoe.Jbu-FyYewZWoOaeO94FtBBfR4df7eMhtqYySu0'

client = commands.Bot(command_prefix='!')
dc = discord.Client()

data=[['Karan',23],['Rohit',22],['Sahil',21],['Aryan',24]]
df=pd.DataFrame(data,columns=['Name','Age'])
#searchTerm = input('Enter name: ')
#print(df[df['Name'].str.contains(searchTerm)])

@client.event
async def on_ready():
    print("kizuna is ready to serve you")


@client.event

async def on_message(message):
    dd=message.content
    data=[['karan',23],['Rohit',22],['Sahil',21],['Aryan',24]]
    df=pd.DataFrame(data,columns=['Name','Age'])
    searchTerm = dd
    doll = df[df['Name'].str.contains(searchTerm)]
    #print(df[df['Name'].str.contains(searchTerm)])
    await message.delete()
    await message.channel.send(doll)
    sleep(0.5)
    #await message.delete()
    #print(dd)
"""
    if message.channel.send() == True:
        sys.exit()
    await message.channel.send(dd)
    if message.author == client.user:
        return
    if message.content == message:
        data=[['karan',23],['Rohit',22],['Sahil',21],['Aryan',24]]
        df=pd.DataFrame(data,columns=['Name','Age'])
        searchTerm = input(message)
        print(df[df['Name'].str.contains(searchTerm)])
        #embed = discord.Embed(title="rena", url="https://i.pinimg.com/564x/ca/a8/33/caa833017476d1adfeaf160e4af64531.jpg", description="i love rena",color=0xffff4d)
        #embed.set_thumbnail(url='https://iopwiki.com/images/4/4b/Griffin_and_Kryuger.png')
        #embed.add_field(name="Rena",value="Selection Project", inline=False)
        #response = 'Halo, selamat pagi'
        #await message.channel.send(embed=embed)
        #await message.channel.send(response)
"""
@client.command()
async def getmsg(ctx, msgID: discord.Message):
    msg = await ctx.fetch_message(msgID)
    print(msg)

@client.command()
async def hello(ctx, *, doll):
    data=[['karan',23],['Rohit',22],['Sahil',21],['Aryan',24]]
    df=pd.DataFrame(data,columns=['Name','Age'])
    searchTerm = input(doll)
    print(df[df['Name'].str.contains(searchTerm)])
    await ctx.send("hello, i'm kizuna")
#async def on_message(message):
#    if message.content == 'halo kizuna':
#        embed = discord.Embed(title="rena", url="https://i.pinimg.com/564x/ca/a8/33/caa833017476d1adfeaf160e4af64531.jpg", description="i love rena",color=0xffff4d)
#        embed.set_thumbnail(url='https://iopwiki.com/images/4/4b/Griffin_and_Kryuger.png')
#        embed.add_field(name="Rena",value="Selection Project", inline=False)
#        await message.channel.send(embed=embed)

@client.command()
async def gfl(ctx):
    embed = discord.Embed(title="rena", url="https://i.pinimg.com/564x/ca/a8/33/caa833017476d1adfeaf160e4af64531.jpg", description="i love rena",color=0xffff4d)
    embed.set_thumbnail(url='https://iopwiki.com/images/4/4b/Griffin_and_Kryuger.png')
    embed.add_field(name="Rena",value="Selection Project", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def Bren(ctx):
    descbren2=[
    '2-star HG\n'
    'Timer: 0:28:00\n'
    'Ammo: 10(x1)/30(x5)    HP:35(x1)->70(x1)/350(x5)\n'
    'Ration: 10(x1)/30(x5)\n'
    ]
    descbren1 = [
    'Damage: 12 -> 31       Evasion: 9 -> 63\n'
    'Accuracy: 17 -> 51     RoF: 40 -> 58\n'
    'Move Speed: 15         Armor: 0\n'
    'Crit rate:20%             Crit Damage:50%\n'
    'Armor Pen.:15\n'
    ]

    skill1=[
    'Increase all allies damage by 10% for 5 seconds\n'
    'Lvl 1: 15s Cooldown, 6s Initial cooldown\n'
    'Lvl 10: 12s Cooldown, 6s Initial cooldown\n'
    ]

    bufftiles=[
    'Affect all guns\n'
    'increases damage by 8%/10%/12%/14%/16%\n'
    'increases rate of fire by 5%/6%/7%/8%/10%\n'
    ]
    embed = discord.Embed(title="Bren Ten (no.139)", description="".join(descbren2),color=0xffff4d)
    embed.set_thumbnail(url='https://raw.githubusercontent.com/randesu/gftiles/main/GFtile%2B.png')
    embed.add_field(name="Combat Data: ",value="".join(descbren1), inline=False)
    embed.add_field(name="Tiles buff", value="".join(bufftiles),inline=False)
    embed.add_field(name="Skill 1(Active)", value="".join(skill1),inline=False)
    embed.set_image(url='https://iopwiki.com/images/4/42/Bren_Ten.png')
    await ctx.send(embed=embed)

@client.command()
async def FNP9(ctx):
    desctop=[
    '2-star HG\n'
    'Timer: 0:25:00\n'
    'Ammo: 10(x1)/30(x5)    HP:30(x1)->60(x1)/300(x5)\n'
    'Ration: 10(x1)/30(x5)\n'
    ]
    descstats = [
    'Damage: 11 -> 28\n           Evasion: 11 -> 83\n'
    'Accuracy: 7 -> 53\n          RoF: 42 -> 61\n'
    'Move Speed: 15\n             Armor: 0\n'
    'Crit rate:20%\n              Crit Damage:50%\n'
    'Armor Pen.:15\n'
    ]

    skill1=[
    'Decrease the enemy squads evasion by 32%(lv.1)/40%(lv.10)\n'
    'Lvl 1: 15s Cooldown, 6s Initial cooldown\n'
    'Lvl 10: 12s Cooldown, 6s Initial cooldown\n'
    ]

    bufftiles=[
    'Affect all guns\n'
    'increases accuracy by 25%/31%/37%/43%/50%\n'
    'increases rate of fire by 10%/12%/15%/17%/20%\n'
    ]
    embed = discord.Embed(title="FNP-9 (No. 90)", description="".join(desctop),color=0xffff4d)
    embed.set_thumbnail(url='https://raw.githubusercontent.com/randesu/gftiles/main/GFtileDfront.png')
    embed.add_field(name="Combat Data: ",value="".join(descstats), inline=False)
    embed.add_field(name="Tiles buff", value="".join(bufftiles),inline=False)
    embed.add_field(name="Skill 1: Cover Suppression", value="".join(skill1),inline=False)
    embed.set_image(url='https://iopwiki.com/images/a/ad/FNP-9.png')
    await ctx.send(embed=embed)

@client.command()
async def M1911(ctx):
    desctop=[
    '2-star HG\n'
    'Timer: 0:20:00\n'
    'Ammo: 10(x1)/30(x5)\n    HP:37(x1)->73(x1)/365(x5)\n'
    'Ration: 10(x1)/30(x5)\n'
    ]
    descstats = [
    'Damage: 10 -> 27\n           Evasion: 9 -> 74\n'
    'Accuracy: 6 -> 50\n          RoF: 38 -> 57\n'
    'Move Speed: 15\n             Armor: 0\n'
    'Crit rate:20%\n              Crit Damage:50%\n'
    'Armor Pen.:15\n'
    ]

    skill1=[
    'Throw a smoke grenade which decreases the enemy rate of fire by 20%(lv.1)/36%(lv.10) and movement speed by 28(lv.1)/45(lv.10) within a radius of 2.5 unit for 4 seconds\n'
    'Lvl 1: 15s Cooldown, 1s Initial cooldown\n'
    'Lvl 10: 12s Cooldown, 1s Initial cooldown\n'
    ]

    bufftiles=[
    'Affect all guns\n'
    'increases accuracy by 25%/31%/37%/43%/40%\n'
    'increases rate of fire by 10%/12%/15%/17%/20%\n'
    ]
    embed = discord.Embed(title="M1911 (No. 2)", description="".join(desctop),color=0xffff4d)
    embed.set_thumbnail(url='https://raw.githubusercontent.com/randesu/gftiles/main/GFtile%2B.png')
    embed.add_field(name="Combat Data: ",value="".join(descstats), inline=False)
    embed.add_field(name="Tiles buff", value="".join(bufftiles),inline=False)
    embed.add_field(name="Skill 1: Cover Suppression", value="".join(skill1),inline=False)
    embed.set_image(url='https://iopwiki.com/images/b/b2/M1911.png')
    await ctx.send(embed=embed)

@client.command()
async def MP446(ctx):
    desctop=[
    '2-star HG\n'
    'Timer: 0:25:00\n'
    'Ammo: 10(x1)/30(x5)\n    HP:33(x1)->66(x1)/330(x5)\n'
    'Ration: 10(x1)/30(x5)\n'
    ]
    descstats = [
    'Damage: 11 -> 30\n           Evasion: 9 -> 74\n'
    'Accuracy: 7 -> 53\n          RoF: 40 -> 59\n'
    'Move Speed: 15\n             Armor: 0\n'
    'Crit rate:20%\n              Crit Damage:50%\n'
    'Armor Pen.:15\n'
    ]

    skill1=[
    'Decreases the enemy squads rate of fire by 12%(lv1)/22%(lv.10)\n'
    'Lvl 1: 15s Cooldown, 1s Initial cooldown\n'
    'Lvl 10: 12s Cooldown, 1s Initial cooldown\n'
    ]

    bufftiles=[
    'Affect all guns\n'
    'increases damage by 14%/17%/21%/24%/28%\n'
    ]
    embed = discord.Embed(title="MP446 (No. 91)", description="".join(desctop),color=0xffff4d)
    embed.set_thumbnail(url='https://raw.githubusercontent.com/randesu/gftiles/main/GFtileDback.png')
    embed.add_field(name="Combat Data: ",value="".join(descstats), inline=False)
    embed.add_field(name="Tiles buff", value="".join(bufftiles),inline=False)
    embed.add_field(name="Skill 1: Assault Suppression", value="".join(skill1),inline=False)
    embed.set_image(url='https://iopwiki.com/images/6/60/MP-446.png')
    await ctx.send(embed=embed)

@client.command()
async def NAGANT(ctx):
    desctop=[
    '2-star HG\n'
    'Timer: 0:20:00\n'
    'Ammo: 10(x1)/30(x5)\n    HP:35(x1)->70(x1)/350(x5)\n'
    'Ration: 10(x1)/30(x5)\n'
    ]

    descstats = [
    'Damage: 11 -> 33\n           Evasion: 11 -> 92\n'
    'Accuracy: 7 -> 53\n          RoF: 29 -> 44\n'
    'Move Speed: 15\n             Armor: 0\n'
    'Crit rate:20%\n              Crit Damage:50%\n'
    'Armor Pen.:15\n'
    ]

    skill1=[
    'During nighttime, decreases all enemy damage by 20%(lv.1/12% daytime)/35%(lv10/20% daytime) for 8 seconds(5 seconds daytime)\n'
    'Lvl 1: 15s Cooldown, 6s Initial cooldown\n'
    'Lvl 10: 12s Cooldown, 6s Initial cooldown\n'
    ]

    bufftiles=[
    'Affect all guns\n'
    'increases damage by 16%/20%/24%/28%/32%\n'
    'increases crit rate by 8%/10%/12%/14%/16%\n'
    ]
    embed = discord.Embed(title="Nagant Revolver (No. 5)", description="".join(desctop),color=0xffff4d)
    embed.set_thumbnail(url='https://raw.githubusercontent.com/randesu/gftiles/main/GFtileDback.png')
    embed.add_field(name="Combat Data: ",value="".join(descstats), inline=False)
    embed.add_field(name="Tiles buff", value="".join(bufftiles),inline=False)
    embed.add_field(name="Skill 1: Firepower Suppression N", value="".join(skill1),inline=False)
    embed.set_image(url='https://iopwiki.com/images/1/1a/Nagant_Revolver.png')
    await ctx.send(embed=embed)


client.run(TOKEN)