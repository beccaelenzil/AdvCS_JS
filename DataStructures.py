class Stack:
    def __init__(self):
        self.items= []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
         self.items.append(item)

    def pop(self):
        item = self.items[-1]
        del self.items[-1]
        return item

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

s = Stack()

#print(s.isEmpty())
#s.push(4)
#s.push('dog')
#print(s.peek())
#s.push(True)
#print(s.size())
#print(s.isEmpty())
#s.push(8.4)
#print(s.pop())
#print(s.pop())
#print(s.size())

def parenChecker(parenString): #returns true if parenthesis are balances, else false
    s = Stack()
    for paren in parenString:
        if paren == "(":
           s.push(paren)
        elif paren == ")":
            if s.isEmpty():
                return False
            else:
                s.pop()
    if s.isEmpty():
        return True
    else:
        return False

def matches(removed_p, top_p):
    if removed_p == top_p:
        return True
    else:
        return False

#work in progress
def balSymChecker(parenString):
    s = Stack()
    for paren in parenString:
        if paren == "(":
            s.push(paren)
        elif paren == ")":
            if s.isEmpty():
                return False
            elif matches(paren, s.peek()):
                s.pop()
        elif paren == "[":
            s.push(paren)
        elif paren == "]":
            if s.isEmpty():
                return False
            elif matches(paren, s.peek()):
                s.pop()
        elif paren == "{":
            s.push(paren)
        elif paren == "}":
            if s.isEmpty():
                return False
            elif matches(paren, s.peek()):
                s.pop()
    if s.isEmpty():
        return True
    else:
        return False

print balSymChecker("{([])}")
