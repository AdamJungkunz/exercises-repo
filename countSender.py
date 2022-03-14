fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

senderDict = dict()
maxVal = None
maxSender = None

for line in fhand:
    if line.startswith('From'):
        words = line.split()
        if (words[0] == 'From:') : continue
        #for c in words :
        sender = words[1]
        #print('day:', day)
        senderDict[sender] = senderDict.get(sender,0) + 1

# Output for Ch9 Exercise 3
#print(senderDict)

# Find most frequent committer; Ch. 9 Exercise 5
#keyList = list(senderDict.keys())
#for key in keyList:
#    curVal = int(senderDict[key])
#    if (maxVal == None) or (curVal > maxVal):
#        maxVal = curVal
#        maxSender = key

#print(maxSender, maxVal)

# Chapter 10, Exercise 1
# Find max sender and frequency using tuple

senderList = list()

for key, val in list(senderDict.items()):
    senderList.append((val, key))

senderList.sort(reverse=True)

(val, key) = senderList[0]
print(key, val)
