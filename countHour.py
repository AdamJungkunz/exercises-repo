fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

hourDict = dict()

for line in fhand:
    if line.startswith('From'):
        words = line.split()
        if (words[0] == 'From:') : continue
        #for c in words :
        timeStamp = words[5]
        (hour, min, sec) = timeStamp.split(':')
        #print('day:', day)
        hourDict[hour] = hourDict.get(hour,0) + 1

# Chapter 10, Exercise 2


hourList = list()

for key, val in list(hourDict.items()):
    hourList.append((key, val))

hourList.sort()

#(val, key) = senderList[0]
for key, val in hourList :
    print(key, val)
