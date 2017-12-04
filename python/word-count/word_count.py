import re
def word_count(phrase):
    word_counter = {}
    words = []
    for match in re.finditer("[\w']+",phrase):
        if "_" in match.group(0):
            for word in match.group(0).split("_"):
                words.append(word)
        else:
            words.append(match.group(0).lower().strip("'"))
    for word in words:
        if word not in word_counter:
            word_counter[word] = words.count(word)
    return word_counter