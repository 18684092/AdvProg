from numberToWords import *


# Test
for n in range(-9999,1002):
  print(n, numberToWords(n))
# Biggest  
print(numberToWords(999999999999.99))
# Overload
print(numberToWords(1000000000000))
# Overload negative
print(numberToWords(-1000000000000))
# minus
print(numberToWords(-79000560001.9))
# decimal
print(numberToWords(-100.021))
print(numberToWords(-09.1))
a = numberToWords(3378)
for i in a:
  print(i)
  
print(a.words()[3])
print(numberToWords(345.1).words())

