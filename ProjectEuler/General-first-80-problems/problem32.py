import time

def ranges(a , b):
  allNines = []
  for multiplicand in range(a, a * 10):
    for multiplier in range(b, b * 10):
      product = multiplicand * multiplier
      digits = str(multiplicand) + str(multiplier) + str(product)
      # put each digit into a list if it isn't already there.
      # if list length is 9 then it is valid. Put this into
      # another list if it does not exist. Add lists together
      if len(digits) == 9 and not ("0" in digits):
        allDigits = []
        for digit in digits:
          if not digit in allDigits:
            allDigits.append(digit)
        if len(allDigits) == 9:
          if not product in allNines:
            allNines.append(product)
  return(allNines)

def pandigitalProducts():
  allNines = []
  allNines += ranges(10, 100)
  allNines += ranges(1, 1000)
  total = 0
  for number in allNines:
    total += number
  return(total)

print("Problem 32")
start = time.time()
print("The Pandigital products: ", pandigitalProducts())
end = time.time()
print("Time taken: " + str(int( ((end - start)*1000)     *100)/100) + " milli seconds")
print()
