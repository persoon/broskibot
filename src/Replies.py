import random
from src import Parameters

# get the borg client from broskibot
client = Parameters.Parameters.client


class Replies:
    def __init__(self):
        self.count = 0

    def getreply(self, message):
        self.count += 1
        print('messages received: ', self.count)

        """
        Start commands
        """
        if message.content.startswith("!hello"):
            # say hi back, tagging the user
            rat = "Hello {0.author.mention}"
            return [rat]
        elif message.content.startswith("!roulette"):
            # 1 in 6 chance to dome yourself
            rat = ["A gun is placed to {0.author.mention}'s head."]
            num = random.randint(1, 6)
            if num == 4:
                rat.append("The trigger is pulled and {0.author.mention} lies dead in the chat.")
            else:
                rat.append("The gun clicks and {0.author.mention} lives to see another day.")
            return rat
        elif message.content.startswith("!roll"):
            # !roll 321d123
            msg = message.content
            msg_split = msg.split()
            dice = msg_split[1]
            left, right = dice.split("d")
            total = 0
            val = "("
            for i in range(int(left)):
                rng = random.randint(1, int(right))
                val += str(rng)
                if i < int(left) - 1:
                    val += ","
                total += rng
            reply = val + ") Total: " + str(total)
            return [reply]
        else:
            print("It doesn't look like anything to me..")
            return [None]
