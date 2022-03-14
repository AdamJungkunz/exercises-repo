# Prompt user for file name to open
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

# Initialize counting and summation variables
count = 0
sumSpam = 0
# Initialize spam confidence string parameters
spamStr = 'X-DSPAM-Confidence:'
lenSpam = len(spamStr)

# Check lines for spam confidence string
for line in fhand:
    if line.find(spamStr) == -1: continue
    #print('Line is: ', line)
    count = count + 1
    #print('Count is: ',count)
    index = line.find(spamStr) + lenSpam
    #print('Index is: ',index)
    currSpam = float(line[index:index + 7])
    #print('currSpam is: ',currSpam)
    sumSpam = currSpam + sumSpam
    #print('sumSpam is: ',sumSpam)

avgSpam = sumSpam / count

print('Average spam confidence:', avgSpam)
    #lineUpper = line.rstrip()
    #print(lineUpper)
