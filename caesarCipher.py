#Name: Aadit Bhatia
#Date Started: 3/5/2026
#Date Finished: 
#Description:


#1: We need to initialize our variables to start with.
alphabetSet = "abcdefghijklmnopqrstuvwxyz"
partialOne = ""
partialTwo = ""
newAlphabet = ""

#2: Set up inputs for the program to take a message to shift and the # of places to shift each letter by

message = input("Please enter the message you wish to encrypt: ")
key = input("Please enter the # of places for the encryption to jump by")

#3: Create the newAlphabet with the partial system
#Two parts of the alphabet, bisecting the alphabetSet string at the index # key, and putting the earlier/later half in partialOne and vice versa
#earlier/later depends entirely on whether key is positive or negative...
if key == 0:
    newAlphabet = alphabetSet #this handles the case where the user doesn't want to encrypt
elif key > 0:
    partialOne = alphabetSet[:key] #sets PartialOne to the alphabetSet's beginning, up until the letter designated by key
    partialTwo = alphabetSet[key:] # sets partialTwo to the index # in alphabetSet, until the end
    newAlphabet = partialTwo + partialOne
else:
    partialOne = alphabetSet[:(26 + key)]
    partialTwo = alphabetSet[key:(26 + key)]
    newAlphabet = partialTwo + partialOne
#4: Switch the message into code

encrypted = ""

#Writing a extensive for loop that looks at each letter in message and switches it to a letter in alphabetSet based on key

for message_index in range(0, len(message)):
    if message[message_index] == "":         #there is no alphabetical character at message_index
        encrypted += ""
    for alphabet_index in range(0, (len(alphabetSet))):
        if message[message_index] == alphabetSet[alphabet_index]:
            encrypted += newAlphabet[alphabetIndex]
print(encrypted)