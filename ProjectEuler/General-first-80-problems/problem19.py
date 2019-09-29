##############
# Problem 19 #
##############

# Obviously the wrong way of doing this!!!
# But it works. Brute force rather than maths.

"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

# Dictionary of days in month
months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

def isLeap(year):
    # Returns True if int(year) is a leap year
    year = int(year)
    leap = False
    if (year % 4 == 0):
        leap = True
        if (year % 100 == 0) and (year % 400 != 0):
            leap = False
    return(leap)

numberSundays = 0
weekDay = 0 # Sunday

for y in range(1900, 2001):
    for m in range(1, 13):
        daysInMonth = months[m]
        if isLeap(y) and m == 2:
            daysInMonth += 1
        for d in range(1, daysInMonth + 1):
            weekDay += 1
            if weekDay == 7:
                if d == 1 and y != 1900:
                    numberSundays += 1
                weekDay = 0
print("Counting Sundays: ",numberSundays)
