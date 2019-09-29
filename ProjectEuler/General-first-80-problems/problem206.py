###############
# Problem 206 #
###############

"""
Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit.
"""
# take sqrt of 1929394959697989990 - 1389026623
# but we can remove the last 2 digits and multiple by 10
# ignore even numbers. Without removing last 2 digits and looking for that square root
# it takes ages, which is probably the bit of the answer they want
print("Problem 206")

import time
start = time.time()
for n in range(138902669,0, -2):
    s = n * n
    s = str(s)
    if len(s) == 17:
        if s[0] == '1' and s[2] == '2' and s[4] == '3' and s[6] == '4' and s[8] == '5' and s[10] == '6' and s[12] == '7' and s[14] == '8' and s[16] == '9':# and s[18] == '0':
            print("Concealed Square",n * 10)
            break

end = time.time()
print("Time taken: ", int((end - start) * 1000) / 1000, "Seconds")
print()
