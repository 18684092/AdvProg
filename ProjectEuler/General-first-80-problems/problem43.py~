###############
# Problem 43  #
###############

"""
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
"""
import time
print("Problem 43")

start = time.time()
# get 0 - 9 10 digit pandigital combinations
from pandigitalNumbers import pandigital10
primes = [2,3,5,7,11,13,17]
count = 0
for nStr in pandigital10:
    # Some numbers start with zero
    if len(nStr) == 10 and int(nStr) % 2 != 0:
        match = True
        for i in range(1, 8):
            if int(nStr[i:i + 3]) % primes[i - 1] != 0:
                match = False
                break
        if match:
            count += int(nStr)
    
end = time.time()
print("sum of all 0 to 9 pandigital numbers", count) 
print("Time taken:", int((end - start)*100) / 100, "Seconds")
print()
