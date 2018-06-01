import random
import numpy as np
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
        elif message.content.startswith("!8ball"):
            coke = ["It is certain", "It is decidedly so", "Without a doubt",
                    "Yes definitely", "You may rely on it", "As I see it, yes",
                    "Most likely", "Outlook good", "Yes", "Signs point to yes",
                    "Reply hazy try again", "Ask again later", "Better not tell you now",
                    "Cannot predict now", "Concentrate and ask again", "Don't count on it",
                    "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]
            return [random.choice(coke)]

        elif message.content.startswith("!trump"):
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

        else:
            print("It doesn't look like anything to me..")
            return [None]
