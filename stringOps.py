def chop(strInp):
    length = len(strInp)
    print('Length:', length)
    lastChar = strInp[length-1]
    print('Last Char:', lastChar)
    strInp = strInp.rstrip(lastChar)
    print(strInp)
    firstChar = strInp[0]
    print('First Char:', firstChar)
    strInp = strInp.lstrip(firstChar)
    print(strInp)
    #del strInp[length-1]
    #del strInp[0]
    return strInp

str = input('Enter a string: ')
test = chop(str)

print('Chopped string:', str)
print('Returned value:', test)
