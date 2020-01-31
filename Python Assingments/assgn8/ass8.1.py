# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 14:31:46 2019

@author: agnib
"""

import module1
s=1
x=int(input("Enter value of x : "))
n=int(input("Enter value of n : "))
p=1
print("(1+x)**n = ",end="")

for i in range(1,n+1):
    for j in range(i):
        p=p*(n-j)
    s=s+((p*(x**i))/module1.fact(i))
    p=1
print(s)