import random

import discord
from ignore import token as Token
from src import log
from src import replies

# secret token for broskibot
token = Token.token

# create the link to discord
client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    # log chat
    log.log(message)

    # parse multiple response replies here for now
    # think of a way to do this even with replies.py
    if message.content.startswith("!roulette"):
        reply = "A gun is placed to {0.author.mention}'s head.".format(message)
        await client.send_message(message.channel, reply)
        num = random.randint(1, 6)
        if num == 4:
            reply = "The trigger is pulled and {0.author.mention} lies dead in the chat.".format(message)
        else:
            reply = "The gun clicks and {0.author.mention} lives to see another day.".format(message)
        await client.send_message(message.channel, reply)

    # parse single reply messages here
    # replies.py will return a -1 if it has no response
    reply = replies.getreply(message)
    # if we don't get a -1 (if we have something to say) send the message
    if reply != -1:
        await client.send_message(message.channel, reply)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(token)
