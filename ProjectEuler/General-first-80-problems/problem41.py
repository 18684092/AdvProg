###############
# Problem 41  #
###############

"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""
import time, math
from primes import *
print("Problem 41")
start = time.time()

# trial and error 
# 7+6+5+4+3+2+1 = 28 is not divisible by 3

for prime in range(7654321,0, -2):
    if ''.join(sorted(str(prime))) == "1234567":
        if isAPrimeNumber(prime):
            break

end = time.time()
print("The largest prime is ",prime)
print("Time taken:", int((end - start)*10000) / 10000, "Seconds")
print()
