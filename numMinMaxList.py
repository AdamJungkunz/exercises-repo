#This file calculates the sum, number of entries, and min and max of entries
# Chapter 8, Exercise 6
# 3/3/2022

inp = 0
entries = []

while inp != 'done':
    inp = input('Enter a number: ')
    try:
        entry = float(inp)
        entries.append(entry)
    except:
        print('Invalid input')

print('Maximum:', max(entries))
print('Minimum:', min(entries))
