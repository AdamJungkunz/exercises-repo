def listToString(s):
    # initialize and empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

    # return string
    return str1

# test code
s = ['39722']
print(listToString(s))
