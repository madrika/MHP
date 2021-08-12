# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 18:50:49 2021

@author: Madrika
"""

def Insertion_Sort(array):
    
    for i in range(len(array)):
        value = array[i]
        index = i
        
        
        while index > 0 and array[index-1] > value:
            
            array[index] = array[index-1]
            index = index-1
        
        array[index] = value
    
    return array


List = [15, 56, 16, 10, 40]     

print(Insertion_Sort(List))     # outpupt: [10, 15, 16, 40, 56]