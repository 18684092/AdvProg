import time
def maximumPathOne():

  triangle = []
  triangle.append([75])
  triangle.append([95, 64])
  triangle.append([17, 47, 82])
  triangle.append([18, 35, 87, 10])
  triangle.append([20, 4, 82, 47, 65])
  triangle.append([19, 1, 23, 75, 3, 34])
  triangle.append([88, 2, 77, 73, 7, 63, 67])
  triangle.append([99, 65, 4, 28, 6, 16, 70, 92])
  triangle.append([41, 41, 26, 56, 83, 40, 80, 70, 33])
  triangle.append([41, 48, 72, 33, 47, 32, 37, 16, 94, 29])
  triangle.append([53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14])
  triangle.append([70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57])
  triangle.append([91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48])
  triangle.append([63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31])
  triangle.append([4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]) 
  # Iterate over triangle from bottom up
  for rows in reversed(range(0, len(triangle))):
    for cols in range(rows):
      a = triangle[rows][cols] + triangle[rows - 1][cols]
      b = triangle[rows][cols + 1] + triangle[rows - 1][cols]
      if a > b:
        triangle[rows - 1][cols] = a
      else: 
        triangle[rows - 1][cols] = b
  return(triangle[0][0])

print("Problem 18")
start = time.time()
print("Maximum Path I Total: ", maximumPathOne())
end = time.time()
print("Time taken: " + str((end - start)*1000) + " milli seconds")
print()

import time
def maximumPathTwo():
  
  triangle = []
  # populate list
  with open("p067_triangle.txt", "r") as f:
    for lines in f:
      triangle.append(lines.rstrip('\n').split())
  f.close()
  # convert strings to ints
  for rows in range(len(triangle)):
    for cols in range(rows+1):
      triangle[rows][cols] = int(triangle[rows][cols])
  
  # From here is identical to problem 18
  
  # Iterate over triangle from bottom up
  for rows in reversed(range(0, len(triangle))):
    for cols in range(rows):
      a = triangle[rows][cols] + triangle[rows - 1][cols]
      b = triangle[rows][cols + 1] + triangle[rows - 1][cols]
      if a > b:
        triangle[rows - 1][cols] = a
      else: 
        triangle[rows - 1][cols] = b
  return(triangle[0][0])

print("Problem 67")
start = time.time()
print("Maximum Path Sum II Total: ", maximumPathTwo())
end = time.time()
print("Time taken: " + str((end - start)*1000) + " milli seconds")
print()
