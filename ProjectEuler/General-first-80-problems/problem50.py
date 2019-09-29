###############
# Problem 50  #
###############

"""
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?

"""
import time
from primes import *
print("Problem 50")
start = time.time()
prime = {}
target = 1000000
for i in range(10):
    if isAPrimeNumber(i):
        t = c = 0
        for j in range(i, 10000):
            if isAPrimeNumber(j):
                t += j
                c += 1
                if t >= target:
                    break
                if isAPrimeNumber(t):
                    if not t in prime:
                        prime[t] = c

c = n = 0
for p in prime:
    if prime[p] > c and p < 1000000:
        n = p
        c = prime[p]
end = time.time()
print("Consecutive prime sum < 1000000:", n)
print("Time taken:", int((end - start)*100) / 100, "Seconds")
print()
