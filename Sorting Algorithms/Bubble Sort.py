# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 18:49:39 2021

@author: Madrika
"""

def Bubble_Sort(array):
    
    def swap(i, j):
        array[i], array[j] = array[j], array[i]
    
    n = len(array)
    swapped = True
    
    x = -1
    while swapped:
        swapped = False
        x = x + 1
        
        for i in range(1, n-x):
            if array[i-1] > array[i]:
                swap(i-1, i)
                swapped  = True
    
    return array

List = [15, 56, 16, 10, 40]     

print(Bubble_Sort(List))        # outpupt: [10, 15, 16, 40, 56]
