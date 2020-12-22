from math import *
from numpy.core import long

def isPrime(n, i):
    #print("n = ",n," i = ", i)
    if i == 1:
        return True
    else:
        if n % i == 0:
            return False
        else:
            isPrime(n, i - 1)

test = int(input())
for test in range(test):
    num = long(input())
    if num == 2:
        print("Prime")
        continue
    else:
        prime = bool(isPrime(num, int(sqrt(num) + 1)))
        print("Prime = ", prime)
        print("Prime") if prime == True else print("Not Prime")
