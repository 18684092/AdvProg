###############
# Problem 46  #
###############

"""
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""

import time, math
from primes import isAPrimeNumber
start = time.time()
found = False
composite = 3
primes = set()
while not found:
    if not isAPrimeNumber(composite):
        found = True
        # sum of prime and twice a square
        for prime in range(2, composite - 1):
            if prime in primes:
                upperBound = int(math.sqrt(0.5 *(composite - prime))) + 1
                for square in range(1, upperBound):
                    if prime + 2 * (square * square) == composite:
                        print(str(composite)+" = "+str(prime)+" + 2 x "+str(square)+chr(178))
                        found = False
                        break
            if not found:
                break
    else:
        primes.add(composite)
    composite += 2
end = time.time()
print("Smallest composite that cannot be made by prime + twice a square is",composite - 2)
print("Time taken:", int((end - start)*100) / 100, "Seconds")
print()
