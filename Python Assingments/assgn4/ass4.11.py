# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 15:39:23 2019

@author: agnib
"""

def sqr(num):
    return num**2
l=[1,2,3,4,5,6]
print("Original list: ",l)
l2=list(map(sqr,l))
print("New list: ",l2)