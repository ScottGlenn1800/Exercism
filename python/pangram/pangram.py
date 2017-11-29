def is_pangram(sentence):
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for word in sentence:
        for letter in word:
            if letter.isalpha() and letter.lower() in letters:
                letters.remove(letter.lower())
    if letters != []:
        return False
    else:
        return True