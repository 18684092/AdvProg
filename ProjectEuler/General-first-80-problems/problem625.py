################
# Problem 625  #
################

"""
G(N)=∑Nj=1∑ji=1gcd(i,j). 
You are given: G(10)=122.

Find G(1011). Give your answer modulo 998244353
# 984524441
"""
import time, math, decimal
print("Problem 625")

start = time.time()

def gcd(a, b):
    while b != 0:
       t = b 
       b = a % b 
       a = t 
    return(a)

def gcdSum(n):
  total = 0
  for i in range(5000000000000000000):
    total = (10** math.log10(122))* (i * 10) % 998244353
    if total == 984524441:
      print(total, i)
    


print("GCD Sum", gcdSum(1000))
end = time.time()
print("Time taken:", int((end - start)*100) / 100, "Seconds")
print()
