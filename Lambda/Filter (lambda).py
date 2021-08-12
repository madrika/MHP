# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 11:50:20 2021

@author: Madrika
"""

List = [2, 3, 4, 5, 6, 7, 8, 9]

print(List)     # output: [2, 3, 4, 5, 6, 7, 8, 9]

New_List = list(filter(lambda Num: Num%2==0, List))

print(New_List)     # output: [2, 4, 6, 8]

