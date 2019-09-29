###############
# Problem 45  #
###############

"""
Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Pentagonal	 	Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
"""
import time, math
print("Problem 45")

start = time.time()
def isPentagonal(n):
    t =(math.sqrt(24 * n + 1) + 1) / 6
    if t == int(t):
        return(int(n))
    else:
        return(False)

def isTriangular(n):
    t =(math.sqrt(8 * n + 1) - 1) / 2
    if t == int(t):
        return(int(n))
    else:
        return(False)

def isHexagonal(n):
    t =(math.sqrt(8 * n + 1) + 1) / 4
    if t == int(t):
        return(int(n))
    else:
        return(False)
    

start = time.time()
n = 144
while True:
    nH = int(n * (2 * n - 1))
    if isPentagonal(nH):
        break
    n += 1 
end = time.time()
print("The next triangle number that is also pentagonal and hexagonal", isPentagonal(nH))
print("Time taken:", int((end - start)*100) / 100, "Seconds")
print()


done = False
for n1 in range(287, 1000000000, 2):
    nT = int((n1 * (n1 + 1)) / 2)
    if nT:
        for n2 in range(1, n1, 1):
            nP = int((n2* (3 * n2 - 1)) / 2)
            if nP > nT:
                break
            if nT == nP:
                for n3 in range(1, n2, 1):
                    nH =  n3 * ((2 * n3) - 1)
                    if nH > nP:
                        break
                    if nT == nP == nH:
                        done = True
                        break
            if done:
                break
        if done:
            break
        
end = time.time()
print("The next triangle number that is also pentagonal and hexagonal", isPentagonal(nH))

print("Time taken:", int((end - start)*100) / 100, "Seconds")
print()

