# python 2
#
# Problem Set 1, Problem 1: Dates


class Date:
    """ a user-defined data structure that
        stores and manipulates dates
    """

    # the constructor is always named __init__ !
    def __init__(self, month, day, year):
        """ the constructor for objects of type Date """
        self.month = month
        self.day = day
        self.year = year


    # the "printing" function is always named __repr__ !
    def __repr__(self):
        """ This method returns a string representation for the
            object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.
        """
        s =  "%02d/%02d/%04d" % (self.month, self.day, self.year)
        return s


    # here is an example of a "method" of the Date class:
    def isLeapYear(self):
        """ Returns True if the calling object is
            in a leap year; False otherwise. """
        if self.year % 400 == 0: return True
        elif self.year % 100 == 0: return False
        elif self.year % 4 == 0: return True
        return False

    def copy(self):
        """ Returns a new object with the same month, day, year
            as the calling object (self).
        """
        dnew = Date(self.month, self.day, self.year)
        return dnew

    def equals(self, d2):
            """ Decides if self and d2 represent the same calendar date,
                whether or not they are the in the same place in memory.
            """
            if self.year == d2.year and self.month == d2.month and self.day == d2.day:
                return True
            else:
                return False

    def tomorrow(self):
        """
        Changes the calling object so it represents one
        calendar day after the date it originally represented
        Ex: Feb 4 to Feb 5
        """
        if self.isLeapYear():
            fdays = 29
        else:
            fdays = 28
        dim = [0,31,fdays,31,30,31,30,31,31,30,31,30,31]

        if self.day > dim[self.month]:
            return "Invalid entry"

        #conditions for special cases
        if self.month == 12 and self.day == 31:
            self.month = 1
            self.year += 1
            self.day = 1
        elif self.day == dim[self.month]:
            self.day = 1
            self.month += 1

        #regular cases
        else:
            self.day += 1
        return self

#Test
#d = Date(4, 31, 2012)
#print(d.tomorrow())

#This should change the calling object so it represents
#one calendar day before the date it represented

    def yesterday(self):
        #leap year cases
        if self.isLeapYear():
            fdays = 29
        else:
            fdays = 28
        dim = [0,31,fdays,31,30,31,30,31,31,30,31,30,31]

        #user error
        if self.day > dim[self.month] or self.month > 12:
            return "Invalid Entry"

        #conditions for special cases
        if self.day == 1 and self.month == 1:
            self.day = 31
            self.month = 12
            self.year -= 1

        elif self.day == 1:
            self.day = dim[self.month - 1]
            self.month -= 1

        #regular cases
        else:
            self.day -= 1
        return self

    def addNdays(self, N):
        #self is the instance of the class that you make
        #user error
        if N < 0:
            return "Invalid Input: N must be non-negative"
        #normal
        for i in range(0,N):
            print(self)
            self.tomorrow()
        print(self)

    def subNDays(self, N):
        #user error
        if N < 0:
            return "Invalid Input: N must be non-negative"

        for i in range(0,N):
            self.yesterday()
        print(self)

    def isBefore(self, d2):






