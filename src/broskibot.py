import discord
from src import log
from src import Replies
from src import Parameters
from ignore import token as Token

# secret token for broskibot
token = Token.token

# create the link to discord
client = discord.Client()
Parameters.Parameters.client = client

# create the replier
replies = Replies.Replies()


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    # log messages
    log.log(message)

    # check for and send responses
    bot_msg = replies.getreply(message)
    for m in bot_msg:
        if m is not None:
            await client.send_message(message.channel, m.format(message))


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


# start the bot
client.run(token)
