# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 14:08:46 2019

@author: agnib
"""

def maxf(x):
    maxv=x[0]
    for i in x:
        if i>maxv:
            maxv=i
    minv=x[0]
    for i in x:
        if i<minv:
            minv=i
    return(maxv,minv)


tup = (1,2,3,4,4,5,55,4,7)

mx,mn=maxf(tup)

print(mx,mn)