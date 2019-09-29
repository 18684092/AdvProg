##############
# Problem 27 #
##############
"""
Quadratic Primes 

Euler discovered the remarkable quadratic formula:

n2+n+41
It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39. However, when n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41 is clearly divisible by 41.

The incredible formula n2−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n2+an+b, where |a|<1000 and |b|≤1000

where |n| is the modulus/absolute value of n
e.g. |11|=11 and |−4|=4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.
"""

import time
# My own prime number module
from primes import *

start = time.time()

# Stores for the best co-efficients
bA = bB = bY = cP = 0

# Brute force it, is there another way?
# This satisfies under 1 minute so is good (about 1.3 seconds)...
# It says |a| and |b| suggesting range might be negative
for a in range(-1000, 1000):
    for b in range(-1000, 1001):
        # Optimisation: primes must be odd so both a and b can't be even
        if not a % 2 and not b % 2:
            break
        # optimisation: b should be a prime (doubles speed)
        if not isAPrimeNumber(b) or a > b:
            continue
        nPrimes = 0
        # Don't know how many primes we'll find
        for n in range(1000000):
            # Quadratic equation
            y = (n * n) + (a * n) + b 
            if isAPrimeNumber(y):
                nPrimes += 1
                if nPrimes > cP:
                    bA = a
                    bB = b
                    cP = nPrimes
            else:
                break

end = time.time()
print("a:",bA,"b:",bB,"Consecutive primes:",cP)
print("Product of a and b", bA * bB)
print("Time taken: ", int((end - start) * 100) / 100, "Seconds")
print()
