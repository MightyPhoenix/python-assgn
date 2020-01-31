# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 15:40:41 2019

@author: agnib
"""
import math

def series(n):
    sum = 0
    print()
    for i in range(1,n+1):
        sum = sum + ((i**i)/math.factorial(i))
        if(i==n):
            print(f"("+str(i)+"ᶦ/"+str(i)+"!)",end="")
        else:
            
            print(f"("+str(i)+"ᶦ/"+str(i)+"!)+",end="")
    
    print("\n\nSum =",str(sum))
    

n=int(input("No. of times you want to print the Series : "))

series(n)