##############
# Problem 26 #
##############

"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""

longestCycle = 0
longestNumber = 0
longestRecurring = ""
for n in range(1, 1001):
    digitStore = []
    remainder = 1 % n
    pos = 0
    seq = ""
    while pos < n:
        if remainder in digitStore:
            if pos > longestCycle:
                longestCycle = pos
                longestNumber = n
                longestRecurring = seq
            occur = digitStore.index(remainder)
            print("1/"+str(n)+" = 0."+seq[:occur]+"("+seq[occur:]+")")
            break
        r = remainder*10//n
        seq += str(r)
        digitStore.append(remainder)
        remainder *= 10
        remainder %= n
        
        pos += 1
print("Longest Number = ", longestNumber)
print("Longest Cycle = ", longestCycle)
print("Longest Recurring Cycle = ", longestRecurring)
print()
               
        
