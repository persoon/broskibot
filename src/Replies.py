import random
from src import Game
import glob

# create game client
game = Game.Game()


class Replies:
    def __init__(self):
        self.count = 0

    def getreply(self, message):
        self.count += 1
        print('### Messages received: ', self.count)

        # Chat sent in the 'game' channel are sent to Game.py
        # Other commands will not work in the game channel - good or bad thing?
        # MUST receive an array/list
        if str(message.channel) == "game":
            reply = game.getmessage(message)
            return reply

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
        elif message.content.startswith("!8ball"):
            coke = ["It is certain", "It is decidedly so", "Without a doubt",
                    "Yes definitely", "You may rely on it", "As I see it, yes",
                    "Most likely", "Outlook good", "Yes", "Signs point to yes",
                    "Reply hazy try again", "Ask again later", "Better not tell you now",
                    "Cannot predict now", "Concentrate and ask again", "Don't count on it",
                    "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]
            return [random.choice(coke)]
        elif message.content.startswith("!create"):
            msg = message.content
            msg_split = msg.split()
            if len(msg_split) == 3:
                cmd_name = msg_split[1]
                cmd_response = msg_split[2]
                cmd_file = "../commands/commands.txt"
                # TODO: save command to file, return confirm message
            return [None]
        elif message.content.startswith("!neckbeard"):
            image_dir = "C:/Users/aaron/Desktop/broskibot-git/images/Neckbeards"
            images = []
            for f in glob.glob(image_dir + "/*"):
                images.append(f)
            num = random.randint(0, len(images) - 1)
            return [images[num]]
        else:
            print("### It doesn't look like anything to me..")
            return [None]
