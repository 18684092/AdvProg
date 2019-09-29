##############
# Problem 48 #
##############
"""
The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
"""
s = 0
for i in range(1,1001):
    s = s + i**i
print("The last 10 digits are: ",str(s)[-10:])
print()

