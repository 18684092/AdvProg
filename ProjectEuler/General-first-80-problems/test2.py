

def getDecimalPart(number):
  s = ""
  found = 0
  for c in str(number):
    if c == ".":
      found = 1
    if found:
      s += c
  return(s)

def numberToWords(number):
  """
  Converts numbers to words in range
  -999,999,999,999 to 999,999,999,999
  including decimal numbers -98.987
  """
  powers = {9: 'Billion', 6: 'Million', 3: 'Thousand'}
  out = ""
  decimalPart = getDecimalPart(number)
  # Check bounds
  if number == 0:
    return("Zero")
  if int(abs(number)) > 999999999999:
    return("Number too large!")
  if number < 0:
    out += "Minus "
    number = abs(number)
  number = int(number)
  # Divide and test powers of
  didWeDivide = 0
  for p in reversed(range(3, 10, 3)):
    # Always break down to less than 1000
    divisor = int(number / 10 ** p)
    if divisor > 0:
      out += speakWords(divisor) + " " + powers[p] + " "
      divisor *= 10 ** p
      # Reduce and loop
      number -= divisor
      didWeDivide = 1
  # Whats left under 1000
  if didWeDivide == 1 and (number < 20 and number > 0):
    out += "and "
  if number > 0:
    out += speakWords(number)
  # Correct the odd whitespace
  out = out.strip()
  # Cope with -.567 or 0.434 etc
  if out == "" or out == "Minus":
    out += " Zero"
  # add decimalPart
  if decimalPart != "":
    # One number at a time
    for c in decimalPart:
      if c == ".":
        out += " Point"
      elif c == "0":
        out += " Zero"
      else:
        out += " " + speakWords(int(c))
  # All done and clean up
  return(out.strip())

def speakWords(number):
  """ Convert numbers under 1000 """
  numbers = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
  tens = {2: 'Twenty', 3: 'Thirty', 4: 'Forty', 5: 'Fifty', 6: 'Sixty', 7: 'Seventy', 8: 'Eighty', 9: 'Ninety'}  
  out = ""
  (hundreds, units) = divmod(number, 100)
  if hundreds > 0:
    out += numbers[hundreds] + " Hundred "
    if units > 0:
      out += "and "
  if units > 19:
    (ten, units) = divmod(units, 10)
    out += tens[ten]
    if units > 0:
      out += "-" + numbers[units]
  elif units > 0:
    out += numbers[units]
  return(out)


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
