# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 17:13:31 2019

@author: agnib
"""

def fib(n): 
    if n<0: 
        print("Incorrect input") 
    elif n==0: 
        return 0
    elif n==1: 
        return 1
    else: 
        return fib(n-1)+fib(n-2) 

a=int(input("Enter : "))

for i in range(a):
    print(fib(i),end=" ")