# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 11:50:20 2021

@author: Madrika
"""

List = [2, 4, 6, 8]

print(List)     # output: [2, 4, 6, 8]

def Func(Num):
    return Num+10

New_List = list(map(Func, List))

print(New_List)     # output: [12, 14, 16, 18]

