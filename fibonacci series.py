'''Program to print fibonacci series upto the given number (note: It's upto the number not hoe many digits)'''

def printFibo(x):
    if x < 0:
        print("Enter a positive interger")
        return
    a,b= 0,1
    print(a ,end= " ")

    if x<1:
        return
    
    print(b, end= " ")
    
    c= a+b

    while(c<=x):
        print (c,end= " ")
        a=b
        b=c
        c=b+a
    

#main

a = int(input("Enter the number"))
printFibo(a)