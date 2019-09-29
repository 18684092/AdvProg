###############
# Problem 66  #
###############

"""

Consider quadratic Diophantine equations of the form:

x2 – Dy2 = 1

For example, when D=13, the minimal solution in x is 6492 – 13×1802 = 1.

It can be assumed that there are no solutions in positive integers when D is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

32 – 2×22 = 1
22 – 3×12 = 1
92 – 5×42 = 1
52 – 6×22 = 1
82 – 7×32 = 1

Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.

Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.
"""
import time, math

print("Problem 66")

start = time.time()


def checkPell(x, d, y):
    if (x * x) - d * (y * y) == 1:
        return(True)
    return(False)

def isSquare(integer):
    root = math.sqrt(integer)
    if int(root + 0.5) ** 2 == integer: 
        return True
    else:
        return False

result = 0;
pmax = 0;
for N in range(0,1001):
    iSqrtN = int(math.sqrt(N))
    if isSquare(N):
        continue

    m = 0
    d = 1
    a = iSqrtN

    x1 = 1
    x = a
    y1 = 0
    y = 1
    while not checkPell(x , N, y):
        m = int(d * a - m)
        d = int((N - m * m) / d)
        a = int((iSqrtN + m) / d)
        x2 = x1
        x1 = x
        y2 = y1
        y1 = y
        x = a * x1 + x2
        y = a * y1 + y2

    if (x > pmax):
        pmax = x
        result = N

print("The largest x obtained:",result)  
end = time.time()
print("Time taken:", int((end - start)*100) / 100, "Seconds")
print()
