def decode(string):
    if len(string) == 0:                                            #if an empty string is pass
        return string                                               #return it back, no operations need to be done
    decoding = ''                                                   #initializing decoding variable    
    number = ''                                                     #initializing a placeholder for numbers
    for i in range(0,len(string)):                                  #for each character in the string
        if string[i].isdigit():                                     #if the character is a digit
            number = number + string[i]                             #append it to the number variable
        else:                                                       #if the character is a letter
            if number == '':                                        #if there are no stored numbers
                decoding = decoding + string[i]                     #add this letter to the decoding string
            else:                                                   #if there is a stored number
                decoding = decoding + int(number)*string[i]         #add this letter to the decoding string [number] times
                number = ''                                         #resets number variable
    return decoding                                                 #return the decoding string        

def encode(string):
    if len(string) == 0:                                            #if an empty string is passed
        return string                                               #return it back, no operations need to be done
    encoding = ''                                                   #initializes the encoding variable    
    count = 1                                                       #initializes the counter
    for i in range(0,len(string)):                                  #Iterates through all the characters in the string
        if i == len(string)-1:                                      #At the last character in the string
            if string[i] == string[i-1]:                            #If the last character matches the previous one
                encoding = encoding + str(count) + string[i]        #adds the encoding
            else:                                                   #If the last character does not match the previous one
                encoding = encoding + string[i]                     #adds the encoding
            return encoding                                         #returns encoding string
        if string[i] == string[i+1]:                                #If the next character is the same as the current one
            count+=1                                                #adds one to the counter
        else:                                                       #If the next character is different than the current one
            if count == 1:                                          # If this character has no consecutive twins
                encoding = encoding + string[i]                     #adds the encoding
            else:                                                   #If this character has consecutive twins
                encoding = encoding + str(count) + string[i]        #adds the encoding
                count = 1                                           #resets the counter        