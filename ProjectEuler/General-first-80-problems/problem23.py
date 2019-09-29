##############
# Problem 23 #
##############
"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

def properDivisors(n):
    # Returns a str of "perfect", "deficient", "abundant" if the sum
    # of the proper divisors is equal to n, < n or > n
    s = 0
    for i in range(1, int(n * 0.5) + 1):
        if n % i == 0:
            s += i
    if s == n:
        out = "perfect"
    elif s > n:
        out = "abundant"
    elif s < n:
        out = "deficient"
    return(out)

import time
start = time.time()
abundantNumbers = []
maximum = 28214
# append dummy (we won't use [0])
abundantNumbers.append(False)

# Get all abundant numbers
for i in range(1, maximum):
    if properDivisors(i) == "abundant":
        abundantNumbers.append(i)

# Make blank list
canBe = [False for i in range(maximum)]

# Mark which numbers can be summed
for i in range(1, len(abundantNumbers)):
    for j in range(i, len(abundantNumbers)):
        if abundantNumbers[i] + abundantNumbers[j] < maximum:
            canBe[abundantNumbers[i] + abundantNumbers[j]] = True            
        else:
            break

# Now sum all non abundant
s = 0
for i in range(1, maximum):
    if canBe[i] == False:
        s += i

print("Non Abundant Sums: ", s)
end = time.time()
print("Time taken:", int((end - start) * 100) / 100)
