import discord
from src import log
from src import Replies
from ignore import token as Token

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

    # log messages
    print('------')
    print("### Author: " + str(message.author))
    print("### Channel: " + str(message.channel))
    log.log(message)

    # private message test
    if message.content.startswith("!secret"):
        await client.send_message(message.author, "OwO")

    # check for and send responses
    bot_msg = replies.getreply(message)
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


# start the bot
client.run(token)
