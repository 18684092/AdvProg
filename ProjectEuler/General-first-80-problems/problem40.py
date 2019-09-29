##############
# Problem 40 #
##############
"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""

def champernownesConstant():
  result = 0
  s = ""
  number = 1
  while len(s) <= 1000000:
    s += str(number)
    number += 1
  result = int(s[0]) * int(s[9]) * int(s[99]) * int(s[999]) * int(s[9999]) * int(s[99999]) * int(s[999999]) 
  return(result)


print("Problem 40")
print("Champernowne's constant: ", champernownesConstant())
print()
