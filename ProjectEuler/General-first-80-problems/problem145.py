###############
# Problem 145 #
###############

"""
Some positive integers n have the property that the sum [ n + reverse(n) ] consists entirely of odd (decimal) digits. For instance, 36 + 63 = 99 and 409 + 904 = 1313. We will call such numbers reversible; so 36, 63, 409, and 904 are reversible. Leading zeroes are not allowed in either n or reverse(n).

There are 120 reversible numbers below one-thousand.

How many reversible numbers are there below one-billion (109)?

"""
import time

def isReversible(number):
    N = str(number)
    # Reverse
    rN = N[::-1]
    
    # must be odd and even starts - optimised
    if not (int(N[0]) % 2 == 0 and int(rN[0]) % 2 != 0):
        if not (int(rN[0]) % 2 == 0 and int(N[0]) % 2 != 0):
            return(False)
    
    # Each digit must be odd
    for digit in str(number + int(rN)):
        if not int(digit) % 2:
            return(False)
    return(True)
    

start = time.time()
print("Problem 145")

reversible = 120
for n in range(999,100000000,2):
    # Optimise by removing zeros in reversed number
    if n % 10 == 0:
        continue
    if isReversible(n):
        reversible += 2
        
end = time.time()
print("There are", reversible, "numbers ")
print("Time taken:", int((end - start)*100) / 100, "Seconds")
print()
