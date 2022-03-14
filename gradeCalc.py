def computegrade(score):
    if (score >= 0.9):
        grade = 'A'
    elif score >= 0.8:
        grade = 'B'
    elif score >= 0.7:
        grade = 'C'
    elif score >= 0.6:
        grade = 'D'
    else:
        grade = 'F'
    return grade

scoreStr = input('Enter score: ')
#add comment to change file.
try:
    score = float(scoreStr)
    if (score >= 0.0) and (score <= 1.0):
        thisGrade = computegrade(score)
        print(thisGrade)
    else:
        print('Bad score')
except:
    print('Bad score')
