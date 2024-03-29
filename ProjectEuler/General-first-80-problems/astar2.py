##############
# Problem 83 #
##############

# Standard imports
import math

# Node structure
class ASTARNode():
  localGoal = math.inf
  globalGoal = math.inf
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

def getNeighbours(grid, y, x):
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

def foundRoute(grid, start, end):
  pathSum = grid[end[0]][end[1]].cost
  temp = []
  (y, x) = end
  while grid[y][x].parent != (-1, -1):
    temp.append((y, x))
    (y, x) = grid[y][x].parent
    pathSum += grid[y][x].cost
  temp.append(start)
  return(list(reversed(temp)), pathSum)
 
grid = []
# populate grid with ints from string file
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

start = (0,0)
end = (len(grid) - 1 , len(grid[0]) - 1)
# Start point
(y, x) = start
# Set starting localGoal and set to zero
grid[y][x].localGoal = 0
nodes = []
nodes.append(start)
while nodes:
  # Current node
  (y, x) = nodes[0]
 
  # Loop thru neighbours
  for neighbour in getNeighbours(grid, y, x): 
    # Test each neighbour
    (Y, X) = neighbour
    localCost = grid[y][x].localGoal + grid[Y][X].cost
    # Update if lower cost
    if localCost < grid[Y][X].localGoal:
      grid[Y][X].localGoal = localCost
      grid[Y][X].parent = (y, x)
      # Calculate heuristic 
      grid[Y][X].globalGoal = heuristic(grid, (Y, X), end) + localCost
    if not grid[neighbour[0]][neighbour[1]].visited:   
      nodes.append(neighbour)
  grid[y][x].visited = True
  
 # Clean the queue of visited nodes
  nodes = [node for node in nodes if not grid[node[0]][node[1]].visited]
  # Priority Queue
  nodes.sort(key=lambda node: grid[node[0]][node[1]].globalGoal)
  
# Track back path to find route and cost
route, pathSum = foundRoute(grid, start, end)
print("PathSUM",pathSum,)
print(route)


 
