import random
arr = []
n = int(input("enter no of terms: "))
for i in range(n):
    arr.append(int(input("enter no: ")))
arr.sort()
S = int(input("enter sum to be found: "))

def listSearchSum(arr, S):
    """
    arr :  array with all numbers
    S : sum to be found
    """ 
    dicto = {}
    for i in arr:
        dicto[(S - i)] = i
    for i in arr:
        if i in dicto:
            return [i, dicto[i]]
    else:
        return -1


print(listSearchSum(arr, S))
 
