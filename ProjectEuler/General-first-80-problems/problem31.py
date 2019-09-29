###############
# Problem 31  #
###############

"""
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""
import time
print("Problem 31")

start = time.time()
# Brute force
goal = 200
combinations = 0
for twoHundred in range(goal + 1, 0, -200):
    for oneHundred in range(twoHundred, 0, -100):
        for fifty in range(oneHundred, 0, -50):
            for twenty in range(fifty, 0, -20):
                for ten in range(twenty, 0, -10):
                    for five in range(ten, 0, -5):
                        for two in range(five, 0, -2):
                            combinations += 1


end = time.time()
print("There are", combinations, "of making £2")
print("Time taken:", int((end - start)*100) / 100, "Seconds")
print()

# Dynamic (Someone elses code idea)
goal = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]
# we have 200 coins
combinations = [0 for a in range(goal + 1)]
combinations[0] = 1
for i in range(0, len(coins)):
    for j in range(coins[i], goal + 1):
        combinations[j] += combinations[j - coins[i]]

print("There are", combinations[len(combinations) - 1], "of making £2")        
