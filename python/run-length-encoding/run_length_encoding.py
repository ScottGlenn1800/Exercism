def decode(string):
    pass


#RIGHT NOW THIS IS WORKING BUT IT IS LOPING OFF THE LAST CHARACTER
def encode(string):
    encoding = ''
    count = 1
    for i in range(0,len(string)-1):
        if i != len(string)-1:
            if string[i] == string[i+1]:count+=1
            elif count == 1:
                encoding = encoding + string[i]
            else:
                encoding = encoding + str(count) + string[i]
                count = 1
    return encoding