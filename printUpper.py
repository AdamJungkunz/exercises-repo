fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
count = 0
for line in fhand:
    #line = line.rstrip()
    lineUpper = line.rstrip().upper()
    print(lineUpper)
