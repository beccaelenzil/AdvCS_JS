class Board:
    """ a datatype representing a 3x3 board of rows and columns
    """

    def __init__(self):
        """ the constructor for objects of type Board """
        W = 3
        H = 3
        self.data = [ [' ']*W for row in range(H) ]

    def __repr__(self):
        """ this method returns a string representation
            for an object of type Board
        """
        H = 3 #because tic-tac-toe has a specific board
        W = 3
        s = ''   # the string to return
        for row in range(0, H):
            s += str(row) + '|'
            for col in range(0,W):
                s += self.data[row][col] + '|'
                #self.data is list of lists; row gives corresponding row
                #col gives on item in column position in row
                #ex: [3][4] gives fourth item in column 3
                #self.data[1] is a list that corresponds to second row
            s += '\n'

        s += (2*W+1) * '-'    # bottom of the board
        s += "\n"
        count = 0
        for col in range(0, W):
            s += " " + str(col) + ""
        return s       # the board is complete, return it

    def addmove(self, col, row, ox):
    #for a user-given column and row, put x or o into it
    #if that space is full, prints Space is full
        if self.data[row][col] == " ":
            self.data[row][col] = ox
        else:
            print "Space is full. Choose another one"

    def win(self):
    #need to check across, horizonally, vertically
        for row in range(0, 3):
            for col in range(0, 3):



d = Board()
#column, row, ox
d.addmove(1, 0, 'X')
d.addmove(2, 0, 'X')
d.addmove(0, 0, 'O')
print(d.win())
print(d)