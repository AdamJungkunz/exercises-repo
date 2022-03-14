def chop(listInp):
    length = len(listInp)
    del listInp[length-1]
    del listInp[0]

def middle(secondList):
    length = len(secondList)
    return secondList[1:length-1]

t = [1, 32, 56, 982]
print('Initial list:', t)
test = chop(t)

print('Chopped list:', t)
print('Returned value:', test)

s = [2, 1987, 2012, 1982]
print('Initial list:', s)
test = middle(s)

print('Original list:', s)
print('Returned value:', test)
