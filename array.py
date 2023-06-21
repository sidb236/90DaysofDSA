
# Create an array in python

from array import *
import numpy as np

arr1 = array('i', [1, 2, 3, 4, 5])
arr2 = array('d', [1.2, 2.3, 3.4, 4.5, 5.6])

print(arr1)
print(arr2)

# traverse an Array


def traversearray(arr):
    for i in arr:
        print(i)


# test the function
traversearray(arr1)

# insert into a array
my_array1 = array('i', [1, 2, 3, 4])
print(my_array1)

my_array1.insert(0, 7)
print(my_array1)


def accessElement(array, index):
    if index> len(array):       # O(1)
        print("The index provided exceeds the length of array")               # O(1)
    else:
        print(array[index])


accessElement(arr1,6)

# Searching in an Array
# Linear Search, we iterate through the elements of array one by one,
# comparing each element with the target value.

arr1 = array('i', [1, 2, 3, 4])


def linear_search(arr1, target):
    for i in range(len(arr1)):
        if arr1[i] ==target:
            print("Found the element {} at {}".format(target, i))
    return -1     #You can also raise ValueError(" Element {} not found in the array".format(target)),
                  # you can also return False


# Input Value in the linear_search function
linear_search(arr1, 3)


def delete_element(arr, target):
    try:
        arr.remove(target)          # Time complexity O(n)
    except Exception as e:
        print(e)


delete_element(arr1, 4)
print(arr1)


 # Time and space complexity of array operations:
 # Operation                    Time Complexity         Space Complexity
 # Creating an empty array          O(1)                    O(1)
 # Creating an array with           O(n)                    O(n)
    # elements
 # Insering a value in an           O(n)                    O(1)
    #array
 # Traversing a given array         O(n)                    O(1)
 # Acessing a given cell            O(1)                    O(1)
 # Acessing a given value           O(1)                    O(1)
 # Searching a given value          O(n)                    O(1)
 # Deleting a given value           O(n)                    O(1)

