
from array import *

# 1. create an array and traverse through it

arr = array('i', [1, 2, 3, 4, 5, 6])
arrStr = array('u', ['a', 's', 's'])

# traverse through the array:
print("The traverse through reference of the object of array")
for a in arr:       # loop using the position of object in the array
    print(a)

# traverse through the array using the index of the object
print("The traverse through index of array")
for i in range(len(arr)):
    print(arr[i])

# traverse through the array using the index of the object
print("The traverse through index of a string array")
for i in range(len(arrStr)):
    print(arrStr[i])


