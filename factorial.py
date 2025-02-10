'''
program to find the factorial of the given number using recursion
'''

def calFactorial(a):
    if a < 0:
        return "Factorial is not defined for negative numbers"
    if (a<=1):
        return 1
    return calFactorial(a-1) * a

#main
a = int(input("Enter the number "))
print(calFactorial(a))