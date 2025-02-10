'''
program to find all the prime numbers between a given range
'''

import math

def printPrime(x):
    if x<=1:
        return
    isPrime = 1
    for i in range(2,int(math.sqrt(x)) + 1):
        if x%i == 0:
            isPrime = 0
    if isPrime ==1:
        print(f"{x} is a prime number")

#main
a,b = int(input("Enter staring integer ")), int(input("Enter ending integer "))
for i in range(a,b+1):
    printPrime(i)