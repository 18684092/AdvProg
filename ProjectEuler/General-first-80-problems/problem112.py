###############
# Problem 112 #
###############

"""
Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) are bouncy. In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.

Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers is exactly 99%.


"""
import time

def isBouncy(number):
    n = str(number)
    increasing = True
    for i in range(len(n) - 1):
        if int(n[i]) > int(n[i + 1]):
            increasing = False
    if increasing:
        return("increasing")
    decreasing = True
    for i in range(len(n) - 1):
        if int(n[i]) < int(n[i + 1]):
            decreasing = False
    if decreasing:
        return("decreasing")
    return("bouncy")

start = time.time()
print("Problem 112")
target = 99
percentage = 0
number = 0
bouncyCount = 0
while percentage != target:
    if isBouncy(number) == "bouncy":
        bouncyCount += 1
        percentage = (bouncyCount / number) * 100
    number += 1
end = time.time()
print("Bouncy number at "+ str(target) + "% is " + str(number - 1))
print("Time taken:", int((end - start)*100) / 100, "Seconds")
