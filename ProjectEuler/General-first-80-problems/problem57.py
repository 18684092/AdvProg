###############
# Problem 57  #
###############

"""
It is possible to show that the square root of two can be expressed as an infinite continued fraction.

√ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?

"""
import time, math
print("Problem 57")

start = time.time()
def sqrt(S, n):
    m = 0
    d = 1
    iS = int(math.sqrt(S))
    a = iS

    store = []

    n1 = 1;
    num = a;
    d1 = 0;
    den = 1;
    
    while n != 0:
        oldA = a
        m = int(d * a - m)
        d = int((S - m * m) / d)
        a = int((iS + m) / d)

        n2 = n1;
        n1 = num;
        d2 = d1;
        d1 = den;
 
        num = a * n1 + n2;
        den = a * d1 + d2;    

        store.append((num, den))
        n -= 1
    return(store)

c = 0
for (n,d) in sqrt(2,1000):
    #print(n,"/",d,"=", n/d) 
    if len(str(n)) > len(str(d)):
        c += 1

end = time.time()
print("The number of iterations with more digits in numerator is", c)
print("Time taken:", int((end - start)*1000) / 1000, "Seconds")
print()
