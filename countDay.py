fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

dayDict = dict()

for line in fhand:
    if line.startswith('From'):
        words = line.split()
        if (words[0] == 'From:') : continue
        #for c in words :
        day = words[2]
        #print('day:', day)
        dayDict[day] = dayDict.get(day,0) + 1

print(dayDict)
