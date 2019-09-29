import math
print("factorials = {",end="")
end = 20
for n in range(0, end):
    print(str(n)+": "+str(math.factorial(n)),end="")
    if n < end - 1:
        print(", ",end="")
print("}")
