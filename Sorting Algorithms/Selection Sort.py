# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 18:50:36 2021

@author: Madrika
"""

def Selection_Sort(array):
    
    for i in range(len(array)):
        minimum = i
        
        for j in range(i+1, len(array)):
            
            if array[j] < array[minimum]:
                minimum = j
        
        
        array[minimum], array[i] = array[i], array[minimum]
    
    return array
    
    
List = [10, 56, 16, 15, 40]  

print(Selection_Sort(List))     # outpupt: [10, 15, 16, 40, 56]




















