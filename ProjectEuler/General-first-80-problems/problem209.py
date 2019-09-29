###############
# Problem 209 #
###############

"""
A k-input binary truth table is a map from k input bits (binary digits, 0 [false] or 1 [true]) to 1 output bit. For example, the 2-input binary truth tables for the logical AND and XOR functions are:

x	y	x AND y
0	0	0
0	1	0
1	0	0
1	1	1
x	y	x XOR y
0	0	0
0	1	1
1	0	1
1	1	0

How many 6-input binary truth tables, τ, satisfy the formula

τ(a, b, c, d, e, f) AND τ(b, c, d, e, f, a XOR (b AND c)) = 0

for all 6-bit inputs (a, b, c, d, e, f)?
"""
import time


start = time.time()
print("Problem 209")
count = 0
for input in range(0,2):
    I1 = "{0:b}".format(input).rjust(6,"0")
    # rotate digits in circular way
    for rotate in range(6):
        I1 = I1[1:] + I1[0:1]
        print(I1)
        a5 = I1[0] # a
        a4 = I1[1] # b
        a3 = I1[2] # c
        a2 = I1[3] # d
        a1 = I1[4] # e
        a0 = I1[5] # f

        b5 = str(int(a4))
        b4 = str(int(a3))
        b3 = str(int(a2))
        b2 = str(int(a1))
        b1 = str(int(a0))
        b0 = str(int(a5) ^ (int(a4) & int(a3))) 

        if b0 == "0":
            print(b0)
            count += 1


end = time.time()
print("Circular logig equals 0:", count)
print("Time taken:", int((end - start)*100) / 100, "Seconds")
print()
