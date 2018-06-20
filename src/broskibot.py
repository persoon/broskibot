import discord
import random
from src import log
from src import Replies
from ignore import token as Token
import logging

# secret token for broskibot
token = Token.token

# create the link to discord
client = discord.Client()
# Parameters.Parameters.client = client

# create the replier
replies = Replies.Replies()

# members = client.get_all_members()


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    # do not reply to other bots
    if message.author.bot:
        return

    # log messages
    print('------')
    print("### Author: " + str(message.author))
    print("### Channel: " + str(message.channel))
    log.log(message)

    if message.content.startswith("!owo"):
        counter = 0
        stop = 1 # how many messages back do you wanna go? 0 is gonna be "!owo"
        #      ^ so 1 will be the message before -- what we wanna owo-fy
        async for message in client.logs_from(message.channel, limit=stop+1):
            print(message.content)
            if counter == stop:
                faces = ["(・`ω´・)", ";;w;;", "owo", "UwU", ">w<", "^w^"]
                owo = message.content.format(message)
                owo = owo.replace("r", "w").replace("R", "W")
                owo = owo.replace("l", "w").replace("L", "W")
                owo = owo.replace("na", "ny")
                owo = owo.replace("ne", "ny")
                owo = owo.replace("ni", "ny")
                owo = owo.replace("no", "ny")
                owo = owo.replace("nu", "ny")
                owo = owo.replace("Na", "Ny")
                owo = owo.replace("Ne", "Ny")
                owo = owo.replace("Ni", "Ny")
                owo = owo.replace("No", "Ny")
                owo = owo.replace("Nu", "Ny")
                owo = owo.replace("NA", "NY")
                owo = owo.replace("NE", "NY")
                owo = owo.replace("NI", "NY")
                owo = owo.replace("NO", "NY")
                owo = owo.replace("NU", "NY")
                r = random.randint(0, len(faces))
                await client.send_message(message.channel, owo + " " + faces[r])
                return
            counter += 1

    # private message test
    if message.content.startswith("!secret"):
        await client.send_message(message.author, "OwO")

    # TODO: change this
    # trigger chris
    if str(message.author) == "Wiggles#3214":
        n = random.randint(1, 3)
        if n == 1:
            await client.send_message(message.channel, "{0.author.mention} YoUr MoM gOeS tO cOlLeGe".format(message))

    # check for and send responses
    bot_msg = replies.getreply(message)

    # TODO: change this
    # check for image
    if message.content.startswith("!neckbeard"):
        await client.send_file(message.channel, bot_msg[0], filename=None, content=None, tts=False)
        return

    for m in bot_msg:
        if m is not None:
            if isinstance(m, str):
                await client.send_message(message.channel, m.format(message))
            else:  # private messages are sent as a tuple: (author, msg)
                await client.send_message(m[0], m[1].format(message))



@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    # print('------')
    # for i in members:
    #    print(i.name)
    # print('------')


# start logging
logging.basicConfig(level=logging.INFO)

# start the bot
client.run(token)
