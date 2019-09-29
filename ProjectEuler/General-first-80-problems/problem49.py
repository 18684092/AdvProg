##############
# Problem 49 #
##############
"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?.
"""
import time
from primes import *

def primePermutations():
    primes = set()
    for p1 in range(1229):
        firstPrime = sorted(str(prime_numbers[p1]))
        if len(firstPrime) >= 4 and not prime_numbers[p1] in primes:
            if (firstPrime[0] != "0"):
                for p2 in range(p1 + 1, 1229):
                    secondPrime = sorted(str(prime_numbers[p2]))
                    if secondPrime == firstPrime and prime_numbers[p2] - prime_numbers[p1] == 3330:
                        for p3 in range(p2 + 1, 1229):
                            thirdPrime = sorted(str(prime_numbers[p3]))
                            if thirdPrime == firstPrime and prime_numbers[p3] - prime_numbers[p2] == 3330:
                                primes.add(prime_numbers[p1])
                                print("Concatenated")
                                print(prime_numbers[p1],end="")
                                print(prime_numbers[p2],end="")
                                print(prime_numbers[p3])
                                print()
                                if len(primes) == 2:
                                    print("The two primes that have 4 digit permutations 3330 apart are:")
                                    print(primes)
                                    return
start = time.time()
primePermutations()
end = time.time()
print("Time taken: ", int((end-start)*100)/ 100, "Seconds")

