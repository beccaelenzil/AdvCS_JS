import random
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

    def scoresFor(self, b):
        """assigns scores to each column based on possible outcomes"""
        scores = [50]*b.width #makes list that's 50 50 50 50...
        # (whatever width of b is, that's the number of 50's)
        for col in range(b.width):
            if not b.allowsMove(col): #if column is full
                scores[col] = -1
            else:
                b.addMove(col, self.ox) #adds move
                if b.winsFor(self.ox): #if you win
                    scores[col] = 100
                else:
                    for colOpp in range(b.width):
                        if b.allowsMove(colOpp): #if it allows move, we must evaluate what happens
                            b.addMove(colOpp, self.oppCh()) #add move using opposite ox
                            if b.winsFor(self.oppCh()):
                                scores[col] = 0
                            b.delMove(colOpp)
                b.delMove(col)
        return scores

    def nextMove(self, b):
        """scores the board"""
        scores = self.scoresFor(b)
        max_index = []
        for i in range(len(scores)):
            if scores[i] == max(scores): #if it's equal to the max value
                max_index.append(i)
                col = random.choice(max_index)
                return col




p = smartPlayer('X')
print p
#Smart Player for X

p = smartPlayer('O')
print p
#Smart Player for O
