###############
# Problem 39  #
###############

"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""
import time, math
print("Problem 39")

start = time.time()
maximised = 0
number = 0
for p in range(0,1001, 2):
    # p = a + b + c
    # c = hypotenuse
    count = 0
    for a in range(1, p):
        for b in range(a, p):
            c = math.sqrt((a * a)+(b * b))
            if a + b + c > p:
                break
            if p == (a + b + c)  :
                count += 1
                if count > maximised:
                    maximised = count
                    number = p
    
end = time.time()
print("",number, maximised)
print("Time taken:", int((end - start)*100) / 100, "Seconds")
print()
