##############
# Problem 36 #
##############
"""
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""
import time
start = time.time()
total = 0
for i in range(1, 1000001, 2):
    D = str(i)
    if D[0] != D[-1]:
        continue
    rD = D[::-1]
    if D != rD:
        continue
    B = bin(i)[2:]
    rB = B[::-1]
    if B == rB:
        total += i
end = time.time()
print("Double-base palindromes Sum:",total)
print("Time taken:", int((end-start) * 100) / 100, "Seconds")
