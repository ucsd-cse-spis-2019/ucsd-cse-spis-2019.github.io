def mylen(s):
    if s == "":
        return 0
    else:
        return 1+mylen(s[1:])


def mylenBad(s):
    if s == "":
        print(str(0))
    else:
        print(str(1+mylen(s[1:])))
        
# Will the code above cause an index out of bounds error when run on
# the empty string
# A. Yes
# B. No


def sajak(s):
    if s == "":
        return 0
    # don't really need else because the if returns,
    # and will abort the functions
    elif isVowel(s[0]):
        return 1 + sajak(s[1:])
    else:
        return sajak(s[1:])
    # Short way to do it, but maybe confusing, so not recommended
    # return int(isVowel(s[0])) + sajak(s[1:])
    
def isVowel(letter):
    return letter in 'aeiou'
