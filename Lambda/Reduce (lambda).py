# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 12:02:58 2021

@author: Madrika
"""

from functools import reduce

List = [2, 3, 4, 5, 6, 7, 8, 9]

print(List)     # output: [2, 3, 4, 5, 6, 7, 8, 9]

result = reduce(lambda x, y: x+y, List)

print(result)     # output: 44

