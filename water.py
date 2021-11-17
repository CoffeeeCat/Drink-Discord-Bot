import discord,asyncio,os,json,random
from discord.ext import commands, tasks
from config import *


me = 350340795519467520
bot = commands.Bot(command_prefix='.')
client = commands.Bot(command_prefix=".")
channel = bot.get_channel(908817594511929366)

#Pre Event / Console Event
@bot.event
async def on_ready():
    change_status.start()
    print('bot in active')


def check(message):
    return message.content == "Mach ich :3" and message.author.id == 350340795519467520


@tasks.loop(hours=2)
async def change_status():
    channel = bot.get_channel(908817594511929366)
    def check(message):
        return message.content == "Mach ich :3" and message.author.id == 350340795519467520
    await bot.change_presence(activity=discord.Game('the reminder for @Coffeeé -.-'))
    await channel.send('Los <@!350340795519467520>, trink jetzt Wasser :3')
    msg = await bot.wait_for('message', check=check, timeout=180)
    if msg:
        await channel.send("Danke c:, ich schreib in Zwei Stunden nochmal :3")

@bot.command(pass_context=True)
async def cat(ctx):
    await ctx.send(file=discord.File(random.choice('cat_01.jpg', 'cat_02.jpg', 'cat_03.jpg')))

# Temp - URL Store
#https://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=381210&key=8E18F88DEE099EC89AEB6756C59B8B18&steamid=76561198088660842&format=json


@bot.command()
async def jsonTest(ctx, type: str = None):
    data = json.loads(response.json())[3]


bot.run(token)


