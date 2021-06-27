# pockychu bot.py
import os
import random
import asyncio

import discord 
from discord.ext import commands
from discord import Game

import giphy_client
from giphy_client.rest import ApiException

from dotenv import load_dotenv 

from keep_alive import keep_alive

keep_alive()
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GIPHY_TOKEN = os.getenv('GIPHY_TOKEN')

api_instance = giphy_client.DefaultApi() #giphy
bot = commands.Bot(command_prefix = '$')

#search gifs function
def search_gifs(query):
    try:
        return api_instance.gifs_search_get(GIPHY_TOKEN, query, limit = 5, rating = 'g')
    except ApiException as e:
        return "Exception when calling DefaultApi->gifs_search_get: %s\n" % e

def gif_response(emotion):
    gifs = search_gifs(emotion)
    lst = list(gifs.data)
    gif = random.choices(lst)
    return gif[0].url

#load pockychu to discord
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    await bot.change_presence(activity = Game(name = "pocky.fam"))

#welcome message
@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name = "general") 
    await channel.send(f"Henlo, **{member.mention}** . Welcome to Pocky Fam!")

#bot commands
@bot.command(name = 'happy', help = 'Responds with some happy messages to turn that frown upside down!')
async def hp(ctx):
    happy_quotes = [
        'everything will work out in the end! just give it a little time <3 ',
        'let\'s go get boba! sending a virtual boba as well! ',
        'sending virtual hugs!',
        'don\'t sweat the small stuff! i believe in you <3',
        'hey! let\'s binge watch something to get your mind off the stressful stuff! ',
        'you are beautiful! BE-YOU-TIFUL :3',
        'sending love and hugs! uwu',
        'you got this! i believe in you!',
        'who hurt you? emma and i will go fight them',
        'take a deep breath... take one step at a time, it\'ll be okay',
        'you\'re not an idiot sandwich 🍞👁👄👁 🍞',
        'you is smart, you is kind, you is important',
        'positive panda says stay positive 🐼',
        'YOU A BOBABE! 🥰',
        'today is gonna be a good day!',
        'you deserve the moon and the stars 🌟🌟',
    ]

    response = random.choice(happy_quotes)
    await ctx.send(response)
    await ctx.send(gif_response('happy'))

@bot.command(name = 'motivation', help = 'Responds with some motivational quote said by someone')
async def mot(ctx):
    motivational_quotes = [
        '"they say the brightest blaze burns the brightest when circumstances are at their worst." -howl\'s moving castle',
        '"always believe in yourself. do this and no matter where you are, you will have nothing to fear." -the cat returns',
        '"believe you can, then you will." -mulan',
        '"today is a good day to try." -quasimodo ',
        'you got this! take a deep breath or break. it\'ll be okay! -christie <3',
        '"all it takes is faith, trust, and a little pixie dust." -peter pan',
        '"big things often have small beginnings." -studio ghibli',
        '"working hard is important, but there is something that even matters more; believing in yourself." -harry potter',
        '"what\'s coming will come, and we\'ll meet it when it does." -hagrid ',
        'hey little fighter, things seem tough rn, but it\'ll be okay!',
        '"take small steps at a time. you can accomplish little by little everyday" -emma :)',
        '"do not go gentle into that goodnight. rage, rage against the dying of the light." -Dylan Thomas',
        '"Our greatest glory is not in never falling, but in rising every time we fall." -Confucius',

    ]

    response = random.choice(motivational_quotes)
    await ctx.send(response)
    await ctx.send(gif_response('motivation'))

@bot.command(name = "songlyrics", help = 'Responds with song lyrics')
async def sl(ctx):
    songlyrics_quotes = [
        '"just tell me what you waiting for..." -SOMI: What You Waiting For',
        '"a hundred bad days make a hundred good stories. a hundred good stories make me interesting at parties..." AJR: 100 Bad Days',
        '"can\'t hold me down cuz you know i\'m a fighter..." BTS: On',
        '"you\'ve shown me i have reasons. i should love myself..." BTS: Love Myself',
        '"let me hold your hand..." GOT7: Let Me',
        '"never ever gonna make you cry..." GOT7: Never Ever',
        '"in the middle of the hardest fight. it\'s true, i will rescue you..." Lauren Daigle: Rescue',
        '"to california, our worries make no sense. colors are sky blue, singing in my view (young and wild)..." The Rose: California ',
        '"who the hell needs soda when i got boba..." Jason Chen: Boba',
        '"standing in a hall of fame and the world\'s gonna know your name..." The Script: Hall of Fame',
        '"i think you and the moon and neptune got it right. \'cause now i\'m shining bright..." Echosmith: Bright',
        '"i love myself ... dalla dalla..." ITZY: Dalla Dalla',
        '"cooking like a chef, i\'m a five star Michelin..." Stray Kids: God\'s Menu',
        '"don\'t hate me, give love a chance..." Jackson Wang + Galantis: Pretty Please',
        '"i\'m a geek, the big paradox..." DREAMCATCHER: BOCA',
        '"it\'s a cruel game, i cannot lose..." NCT 127: Sit Down!'
        '"Don\'t give up, I won\'t give up Don\'t give up, no no no..." SIA: The Greatest',
        '"I got this. I\'m truly fine" IU: Palette',
        '"There\'s nothing really wrong with the master plan, but you don\'t really need one to be a happy man" Thea: TwentyTwo',
        '"OH WAH AH AH AH" Disturbed: Down with the Sickness',
        '"I can\'t wait to be your number one. I\'ll be your biggest fan and you\'ll be mine" Rex Orange County: Best Friend',
        '"I\'m a shooting star, leaping through the sky" Queen: Don\'t Stop Me Now',
        '"i\'m a ten out of ten even when i forget..." Demi Lovato: I Love Me',
        '"don\'t hate me, give love a chance..." Jackson Wang, GALANTIS: Pretty Please',

    ]

    response = random.choice(songlyrics_quotes)
    await ctx.send(response)

@bot.command(name = "8ball", help = 'Magic 8 ball. Need help in deciding something / want to look in the future? 8ball is here to help')
async def eightball(ctx):
    eightball_quotes = [
        'Without a doubt',
        'Outlook good',
        'Better not tell you now',
        'Cannot predict now',
        'Answer is no',
        'Outlook not so good', 
        'I suppose',
    ]

    response = random.choice(eightball_quotes)
    await ctx.send(response)

@bot.command(name = "whoareyou", help = 'Pockychu will reveal its origin')
async def whoyou(ctx):
    whoyou_quotes = [
        'i am pockychu',
        'your mom',
        'Emma created me because she had nothing better to do',
        'my favorite flavor of pocky is strawberry',
        'yes',
        'i am you but stronger', 
        'i cannot tell you my real identity... or you would be in danger',
    ]

    response = random.choice(whoyou_quotes)
    await ctx.send(response)

#client.run(TOKEN)
bot.run(TOKEN)