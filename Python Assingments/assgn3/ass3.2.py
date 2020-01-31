# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 14:01:31 2019

@author: agnib
"""

def swap(a,b):
    temp=a
    a=b
    b=temp
    return print("a =",str(a),"and b =",str(b))

a = int(input("Enter Value of a : "))
b = int(input("Enter Value of b : "))

swap(a,b)

