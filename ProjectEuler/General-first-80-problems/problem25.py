###############
# Problem 25  #
###############

"""
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

"""
import time


def fib(number):
    # Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1
    if number < 1:
        return(0)
    if number <= 2:
        return(1)
    f1 = 1
    f2 = 1
    for n in range(3,number + 1):
        f = f1 + f2
        f1 = f2
        f2 = f
    return(f)
    

print("Problem 25")

start = time.time()

n = 0
while len(str(fib(n))) != 1000:
    n += 1
end = time.time()
print("First term in fib sequence with 1000 digits", n)
print("Time taken:", int((end - start)*100) / 100, "Seconds")
print()
