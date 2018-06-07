import random
import numpy as np
from src import Game
import glob

# create game client
game = Game.Game()

# file to store custom commands
cmd_file = "../private/replies.txt"
lenny_file = "../text-files/lenny.txt"

# get the borg client from broskibot
# client = Parameters.Parameters.client

# command prefix
prefix = "!"


class Replies:
    def __init__(self):
        self.count = 0

    def getreply(self, message):
        msg = message.content
        self.count += 1
        print('messages received: ', self.count)

        # Chat sent in the 'game' channel are sent to Game.py
        # Other commands will not work in the game channel - good or bad thing?
        # MUST receive an array/list
        if str(message.channel) == "game":
            reply = game.getmessage(message)
            return reply

        """
        Start commands
        """
        if msg.startswith(prefix + "hello"):
            # say hi back, tagging the user
            rat = "Hello {0.author.mention}"
            return [rat]
        elif msg.startswith(prefix + "roulette"):
            # 1 in 6 chance to dome yourself
            rat = ["A gun is placed to {0.author.mention}'s head."]
            num = random.randint(1, 6)
            if num == 4:
                rat.append("The trigger is pulled and {0.author.mention} lies dead in the chat.")
            else:
                rat.append("The gun clicks and {0.author.mention} lives to see another day.")
            return rat
        elif msg.startswith(prefix + "roll"):
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
        elif msg.startswith(prefix + "8ball"):
            coke = ["It is certain", "It is decidedly so", "Without a doubt",
                    "Yes definitely", "You may rely on it", "As I see it, yes",
                    "Most likely", "Outlook good", "Yes", "Signs point to yes",
                    "Reply hazy try again", "Ask again later", "Better not tell you now",
                    "Cannot predict now", "Concentrate and ask again", "Don't count on it",
                    "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]
            return [random.choice(coke)]
        elif msg.startswith(prefix + "trump"):
            trump = open('../text-files/speeches.txt', encoding='utf8').read()
            corpus = trump.split()

            def make_pairs(corpus):
                for i in range(len(corpus) - 1):
                    yield (corpus[i], corpus[i + 1])

            pairs = make_pairs(corpus)
            word_dict = {}
            for word_1, word_2 in pairs:
                if word_1 in word_dict.keys():
                    word_dict[word_1].append(word_2)
                else:
                    word_dict[word_1] = [word_2]
            first_word = np.random.choice(corpus)
            while first_word.islower():
                first_word = np.random.choice(corpus)
            chain = [first_word]
            n_words = 5
            for i in range(n_words):
                chain.append(np.random.choice(word_dict[chain[-1]]))
            speech = ' '.join(chain)
            return [speech]
        elif msg.startswith(prefix + "create"):
            # takes in a command and response pair
            # "!create foo bar" would auto respond to "foo" with "bar"
            # TODO: check for duplicates, remove commands.. only works if the msg is JUST the command
            msg = message.content
            msg_split = msg.split()
            if len(msg_split) >= 3:
                with open(cmd_file, 'a') as the_file:
                    the_file.write(msg_split[1] + " | ")
                    for a in msg_split[2:]:
                        the_file.write(a + " ")
                    the_file.write("\n")
            return ["Command " + msg_split[1] + " created!"]
        elif msg.startswith(prefix + "neckbeard"):
            image_dir = "C:/Users/aaron/Desktop/broskibot-git/images/Neckbeards"
            images = []
            for f in glob.glob(image_dir + "/*"):
                images.append(f)
            num = random.randint(0, len(images) - 1)
            return [images[num]]
        elif msg.startswith(prefix + "lenny"):
            with open(lenny_file) as f:
                lines = f.readlines()
            face = random.randint(0,len(lines))
            return [lines[face]]
        else:
            # check through replies.txt
            mstr = str(message.content)
            cmds = []
            with open(cmd_file) as f:
                lines = f.readlines()
            for b in lines:
                mstr_split = b.split("|")
                cmds.append([mstr_split[0].strip(), mstr_split[1].strip()])
            for a in cmds:
                if mstr == a[0]:
                    return [a[1]]
            # no response
            print("It doesn't look like anything to me..")
            return [None]
