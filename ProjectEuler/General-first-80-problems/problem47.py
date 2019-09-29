##############
# Problem 47 #
##############
"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
"""
import time
from primes import *

def groupFactors(factors):
    fD = {}
    dSet = []
    for item in factors:
        if item in fD:
            fD[item] += 1
        else:
            fD[item] = 1
    for item in fD:
        dSet.append(str(item) + "^" + str(fD[item]) )   
    return(dSet)

start = time.time()

first = 0
consecutive = 0
for number in range(100000,1000000):
    f = primeFactorise(number)
    factors = groupFactors(f)
    if len(factors) == 4:
        consecutive +=1
        if consecutive == 1:
            first = number
        elif consecutive == 4:
            break
    else:
        consecutive = 0
        first = 0

end = time.time()
print("Distinct Prime Factors", first)
print("Time taken:", int((end-start) * 100) / 100, "Seconds")
print()
