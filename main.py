import discord
import json
import requests
from discord.ext import commands
from discord import utils
from discord import FFmpegPCMAudio
import keep_alive
import youtube_dl
from os import environ

bot = commands.Bot(command_prefix='$')


@bot.command()
async def mem(ctx):
    r = requests.get('https://ivall.pl/memy')
    json_data = r.json()
    image_url = json_data['url']
    await ctx.send(image_url)


@bot.command()
async def play(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        await channel.connect()
    else:
        return
    #discord.PCMVolumeTransformer(volume=0.5)
    guild = ctx.guild
    voice_client = utils.get(bot.voice_clients, guild=guild)
    audio_source = FFmpegPCMAudio('music/dokidoki.mp3')

    if not voice_client.is_playing():
        voice_client.play(audio_source, after=None)

#@bot.command()
#async def next(ctx):
#  guild = ctx.guild
#  voice_client = utils.get(bot.voice_clients, guild=guild)
#  audio_source = FFmpegPCMAudio("music/stronger.mp3")


@bot.command()
async def pause(ctx):
    guild = ctx.guild
    voice_client = utils.get(bot.voice_clients, guild=guild)
    voice_client.pause()

@bot.command()
async def stop(ctx):
    try:
        ctx.voice_client.is_connected()
        await pause(ctx)
        await ctx.voice_client.disconnect()
        await ctx.send("naura")
    except:
        await ctx.send("juz wyszedlem od ciebie huju")

@bot.command()
async def resume(ctx):
  guild = ctx.guild
  voice_client = utils.get(bot.voice_clients, guild=guild)
  voice_client.resume()


keep_alive.keep_alive()
bot.run(environ['token'])
