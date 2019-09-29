###############
# Problem 99  #
###############

"""
Comparing two numbers written in index form like 211 and 37 is not difficult, as any calculator would confirm that 211 = 2048 < 37 = 2187.

However, confirming that 632382518061 > 519432525806 would be much more difficult, as both numbers contain over three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a base/exponent pair on each line, determine which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example given above.
"""
import time, math
print("Problem 99")

start = time.time()
largest = l = lN = 0
with open('p099_base_exp.txt') as fp:
    for line in fp:
        l += 1
        base, exp = line.split(',')
        base = math.log(int(base))
        number = base * int(exp)
        if number > largest:
            largest = number
            lN = l

print("The largest line is", lN)
end = time.time()
print("Time taken:", int((end - start)*1000) / 1000, "Seconds")
print()
