###############
# Problem 80  #
###############

"""
It is well known that if the square root of a natural number is not an integer, then it is irrational. The decimal expansion of such square roots is infinite without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.
"""
import time, math
from decimal import *
getcontext().prec = 110
print("Problem 80")

start = time.time()
total = 0
for n in range(1,101):
    nStr = str(Decimal(n).sqrt())[0:101]
    if len(nStr) > 2:
        for digit in nStr:
            if digit != ".":
                total += int(digit)

end = time.time()
print("Square root digital exspansion",total)
print("Time taken:", int((end - start)*100) / 100, "Seconds")
print()
