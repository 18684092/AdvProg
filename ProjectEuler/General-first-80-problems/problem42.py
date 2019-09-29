##############
# Problem 42 #
##############

"""
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
"""
import time, math
print("Problem 42")

start = time.time()

def isTriangleNumber(n):
    x = (math.sqrt(8*n + 1) - 1) / 2
    if x - int(x) > 0: # if x is not an integer
        return False
    return int(x)

count = 0
with open("p042_words.txt", "r") as f:
    lines = f.readline().replace("\"","")
f.close()
for word in lines.split(","):
    cCount = 0
    for char in word:
        cCount += (ord(char) - 64)
    if isTriangleNumber(cCount):
        count += 1

end = time.time()
print("There are",count,"triangle words")
print("Time taken:", int((end - start)*100) / 100, "Seconds")
print()
