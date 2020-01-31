# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 16:59:09 2019

@author: agnib
"""

def gcd(a,b):
    if(a==0):
        return b;
    else:
        return gcd(a%b,b)
    
print(gcd(15,5))