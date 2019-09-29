###############
# Problem 53  #
###############

"""
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,

nCr = n! / r!(n−r)!
,where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.
It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are greater than one-million?
"""
import time, math
print("Problem 53")

start = time.time()
def nCr(n, r):
    combinations = math.factorial(n) / (math.factorial(r) * math.factorial(n - r))
    return(combinations)

end = time.time()
count = 0
for n in range(1, 101):
    for r in range (1, n + 1):
        combinations = nCr(n,r)
        if combinations > 1000000:
            count += 1

print("There are ",count, "values of nCr > 1000000")
print("Time taken:", int((end - start)*100) / 100, "Seconds")
print()
