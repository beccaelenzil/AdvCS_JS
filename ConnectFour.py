class Board:
    """ a datatype representing a C4 board
        with an arbitrary number of rows and cols
    """

    def __init__( self, width, height ):
        """ the constructor for objects of type Board """
        self.width = width
        self.height = height
        W = self.width
        H = self.height
        self.data = [ [' ']*W for row in range(H) ]

        # we do not need to return inside a constructor!

    def __repr__(self):
        """ this method returns a string representation
            for an object of type Board
        """
        H = self.height
        W = self.width
        s = ''   # the string to return
        for row in range(0,H):
            s += '|'
            for col in range(0,W):
                s += self.data[row][col] + '|'
            s += '\n'

        s += (2*W+1) * '-'    # bottom of the board
        s += "\n"
        count = 0
        for col in range(1, W+1):
            s += " " + str(col)
        return s       # the board is complete, return it

    def addMove(self, col, ox):
        for col in range(0, W+1):
           if self.data == True:
               print("h")

d = Board(6, 7)
print(d.addMove)
