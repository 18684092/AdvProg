###############
# Problem 28  #
###############

"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

"""
import time
print("Problem 28")

start = time.time()

def right(matrix, y, x, n):
    x += 1
    n += 1
    matrix[y][x] = n
    return(matrix, y, x, n)

def left(matrix, y, x, n):
    x -= 1
    n += 1
    matrix[y][x] = n
    return(matrix, y, x, n)

def down(matrix, y, x, n):
    y += 1
    n += 1
    matrix[y][x] = n
    return(matrix, y, x, n)

def up(matrix, y, x, n):
    y -= 1
    n += 1
    matrix[y][x] = n
    return(matrix, y, x, n)

def numberSpiral(size):
    matrix = [[0 for x in range(size)] for y in range(size)]
    middle = int((size / 2))
    x = middle
    y = middle
    n = 1
    # Set starting number
    matrix[y][x] = n
    loop = 1
    while n != (size * size):
        matrix, y, x, n = right(matrix, y, x, n)
        for d in range(loop):
            matrix, y, x, n = down(matrix, y, x, n)
        for l in range(loop + 1):
            matrix, y, x, n = left(matrix, y, x, n)
        for u in range(loop + 1):
            matrix, y, x, n = up(matrix, y, x, n)
        for r in range(loop + 1):
            matrix, y, x, n = right(matrix, y, x, n)
        loop += 2

    # get diaganol sums
    rD = 0
    for d1 in range(size):
        rD += matrix[d1][d1]
    for d2 in range(size):
        rD += matrix[d2][(size - 1) - d2]
    return(rD - 1)



print("Diaganols summed", numberSpiral(1001))
end = time.time()
print("Time taken:", int((end - start)*100) / 100, "Seconds")
print()
