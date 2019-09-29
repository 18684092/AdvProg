################
# Problem 407  #
################

"""
If we calculate a2 mod 6 for 0 ≤ a ≤ 5 we get: 0,1,4,3,4,1.

The largest value of a such that a2 ≡ a mod 6 is 4.
Let's call M(n) the largest value of a < n such that a2 ≡ a (mod n).
So M(6) = 4.

Find ∑M(n) for 1 ≤ n ≤ 10^7.

"""
import time, math
print("Problem 407")
start = time.time()

def M(n):
  m = 0
  for a in range(n):
    a2 = (a * a) % n
    if a2 > m:
      m = a2
  print(m)
  return(m)

s = 0
for n in range(1,10**7):
  if n % 10000 == 0:
    print(n)
  a2 = M(n)
  s += a2



print("Find ∑M(n) for 1 ≤ n ≤ 10^7", s)
end = time.time()
print("Time taken:", int((end - start)*100) / 100, "Seconds")
print()
