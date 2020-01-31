# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 15:36:58 2019

@author: agnib
"""

def pstv(num):
    if(num>=0):
        return 1
    else:
        return 0
list1=[-1,2,3,-5,-8,10]
print("Original list: ",list1)
list2=list(filter(pstv,list1))
print("Filtered list: ",list2)
