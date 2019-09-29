"""
Euler functions
"""

def gcd(a, b):
  """Calculate the Greatest Common Divisor of a and b.
  Unless b==0, the result will have the same sign as b (so that when
  b is divided by it, the result comes out positive).
  """
  while b:
    a, b = b, a%b
  return a

def phi(n) :
    result = n 
    # Consider all prime factors
    # of n and for every prime
    # factor p, multiply result with (1 - 1 / p)
    p = 2
    while(p * p <= n) :
        # Check if p is a prime factor.
        if (n % p == 0) :
            # If yes, then update n and result
            while (n % p == 0) :
                n //= p # int division is quicker
            result *= (1 - (1 / p))
        p = p + 1
    # If n has a prime factor
    # greater than sqrt(n)
    # (There can be at-most one
    # such prime factor)
    if (n > 1) :
        result *= (1 - (1 / n))
    return(result)


def eulerTotient(number):
  cP = set()
  for n in range(number):
    if gcd(number, n) == 1:
      cP.add(n)
  return(cP)

def coPrimeSet(number):
  cP = 0
  for n in range(number):
    if gcd(number, n) == 1:
      cP += 1
  return(cP)

def Q(number):
  return(eulerTotient(number))


