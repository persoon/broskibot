import random
# TODO: separate parts so certain code can be reused for different games (e.g. secret for PMs, joining, starting)
### YOU MUST RETURN AN ARRAY

# The person who starts the game with !start is the Leader (players[0])
# leader can issue commands such as resetgame

# command prefix
prefix = "!"


class Game:
    def __init__(self):
        # Useful for implementing many games
        self.leader = ""
        self.players = []
        self.gamestate = False

        # Secret Hitler dependant variables
        self.roles = []
        self.liberals = []
        self.fascists = []
        self.hitler = None
        self.known = False  # Does hitler know who fascists are? True/False

    def getmessage(self, message):
        msg = message.content
        reply = []
        author = message.author  # author = Name#1234
        if msg.startswith(prefix + "start"):
            if self.gamestate:  # ignore if game is started
                return [None]
            print("### Game has started")
            self.gamestate = True
            self.leader = author
            self.join(author)
            reply.append("Game has started! Players please type \"!join\" to join the game.")
            return reply
        elif msg.startswith(prefix + "join"):
            if self.gamestate:  # ignore if game is not started
                return self.join(author)
        elif msg.startswith(prefix + "actuallystart"):
            # start handing out roles and cards and shit
            self.role_select()
            for r in self.roles:
                reply.append((r[0], r[1]))
            # if self.gamestate:
                # if author == self.leader:
                    # show getcurrentplayers(), start the game? will need new boolean?
            return reply
        elif msg.startswith(prefix + "players") or msg.startswith(prefix + "headcount"):
            if self.gamestate:  # game is not started -- ignore
                return self.getplayers()
        elif msg.startswith(prefix + "resetgame"):
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

    # TODO: make sure (players > 10 || players < 5) != True before starting.
    # TODO: rule reminder based on # of players
    # players ; liberals ; fascists ; hitlers ; fascists known by hitler? ;
    #       5 ;        3 ;        1 ;       1 ;                       yes ;
    #       6 ;        4 ;        1 ;       1 ;                       yes ;
    #       7 ;        4 ;        2 ;       1 ;                        no ;
    #       8 ;        5 ;        2 ;       1 ;                        no ;
    #       9 ;        5 ;        3 ;       1 ;                        no ;
    #      10 ;        6 ;        3 ;       1 ;                        no ;
    def role_select(self):
        num_players = len(self.players)
        libs = None
        fasc = None
        hit = 1
        h_know = False
        if num_players is 5:
            libs = 3
            fasc = 1
            h_know = True
        elif num_players is 6:
            libs = 4
            fasc = 1
            h_know = True
        elif num_players is 7:
            libs = 4
            fasc = 2
        elif num_players is 8:
            libs = 5
            fasc = 2
        elif num_players is 9:
            libs = 5
            fasc = 3
        elif num_players is 10:
            libs = 6
            fasc = 3
        elif 2 < num_players < 5:  # for testing
            libs = num_players - 2
            fasc = 1
        elif num_players <= 2:  # for testing
            libs = 1
            fasc = 0

        roles = []
        liberals = []
        fascists = []
        hitler = None
        for p in self.players:
            _role = random.randint(1, libs + fasc + hit)
            if _role <= libs:
                roles.append((p, 'liberal'))
                liberals.append(p)
                libs -= 1
                if libs < 0:
                    print('ERROR: To many liberals!')
            elif _role - libs <= fasc:
                roles.append((p, 'fascist'))
                fascists.append(p)
                fasc -= 1
                if fasc < 0:
                    print('ERROR: To many fascists!')
            else:  # hitler
                roles.append((p, 'hitler'))
                hitler = p
                hit -= 1
                if hit < 0:
                    print('ERROR: More than one hitler!')

        # these lists make our life easier for rule checks
        self.liberals = liberals
        self.fascists = fascists
        self.hitler = hitler
        self.known = h_know
        # this list is necessary for the game
        self.roles = roles

        return roles
