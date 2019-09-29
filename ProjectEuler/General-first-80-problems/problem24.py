###############
# Problem 24  #
###############

"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

"""
import time

def permutations(word):
    stack = list(word)
    results = stack.pop()
    while len(stack) != 0:
        c = stack.pop()
        new_results = []
        for w in results:
            for i in range(len(w)+1):
                new_results.append(w[:i] + c + w[i:])
        results = new_results
    return (sorted(results))


print("Problem 24")

start = time.time()

p = permutations("0123456789")
for i in range(len(p)):
    if i == 999999:
        break

end = time.time()
print("The millionth per of ", "0123456789", "is", p[i])
print("Time taken:", int((end - start)*100) / 100, "Seconds")
print()
