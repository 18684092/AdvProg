# continued fractions from
# https://en.wikipedia.org/wiki/Methods_of_computing_square_roots

import math

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
    
def pell(S):
    m = 0
    d = 1
    iS = int(math.sqrt(S))
    a = iS

    x = a
    xPrevious = 1
    yPrevious = 0
    y = 1
    
    while not checkPell(x ,S, y):
        m = int(d * a - m)
        d = int((S - m * m) / d)
        a = int((iS + m) / d)

        x2 = xPrevious
        xPrevious = x
        y2 = yPrevious
        yPrevious = y
        
        x = a * xPrevious + x2
        y = a * yPrevious + y2

    return(x, y)

for n in range(0, 1001):
    if isSquare(n):
        continue
    x, y = pell(n)
    print(n, x, y)
