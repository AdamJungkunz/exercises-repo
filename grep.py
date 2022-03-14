
import re
print('$ python grep.py')
regexp = input('Enter a regular expression: ')

fname = 'mbox.txt'
fhand = open(fname)
count = 0;
for line in fhand:
    line = line.rstrip()
    if re.search(regexp, line) :
        count += 1

print('%s had %d lines that matched %s' % (fname, count, regexp))
