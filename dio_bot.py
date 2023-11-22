import discord
from discord.ext import commands
import numpy as np
from insultgenerator import phrases
from urllib.request import urlopen
import json

# to add to your discord channel,
# https://discord.com/api/oauth2/authorize?client_id=1176704386282565772&permissions=67584&scope=bot

bot = commands.Bot(command_prefix='$', intents=discord.Intents.all())


@bot.event
async def on_ready():
    print("type $insultdio")


@bot.command()
async def insultdio(ctx):

    if np.random.random() < 0.5:
        data = json.loads(urlopen("https://evilinsult.com/generate_insult.php?lang=en&type=json").read().decode("utf-8"))
        insult = str(data["insult"])
        await ctx.send("Hey Dio, " + insult)
    else:
        await ctx.send(phrases.get_so_insult_with_action_and_target("Dio", "he"))


# give me a random int from 1 -> n
@bot.command(pass_context=True)
async def rand(ctx, val):
    if isinstance(int(val), int):
        val = int(val)
        await ctx.send(':game_die: ' + str(int(np.ceil(np.random.random() * val))))
    else:
        await ctx.send("that's not an integer")


# run the bot using super special secret token
bot.run(str(
    np.genfromtxt('TOKEN', dtype='str')
))
