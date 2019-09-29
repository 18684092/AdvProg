###############
# Problem 33  #
###############

"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

"""
import time
print("Problem 33")
print("The Fractions with double digit numerator and denominators which can be reduced by cancelling are:")
start = time.time()

count = 1
sumDenominators = 0
for numerator in range(10,100):
    for denominator in range(numerator,100):
        nStr = str(numerator)
        dStr = str(denominator)
        changed = False
        if nStr[1] == dStr[0]:
            nStr = nStr[0]
            dStr = dStr[1]
            changed = True
        elif nStr[0] == dStr[1]:
            nStr = nStr[1]
            dStr = dStr[0]
            changed = True
        nStr = int(nStr)
        dStr = int(dStr)
        if  dStr > nStr  and changed == True:
            if (numerator / denominator) == nStr / dStr :
                count *= nStr / dStr
                print(str(numerator)+"/"+str(denominator)+" = "+str(nStr)+"/"+str( dStr))
print("The product = ", round(count, 8))
mul = 1
while count < 1:
    mul *= 10
    count *= mul
print("Product fraction = "+str(int(round(count / mul * 10,8))) +"/"+str(mul))
end = time.time()    
print("Denominator in LCT:", mul)
print("Time taken:", int((end - start)*100) / 100, "Seconds")
print()
