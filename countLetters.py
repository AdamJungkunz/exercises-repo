import string

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

counts = dict()

for line in fhand:
    # Split line into words
    #line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    #print('words:', words)
    for word in words:
        # Check if word is already in list
        #print('word:', word)
        letters = tuple(word)
        for letter in letters :
            if letter.isalpha() == False : continue
            if (letter not in counts) :
                counts[letter] = 1
            else:
                counts[letter] += 1
        # Add new word to list
        #wordList.append(word)

#origWordList = wordList[:]
#wordList.sort()

#print(counts)

# Sort the dictionary by value
lst = list()
for key, val in list(counts.items()):
    lst.append((val, key))

lst.sort(reverse=True)

for val, key in lst:
    print(key)
