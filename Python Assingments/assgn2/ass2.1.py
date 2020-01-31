# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 20:27:50 2019

@author: agnib
"""

num = int(input("Enter a Number : "))
lim = int(input("Enter Table Limit : "))

for x in range(lim+1):
    mul = num*x
    print("\n",str(num)," * ",str(x)," = ",str(mul))