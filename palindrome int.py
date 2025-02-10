'''
Program that checks if the given integer is a palindrome or not
'''

def checkPalindrome(x):
    if (x == int(str(x)[::-1])):
        print("The given integer is a palindrome")
        return
    else:
        print("The given integer is Not a palindrome")
        return


#main
a = int(input("Enter the number "))
checkPalindrome(abs(a))