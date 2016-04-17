import random

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
        if col < 0 or row < 0 or col >= 3 or row >= 3: #column and rows can only be within range of tic-tac-toe board
            return False
        elif self.data[row][col] != " ":
            return False
        else:
            return True

    def isFull(self): #Returns True if the entire board is filled
        for col in range(3):
            for row in range(3):
                if self.data[row][col] == " ":
                    return False
        return True

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
        nextChar = "X"
        while True:
            print(self)

            person_col = raw_input("Player "+ nextChar + ": Enter a column between 0 and 2 \n")

            while not person_col.isdigit(): #if player input is not a number
                person_col = raw_input("Player "+ nextChar + ": Enter a column between 0 and 2 \n")
                if person_col.isdigit() == True:
                    person_col = int(person_col)
                    break #stops since it no longer needs to be in this loop; it can go to the next thing
                else:
                    print("Please enter a number!")
                    person_col = raw_input("Player "+ nextChar + ": Enter a column between 0 and 2 \n") #this repeats until the player enters something correct

            person_col = int(person_col) #turns person_col into an integer since raw_input is a string

            person_row = raw_input("Player " + nextChar+ ": Enter a row between 0 and 2 \n")

            while not person_row.isdigit():
                person_row = raw_input("Player " + nextChar+ ": Enter a row between 0 and 2 \n")
                if person_row.isdigit() == True:
                    person_row = int(person_row)
                    break
                else:
                    print("Please Enter a number!")
                    person_row = raw_input("Player " + nextChar+ ": Enter a row between 0 and 2 \n")

            person_row = int(person_row)

            while not self.allowmove(person_col, person_row, nextChar): #if player inputs a full space
                print ("Choose an open space.")
                person_col = input("Player "+ nextChar + ": Enter a column between 0 and 2 \n")
                person_row = input("Player " + nextChar+ ": Enter a row between 0 and 2 \n")

            self.addmove(person_col, person_row, nextChar) #adds move using column and row given by user

            if self.win(nextChar): #if a player wins, tells them and stops
                print(self)
                print "Player " + nextChar + " has won! \n"
                break

            elif self.isFull(): #if the board is filled up completely, tells them and stops
                print("The game is tied! \n")
                break

            else: #switches player
                if nextChar == "X":
                    nextChar = "O"
                elif nextChar == "O":
                    nextChar = "X"

#AI:
#needs to use hostgame to create new host function to play with human vs computer or computer vs computer or human vs human
class BasicPlayer():
    #a basic (dumb) player for tic-tac-toe

    def __init__(self, char):
        self.char = char

    def __repr__(self):
        s = "Basic player for " + self.char + "\n"
        return s

    def random_move(self, b):
        row = random.randrange(3)
        col = random.randrange(3)

        while not b.allowmove(col, row, self.char): #if the randomly chosen space is full
            row = random.randrange(3)
            col = random.randrange(3)

        return (col, row)

def play_game(player_x, player_o):
    if player_x == "basic":
        player_x = BasicPlayer("X")
    elif player_x != "human":
        print("Player must be human or basic")

    if player_o == "basic":
        player_o = BasicPlayer("O")
    elif player_o != "human":
        print("Player must be human or basic")

    d = Board()
    game_player = player_x
    nextChar = "X"

    while True: #repeat of hostgame error-checking
        print(d)
        if game_player == "human": #if it's a human player
            person_col = raw_input("Player "+ nextChar + ": Enter a column between 0 and 2 \n")

            while not person_col.isdigit(): #if player input is not a number
                person_col = raw_input("Player "+ nextChar + ": Enter a column between 0 and 2 \n")
                if person_col.isdigit() == True:
                    person_col = int(person_col)
                    break #stops since it no longer needs to be in this loop; it can go to the next thing
                else:
                    print("Please enter a number!")
                    person_col = raw_input("Player "+ nextChar + ": Enter a column between 0 and 2 \n") #this repeats until the player enters something correct

            person_col = int(person_col) #turns person_col into an integer since raw_input is a string

            person_row = raw_input("Player " + nextChar+ ": Enter a row between 0 and 2 \n")

            while not person_row.isdigit():
                person_row = raw_input("Player " + nextChar+ ": Enter a row between 0 and 2 \n")
                if person_row.isdigit() == True:
                    person_row = int(person_row)
                    break
                else:
                    print("Please Enter a number!")
                    person_row = raw_input("Player " + nextChar+ ": Enter a row between 0 and 2 \n")

            person_row = int(person_row)

            d.addmove(person_col, person_row, nextChar)

        else: #if the player is basic AI
            print("AI")
            s = game_player.random_move(d) #chooses random move
            d.addmove(s[0], s[1], nextChar)

        if d.win(nextChar): #checking if someone has won
            print("Player" + nextChar + " has won!")
            break

        if d.isFull(): #if game tied
            print("Game is tied!")
            break

        if nextChar == "X": #changing player turn
            nextChar = "O"
            game_player = player_o
            print(player_o)
        else:
            nextChar = "X"
            game_player = player_x



play_game("basic", "basic")


#d.addmove(2, 2, "X")
#print(d.allowmove(2, 2, "X"))
#print(d.hostgame())

#d.hostgame()
#column, row, ox
#d.addmove(0, 2, "X")
#d.addmove(1, 1, 'X')
#d.addmove(2, 0, 'O')
#print(d.win('X'))

'''
d = Board()
d.addmove(0, 1, "X")
d.addmove(1, 1, "X")
d.addmove(2, 1, "X")
d.addmove(0, 2, "O")
d.addmove(0, 0, "O")
d.addmove(2, 2, "O")
d.addmove(1, 2, "O")
d.addmove(1, 0, "O")
d.addmove(2, 0, "O")
print(d)
print(d.isFull())
'''
