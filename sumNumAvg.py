#This file calculates the sum, number of entries, and average of entries
# Chapter 5, Exercise 1
# 3/2/2022

inp = 0
numEntries = 0
sumEntries = 0
#print(sumEntries)

while inp != 'done':
    inp = input('Enter a number: ')
    try:
        entry = float(inp)
        numEntries = numEntries + 1
        sumEntries = sumEntries + entry
        avgEntries = sumEntries / numEntries
    except:
        print('Invalid input')

print(sumEntries, numEntries, avgEntries)
