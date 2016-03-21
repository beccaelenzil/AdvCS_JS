#Rational class describes a template for manufacturing a new type of data
#Factory instantiates objects of that type
#Each object has its own attributes (variables)-- in this cases numerator and denominator, each with own values

class Rational:
    def __init__(self, num, denom):
        self.numerator = num
        self.denominator = denom

    def add(self, other):
        newNumerator = self.numerator * other.denominator + self.denominator * other.numerator
        newDenominator = self.denominator*other.denominator
        return Rational(newNumerator, newDenominator)

    def __eq__(self, other):
        return self.numerator * other.denominator == self.denominator *  other.numerator

    #def __ge__(self, other):
        #return self.numerator * other.denominator >= self.denominator * other.numerator

    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)

#simplify self by finding GCF for fraction, if GCF == 1, return imput; if
#no GCF, return imput; if 0?
#look from N to 2
    def simplify(self, num, denom):
        a = min(num, denom)
        for n in range(a, 1, -1):
            if num%n == 0 and denom%n == 0:
                self.num /= n
                self.denom /= n
                break
d = Rational(10, 20)
d.simplify()
print(d)

