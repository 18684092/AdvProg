##############
# Problem 20 #
##############
"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

def factorialDigitSum(number):
  total = 1
  for i in range(number, 1, -2):
    total *= ( i * (i - 1))
  s = str(total)
  total = 0
  for i in s:
    total += int(i)
  return(total)


print("Problem 20")
print("Factorial Digit Sum: ", factorialDigitSum(100))
print()
