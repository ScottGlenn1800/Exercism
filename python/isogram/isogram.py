def is_isogram(string):
    isogram = []
    for letter in string:
        if letter not in isogram: 
            if letter != '-' and letter != " ":
                if letter.upper() not in isogram and letter.lower() not in isogram:
                    isogram.append(letter)
                return False
        return False
    return True