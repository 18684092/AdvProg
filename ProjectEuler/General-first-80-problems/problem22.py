##############
# Problem 22 #
##############

"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""
def nameScores():
  # populate list
  with open("p022_names.txt", "r") as f:
    for lines in f:
      names=lines.split(',')
  f.close()
  n = []
  total = 0
  for i, name in enumerate(sorted(names)):
    n = name.strip('"').lower()
    print((i+1), n, end="")
    score = 0
    for c in n:
      v = ord(c) - 96
      score += v
      print("",v,end="")
    score *= (i+1)
    print("",score)
    total += score
  return(total)

print("Problem 22")
print("Name Scores:", nameScores())
print()
