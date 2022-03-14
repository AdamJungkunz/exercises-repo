#This file calculates the sum, number of entries, and min and max of entries
# Chapter 5, Exercise 2
# 3/2/2022

inp = 0
numEntries = 0
sumEntries = 0
maxEntries = None
minEntries = None

while inp != 'done':
    inp = input('Enter a number: ')
    try:
        entry = float(inp)
        numEntries = numEntries + 1
        sumEntries = sumEntries + entry
        if (maxEntries == None) or (maxEntries < entry):
            maxEntries = entry
        if (minEntries == None) or (minEntries > entry):
            minEntries = entry
    except:
        print('Invalid input')

print(sumEntries, numEntries, maxEntries, minEntries)
