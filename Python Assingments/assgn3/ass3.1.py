# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 13:44:15 2019

@author: agnib
"""

def equal(a,b):
    if(a==b):
        return print(str(a),"and",str(b),"is equal")
    else:
        return print(str(a),"and",str(b),"is NOT! equal")
    

num1=int(input("Enter Number 1: "))
num2=int(input("Enter Number 2: "))

equal(num1,num2)