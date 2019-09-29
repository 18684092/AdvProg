##############
# Problem 82 #
##############

# Standard imports
import math

# Global variables
INFINITY = 99999999999999

# Node structure
class ASTARNode():
  localGoal = INFINITY
  globalGoal = INFINITY
  parent = (-1, -1)
  visited = False
  neighbours = []
  cost = 0

#################################
# Functions specific to problem #
#################################

def heuristic(grid, start, end):
  # Euclidean Distance
  y = abs(end[0] - start[0])
  x = abs(end[1] - start[1])
  return(math.sqrt(y * y + x * x))

def getNeighbours(grid, row, col):
  neighbours = []
  if row > 0:
    neighbours.append((row - 1, col)) # up
  if row < len(grid) - 1:
    neighbours.append((row + 1, col)) # down
  if col < len(grid[row]) - 1:
    neighbours.append((row, col + 1)) # right

  return(neighbours)
    
def foundRoute(grid, start, end):
  pathSum = grid[end[0]][end[1]].cost
  t = []
  (y, x) = end
  while grid[y][x].parent != (-1, -1):
    t.append((y, x))
    (y, x) = grid[y][x].parent
    pathSum += grid[y][x].cost
  t.append(start)
  return(t, pathSum)

import time
stime = time.time()
 
lowest = INFINITY
gridF = []
global grid
grid = []
# populate grid with ints from string file
with open("p082_matrix.txt", "r") as f:
  for lines in f:
    gridF.append([int(i) for i in lines.split(',')])
f.close()

    
#############################################
# Two test grids - uncomment either and run #
# to test. Uncomment both to work on file   #
#############################################

# Shortest path cost here is 994
# path = (1, 0), (1, 1), (1, 2), (0, 2), (0, 3), (0, 4)
#
#gridF = []
#gridF.append([131,673,234,103,18])
#gridF.append([201,96,342,965,150])
#gridF.append([630,803,746,422,111])
#gridF.append([537,699,497,121,956])
#gridF.append([805,732,524,37,331])

# Shortest path cost here is 95
# (0, 0), (0, 1), (1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (2, 3), (1, 3), (0, 3), (0, 4)
#gridF = []
#gridF.append([21,10,61,2,10])
#gridF.append([42, 8,51,7,35])
#gridF.append([63,11,45,9,38])
#gridF.append([81, 5,11,1,22])
#gridF.append([99,10,2,10,90])
routes = []
lowestRoute = INFINITY
# Initialise our working grid
for st in range(len(gridF)):
  for e in range(len(gridF)):
    grid = [[0 for i in range(len(gridF))] for j in range(len(gridF[0]))]
    for row in range(len(gridF)):
      for col in range(len(gridF[0])):
        node = ASTARNode()
        grid[row][col] = node
        grid[row][col].cost = gridF[row][col]

    start = (st,0)
    end = (e , len(gridF[0]) - 1)
    print(start, end)
    # Start point
    (y, x) = start
    # Update the starting node's localGoal and set to zero
    grid[y][x].localGoal = 0
    #grid[end[0]][end[1]].globalGoal = 0
    nodes = []
    nodes.append(start)
    while True:
      # Loop thru neighbours
      for neighbour in getNeighbours(grid, y, x): 
        # Test each neighbour
        (Y, X) = neighbour
        localCost = grid[y][x].localGoal + grid[y][x].cost
        # Update if lower cost
        if localCost < grid[Y][X].localGoal:
          grid[Y][X].localGoal = localCost
          grid[Y][X].parent = (y, x)
          # Calculate heuristic 
          grid[Y][X].globalGoal = heuristic(grid, (Y, X), end) + localCost
        if not grid[neighbour[0]][neighbour[1]].visited:   
          nodes.append(neighbour)
          
      grid[y][x].visited = True
      
      # Priority Queue
      nodes.sort(key=lambda c: grid[c[0]][c[1]].globalGoal)
      
      # Clean the queue
      nodes = [node for node in nodes if not grid[node[0]][node[1]].visited]
          
      if len(nodes) == 0:
        # Found shortest
        break
      (y, x) = nodes[0]
      
    # Track back path to find route and cost
    temp, pathSum = foundRoute(grid, start, end)
    # Do we have a lower cost route? 
    if pathSum < lowestRoute:
      lowestRoute = pathSum
      routes = temp
      print("------------------>>>>>PathSUM",pathSum,)
print(lowestRoute, list(reversed(routes)))
etime = time.time()
print("Time taken: " + str(etime - stime) + " seconds")


 