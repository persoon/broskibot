import random
import discord
import asyncio
from src import Parameters
client = Parameters.Parameters.client
# For now any message that requires multiple replies has to go in broskibot.py
# I'll think about how to handle them in here later

# if tagging the user you MUST end the reply with .format(message)


class Replies:
    def __init__(self):
        self.count = 0

    def getreply(self, message):
        self.count += 1
        print('messages received: ', self.count)
        # Say hi
        if message.content.startswith("!hello"):
            # say hi back, tagging the user
            str = "Hello {0.author.mention}"
            return [str]
        elif message.content.startswith("!roulette"):
            str = ["A gun is placed to {0.author.mention}'s head."]
            num = random.randint(1, 6)
            if num == 4:
                str.append("The trigger is pulled and {0.author.mention} lies dead in the chat.")
            else:
                str.append("The gun clicks and {0.author.mention} lives to see another day.")
            return str
        else:
            # return -1 if we don't need to reply to the message
            print("It doesn't look like anything to me..")
            return [None]


