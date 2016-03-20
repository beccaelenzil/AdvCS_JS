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
                #self.data is list of lists; row gives corresponding row
                #col gives on item in column position in row
                #ex: [3][4] gives fourth item in column 3
                #self.data[1] is a list that corresponds to second row
            s += '\n'

        s += (2*W+1) * '-'    # bottom of the board
        s += "\n"
        count = 0
        for col in range(0, W):
            s += " " + str(col)
        return s       # the board is complete, return it


    def addMove(self, col, ox):
        for row_index in range(self.height-1, -1, -1):
            if self.data[row_index][col] == " ": #if self.data is empty
                self.data[row_index][col] = ox
                break

#find position using self.data: holds the board

    def clear(self):
        for row_index in range(0, self.height):
            for col in range(0, self.width):
                self.data[row_index][col] = " "

    def setBoard( self, moveString ):
        """ takes in a string of columns and places
            alternating checkers in those columns,
            starting with 'X'

            For example, call b.setBoard('012345')
            to see 'X's and 'O's alternate on the
            bottom row, or b.setBoard('000000<--columns') to
            see them alternate in the left column.

            moveString must be a string of integers
        """
        nextCh = 'X'   # start by playing 'X'
        for colString in moveString:
            col = int(colString)
            if 0 <= col <= self.width:
                self.addMove(col, nextCh)
            if nextCh == 'X': nextCh = 'O'
            else: nextCh = 'X'

    def allowsMove(self, c): #checks that column isnt totally full
    #also makes sure legal col size
        if c >= self.width or c < 0:
            return False
        else:
            return self.data[0][c] == " " #if full, returns False since not true

    def isFull(self):
#returns True if object is completely full, returns False otherwise
        for col in range(0, self.width):
            if self.allowsMove(col): #checks all columns, if any are not full,
            #returns False
            #can only get past if haven't returned false, which happens if all full
            #ergo, all full
                return False
        return True

    def delMove(self, c):
#removes top checker from column c
#If column is empty, then delMove does nothing
        #for col in range(0, self.width):
        for row_index in range(0, self.height): #go down from top
            if self.data[row_index][c] != " ":
                self.data[row_index][c] = " "
                break

    def winsFor(self, ox):
#returns True if four checkers of same kind in a row
#returns True if four checks of same kind in a column
#returns True if four checks of same kind in a diagonal x2 (2 ways)
#Otherwise, returns false
        D = self.data
        for row_index in range(0, self.height):
            for col in range(0, self.width-3):#for horizonal wins; -3 makes sure it doesnt go out of bounds
                if D[row_index][col] == ox and \
                    D[row_index][col+1] == ox and \
                    D[row_index][col+2] == ox and \
                    D[row_index][col+3] == ox:
                        return True

        for col in range(0, self.width):#for vertical
            for row_index in range(0, self.height-3):
                if D[row_index][col] == ox and \
                    D[row_index+1][col] == ox and \
                    D[row_index+2][col] == ox and \
                    D[row_index+3][col] == ox:
                        return True

        for col in range(0, self.width-3): #starting at (0,0)-- upper left corner
            for row_index in range(0, self.height-3):
                if self.data[row_index][col] == ox and \
                self.data[row_index+1][col+1] == ox and \
                self.data[row_index+2][col+2] == ox and \
                self.data[row_index+3][col+3] == ox:
                    return True

        for col in range(3, self.width): #starting at (3,0)-- upper right middle
            for row_index in range(0, self.height-3):
                if self.data[row_index][col] == ox and \
                self.data[row_index+1][col-1] == ox and \
                self.data[row_index+2][col-2] == ox and \
                self.data[row_index+3][col-3] == ox:
                    return True

        return False

#d = Board(7, 6)
#d.setBoard("65543443323")
#print(d)
#print(d.winsFor('O'))

    def hostGame(self):
#ask for user input on column
#alternate between X and O for actions
#whileTrue: if not winsFor?
#at end, check winsFor
        nextChar = "X"
        while True:
            print(self)
            person_col = -1
            while self.allowsMove(person_col) == False:
                person_col = input("It's "+ nextChar + "'s turn. Enter a column: ")
                person_col = int(person_col)
            self.addMove(person_col, nextChar)   #adds character to board
            if self.winsFor(nextChar): #if char has won
                print(self)
                print(nextChar + " has won!")
                break
            if self.isFull():
                print("The board is full. Game is over.")
                break
            if nextChar == "X":
                nextChar = "O"
            else:
                nextChar = "X"

d = Board(7, 6)
d.hostGame()








