###############
# Problem 381 #
###############

"""
For a prime p let S(p) = (∑(p-k)!) mod(p) for 1 ≤ k ≤ 5.

For example, if p=7,
(7-1)! + (7-2)! + (7-3)! + (7-4)! + (7-5)! = 6! + 5! + 4! + 3! + 2! = 720+120+24+6+2 = 872.
As 872 mod(7) = 4, S(7) = 4.

It can be verified that ∑S(p) = 480 for 5 ≤ p < 100.

Find ∑S(p) for 5 ≤ p < 108.
"""
import time, math
from primes import *
print("Problem 381")

start = time.time()



def S(p):
    pK = 0
    for k in range(1, 6):
        pK += math.factorial(p-k)
    sP = pK % p
    return(sP)

primeFactorialSum = 0
for p in range(5,1000 + 1, 2):
  if isAPrimeNumber(p):
    s = S(p)
    print(p, s)  
    primeFactorialSum += s



end = time.time()
print("Prime-k Factorial", primeFactorialSum)
print("Time taken:", int((end - start)*100) / 100, "Seconds")
print()
