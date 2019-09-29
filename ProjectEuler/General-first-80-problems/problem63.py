###############
# Problem 63  #
###############

"""
The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 134217728=89, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""

# So the easy answer is the sum over i from 2 to 9 of (int)(i/log(i)) plus 1. The extra 1 is for 1^1 since log of 1 is zero we can't divide by zero.
# Obviously I didn't know that and brute force can't do it. 
import time, math
print("Problem 63")

start = time.time()

count = 0
for n in range(2, 9):
    count += int(n/math.log10(n))

end = time.time()
print("There are",count + 1,"powerful numnbers")
print("Time taken:", int((end - start)*100) / 100, "Seconds")
print()
