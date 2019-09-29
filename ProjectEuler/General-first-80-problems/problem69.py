###############
# Problem 69  #
###############

"""
Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of numbers less than n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.

n	Relatively Prime	φ(n)	n/φ(n)
2	1	1	2
3	1,2	2	1.5
4	1,3	2	2
5	1,2,3,4	4	1.25
6	1,5	2	3
7	1,2,3,4,5,6	6	1.1666...
8	1,3,5,7	4	2
9	1,2,4,5,7,8	6	1.5
10	1,3,7,9	4	2.5
It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.
"""

import time
print("Problem 69")

start = time.time()

def phi(n) :
    result = n 
    # Consider all prime factors
    # of n and for every prime
    # factor p, multiply result with (1 - 1 / p)
    p = 2
    while(p * p <= n) :
        # Check if p is a prime factor.
        if (n % p == 0) :
            # If yes, then update n and result
            while (n % p == 0) :
                n //= p # int division is quicker
            result *= (1 - (1 / p))
        p = p + 1
    # If n has a prime factor
    # greater than sqrt(n)
    # (There can be at-most one
    # such prime factor)
    if (n > 1) :
        result *= (1 - (1 / n))
    return(result)

m = 0
q = 0
for n in range(10,1000000,10):
  Qn = phi(n)
  nQn = n / Qn
  if nQn > q:
    q = nQn
    m = n

print("Maximum ratio is when n =", m)
  
end = time.time()
print("Time taken:", int((end - start)*100) / 100, "Seconds")
print()
