# -*- coding: utf-8 -*-
"""
Created on Thu May 27 09:57:38 2021

@author: Madrika
"""

import subprocess as sub

while True:
     command = input("Shell => ")
     cmd = sub.check_output(command, shell=True).decode()
     print(cmd)
     if command=="Exit":
         break
