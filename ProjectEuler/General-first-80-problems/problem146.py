################
# Problem 146  #
################

"""
The smallest positive integer n for which the numbers n2+1, n2+3, n2+7, n2+9, n2+13, and n2+27 are consecutive primes is 10. The sum of all such integers n below one-million is 1242490.

What is the sum of all such integers n below 150 million?
#676333270
"""
import time
# My own module - runs pypy3 in 6131.67 Seconds
from primes import isAPrimeNumber
# Not my module isPrime - runs pypy3 in 5.5 seconds
from rabinmiller import *
print("Problem 146")

start = time.time()
check = [1,3,7,9,13,27]
# Depending on the isPrime checking function this group may be expanded to primes upto 4000. Some primes
# are purposely missed out because they would match n * n + c
quickTest = [17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,541,547,557,563,569,571,577,587,593,599,631,641,643,647,653,659,661,673,677,683,691,733,739,743,751,757,761,769,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997,1031,1033,1039,1049,1051,1061,1063,1069,1087,1091,1093,1097,1129,1151,1153,1163,1171,1181,1187,1193,1229,1231,1237,1249,1259,1277,1279,1283,1289,1291,1297,1361,1367,1373,1381,1399,1409,1423,1429,1433,1439,1447,1451,1453,1459,1471,1481,1483,1487,1489,1493,1499,1511,1523,1531,1543,1549,1553,1559,1567,1571,1579,1583,1597,1637,1657,1663,1667,1669,1693,1697,1699,1733,1741,1747,1753,1759,1777,1783,1787,1789,1831,1847,1861,1867,1871,1873,1877,1879,1889,1931,1933,1949,1951,1973,1979,1987,1993,1997,1999,2029,2039,2053,2063,2069,2081,2083,2087,2089,2099,2129,2131,2137,2141,2143,2153,2161,2179,2237,2239,2243,2251,2267,2269,2273,2281,2287,2293,2297,2333,2339,2341,2347,2351,2357,2371,2377,2381,2383,2389,2393,2399,2437,2441,2447,2459,2467,2473,2477,2531,2539,2543,2549,2551,2557,2579,2591,2593,2633,2647,2657,2659,2663,2671,2677,2683,2687,2689,2693,2699,2729,2731,2741,2749,2753,2767,2777,2789,2791,2797,2833,2837,2843,2851,2857,2861,2879,2887,2897,2927,2939,2953,2957,2963,2969,2971,2999,3037,3041,3049,3061,3067,3079,3083,3089,3137,3163,3167,3169,3181,3187,3191,3221,3229,3251,3253,3257,3259,3271,3299,3329,3331,3343,3347,3359,3361,3371,3373,3389,3391,3433,3449,3457,3461,3463,3467,3469,3491,3499,3529,3533,3539,3541,3547,3557,3559,3571,3581,3583,3593,3631,3637,3643,3659,3671,3673,3677,3691,3697,3733,3739,3761,3767,3769,3779,3793,3797,3833,3847,3851,3853,3863,3877,3881,3889,3929,3931,3943,3947,3967,3989]
total = 0
# Optimisations:
# start at 10 and increment by 10 because n * n must be even and mod 2 , 5 & 10 (my own work)
# n * n must be mod 3 == 1, mod 7 == 2 or 3 (my own work)
# n * n mod 9, 13 & 27 must not be 0 (not mine)
# quick check n * n + {1,3,7,9,13,27} against small group of primes. Speeds up massively (my own work)
# Finally a deterministic Rabin-Miller test is used for Primality test but before that a test
# is done to see if the number is not prime (rules out 1/3 of non primes)
for n in range(10,150000000, 10): # step 10 saves 41.5 seconds
  nn = n * n
  # These were determined by analysing the results of upto 10,000,000
  if nn % 7 != 2 and nn % 7 != 3: continue # saves 13 seconds
  if nn % 9 == 0 or nn % 13 == 0 or nn % 27 == 0: continue # saves 0.5 seconds
  if nn % 3 != 1: continue # saves very little 0.1 seconds
  # Do quick check - saves about 38 seconds
  failed = False
  for p in quickTest:
    for c in check:
      if (nn + c) % p == 0:
        failed = True
        break
    if failed: break
  if failed: continue
  # The actual F(n) tests - a good primality test is essential!
  if isPrime(nn + 1):
    if isPrime(nn + 3):
      if isPrime(nn + 7):
        if isPrime(nn + 9):
          if isPrime(nn + 13):
            if isPrime(nn + 27): # This line and ...
              if not isPrime(nn + 19) and not isPrime(nn + 21): # this line saves about 0.1s in this order
                total += n

print("The sum of all integers below 150,000,000 is", total)
end = time.time()
print("Time taken:", int((end - start)*100) / 100, "Seconds")
print()
