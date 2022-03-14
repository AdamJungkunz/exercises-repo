fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

senderDict = dict()
domainDict = dict()
maxVal = None
maxSender = None
maxDomain = None
maxValDomain = None

for line in fhand:
    if line.startswith('From'):
        words = line.split()
        if (words[0] == 'From:') : continue
        #for c in words :
        sender = words[1]
        #print('sender:', sender)
        index = sender.find('@')
        #print('index:', index)
        domain = sender[index:]
        senderDict[sender] = senderDict.get(sender,0) + 1
        domainDict[domain] = domainDict.get(domain,0) + 1

# Output for Ch9 Exercise 3
#print(senderDict)

# Find most frequent committer
keyList = list(senderDict.keys())
for key in keyList:
    curVal = int(senderDict[key])
    if (maxVal == None) or (curVal > maxVal):
        maxVal = curVal
        maxSender = key

#print(maxSender, maxVal)

# Find domain with most frequent commits

#keyList = list(domainDict.keys())
#for key in keyList:
#    curVal = int(domainDict[key])
#    if (maxValDomain == None) or (curVal > maxDomainVal):
#        maxValDomain = curVal
#        maxDomain = key
# Output for Ch 9 Exercise 5
print(domainDict)
