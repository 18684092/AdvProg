##############
# Problem 79 #
##############
"""
A common security method used for online banking is to ask the user for three random characters from a passcode. For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length.
"""

# 7 3 1 6 2 8 9 0
import time
def shouldWeSwap(numbers, i, j):
  if i == j:
    return(False)
  if str(i) in numbers[j]:
    return(True)
  if len(numbers[j]) == 0:
    return(False)
  return(False)

def passcodeDerivation():
  numbers=[]
  for i in range(10):
    numbers.append(set())
  # read in all numbers and work out which number follows other numbers
  with open("p079_keylog.txt", "r") as f:
    for lines in f:
      a = int(lines[0])
      b = int(lines[1])
      c = int(lines[2])
      numbers[a].add(str(b))
      numbers[b].add(str(c))
  f.close()
  l = set()
  for rows in numbers:
    for i in range(10):
      if str(i) in rows:
        l.add(i)
      if len(numbers[i]) > 0:
        l.add(i)
  l = list(l)
  changed = True
  c = 0
  # move along list repeatedly until no change
  while changed:
    changed = False
    for i in range(len(l) - 1 ):
      for j in range(i+1 ,len(l)):
        swap = False
        if j > i:
          swap = shouldWeSwap(numbers, l[i], l[j])
        if swap:
          c += 1
          old = l[i]
          l[i] = l[j]
          l[j] = old
          changed = True
  # Put into string
  print(c)
  s = ""
  for n in l:
    s += str(n)
  return(s)

print("Problem 79")
start = time.time()
print("Passcode Derivation : ", passcodeDerivation())
end = time.time()
print("Time taken: " + str(end - start)  + " seconds")
print()
