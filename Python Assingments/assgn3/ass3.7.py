# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 16:40:37 2019

@author: agnib
"""

def fact(n,x):
    if n==0:
        return x
    else:
        return fact(n-1,x*n)
    
    
print(fact(5,1))