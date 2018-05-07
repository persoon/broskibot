import random

import discord
from ignore import token as Token
from src import log
from src import Replies
from src import Parameters


# secret token for broskibot
token = Token.token

# create the link to discord
client = discord.Client()
Parameters.Parameters.client = client
replies = Replies.Replies()


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    # log chat
    log.log(message)

    bot_msg = replies.getreply(message)
    for m in bot_msg:
        if m is not None:
            await client.send_message(message.channel, m.format(message))

    # parse multiple response replies here for now
    # parse single reply messages here
    # Replies.py will return a -1 if it has no response



@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(token)
