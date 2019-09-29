##############
# Problem 34 #
##############

"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""
import time
start = time.time()
# 2,540,160 is the upper bound
# because 9! = 362,880 x 7 digits.
# x 8 still gives us 7 digits and this upper bound
# only speeds things up
# You can double the speed again by caching the factorial results
# for each digit
factorial = {'0':1, '1':1, '2':2, '3':6, '4':24, '5':120, '6':720, '7':5040, '8':40320, '9':362880}
grandTotal = 0
for n in range(3, 2540160):
    # Convert to str to make each digit accessible
    sN = str(n)
    total = 0
    # sum each digit's factorial
    for i in sN:
        total += factorial[i]
    # if total matches the number then sum with any other results
    if total == n:
        grandTotal += total

end = time.time()
print("Digital Factorials Sum:", grandTotal)
print("Time take: ", int((end - start)* 100) / 100, " Seconds")
print()
