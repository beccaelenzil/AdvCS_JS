import random
import sys
from ConnectFour import Board as b

class basePlayer():
    """a basic player class that selects the next move"""
    def __init__(self, ox):
        """the constructor"""
        self.ox = ox

    def __repr__( self ):
        """ creates an appropriate string """
        s = "Basic player for " + self.ox + "\n"
        return s

    def nextMove(self,b):
        """selects an allowable next move at random"""
        col = -1
        while b.allowsMove(col) == False:
            col = random.randrange(b.width)
        return col

class smartPlayer(basePlayer):
    """ an AI player for Connect Four """
    def __init__(self, ox):
        """ the constructor inherits from from the basicPlayer class"""
        basePlayer.__init__(self, ox)

    def __repr__( self ):
        """ creates an appropriate string """
        s = "Smart player for " + self.ox + "\n"
        return s

    def oppCh(self):
        """returns opposite ox-- if X, return O"""
        if self.ox == "X":
            return "O"
        elif self.ox == "O":
            return "X"

    def scoresFor(self, q):
        """assigns scores to each column based on possible outcomes"""
        scores = [50]*q.width #makes list that's 50 50 50 50...
        # (whatever width of b is, that's the number of 50's)
        for col in range(q.width):
            if not q.allowsMove(col): #if column is full
                scores[col] = -1
            else:
                q.addMove(col, self.ox) #adds move
                if q.winsFor(self.ox): #if you win
                    scores[col] = 100
                else:
                    for colOpp in range(q.width):
                        if q.allowsMove(colOpp): #if it allows move, we must evaluate what happens
                            q.addMove(colOpp, self.oppCh()) #add move using opposite ox
                            if q.winsFor(self.oppCh()):
                                scores[col] = 0
                            q.delMove(colOpp)
                q.delMove(col)
        return scores

    def nextMove(self, q):
        """scores the board"""
        scores = self.scoresFor(q)

        #find index of maximum scores
        max_index = []
        for i in range(len(scores)):
            if scores[i] == max(scores): #if it's equal to the max value
                max_index.append(i)

        col = random.choice(max_index)
        return col


def playGame(playerX, playerO):

    pO = playerO
    pX = playerX

    # check for valid input, and instantiate the players
    if playerX == 'smart':
        pX = smartPlayer('X') #SELF.CHARACTER =
    elif playerX == 'basic':
        pX = basePlayer('X')
    elif playerX != 'human':
        print "Player X should be 'smart', 'basic', or 'human'. Try again!"
        sys.exit()

    if playerO == 'smart':
        pO = smartPlayer('O')
    elif playerO == 'basic':
        pO = basePlayer('O')
    elif playerO != 'human':
        print "Player O should be 'smart', 'basic', or 'human'. Try again!"
        sys.exit()

    q = b(7,6)
    print q


    game_player = pX #I found the bug! We were setting game player to pX in the while loop, so that every time it looped through
                    # the game_player was pX, even when we wanted it to be pO. Simple fix: move this statement outside of the while loop
                    # because it's simply there to initialize your game player.
                    # I also set next char equal to game_player.ox. This doesn't change anything, but should help eliminate bugs
    nextChar = game_player.ox

    #get the next play
    while True:
        print(q)
        person_col = -1
        while not q.allowsMove(person_col):
            if game_player == "human":
                person_col = input("It's " + nextChar + "s turn. Enter a column: ")
            else:
                person_col = game_player.nextMove(q)
            person_col = int(person_col)
        q.addMove(person_col, nextChar)   #adds character to board

        #check for a win
        if q.winsFor(nextChar): #if char has won
            print q
            print(nextChar + " has won!")
            if nextChar == 'O':
                return 0
            elif nextChar == 'X':
                return 1
        #check for a truce
        elif q.isFull():
            print("The board is full. Game is over.")
            return 2

        #switch the player
        if nextChar == "X":
            game_player = pO
            nextChar = game_player.ox
        else:
            game_player = pX
            nextChar = game_player.ox




numGames = 50
oxTruce = [0, 0, 0]
for i in range(numGames):
    winner = playGame("smart", "basic")
    oxTruce[winner] += 1

print oxTruce


#print(q.hostGame())
