import re
def hey(phrase):
    if re.search("[A-z]",phrase):
        if phrase.upper() == phrase: #This is true if its only numbers
            print"Whoa, chill out!"
            return"Whoa, chill out!"
        elif phrase[-1] == "?":
            print"Sure."
            return"Sure."
        else:pass
    elif phrase.isspace():
        print"Fine. Be that way!"
        return"Fine. Be that way!"
    else:
        print"Whatever."
        return"Whatever."
    print"I didnt go into anything"
    
hey("Let's go make out behind the gym!")



#If the last character in the statement is a ? then it is a question
#If all characters are in caps then its "yelling"
#If there are not symbols or alphanumeric characters, then it is "saying nothing"

