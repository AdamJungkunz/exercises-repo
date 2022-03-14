def computepay(hours, rate):
    if hours <= 40.0:
        pay = hours * rate
    else:
        pay = (40  + (hours - 40) * 1.5) * rate
    return pay

hoursStr = (input('Enter Hours: '))
try:
    rateStr = (input('Enter Rate: '))
    hours = float(hoursStr)
    rate = float(rateStr)
    paycheck = computepay(hours, rate)
    print('Pay:', paycheck)
except:
    print('Error, please enter numeric input')
