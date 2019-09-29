##############
# Problem 83 #
##############

# A* solution to Euler problem 83 

# Standard imports
import math

# Node structure
class ASTARNode():
  localGoal = math.inf
  globalGoal = math.inf
  parent = (-1, -1)
  visited = False
  neighbours = []
  partOfRoute = False
  cost = 0

#################################
# Functions specific to problem #
#################################
def heuristic(grid, start, end):
  # Euclidean / Pythagoreon Distance
  y = abs(end[0] - start[0])
  x = abs(end[1] - start[1])
  return(math.sqrt(y * y + x * x))

def getNeighbours(grid, y, x):
  # Get neighbours of (y, x)
  neighbours = []
  if y > 0:
    neighbours.append((y - 1, x)) # up
  if y < len(grid) - 1:
    neighbours.append((y + 1, x)) # down
  if x < len(grid[y]) - 1:
    neighbours.append((y, x + 1)) # right
  if x > 0:
    neighbours.append((y, x - 1)) # left
  return(neighbours)

def getRoute(grid, start, end):
  # Follow parent back from end to start
  pathSum = grid[end[0]][end[1]].cost
  grid[end[0]][end[1]].partOfRoute = True
  temp = []
  (y, x) = end
  while grid[y][x].parent != (-1, -1):
    temp.append((y, x))
    (y, x) = grid[y][x].parent
    pathSum += grid[y][x].cost
    grid[y][x].partOfRoute = True
  temp.append(start)
  grid[start[0]][start[1]].partOfRoute = True
  # Reverse route for finished route
  return(grid, list(reversed(temp)), pathSum)

def readEulerFile():
  # populate grid and initiate nodes
  grid = []
  with open("p082_matrix.txt", "r") as f:
    y = 0
    for lines in f:
      line = ([int(i) for i in lines.split(',')])
      grid.append([0] * len(line))
      for x, value in enumerate(line):
        node = ASTARNode()
        grid[y][x] = node
        grid[y][x].cost = value
      y += 1
  f.close()
  return(grid)

def showRoute(grid):
  for y in range(len(grid)):
    for x in range(len(grid[y])):
      if grid[y][x].partOfRoute:
        print(".", end="")
      else:
        print("x", end="")
    print()

########
# Main #
########
grid = readEulerFile()
# Find lowest cost path from top left to bottom right
# of 80 x 80 grid pulled in from file
start = (0, 0)
end = (len(grid) - 1 , len(grid[0]) - 1)
# Start point
(y, x) = start
# Set starting localGoal and set to zero
grid[y][x].localGoal = 0

# Initialise our node queue
qNodes = []
qNodes.append(start)
# Loop while there ARE nodes still in queue
while qNodes:
  # Current node is first from queue
  (y, x) = qNodes[0]
 
  # Loop thru neighbours looking for better path
  for neighbour in getNeighbours(grid, y, x): 
    # Test each neighbour
    (nY, nX) = neighbour
    localCost = grid[y][x].localGoal + grid[nY][nX].cost
    # Update neighbour if lower cost local path found
    if localCost < grid[nY][nX].localGoal:
      # New local path cost
      grid[nY][nX].localGoal = localCost
      # The current node is this nodes parent
      grid[nY][nX].parent = (y, x)
      # Calculate heuristic to end
      grid[nY][nX].globalGoal = heuristic(grid, (nY, nX), end) + localCost
      
    # Only add to node queue if not visited before
    if not grid[neighbour[0]][neighbour[1]].visited: 
      # Queue neighbour
      qNodes.append(neighbour)
      
  # Mark current node as visited    
  grid[y][x].visited = True
  
  # Clean the queue of visited nodes
  qNodes = [node for node in qNodes if not grid[node[0]][node[1]].visited]
  # Priority Queue - sort based upon the node's global goal / heuristic
  qNodes.sort(key=lambda node: grid[node[0]][node[1]].globalGoal)

# The end results in lowest cost path / route  
grid, route, pathSum = getRoute(grid, start, end)
print("PathSUM",pathSum,)
#print(route)
showRoute(grid)
