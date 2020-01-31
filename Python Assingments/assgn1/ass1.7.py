# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 16:50:01 2019

@author: agnib
"""

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if(a>b and a>c):
    print("a is greatest")

elif(b>c):
    print("b is greatest")
    
else:
    print("c is greatest")