
import math

    
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
    print(n,"/",d,"=", n/d) 
    if len(str(n)) > len(str(d)):
        c += 1
print(c)
