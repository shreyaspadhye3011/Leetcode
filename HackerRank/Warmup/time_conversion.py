# https://www.hackerrank.com/challenges/time-conversion/problem
def timeConversion(s):
    hour = s[:2]
    remaining = s[2:-2]
    timeOfDay = s[-2:]
    if timeOfDay == 'PM':
        hour_val = int(hour)
        if hour_val != 12:
            hour = hour_val + 12
    elif timeOfDay == 'AM':
        if hour == '12':
            hour = '00'
    return str(hour) + remaining
    