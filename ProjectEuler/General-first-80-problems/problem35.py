##############
# Problem 35 #
##############

"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""
import time
from primes import *

def cyclic(n):
    # returns list of cyclic perms
    number = str(n)
    l = []
    for i in range(len(number)):
        # remove the fist add to end
        p = number[1:] + number[0:1]
        number = p
        l.append(p)
    return(l)

def evenFive(prime):
    p = str(prime)
    for digit in p:
        if int(digit) == 5 or (int(digit) % 2 == 0):
            return(True)
    return(False)

start = time.time()
nCircularPrimes = 0
for prime in prime_numbers:
    if prime >= 1000000:
        break
    # check for even digits or a 5
    if prime != 2 and prime != 5:
        if evenFive(prime):
            continue
    print(prime, nCircularPrimes)
    prime_perms = cyclic(prime)
    isCircular = True
    for i in prime_perms:
        if not int(i) in prime_numbers:
            isCircular = False
            break
            
    if isCircular:
        nCircularPrimes += 1
end = time.time()
print("Number of Circular primes under 1000000:", nCircularPrimes)
print("Time taken:", int((end-start) * 100) / 100, "Seconds")
