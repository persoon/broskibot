import random

# For now any message that requires multiple replies has to go in broskibot.py
# I'll think about how to handle them in here later

# if tagging the user you MUST end the reply with .format(message)


def getreply(message):
    # check for commands
    # Say hi
    if message.content.startswith("!hello"):
        # say hi back, tagging the user
        return "Hello {0.author.mention}".format(message)

    #if message.content.startswith("!roll"):


    else:
        # return -1 if we don't need to reply to the message
        print("It doesn't look like anything to me..")
        return -1
