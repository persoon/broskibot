
### YOU MUST RETURN AN ARRAY

# The person who starts the game with !start is the Leader (players[0])
# leader can issue commands such as resetgame


class Game:
    def __init__(self):
        self.leader = ""
        self.players = []
        self.gamestate = False

    def getmessage(self, message):
        reply = []
        author = str(message.author)  # author = Name#1234
        if message.content.startswith("!start"):
            if self.gamestate:  # ignore if game is started
                return [None]
            print("### Game has started")
            self.gamestate = True
            self.leader = author
            self.join(author)
            reply.append("Game has started! Players please type \"!join\" to join the game.")
            return reply
        elif message.content.startswith("!join"):
            if self.gamestate:  # ignore if game is not started
                return self.join(author)
        elif message.content.startswith("!actuallystart"):
            # start handing out roles and cards and shit
            # if self.gamestate:
                # if author == self.leader:
                    # show getcurrentplayers(), start the game? will need new boolean?
            return [None]
        elif message.content.startswith("!players") or message.content.startswith("!headcount"):
            if self.gamestate:  # game is not started -- ignore
                return self.getplayers()
        elif message.content.startswith("!resetgame"):
            if self.gamestate:  # ignore if game is not started
                if author == self.leader:  # only reset game if they are the Leader
                    self.resetgame()
                    return ["Game has been reset!"]
        else:
            return [None]

    def join(self, author):
        reply = []
        for i in self.players:  # ignore if player has already joined
            if i == author:
                return [None]
        self.players.append(author)
        reply.append(self.getname(author) + " has joined the game!")
        reply.append("There are currently " + str(len(self.players)) + " players in the game.")
        return reply

    def getplayers(self):
        # return list of current players
        reply = "Current players: "
        for i in self.players:
            if i == self.players[len(self.players)-1]:
                reply += self.getname(i)
            else:
                reply += (self.getname(i) + ", ")
        return [reply]

    # gets a Name#1234 and returns Name
    def getname(self, author):
        name, r = str(author).split("#")
        return name

    def resetgame(self):
        # reset all game variables here
        self.leader = ""
        self.players = []
        self.gamestate = False
        return [None]
