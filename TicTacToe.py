class Board:
    """ a datatype representing a 3x3 board of rows and columns
    """

    def __init__(self):
        """ the constructor for objects of type Board """
        self.W = 3
        self.H = 3
        self.data = [ [' ']*self.W for row in range(self.H) ]

    def __repr__(self):
        """ this method returns a string representation
            for an object of type Board
        """
        #H = 3 #because tic-tac-toe has a specific board
        #W = 3
        s = ''
        for row in range(0, self.H):
            s += str(row) + '|'
            for col in range(0,self.W):
                s += self.data[row][col] + '|'
                #self.data is list of lists; row gives corresponding row
                #col gives on item in column position in row
                #ex: [3][4] gives fourth item in column 3
                #self.data[1] is a list that corresponds to second row
            s += '\n'

        s += (2*self.W+1) * '-'    # bottom of the board
        s += "\n"
        count = 0
        for col in range(0, self.W):
            s += " " + str(col) + ""
        return s       # the board is complete, return it

    def addmove(self, col, row, ox):
    #for a user-given column and row, put x or o into it
    #if that space is full, prints Space is full
        if ox == "X" or ox == "O":
            if self.data[row][col] == " ":
                self.data[row][col] = ox
            else:
                print "Space is full. Choose another one"
        else:
            print "Choose X or O"

    def allowmove(self, col, row, ox):
        #if full, print its full
        if self.data[row][col]

    def win(self, ox):
    #need to check across, horizonally, vertically
    #can be fragile because tic-tac-toe never changes the size of box
        for row in range(0, self.H): #across
            if self.data[row][0] == ox and \
                self.data[row][1] == ox and \
                self.data[row][2] == ox:
                    return True
        for col in range(0, self.W): #vertical
            if self.data[0][col] == ox and \
                self.data[1][col] == ox and \
                self.data[2][col] == ox:
                    return True
        #diagonal from left upper corner
        if self.data[0][0] == ox and \
            self.data[1][1] == ox and \
            self.data[2][2] == ox:
                return True
        #diagonal from right upper corner
        elif self.data[0][2] == ox and \
            self.data[1][1] == ox and \
            self.data[2][0] == ox:
                return True
        else:
            return False
"""
    def hostgame(self):
# addmove uses players input of column, row to make sure spot
# is available then places player's ox in
        first_char = "X"
        while True:
            player_col = input("It's " + first_char + "'s turn. Enter a column")
            player_row = input("Enter a row.")
            while self.allowsmove(player_col, player_row, first_char):
                self.addmove(player_col, player_row, first_char)
                if self.win(first_char):
                    print first_char + " has won!"
                    break
                else:
                    if first_char == "X":
                        first_char = "O"
                    else:
                        first_char = "X"
            if self.allowsmove(player_col, player_row, first_char == False:
                return "Not a valid entry"
"""

d = Board()
d.hostgame()
#column, row, ox
#d.addmove(0, 2, "X")
#d.addmove(1, 1, 'X')
#d.addmove(2, 0, 'O')
#print(d.win('X'))
print(d)