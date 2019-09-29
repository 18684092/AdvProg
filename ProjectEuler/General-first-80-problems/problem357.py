################
# Problem 357  #
################

"""
Consider the divisors of 30: 1,2,3,5,6,10,15,30.
It can be seen that for every divisor d of 30, d+30/d is prime.

Find the sum of all positive integers n not exceeding 100 000 000
such that for every divisor d of n, d+n/d is prime.
"""
import time
from primes import primesieve

print("Problem 357")

start = time.time()
# because we miss the first n (1 + 1 / 1 == prime)
total = 1
# Generate list of primes
p = primesieve(100000000)
def prime(n):
    # n will be even so the range for divisors is n /2
    # n / 2 can't be even. The biggest prime therefore
    # will be sqrt(n) 
    for d in range(1,int(n ** 0.5)+1):
        # is d a divisor?
        if n % d == 0:
            # if so does it qualify?
            # we are dealing with ints and // is quicker than /
            if (d + n // d) not in p:
                return(False)
    return(True)
# n has to be even
for n in range(0,100000001, 2):
    # as it turns out n + 1 is a prime when n satisfies
    # d + n / d
    if n + 1 in p:
        if prime(n):
            total += n

print("Sum of all positive integers",total)
end = time.time()
print("Time taken:", int((end - start)*100) / 100, "Seconds")
print()
