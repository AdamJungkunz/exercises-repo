# This file creates a dictionary with keys from a file
# Chapter 9, Exercise 1
# 3/3/2022

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

newDict = dict()

for line in fhand:
    words = line.split()
    #print('Words:', words)
    # For each word, check if it's in the dictionary
    for word in words:
        #print('Word:', word)
        if word in newDict: continue
        #print('Word:', word)
        #print('newDict:', newDict)
        newDict[word] = []

#print(newDict)
