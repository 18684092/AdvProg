##############
# Problem 52 #
##############
"""
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""
def sortDigits(n):
  numbers = str(n)
  l = []
  for number in numbers:
    l.append(number)
  return(sorted(l))

def cmpLists(l1, l2):
  if len(l1) != len(l2):
    return(False)
  for i,v in enumerate(l1):
    if l1[i] != l2[i]:
      return(False)
  return(True)

def permutedMultiples():
  found = 0
  n = 0
  while not found:
    n += 1
    t1 = sortDigits(n)
    t2 = sortDigits(n*2)
    t3 = sortDigits(n*3)
    t4 = sortDigits(n*4)
    t5 = sortDigits(n*5)
    t6 = sortDigits(n*6)
    if cmpLists(t1, t2) and cmpLists(t1, t3) and cmpLists(t1, t4) and cmpLists(t1, t5) and cmpLists(t1, t6):
      found = 1
  return(n)


print("Problem 52")
print("Permuted multiples 1x 2x 3x 4x 5x 6x: ", permutedMultiples())
print()
