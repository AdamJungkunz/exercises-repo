def count(inString, letter):
  countLetter = 0
  for character in inString:
      if character == letter:
          countLetter = countLetter + 1
  return countLetter

inputString = input('Enter a character string: ')
inputLetter = input('Enter the letter to count: ')
numLetter = count(inputString, inputLetter)

print(numLetter)
