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
        if word not in counts :
            counts[word] = 1
        else:
            counts[word] += 1
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

for key, val in lst[:10]:
    print(key, val)
