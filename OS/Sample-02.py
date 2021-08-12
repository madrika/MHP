# -*- coding: utf-8 -*-
"""
Created on Thu May 27 10:03:49 2021

@author: Madrika
"""

import subprocess as sub

while True:
    NUM = input("Enter a Number: ")
    
    if NUM=="1":
        command = "arp /a"
        cmd = sub.check_output(command, shell=True).decode()
        print(cmd)
    
    if NUM=="2":
        command = "ipconfig"
        cmd = sub.check_output(command, shell=True).decode()
        print(cmd)
    
    if NUM=="Exit":
        break