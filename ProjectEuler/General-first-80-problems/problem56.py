###############
# Problem 56  #
###############

"""
A googol (10**100) is a massive number:
one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a**b, where a, b < 100, what is the maximum digital sum?

"""
import time, math
print("Problem 56")

start = time.time()
largest = 0
for a in range(100):
    for b in range(100):
        total = 0
        digits = str(a ** b)
        for d in digits:
            total += int(d)
        if total > largest:
            largest = total

end = time.time()
print("The largest powerful digit sum is ",largest)
print("Time taken:", int((end - start)*100) / 100, "Seconds")
print()
