fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

wordList = []

for line in fhand:
    # Split line into words
    words = line.split()
    #print('words:', words)
    for word in words:
        # Check if word is already in list
        #print('word:', word)
        if word in wordList : continue
        # Add new word to list
        #print('wordList:', wordList)
        wordList.append(word)

origWordList = wordList[:]
wordList.sort()

print(wordList)
