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
async def cat():
    await channel.send(file=discord.File('cat_01.jpg'))


bot.run(token)


