# https://www.youtube.com/watch?v=SPTfmiYiuok
# fevane2462@nonicamy.com:qwerty123
# https://repl.it/@fevane2462/DiscordDemoBot#main.py
# https://uptimerobot.com/dashboard#mainDashboard
# https://discorddemobot.fevane2462.repl.co/

# https://discordpy.readthedocs.io/en/latest/api.html
# https://discordpy.readthedocs.io/en/latest/faq.html

from replit import db
import discord
import requests
import os
import keep_alive

bad_words = ["bad", "chicken"]

client = discord.Client()

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    data = response.json()
    data = data[0]
    text = f"{data['q']} - {data['a']}"
    return text

def addBadWord(word):
    #for k in db:
    #    print(k, db[k])

    key = "words"
    if key in db.keys():
        data = db[key]
        data.append(word)
        db[key] = data
    else:
        db[key] = [word]
    
    return str(db[key])

async def send_message(message):
    #for c in client.get_all_channels():
    #    print(c.name, c.id)

    general = client.get_channel(794495262461788174)
    await general.send(message)

async def mention_dima(message):
    # ? client.get_user(id) returns None
    dima = await client.fetch_user(647139149941309455)
    #text = "Dima" if dima is not None else "Outside"
    #print(text)
    if dima is not None:
        # <@64...55>
        text = f"{dima.mention}, {message}"
        await send_message(text)

@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))
    #await mention_dima("I'm logged in!")

@client.event
async def on_message(message):
    if message.author is client.user or message.author.bot:
        return

    text = message.content

    if text.startswith("$hello"):
        icon = ":sunglasses:"
        reply = "Hello, {}! {}".format(message.author.mention, icon)
        await message.channel.send(reply)
    elif text.startswith("$quote"):
        reply = get_quote()
        await message.channel.send(reply)
    elif text.startswith("$add"):
        word = text.split("$add ")[1]
        words = addBadWord(word)
        reply = "Added! " + words
        await message.channel.send(reply)

    match_bad_word = any(word in text for word in bad_words)
    if match_bad_word:
        reply = "Said bad word!"
        await message.channel.send(reply)


token = os.getenv("TOKEN")

if token is not None:
    #keep_alive.keep_alive()
    print("Running the bot")
    client.run(token)
else:
    print("Token doesn't found")
