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
            if col == 0:
                s+= ' '
            s += " " + str(col) + ""
        return s       # the board is complete, return it

    def addmove(self, col, row, ox):
    #for a user-given column and row, put x or o into it
    #if that space is full, prints Space is full
        if ox == "X" or ox == "O":
            if self.data[row][col] == " ": # could you use allowmove here ?
                self.data[row][col] = ox
            else:
                print "Space is full. Choose another one" # are you sure you want to put this valid move checking logic in your addmove method, or maybe it should go into your hostGame()
        else:
            print "Choose X or O"

    def allowmove(self, col, row, ox):
        if col < 0 or row < 0 or col >= 3 or row >= 3: # should it be > 3 or >= 3 ? - Becca
            return False
        elif self.data[row][col] != " ":
            return False
        else:
            return True

    def isFull(self):
        for col in range(3):
            for row in range(3):


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
            return False # I think perhaps this should go one tab level back outside the else statement ?

    def hostgame(self):
#checklist:
#move allowed; add; win; change turn

#TO Fix
#will continue even after someone has won
#also, won't stop if board is completely full
        nextChar = "X"
        while True:
            print(self)
            person_col = -1
            person_row = -1

            while self.allowmove(person_col, person_row, nextChar) == False:
                person_col = input("Player "+ nextChar + ": Enter a column between 0 and 2")
                person_row = input("Player " + nextChar+ ": Enter a row between 0 and 2")
                if self.allowmove(person_col, person_row, nextChar):
                    self.addmove(person_col, person_row, nextChar)
                elif self.data[person_row][person_col] != " ":
                    person_col = input("Space is full! Choose another column.")
                    person_row = input("Choose another row.")

                if self.win(nextChar):
                    print(self)
                    print "Player " + nextChar + " has won!"
                    break

                print(self)
                if nextChar == "X":
                    nextChar = "O"
                elif nextChar == "O":
                    nextChar = "X"


d = Board()
#d.addmove(2, 2, "X")
#print(d.allowmove(2, 2, "X"))
print(d.hostgame())

#d.hostgame()
#column, row, ox
#d.addmove(0, 2, "X")
#d.addmove(1, 1, 'X')
#d.addmove(2, 0, 'O')
#print(d.win('X'))