str = 'X-DSPAM-Confidence:0.8475'

index = str.find(':')

numStr = str[index+1:]

number = float(numStr)

print(number)

#print(number * 10)
