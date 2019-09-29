################
# Problem 104  #
################

"""
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
It turns out that F541, which contains 113 digits, is the first Fibonacci number for which the last nine digits are 1-9 pandigital (contain all the digits 1 to 9, but not necessarily in order). And F2749, which contains 575 digits, is the first Fibonacci number for which the first nine digits are 1-9 pandigital.

Given that Fk is the first Fibonacci number for which the first nine digits AND the last nine digits are 1-9 pandigital, find k.

"""
import time
print("Problem 104")
start = time.time()
# This is about 2.5hrs long - but it works!!!
# K = 329468
# Time taken: 8999.23 Seconds
def fib():
    n1, n2, s = 1, 1, 3
    compare = ['1','2','3','4','5','6','7','8','9']
    while True:
        n = n1 + n2
        if sorted(str(n)[-9:]) == compare:
            if sorted(str(n)[:9]) == compare:
                return(s)
        s += 1
        n1, n2 = n2, n

print("K =", fib())
end = time.time()
print("Time taken:", int((end - start)*100) / 100, "Seconds")
print()
