# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 20:36:13 2019

@author: agnib
"""

lolim = int(input("Enter Lower Limit : "))
uplim = int(input("Enter Upper Limit : "))

for x in range(lolim,uplim+1):
    if(x%2==0):
        print(str(x)," -- Even Number!")
    else:
        print(str(x)," -- Odd Number!")