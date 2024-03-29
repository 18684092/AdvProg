##############
# Problem 81 #
##############
"""
In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right and down, is indicated in bold red and is equal to 2427.


Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by only moving right and down.
"""
import time

def pathSumTwoWays():
  grid = []
  # populate grid
  with open("p081_matrix.txt", "r") as f:
    for lines in f:
      grid.append(lines.rstrip('\n').split(','))
  f.close()
  
  # Init weighting grid
  weights = [[0 for i in range(len(grid))] for j in range(len(grid[0]))]

  # turn elements into ints and find max
  #MAXIMUM = 0
  #for rows in range(len(grid)):
  #  for cols in range(len(grid[rows])):
  #    grid[rows][cols] = int(grid[rows][cols])
  #    MAXIMUM += grid[rows][cols]
  # Can't think MAXIMUM will ever be reached but...
  #MAXIMUM += 1
  MAXIMUM = 99999999999
  # Make weights by climbing grid bottom up (reversed path)
  for row in reversed(range(len(grid))):
    for col in reversed(range(len(grid[row]))):
      # no right or down for corner
      if row == len(grid) - 1 and col == len(grid[row]) - 1:
        weights[row][col] = int(grid[row][col])
        continue
      if (row + 1) < len(grid):
        down = weights[row + 1][col]
      else: 
        down = MAXIMUM
      if (col + 1) < len(grid[row]):
        right = weights[row][col + 1]
      else:
        right = MAXIMUM
      if down < right:
        weights[row][col] = int(grid[row][col]) + down
      else:
        weights[row][col] = int(grid[row][col]) + right
      
  # find minimal path (top down)
  startY = startX = 0
  endY = len(grid) -1
  endX = len(grid[endY]) - 1
  # Add starting value
  sumOfMin = int(grid[startY][startX])
  while startY < endY and startX < endX:
    if startX < endX:
      right = weights[startY][startX + 1]
    else:
      right = MAXIMUM
    if startY < endY:
      down = weights[startY + 1][startX]
    else:
      down = MAXIMUM
    if right < down:
      startX += 1
    else:
      startY += 1
    sumOfMin += int(grid[startY][startX])
  # Add destination value    
  sumOfMin += int(grid[endY][endX])
  return(sumOfMin)

print("Problem 81")
start = time.time()
print("Path sum two way: ", pathSumTwoWays())
end = time.time()
print("Time taken: " + str(int( ((end - start)*1000)     *100)/100) + " milli seconds")
print()
