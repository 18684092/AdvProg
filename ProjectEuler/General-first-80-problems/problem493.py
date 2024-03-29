################
# Problem 493  #
################

"""
70 colored balls are placed in an urn, 10 for each of the seven rainbow colors.

What is the expected number of distinct colors in 20 randomly picked balls?

Give your answer with nine digits after the decimal point (a.bcdefghij).
"""
import time, math
print("Problem 493")

start = time.time()

# 7(1 - (60 choose 20)/(70 choose 20))

def choose(fromTotal, chooseNumber):
  # 40! / 20! * (40 - 20)!
  result = math.factorial(fromTotal) / (math.factorial(chooseNumber) * (math.factorial(fromTotal - chooseNumber)))
  return(result)



print("Expected number of distinct colors in 20 randomly picked balls:",str(7 * (1 - choose(60, 20) / choose(70 ,20)))[:11])
end = time.time()
print("Time taken:", int((end - start)*100) / 100, "Seconds")
print()
