# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 21:12:47 2024

@author: Asus
"""

import numpy as np

arr = np.array([1,2,3,4,5])
print(arr)

array = np.arange(30).reshape(6,5)
print(array)

a = np.zeros((3,4))
print(a)


def create_filled_array(rows, columns, fill_value):
    return np.full((rows, columns), fill_value)
array_2d = create_filled_array(5, 6, 7)
print(array_2d)

print("slicing")
print(array_2d[:])
print("Q2")
print(array_2d[2:5,0:3])
print("Q3")
print(array_2d[0:2,0:5])
print("Q4")
print(array_2d[2:4,2:4])
print("Q5")
print(array_2d[-3:-1,3:1])
print("Q6")
print(array_2d[-4:-1,-4-1])

print(array_2d.shape)

l = np.full((2,2),2)
print(l)

