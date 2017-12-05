import re
def hey(phrase):
    if phrase.isspace() or not phrase:          #This satisfies all the "nothing" conditions!
        return"Fine. Be that way!"
    elif phrase.upper() == phrase and re.search("[A-z]",phrase): #This satisfies all the "yelling" conditions!
        return"Whoa, chill out!"
    elif phrase.strip(" ").split(" ")[len(phrase.strip(" ").split(" "))-1][-1] == "?": #This satisfies all the "question" conditions!
        return"Sure."
    else: #This satisfies the "other" conditions!
        return"Whatever."        
    
#If the last character in the statement is a ? then it is a question
#If all characters are in caps then its "yelling"
#If there are not symbols or alphanumeric characters, then it is "saying nothing"

