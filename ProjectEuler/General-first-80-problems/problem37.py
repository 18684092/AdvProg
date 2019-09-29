##############
# Problem 37 #
##############
"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""
import time
from primes import *

def makeTruncatedSet(prime):
    tSet = []
    p = str(prime)
    for digit in range(len(p) -1):
        d = p[1:]
        if int(d) % 2 == 0 and int(d) != 2:
            return([])
        tSet.append(int(d))
        p = d
    p = str(prime)
    for digit in range(len(p) - 1):
        d = p[:-1]
        if int(d) % 2 == 0 and int(d) != 2:
            return([])
        tSet.append(int(d))
        p = d
    return(tSet)

start = time.time()
total = 0
setCount = 0
for prime in prime_numbers:
    if prime <= 7:
        continue
    # we know there are only 11
    if setCount == 11:
        break
    primeTest = makeTruncatedSet(prime)
    # Also skip if there is an even truncated number
    if len(primeTest) == 0:
        continue
    truncatable = True
    for number in primeTest:
        if not number in prime_numbers:
            truncatable = False
            break
    if truncatable:
        total += prime
        setCount += 1
        
end = time.time()
print("Sum of all 11 truncatable primes", total)
print("Time taken:", int((end-start) * 100) / 100, "Seconds")
