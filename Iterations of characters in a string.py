'''
program to find the iterations of characters in the given string
(note: more efficient way would be using Python's built-in collections.Counter)
'''

def calcIterations(x):
    #converting str to list
    lst = list(x)
    #getting unique characters
    unique = set(lst)
    iterations = dict()
    for i in unique:
        count = 0
        for j in lst:
            if i == j:
                count += 1
        iterations[i] = count
    return iterations       

#main
a = input("Enter the string ")
iterations = calcIterations(a)
for x,y in iterations.items():
    print(f"{x} occured {y} times")