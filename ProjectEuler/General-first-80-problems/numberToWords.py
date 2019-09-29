

class numberToWords():
  """
  Module to convert decimal numbers to English words
  
  USAGE:
  ------
  
  from numberToWords import *
  
  print(numberToWords(-9876.44)) will return:

  >>> Minus Nine Thousand Eight Hundred and Seventy-Six Point Four Four

  a = numberToWords(101)
  print(a.words())
  
  >>> ['One','Hundred','and','One']
  
  """
  
  def __init__(self, number):
    self.__powers = {9: 'Billion', 6: 'Million', 3: 'Thousand'}
    self.__numbers = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
    self.__tens = {2: 'Twenty', 3: 'Thirty', 4: 'Forty', 5: 'Fifty', 6: 'Sixty', 7: 'Seventy', 8: 'Eighty', 9: 'Ninety'}
    self.__converted = self.__number2Words(number)
  
  def __repr__(self):
    """ Converted number is printable """
    return(self.__converted)
  
  def __len__(self):
    """ Returns length of characters after conversion """
    return(len(self.__converted))
  
  def __getitem__(self, key):
    """ Object is subscriptable """
    return(self.__converted[key])
  
  def __iter__(self):
    """ Number conversion is iterable """
    for i in self.__converted:
      yield i
    
  def lower(self):
    """ Converts converted number to lowercase """
    return(self.__converted.lower())
  
  def upper(self):
    """ Converts converted number to UPPERcase """
    return(self.__converted.upper())

  def words(self):
    """ Returns the converted number as a list """
    return(self.__converted.split())
    
  def __getDecimalPart(self, number):
    """ Internal function """
    s = ""
    found = 0
    for c in str(number):
      if c == ".":
        found = 1
      if found:
        s += c
    return(s)

  def __number2Words(self, number):
    """
    Internal function
    Converts numbers to words in range
    -999,999,999,999 to 999,999,999,999
    including decimal numbers -98.987
    """
    out = ""
    decimalPart = self.__getDecimalPart(number)
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
        out += self.__speakWords(divisor) + " " + self.__powers[p] + " "
        divisor *= 10 ** p
        # Reduce and loop
        number -= divisor
        didWeDivide = 1
    # Whats left under 1000
    if didWeDivide == 1 and (number < 20 and number > 0):
      out += "and "
    if number > 0:
      out += self.__speakWords(number)
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
          out += " " + self.__speakWords(int(c))
    # All done and clean up
    return(out.strip())

  def __speakWords(self, number):
    """ 
    Internal function
    Convert numbers under 1000
    """
    out = ""
    (hundreds, units) = divmod(number, 100)
    if hundreds > 0:
      out += self.__numbers[hundreds] + " Hundred "
      if units > 0:
        out += "and "
    if units > 19:
      (ten, units) = divmod(units, 10)
      out += self.__tens[ten]
      if units > 0:
        out += "-" + self.__numbers[units]
    elif units > 0:
      out += self.__numbers[units]
    return(out)
