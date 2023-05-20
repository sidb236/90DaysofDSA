
#Create an array in python

from array import *
import numpy as np

arr1 = array('i', [1, 2, 3, 4, 5])
arr2 = array('d', [1.2, 2.3, 3.4, 4.5, 5.6])

print(arr1)
print(arr2)

#traverse an Array

def traverseArray(array):
    for i in array:
        print(i)

traverseArray(arr1)

#insert into a array
my_array1 = array('i', [1, 2, 3, 4])
print(my_array1)

my_array1.insert(0, 7)
print(my_array1)

def access
