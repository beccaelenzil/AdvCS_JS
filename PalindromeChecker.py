def PalindromeChecker(string):
    print string
    if string[0].lower() == string[-1].lower():
        if len(string) <= 2:
            return True
        else:
            return PalindromeChecker(string[1:-1])
    else:
        return False

print(PalindromeChecker("a man a plan a canal panama"))

