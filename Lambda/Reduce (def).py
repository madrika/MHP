# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 11:50:20 2021

@author: Madrika
"""

from functools import reduce

List = [2, 3, 4, 5, 6, 7, 8, 9]

print(List)     # output: [2, 3, 4, 5, 6, 7, 8, 9]

def Func(x, y):
    return x+y

result = reduce(Func, List)

print(result)     # output: 44



