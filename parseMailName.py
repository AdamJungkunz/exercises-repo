fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
count = 0
for line in fhand:
    # Check beginning of line to see if it starts with 'From'
    if line.startswith('From'):
        #print(line)
        words = line.split()
        if (words[0] == 'From:') : continue
        print(words[1])
        count = count + 1

print('There were', count, 'lines in the file with From as the first word')
