"""
from itertools import permutations
text_file = open("numberRanges.py", "w")

pans = [''.join(p) for p in permutations('9876543210')]

text_file.write("pandigital10 = {")
for i,n in enumerate(pans):
    text_file.write("\""+str(n)+"\"")
    if i != len(pans) - 1:
        text_file.write(", ")
text_file.write("}")
text_file.write("\n")
text_file.write("\n")
text_file.close()

del pans

# Sieve of Eratosthenes

def gen_primes(n):

    D = {}   
    # The running integer that's checked for primeness
    q = 2
    
    while q < n:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]   
        q += 1

text_file = open("numberRanges.py", "a")
p = list(gen_primes(10**8))
text_file.write("primes = {")
for i,n in enumerate(p):
    text_file.write("\""+str(n)+"\"")
    if i != len(p) - 1:
        text_file.write(", ")
text_file.write("}")


text_file.close()

text_file = open("numberRanges.py", "a")
p = list(gen_primes(10**8))
text_file.write("primes = {")
for i,n in enumerate(p):
    text_file.write("\""+str(n)+"\"")
    if i != len(p) - 1:
        text_file.write(", ")
text_file.write("}")


text_file.close()
"""

for n in range(1,10**7):
    nn = int((n*(n+1)/2))

