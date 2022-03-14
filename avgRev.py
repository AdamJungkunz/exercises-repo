import re

def listToString(s):
    # initialize and empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

    # return string
    return str1

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

lst = list()
#lstint = list()
count = 0

for line in fhand:
    line = line.rstrip()
    x = re.findall('^New Revision: * ([0-9]*)', line)
    #print('type of x is:', type(x))
    if len(x) > 0:
        #lst.append(x)
        #value =
        str1 = listToString(x)
        val = int(str1)
        lst.append(val)

avg = sum(lst)/len(lst)

print(avg)
