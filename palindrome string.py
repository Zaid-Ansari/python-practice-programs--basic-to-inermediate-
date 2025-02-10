'''
Program that checks if the given string is a palindrome or not 
(note: This program is case-sensitive and considers whitespaces that might be present before, between or/and after the string)
'''

def checkPalindrome(x):
    if (x == str(x)[::-1]):
        print("The given string is a palindrome")
    else:
        print("The given string is Not a palindrome")


#main
a = input("Enter the string ")
checkPalindrome(a)