# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 11:50:20 2021

@author: Madrika
"""

List = [2, 3, 4, 5, 6, 7, 8, 9]

print(List)     # output: [2, 3, 4, 5, 6, 7, 8, 9]

def Func(Num):
    if Num%2==0:
        return True
    else:
        return False

New_List = list(filter(Func, List))

print(New_List)     # output: [2, 4, 6, 8]

