import math
from decimal import Decimal
from decimal import *
from fractions import Fraction
getcontext().prec = 600











def gcd(a, b):
  while b:
    a, b = b, a%b
  return a

def fraction(a, b, i):
    f = str(Fraction(a/b).limit_denominator(10)).split('/')
    if len(f) > 1:
        a = Decimal(f[0])
        b = Decimal(f[1])
        return(a,b)
    return(f[0],0)

def sqrt(a):
    length = len(str(a)) + 1
    n = 10 ** length
    x = 0
    for i in range(300):
        x = (1.0) + (((a) - (1.0)) / (((1.0) + (x)))) 
        n, d = fraction(a, x, i)
        yield (n , d)

def isSquare(integer):
    root = math.sqrt(integer)
    if int(root + 0.5) ** 2 == integer: 
        return True
    else:
        return False 

for D in range(1, 62):
    if isSquare(D):
        continue
    c = 0
    for (n,d) in sqrt(D):
        
        n = Decimal(n)
        d = Decimal(d)
        pell = Decimal(n*n)-Decimal(D*(d*d))
        if pell == 1 and c <2 :
            print(D, n, d)
            c += 1
            


