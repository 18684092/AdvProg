###############
# Problem 205 #
###############

"""
Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3, 4.
Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5, 6.

Peter and Colin roll their dice and compare totals: the highest total wins. The result is a draw if the totals are equal.

What is the probability that Pyramidal Pete beats Cubic Colin? Give your answer rounded to seven decimal places in the form 0.abcdefg

"""
import time, math
import random

def peterRolls():
    total = 0
    for n in range(9):
        total += random.randint(1,4)
    return(total)
    
def colinRolls():
    total = 0
    for n in range(6):
        total += random.randint(1,6)
    return(total)

start = time.time()
print("Problem 205")
random.seed(1)
probability = 0
peterWins = 0
colinWins = 0
draws = 0
smallestDiff = 1
for n in range(1,908926):
    p = peterRolls()
    c = colinRolls()
    if p > c :
        peterWins += 1
    elif p < c:
        colinWins += 1
    else:
        draws += 1
    probability = peterWins / (peterWins + colinWins + draws)


end = time.time()
print("Peter beats Colin ", round(probability, 7) , "of the time. After", n, "Sets of throws")
print("Time taken:", int((end - start)*100) / 100, "Seconds")
print()
