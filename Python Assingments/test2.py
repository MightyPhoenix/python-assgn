# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 22:39:36 2019

@author: agnib
"""
a = input().split()
a=list(map(int,a))

for i in a:
    if(i%5==0):
        a.remove(i)

for i in a:
    print(i, end=" ")