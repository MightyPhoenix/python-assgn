# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 15:40:28 2019

@author: agnib
"""

def fibo(i):
    if(i==0):
        return 0;
    if(i==1):
        return 1;
    else:
        return fibo(i-1)+fibo(i-2)
def even(elem):
    if(elem%2==0):
        return 1
    else:
        return 0

l=[]
n=int(input("Enter no. of terms: "))
print("FIBONACCI SERIES: ",end="")
for i in range(n):
    val=fibo(i)
    l.append(val)
print(l)
l2=list(filter(even,l))
print("Even terms: ",l2)
print("Sum of even terms= ",sum(l2))