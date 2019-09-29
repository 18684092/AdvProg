##############
# Problem 30 #
##############
"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""
def digitFifthPowers():
  # upper bound is 6 * 9^5
  fifths = []
  for n in range(10,6 * (9**5)):
    s = str(n)
    total = 0
    for digit in s:
      total += int(digit) ** 5
    if total == n:
      fifths.append(n)
  total = 0
  for n in fifths:
    total += n
    # print(n)
  return(total)

print("Problem 30")
print("Digit Fifth Powers:", digitFifthPowers())
print()
