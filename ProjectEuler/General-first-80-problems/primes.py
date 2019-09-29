
"""
Prime number related functions.
All code by Andy Perrett 2018

isAPrimeNumber(positive int) - returns True or False.
listPrimesTo(positive int) - yields a list of primes upto and inc number.
primeFactorise(positive int) - returns a list of prime factors.

A DB of prime numbers upto 1,000,000 is imported. 

* listPrimesTo will add primes to the DB so will cache new primes over
1,000,000 for faster retrieval on subsequent calls.

"""
from random import * 
from prime_numbers_to_1000000 import prime_numbers
import math , time


# Gloabls
hi_prime = 1000000 # DB contains all primes to this number

lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

def sieveBounds(n):
  """ Set bounds for the sieve of our DB """
  # Pierre Dusart's bounds (log is ln)
  totalPrimes = len(prime_numbers)
  lowerBound = 0
  # upperBound true for x > 1
  upperBound = (n / math.log(n)) * (1 + 1.2762 / math.log(n)) 
  if upperBound > totalPrimes: # don't go above DB
    upperBound = totalPrimes
  if n > 598: # lowerBound only true above this
    lowerBound = (n / math.log(n)) * (1 + 0.992  / math.log(n)) 
  return(int(lowerBound),int(upperBound))

def isAPrimeNumberDB(number):
  """ If number is prime return True or False """
  for i in range(sieveBounds(number)):
    if number == prime_numbers[i] :
      return(True)
  return(False)

def isAPrimeNumber(number):
  """ Return True if number is a prime """
  if number <= 1: return(False)
  if number == 2: return(True)
  if number % 2 == 0: return(False)
  if number < 9: return(True)
  if number % 3 == 0: return(False)
  if number % 5 == 0: return(False)
  
  if number in lowPrimes:
    return True
  
  # See if any of the low prime numbers can divide num
  for p in lowPrimes:
    if (number % p == 0):
      return False
    
  # check odd numbers to sqrt(number) + 1
  for i in range(997, int(number ** 0.5) + 1, 2):
    if number % i == 0:
      return(False)
  return(True)

def add_prime(number):
  """ add all primes above hi_prime until number """
  global hi_prime
  for i in range(hi_prime + 1, number + 1):
    if isAPrimeNumber(i):
      prime_numbers.append(i)
    hi_prime += 1

def listPrimesTo(number):
  """ Returns list of primes upto number """
  if number > hi_prime:
    add_prime(number)
  #if number <= hi_prime:
  for i in range(len(prime_numbers)):
    if prime_numbers[i] <= number:
      yield prime_numbers[i]
    if prime_numbers[i] >= number:
      return


def primeFactorise(number):
  """ Return all the prime factors of number as a list """
  if isAPrimeNumber(number):
    return([number])
  primes = list(listPrimesTo(int(number * 0.5) + 1))
  factors = []
  while number > 1:
    for prime in primes:
      if number % prime == 0:
        factors.append(prime)
        number /= prime
        break
  return(factors)

def primesieve(ubound):
    size = int((ubound - 3) / 2)
    a = [False] * size
    s = 0
    primes = []
    while s < size:
        t = 2 * s
        p = t + 3
        primes.append(p)
        for n in range(t * (s + 3) + 3, size, p):
            a[n] = True
        s = s + 1
        while s < size and a[s]:
            s = s + 1
    return(set(primes))

"""
# Example uses #

# Factorise
print("Getting prime factors for 3,000,000.\nThis uses primes beyound DB, there will be a delay...")
print(primeFactorise(3000000))
print()

# Print primes to n
print("Primes from 0 to 100")
a =  list(listPrimesTo(100))
print("prime_numbers = ",a)

print("Number of primes: ", len(a))
print()
# Is n a prime?
for i in range(4000078, 4000084):
  print("Is " + str(i) + " a prime: ", end = "")
  print(isAPrimeNumber(i))
print()

# Factorise a range of numbers
for number in range(0,101):
  factors = primeFactorise(number)
  print(str(number) + " = ", end = "")
  for i, factor in enumerate(factors):
    print(factor, end="")
    if i < len(factors) -1:
      print(" x ", end = "")
  print()
print()
# cached
print("Getting prime factors for 3,000,000.\nThis uses cached result from earlier.\nSo will be much quicker...")
print(primeFactorise(3000000))

s = time.time()
for i in range(1000):
  n = randint(1,100000000)
  r = isAPrimeNumber(n)
e = time.time()
t = int((e - s)*1000) / 1000
print("1000 random prime tests averaged: "+str(t)+" mS per test")


s = time.time()
for i in range(1000):
  n = randint(1,1000000)
  r = primeFactorise(n)
e = time.time()
t = int((e - s)*1000) / 1000
print("1000 random primeFactorise tests averaged: "+str(t)+" mS per test")


print()
print("Testing the sieve")
l = [10,100,1000,10000,100000, 1000000]
for n in l:
  lowerBound, upperBound = sieveBounds(n)
  a = int(n / (math.log(n) - 1))
  print("Number of primes under: " + str(n) + " (x / log x -1: "+ str(a)+ ") " + " = low: " + str(lowerBound) + " high: " + str(upperBound))

  
"""
