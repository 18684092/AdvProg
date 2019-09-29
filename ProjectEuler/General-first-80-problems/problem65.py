###############
# Problem 65  #
###############

"""
The square root of 2 can be written as an infinite continued fraction.

√2 = 1 +	
1
 	2 +	
1
 	 	2 +	
1
 	 	 	2 +	
1
 	 	 	 	2 + ...
The infinite continued fraction can be written, √2 = [1;(2)], (2) indicates that 2 repeats ad infinitum. In a similar way, √23 = [4;(1,3,1,8)].

It turns out that the sequence of partial values of continued fractions for square roots provide the best rational approximations. Let us consider the convergents for √2.

1 +	
1
= 3/2
 	
2
 
1 +	
1
= 7/5
 	2 +	
1
 	 	
2
 
1 +	
1
= 17/12
 	2 +	
1
 
 	 	2 +	
1
 
 	 	 	
2
 
1 +	
1
= 41/29
 	2 +	
1
 	 	2 +	
1
 
 	 	 	2 +	
1
 
 	 	 	 	
2
 
Hence the sequence of the first ten convergents for √2 are:

1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378, ...
What is most surprising is that the important mathematical constant,
e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].

The first ten terms in the sequence of convergents for e are:

2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...
The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.

Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e.

"""
import time

print("Problem 65")

start = time.time()
nth = 100
# Starting seeds
n = 2
n1 = 1
d = 1
d1 = 0
s = 0
print("1 =",n,d,1)

for i in range(2,nth+1):
    n0 = int(n1)
    d0 = int(d1)
    # repeating pattern of 1, 1, 2 (+2 for each 3) {112,114,116,118 etc)
    if (i % 3 == 0):
        c = int(2 * (i / 3))
    else:
        c = 1
    n1 = n
    d1 = d
    n = int(c * n1 + n0)
    d = int(c * d1 + d0)
    print(i,"=",n,d,c)

# Sum the last numerator
for i in str(int(n)):
    s += int(i)

end = time.time()
print("The sum of the 100th numerator:",s)
print("Time taken:", int((end - start)*100) / 100, "Seconds")
print()
