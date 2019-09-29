###############
# Problem 97  #
###############

"""
The first known prime found to exceed one million digits was discovered in 1999, and is a Mersenne prime of the form 26972593−1; it contains exactly 2,098,960 digits. Subsequently other Mersenne primes, of the form 2p−1, have been found which contain more digits.

However, in 2004 there was found a massive non-Mersenne prime which contains 2,357,207 digits: 28433×27830457+1.

Find the last ten digits of this prime number."""
import time
print("Problem 97")

# To speed up use mod
# print((28433*2**7830457+1) % (10 ** 10))
start = time.time()

p = (28433 * pow(2, 7830457, 10000000000) + 1) % 10000000000

end = time.time()
print("First 10 digits are", p)
print("Time taken:", int((end - start)*100) / 100, "Seconds")
print()
