# Chapter 6, Exercise 1
# 3/2/2022

inp = input('Input a character string: ')

index = len(inp)

while index > 0:
    letter = inp[index-1]
    print(letter)
    index = index - 1
